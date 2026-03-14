import requests
import os
from dotenv import load_dotenv
import re

# Load environment variables from .env file
load_dotenv()
MAILERLITE_API_KEY = os.getenv('MAILERLITE_API_KEY')
API_URL = 'https://connect.mailerlite.com/api/campaigns'
HEADERS = {
    'Authorization': f'Bearer {MAILERLITE_API_KEY}',
    'Content-Type': 'application/json'
}

def download_email_content(campaign_id, output_dir='campaign_email'):
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
    html_content = email.get('content', '')  # Updated to use 'content' field
    subject = email.get('subject', 'No Subject')
    # Save HTML content
    html_path = os.path.join(output_dir, f'{campaign_id}_email.html')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f'Email HTML saved to {html_path}')
    # Find and download images
    img_urls = re.findall(r'<img[^>]+src=["\"]([^"\"]+)["\"]', html_content)
    for idx, url in enumerate(img_urls):
        try:
            img_resp = requests.get(url)
            img_resp.raise_for_status()
            ext = url.split('.')[-1].split('?')[0]
            img_path = os.path.join(output_dir, f'{campaign_id}_img_{idx}.{ext}')
            with open(img_path, 'wb') as img_file:
                img_file.write(img_resp.content)
            print(f'Downloaded image: {img_path}')
        except Exception as e:
            print(f'Failed to download image {url}: {e}')
    print(f'Subject: {subject}')

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: python download_mailerlite_campaign_email.py <campaign_id>')
    else:
        download_email_content(sys.argv[1])
