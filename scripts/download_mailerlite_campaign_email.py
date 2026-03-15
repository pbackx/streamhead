import argparse
import hashlib
import mimetypes
import os
import re
from pathlib import Path
import requests
from urllib.parse import unquote, urlparse
from bs4 import BeautifulSoup, Comment
from dotenv import load_dotenv
from markdownify import markdownify

# Load environment variables from .env file
load_dotenv()
MAILERLITE_API_KEY = os.getenv('MAILERLITE_API_KEY')
API_URL = 'https://connect.mailerlite.com/api/campaigns'
REPO_ROOT = Path(__file__).resolve().parent.parent
IMAGE_ASSET_ROOT = REPO_ROOT / 'assets' / 'brick_sorter_updates'
HEADERS = {
    'Authorization': f'Bearer {MAILERLITE_API_KEY}',
    'Content-Type': 'application/json'
}


def get_sent_campaigns() -> list[dict]:
    response = requests.get(API_URL, headers=HEADERS)
    response.raise_for_status()
    campaigns = response.json().get('data', [])
    return [campaign for campaign in campaigns if campaign.get('status') == 'sent']


def slugify(text: str) -> str:
    """Create a filesystem-friendly slug from the given text."""
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = text.strip('-')
    return text or 'campaign'


def normalize_whitespace(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip()


def sanitize_filename_component(text: str) -> str:
    text = re.sub(r'[^a-zA-Z0-9._-]+', '-', text)
    text = text.strip('-._')
    return text or 'image'


def is_footer_block(section) -> bool:
    text = normalize_whitespace(section.get_text(' ', strip=True)).lower()
    if section.select_one('[data-link-type="unsubscribe"]'):
        return True
    return (
        'you received this email because' in text
        or 'unsubscribe' in text
        or 'sent by mailerlite' in text
    )


def is_header_block(section) -> bool:
    text = normalize_whitespace(section.get_text(' ', strip=True)).lower()
    return bool(section.select_one('[data-link-type="webview"]')) and len(text) < 200


def extract_mailerlite_sections(soup: BeautifulSoup) -> str | None:
    sections = soup.select('.wrapper .ml-default, .wrapper .ml-card, .wrapper .ml-fullwidth')
    if not sections:
        return None

    selected_sections = []
    seen_signatures = set()

    for section in sections:
        if is_header_block(section) or is_footer_block(section):
            continue

        text = normalize_whitespace(section.get_text(' ', strip=True))
        image_sources = [img.get('src', '').strip() for img in section.find_all('img') if img.get('src')]

        if not text and not image_sources:
            continue

        signature = text.lower()
        if not signature:
            signature = '|'.join(image_sources)

        if signature in seen_signatures:
            continue

        seen_signatures.add(signature)
        selected_sections.append(str(section))

    if not selected_sections:
        return None

    return '\n'.join(selected_sections)


def extract_simple_mailerlite_blocks(soup: BeautifulSoup) -> str | None:
    blocks = soup.select('.ml-rte-text, .ml-rte-image')
    if not blocks:
        return None

    selected_blocks = []
    seen_signatures = set()

    for block in blocks:
        text = normalize_whitespace(block.get_text(' ', strip=True))
        image_sources = [img.get('src', '').strip() for img in block.find_all('img') if img.get('src')]

        if not text and not image_sources:
            continue

        signature = text.lower()
        if not signature:
            signature = '|'.join(image_sources)

        if signature in seen_signatures:
            continue

        seen_signatures.add(signature)
        selected_blocks.append(str(block))

    if not selected_blocks:
        return None

    return '\n'.join(selected_blocks)


def download_image(image_url: str, post_stem: str) -> str | None:
    if not image_url.startswith(('http://', 'https://')):
        return None

    parsed_url = urlparse(image_url)
    original_name = Path(unquote(parsed_url.path)).name
    original_stem = sanitize_filename_component(Path(original_name).stem or 'image')
    suffix = Path(original_name).suffix.lower()

    response = requests.get(image_url, timeout=60)
    response.raise_for_status()

    if not suffix:
        content_type = response.headers.get('Content-Type', '').split(';')[0].strip().lower()
        suffix = mimetypes.guess_extension(content_type) or '.img'

    if suffix == '.jpe':
        suffix = '.jpg'

    image_hash = hashlib.sha1(image_url.encode('utf-8')).hexdigest()[:10]
    filename = f'{original_stem}-{image_hash}{suffix}'

    asset_dir = IMAGE_ASSET_ROOT / post_stem
    asset_dir.mkdir(parents=True, exist_ok=True)
    asset_path = asset_dir / filename
    if not asset_path.exists():
        asset_path.write_bytes(response.content)

    return f'/assets/brick_sorter_updates/{post_stem}/{filename}'


def rewrite_image_sources(html_content: str, post_stem: str) -> str:
    soup = BeautifulSoup(html_content, 'html.parser')
    source_cache: dict[str, str] = {}

    for img in soup.find_all('img'):
        source = img.get('src', '').strip()
        if not source:
            continue

        if source in source_cache:
            img['src'] = source_cache[source]
            continue

        try:
            local_url = download_image(source, post_stem)
        except requests.RequestException as exc:
            print(f'Warning: failed to download image {source}: {exc}')
            continue

        if local_url:
            source_cache[source] = local_url
            img['src'] = local_url

    return str(soup)


def download_email_content(campaign_id, output_dir='../_brick_sorter_updates'):
    os.makedirs(output_dir, exist_ok=True)

    # Fetch campaign details
    response = requests.get(f'{API_URL}/{campaign_id}', headers=HEADERS)
    response.raise_for_status()
    campaign = response.json().get('data', {})

    emails = campaign.get('emails', [])
    if not emails:
        print('No emails found for this campaign.')
        return

    email = emails[0]
    html_content = email.get('content', '')
    subject = email.get('subject', 'No Subject')

    if not html_content.strip():
        # Some campaigns may only provide plain text
        html_content = email.get('plain_text', '')

    # Clean up MailerLite email wrappers (layout tables are not useful in Markdown).
    soup = BeautifulSoup(html_content, 'html.parser')

    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    for tag in soup.select('style, script, meta, head, link, title'):
        tag.decompose()

    for tag in soup.select('.ml-hide-branding'):
        tag.decompose()

    extracted_sections = extract_mailerlite_sections(soup)
    if extracted_sections:
        cleaned_html = extracted_sections
    else:
        simple_blocks = extract_simple_mailerlite_blocks(soup)
        if simple_blocks:
            cleaned_html = simple_blocks
        else:
            document_div = soup.select_one('div.document')
            cleaned_html = str(document_div or soup)

    soup_tables_removed = BeautifulSoup(cleaned_html, 'html.parser')
    for tag in soup_tables_removed.find_all(['table', 'thead', 'tbody', 'tr', 'th', 'td']):
        tag.name = 'div'
    for tag in soup_tables_removed.find_all(['font']):
        tag.unwrap()
    cleaned_html = str(soup_tables_removed)

    # If cleaning left us with very little, fall back to raw HTML or plain text
    if len(cleaned_html.strip()) < 20:
        cleaned_html = html_content

    # Determine date to use for the post
    date = email.get('created_at') or campaign.get('created_at')
    if date and ' ' in date:
        date = date.split(' ')[0]  # YYYY-MM-DD

    slug = slugify(subject)
    post_stem = f'{date}-{slug}' if date else slug

    html_content = rewrite_image_sources(cleaned_html, post_stem)

    # Convert HTML to Markdown
    markdown_body = markdownify(html_content, heading_style='ATX')

    # Build output file path
    filename = f'{post_stem}.md'
    output_path = os.path.join(output_dir, filename)

    safe_title = subject.replace('"', '\\"')

    front_matter = (
        '---\n'
        f'layout: page\n'
        f'title: "{safe_title}"\n'
        f'date: {date}\n'
        f'category: Brick Sorter Updates\n'
        f'back_page: brick_sorter_updates_archive\n'
        '---\n\n'
    )

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(front_matter)
        f.write(markdown_body)

    print(f'Written Jekyll post to {output_path}')


def download_all_sent_campaigns(output_dir='../_brick_sorter_updates'):
    sent_campaigns = get_sent_campaigns()
    if not sent_campaigns:
        print('No sent campaigns found.')
        return

    for campaign in sent_campaigns:
        campaign_id = campaign.get('id')
        if not campaign_id:
            continue

        subject = 'N/A'
        emails = campaign.get('emails', [])
        if emails:
            subject = emails[0].get('subject', 'N/A')

        print(f'Downloading campaign {campaign_id}: {subject}')
        download_email_content(campaign_id, output_dir=output_dir)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='Download MailerLite campaign emails as Jekyll posts.'
    )
    parser.add_argument(
        'campaign_id',
        nargs='?',
        help='MailerLite campaign ID to download.'
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Download all sent campaigns returned by the MailerLite campaigns endpoint.'
    )
    parser.add_argument(
        '--output-dir',
        default='../_brick_sorter_updates',
        help='Directory where generated Markdown and debug files are written.'
    )
    return parser


if __name__ == '__main__':
    parser = build_parser()
    args = parser.parse_args()

    if args.all:
        download_all_sent_campaigns(output_dir=args.output_dir)
    elif args.campaign_id:
        download_email_content(args.campaign_id, output_dir=args.output_dir)
    else:
        parser.error('Provide a campaign_id or use --all.')
