# MailerLite Markdown-to-Campaign Plan

This note describes a possible future workflow for creating MailerLite campaigns from newsletter Markdown files in `_brick_sorter_updates/`.

## Goal

Use the Markdown newsletter file as the source of truth:

1. Draft the newsletter locally in `_brick_sorter_updates/`.
2. Preview and revise it until the content is ready.
3. Create or update a MailerLite draft campaign from that Markdown.
4. When ready, publish the Jekyll page and schedule/send the MailerLite campaign.

## Is It Possible?

Yes, with one important constraint:

- MailerLite's API supports creating and updating campaigns with raw HTML using `emails[*].content`.
- According to the MailerLite API docs, this requires the Advanced plan.
- If the account does not have that capability, the Markdown-to-HTML part can still be automated, but the final content may need to be pasted or imported manually in MailerLite.

## Alternative to Evaluate

Before building this workflow around MailerLite, evaluate whether Mailcoach would be a better fit.

Questions to answer when resuming this work:

- Does Mailcoach provide a simpler Markdown-to-campaign workflow?
- Does Mailcoach make draft creation, editing, and scheduling easier from local files?
- Does Mailcoach avoid the MailerLite Advanced plan requirement for pushing raw HTML content by API?
- Would Mailcoach fit the current hosting, budget, and maintenance constraints of this project?

If Mailcoach turns out to be a better fit, the overall source-of-truth workflow can stay the same, but the campaign creation and scheduling integration should target Mailcoach instead of MailerLite.

## Recommended Workflow

### 1. Draft newsletter locally

Create a new file in `_brick_sorter_updates/` with front matter like:

```yaml
---
layout: page
title: "My Newsletter Title"
date: 2026-03-15
category: Brick Sorter Updates
back_page: brick_sorter_updates_archive
published: false
mailerlite_campaign_id:
mailerlite_name:
mailerlite_groups: []
mailerlite_segments: []
mailerlite_from_name: "Peter Backx"
mailerlite_from: "peter@streamhead.com"
mailerlite_reply_to: "peter@streamhead.com"
---
```

Notes:

- `published: false` keeps the page out of the public site while drafting.
- `mailerlite_campaign_id` can be filled in automatically after draft creation.
- `mailerlite_groups` or `mailerlite_segments` define the recipients.

### 2. Convert Markdown to email HTML

A future script should:

1. Read the Markdown file.
2. Parse front matter.
3. Convert Markdown body to HTML.
4. Wrap it in a simple email-safe HTML template.
5. Rewrite links and image URLs to absolute public URLs.

Absolute URLs are required for email content.

Examples:

- `/assets/brick_sorter_updates/...` becomes `https://www.streamhead.com/assets/brick_sorter_updates/...`
- Internal page links should also become full `https://www.streamhead.com/...` links.

The public site URL is already defined in `_config.yml`:

- `url: https://www.streamhead.com`

## Why Absolute URLs Matter

The current Jekyll posts can use site-relative asset URLs, but email clients cannot reliably resolve relative paths.

For MailerLite campaigns:

- Images must be publicly accessible.
- Internal links should be absolute.
- If the newsletter page itself is unpublished, links to that page will not work until the site is deployed with that page published.

## MailerLite API Flow

### Create draft campaign

Use:

- `POST /api/campaigns`

Required fields include:

- `name`
- `type: regular`
- `emails[0].subject`
- `emails[0].from_name`
- `emails[0].from`
- optional `emails[0].reply_to`
- optional `emails[0].content` (HTML, Advanced plan required)
- `groups` or `segments`

### Update existing draft campaign

Use:

- `PUT /api/campaigns/{campaign_id}`

Important:

- This only works while the campaign is still in `draft` status.

### Send or schedule campaign

Use:

- `POST /api/campaigns/{campaign_id}/schedule`

This can send immediately or schedule for later.

## Suggested Script Design

A future script could be named:

- `create_mailerlite_campaign_from_markdown.py`

It would support modes like:

### Preview mode

- Convert a Markdown file to HTML locally.
- Save or print the generated HTML for inspection.
- Useful before creating a campaign.

### Create mode

- Read one Markdown newsletter file.
- Build the email HTML.
- Create a MailerLite draft campaign.
- Write `mailerlite_campaign_id` back into front matter.

### Update mode

- Read the Markdown file.
- Rebuild the HTML.
- Update the existing draft campaign using `mailerlite_campaign_id`.

### Schedule mode

- Schedule or immediately send the campaign after content is finalized.

## What Else Would Be Needed

### 1. Front matter conventions

The script needs agreed fields for:

- campaign name
- subject
- sender name
- sender email
- reply-to email
- groups or segments
- stored MailerLite campaign id

### 2. Markdown to HTML conversion

A converter is needed that works well for email:

- headings
- paragraphs
- lists
- links
- images

### 3. Email wrapper template

Raw converted Markdown will work, but a basic wrapper is better:

- constrained width
- inline-safe typography
- spacing
- optional intro/header block

### 4. Absolute asset handling

This is already partially solved by the current importer pattern:

- newsletter images are stored in `assets/brick_sorter_updates/<post-stem>/`
- outgoing campaign generation should use the deployed absolute URL to those files

### 5. Deployment order

The safest workflow would be:

1. finish the draft locally
2. ensure images exist in `assets/brick_sorter_updates/...`
3. publish/deploy the site
4. create or update the MailerLite campaign using absolute public URLs
5. preview in MailerLite
6. schedule/send

## Risks and Caveats

### MailerLite plan limitation

If the account cannot set `emails[*].content` through the API, fully automated draft creation may not be possible.

Fallback:

- still generate HTML locally
- copy/paste or import it manually into MailerLite

### Email-safe HTML

Jekyll page HTML and email HTML are not the same thing.

A future script should generate email-oriented HTML, not reuse full site page HTML.

### Published vs unpublished content

If a campaign links to a page that is still unpublished on the site, recipients will get broken links.

### Draft-only updates

Once a campaign is no longer in `draft`, the update endpoint will reject changes.

## Best Minimal First Version

When this work resumes, the best first milestone is:

1. Read one Markdown newsletter file.
2. Parse front matter.
3. Convert the body to HTML.
4. Rewrite asset URLs to absolute `https://www.streamhead.com/...` URLs.
5. Create a MailerLite draft campaign.
6. Save the returned campaign id back into the Markdown file.

That would be enough to prove the workflow end-to-end.

## Recommended Next Step When Resuming

Start by building preview-only support first:

- input: one Markdown newsletter file
- output: generated email HTML

Once that looks good, add MailerLite draft creation and campaign id write-back.
