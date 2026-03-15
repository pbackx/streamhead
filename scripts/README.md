# MailerLite Script Helpers

This folder contains scripts to interact with the MailerLite API and generate Jekyll posts from your campaign content.

## Setup
1. Copy your API key into `.env`:

```bash
MAILERLITE_API_KEY=your_api_key_here
```

2. Install dependencies using **UV** (recommended):

```bash
uv pip install .
```

Dependencies include: `python-dotenv`, `markdownify`, and `beautifulsoup4`.

## Scripts

### List sent campaigns

```bash
uv run list_sent_mailerlite_campaigns.py
```

### Download a campaign as a Jekyll post

```bash
uv run download_mailerlite_campaign_email.py <campaign_id>
```

Download all sent campaigns returned by the same endpoint as the listing script:

```bash
uv run download_mailerlite_campaign_email.py --all
```

Optionally choose a different output directory:

```bash
uv run download_mailerlite_campaign_email.py --all --output-dir ../_brick_sorter_updates
```

This creates a file under `_brick_sorter_updates/` with front matter and Markdown content.
Any remote images found in the campaign HTML are downloaded into
`assets/brick_sorter_updates/<post-slug>/` and rewritten to local site URLs.

## Linting (Ruff)

Run Ruff to verify styling and catch issues:

```bash
uv run ruff check .
```

(Optional) To automatically fix lint issues where supported:

```bash
uv run ruff check --fix .
```
