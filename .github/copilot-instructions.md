# Copilot Workspace Instructions

## Project Overview
This workspace is a Jekyll-based static site for [www.streamhead.com](https://www.streamhead.com/). Content is managed via Markdown files and posts, with site generation handled by Jekyll.

## Build & Test Commands
- **Install dependencies:**
  - `bundle install`
- **Run locally:**
  - `bundle exec jekyll serve`
- **Upgrade GitHub Pages gem:**
  - `bundle update github-pages`

## Key Conventions
- Posts are stored in `_posts/` and follow the standard Jekyll naming format.
- Includes are in `_includes/` for reusable HTML snippets.
- Site configuration is in `_config.yml`.
- Drafts and scheduled posts may use IFTTT triggers (see README for details).

## Common Pitfalls
- Ruby and Jekyll setup can be tricky, especially on Windows. See README for scoop/msys2 tips.
- WDM gem installation requires a specific flag.
- Upgrading dependencies may be needed for security.

## Agent Guidance
- When editing or creating posts, follow Jekyll Markdown conventions.
- For site changes, update `_config.yml` or `_includes/` as needed.
- Use the build/test commands above for local development.
- If unclear, check README.md for additional instructions.

## Example Prompts
- "Create a new blog post about streaming radio tips."
- "Update the site configuration to add a new category."
- "Add a reusable copyright notice to all pages."

---

For further customization, consider agent instructions for frontend (HTML/CSS), backend (Jekyll/Ruby), or automation (IFTTT, scheduled posts).
