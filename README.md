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

Seminar details (room, time, contact, blurb) are written directly in `seminar/index.html`.

Push to `main` and GitHub Pages rebuilds the site. The seminar page splits talks into upcoming and past using the build date; `.github/workflows/daily-rebuild.yml` triggers a rebuild every night
so they stay current.

To preview locally: `bundle exec jekyll serve` (with the `github-pages` gem).

## Executive page

Each year's council is one file in `_executive/`, named like `2026-27.md`:

```markdown
---
year: "2026/27"
President: Jane Doe
Vice-President External: ...
Vice-President Internal: ...
PhD Mathematics: ...
PhD Statistics: ...
MSc Mathematics: ...
MSc Statistics: Vacant
---
```

The newest year is shown as the current executive; older years are listed under
"Past executives". The role descriptions and layout are in `executive.html`.
A role left out of a year's file shows as "Vacant".

## Markdown pages

Any `.md` file in the site becomes a page with the site's header, nav and
footer. `welcome.md` is published at `/welcome.html`; a file at
`resources/housing.md` would be at `/resources/housing.html`. Start the file
with a title:

```markdown
---
title: Welcome Package
---
# MSGSS Welcome Package

Normal Markdown from here on.
```

The `title` shows in the browser tab. To add the page to the nav bar, add a
link in `_layouts/default.html`.
