# dal-msgss.github.io
Website for the society, built by GitHub Pages with Jekyll. Push to `main` and
GitHub Pages rebuilds the site within a few minutes.

## Quick edit links

You can update the site from your browser on GitHub, without installing anything.
Each link opens GitHub's editor. Make your changes, then click **Commit changes**
(committing straight to `main` is fine). The site updates within a few minutes.

**Seminar**
- [Add a talk](https://github.com/dal-msgss/dal-msgss.github.io/new/main/_talks?filename=YYYY-MM-DD-firstname-lastname.md&value=---%0Atitle%3A%20TBA%0Aspeaker%3A%20Firstname%20Lastname%0Adate%3A%20YYYY-MM-DD%0A---%0AAbstract%20goes%20here.%20Leave%20a%20blank%20line%20between%20paragraphs.%0A): opens a new talk with the template filled in.
  Replace every placeholder: the file name (`YYYY-MM-DD-firstname-lastname.md`,
  lowercase with hyphens), the date, the speaker and the abstract. Leave the title
  as `TBA` if you don't know it yet.
- [Edit a talk](https://github.com/dal-msgss/dal-msgss.github.io/tree/main/_talks): click the talk's file, then the
  pencil icon.
- [Change the seminar room or time](https://github.com/dal-msgss/dal-msgss.github.io/edit/main/_data/society.yml)

**Executive**
- [Add a new year's executive](https://github.com/dal-msgss/dal-msgss.github.io/new/main/_executive?filename=YYYY-YY.md&value=---%0Ayear%3A%20%22YYYY/YY%22%0APresident%3A%20%0AVice-President%20External%3A%20%0AVice-President%20Internal%3A%20%0APhD%20Mathematics%3A%20%0APhD%20Statistics%3A%20%0AMSc%20Mathematics%3A%20%0AMSc%20Statistics%3A%20%0A---%0A): use it after each AGM. Replace
  `YYYY/YY` and the file name with the new academic year (for example `2027/28` and
  `2027-28.md`), then type each name after the colon. Leave a role blank if it's
  vacant.
- [Edit an executive year](https://github.com/dal-msgss/dal-msgss.github.io/tree/main/_executive): to fix a name or fill
  a vacancy, click that year's file, then the pencil icon.

If you commit a typo, GitHub emails the person who committed and the live site
keeps its previous version. Open the file again, fix it and commit.

## Handover checklist (after each AGM)

- [ ] Give the new council access to the `dal-msgss` GitHub organization. Keep at
      least two owners at all times, ideally including an account tied to msgss@dal.ca,
      so access never leaves with a graduating student.
- [ ] Add the new year's file to `_executive/` (use the "Add a new year's executive"
      link above, or see "Executive page" below).
- [ ] Update the seminar room and time in `_data/society.yml`.
- [ ] If the bylaws or constitution were amended, replace `docs/bylaws.pdf` and
      `docs/constitution.pdf` (keep those file names so links don't break).
- [ ] Show the new council the "Quick edit links" above.
- [ ] Make sure this checklist is in the society's transition notes for next year.

## Where things are

- `index.md`, `docs/index.md`, `travel-grant.md`: page text, in Markdown.
- `seminar/index.html`, `executive.html`: pages built from `_talks/` and `_executive/`.
- `_data/society.yml`: contact email, social links, and seminar room and time.
- `_data/roles.yml`: council roles and their descriptions.
- `_data/navigation.yml`: the links in the navigation bar.
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

The seminar room and time are in `_data/society.yml`; the blurb is in `seminar/index.html`.

If the title isn't known yet, use `TBA`; it is shown as "Talk by Jane Doe".

The seminar page lists every talk, newest first, grouped by academic year
(July to June, labelled like 2025/26).

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
"Past executives". Each name before the colon must match a role's `key` in
`_data/roles.yml`. In the current year, a role left out of the file shows as
"Vacant"; in past years it is simply not listed.

Role names, descriptions and order are in `_data/roles.yml`. To rename a role,
change its `title` there and leave its `key` alone. To add a role, add an entry
there and a line for it in the current year's file.

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
from `_config.yml` is used). To add the page to the nav bar, add it
to `_data/navigation.yml`.

Pages in `_drafts/` (such as the welcome package) are not published. To publish
one, move it out of `_drafts/`.
