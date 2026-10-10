# msgss-dal.github.io
Website for the society, built by GitHub Pages with Jekyll.

- `_layouts/default.html`: the shared header, navigation and footer for every page.
- `index.html`, `executive.html`, `docs/index.html`, `404.html`: page content only.
- `style.css`: all styling.

## Grad seminar

Each talk is one Markdown file in `_talks/`, named `YYYY-MM-DD-speaker-name.md`:

```markdown
---
title: My Talk Title        # use TBA if not known yet
speaker: Jane Doe
date: 2026-10-15
---
The abstract, in Markdown. Leave a blank line between paragraphs.
```

Seminar details (room, time, contact, blurb) are in `_data/seminar.yml`.

Push to `main` and GitHub Pages rebuilds the site. The seminar page splits talks into upcoming and past using the build date; `.github/workflows/daily-rebuild.yml` triggers a rebuild every night
so they stay current.

To preview locally: `bundle exec jekyll serve` (with the `github-pages` gem).
