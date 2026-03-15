# MailerLite Campaign Fetcher Skill

## Purpose
Automate retrieval of sent MailerLite campaigns and download their content for archiving or review.

## Workflow
1. **Set up API access**
   - Obtain MailerLite API key.
   - Add API key to a `.env` file as `MAILERLITE_API_KEY=your_key_here`.
   - Use `python-dotenv` to load the `.env` file in scripts.
   - Install dependencies using UV and pyproject.toml (see below).
  - Required packages: `requests`, `python-dotenv`, `markdownify`.
2. **List sent campaigns**
   - Use MailerLite API endpoint to fetch all campaigns.
   - Filter for campaigns with status 'sent'.
   - Display campaign IDs, names, dates, and subjects.
3. **Download campaign content**
   - Select campaign by ID.
   - Fetch campaign details and email content (subject, plain text, HTML if available).
   - Save or display content for archiving.

## Dependency Management
- Dependencies are managed using UV and pyproject.toml.
- To install dependencies, run: `uv pip install -r requirements.txt` or `uv pip install .` if using pyproject.toml.

## Decision Points
- API key setup: If not set, prompt user to provide or configure.
- Campaign selection: User can choose by ID, name, or date.
- Content format: Optionally download plain text or HTML.

## Quality Criteria
- Handles API errors gracefully (invalid key, no campaigns, etc).
- Uses consistent quoting (single quotes) in Python scripts.
- Loads API key from .env file reliably using python-dotenv.
- Lists only sent campaigns (not drafts).
- Downloads and saves content reliably.
- Clear output for user review or archiving.

## Example Prompts
- "List all sent MailerLite campaigns."
- "Download content from campaign ID 123456."
- "Archive the latest MailerLite newsletter."

## Related Customizations
- Schedule automatic archiving of new campaigns.
- Integrate with Jekyll collection for newsletter import.
- Add support for downloading attachments or campaign stats.

---

This skill is workspace-scoped and can be adapted for personal or team workflows. For more advanced integration, see MailerLite API docs via context7.