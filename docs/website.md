---
title: Maintaining this website
---
# Maintaining this website

The website is built by GitHub Pages from the [`dal-msgss.github.io`](https://github.com/dal-msgss/dal-msgss.github.io) repository. Commit your changes and push to `main` and the site rebuilds within a few minutes.  You can update the site from your browser on GitHub, via VS Code, or via VS Code on the browser at `https://github.dev/dal-msgss/dal-msgss.github.io`. The website is written Markdown via Jekyll, and it is designed in such a way that routine updates can be done by solely editing the ``.md`` files.

You need to be a member of the [`dal-msgss`](https://github.com/dal-msgss) GitHub organization to make changes. Ask a current owner to add you.

#### Quick links	

Each link opens GitHub's editor in the browser. Make your changes, then click **Commit changes**, add a title and description for your edit, and commit directly to the `main` branch. The site updates within a few minutes.

* [Add a talk to the grad seminar.](<https://github.com/dal-msgss/dal-msgss.github.io/new/main/_talks?filename=YYYY-MM-DD-firstname-lastname.md&value=---%0Atitle%3A%20Talk%20Title%0Aspeaker%3A%20Firstname%20Lastname%0Adate%3A%20YYYY-MM-DD%0A---%0AAbstract%20goes%20here.%20Leave%20a%20blank%20line%20between%20paragraphs.%0A>)
* [Update the grad seminar information.](https://github.com/dal-msgss/dal-msgss.github.io/edit/main/seminar.md)
* [Add a new executive team.](<https://github.com/dal-msgss/dal-msgss.github.io/new/main/_executive?filename=YYYY-YY.md&value=---%0Ayear%3A%20%22YYYY/YY%22%0A---%0A-%20President%3A%20%0A-%20VP%20External%3A%20%0A-%20VP%20Internal%3A%20%0A-%20PhD%20Math%20Representative%3A%20%0A-%20PhD%20Stat%20Representative%3A%20%0A-%20MSc%20Math%20Representative%3A%20%0A-%20MSc%20Stat%20Representative%3A%20%0A>)

#### File guide

- `index.md`, `docs/index.md`, `travel-grant.md`: page text, in Markdown.
- `seminar.md`: the seminar page, with the talk list built from `_talks/`.
- `executive.md`: the executive page, including the role descriptions. It shows the newest file in `_executive/` as the current executive and links to the older years.
- `_executive/`: one Markdown file per year, listing that year's executive.
- `_data/navigation.yml`: the links in the navigation bar.
- `_layouts/default.html`: the shared header, navigation and footer for every page.
- `style.css`: all styling. `images/`: logo and icons.
