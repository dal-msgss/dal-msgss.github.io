# msgss-dal.github.io
Website for the society, built by GitHub Pages with Jekyll. Push to `main` and
GitHub Pages rebuilds the site within a few minutes.

## Handover checklist (after each AGM)

- [ ] Give the new council access to the `msgss-dal` GitHub organization. Keep at
      least two owners at all times, ideally including an account tied to msgss@dal.ca,
      so access never leaves with a graduating student.
- [ ] Add the new year's file to `_executive/` (see "Executive page" below).
- [ ] Update the seminar room and time at the top of `seminar/index.html`.
- [ ] If the bylaws or constitution were amended, replace `docs/bylaws.pdf` and
      `docs/constitution.pdf` (keep those file names so links don't break) and
      update the "Last amended" line in `docs/index.md`.
- [ ] Make sure this checklist is in the society's transition notes for next year.

## Where things are

- `index.md`, `docs/index.md`, `travel-grant.md`: page text, in Markdown.
- `seminar/index.html`, `executive.html`: pages built from `_talks/` and `_executive/`.
- `_layouts/default.html`: the shared header, navigation and footer for every page.
- `_drafts/`: Markdown pages that are not published yet.
- `style.css`: all styling. `images/`: logo and icons.

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

The seminar page lists every talk, newest first, grouped by year.

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
footer. `travel-grant.md` is published at `/travel-grant.html`; a file at
`resources/housing.md` would be at `/resources/housing.html`. Start the file
with a title:

```markdown
---
title: Welcome Package
---
# MSGSS Welcome Package

Normal Markdown from here on.
```

The `title` shows in the browser tab. You can also add a `description:` line; it's the
summary shown in search results and link previews (otherwise the site's description
from `_config.yml` is used). To add the page to the nav bar, add a
link in `_layouts/default.html`.

Pages in `_drafts/` (such as the welcome package) are not published. To publish
one, move it out of `_drafts/`.
