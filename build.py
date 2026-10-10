"""Build seminar/index.html and one page per talk (seminar/talks/) from talks.yaml.

Edit talks.yaml, then run:  python build.py
(GitHub Actions also runs this automatically when talks.yaml changes.)
"""
import html
import datetime
import glob
import os
import re
import unicodedata
import yaml

with open("talks.yaml", encoding="utf-8") as f:
    data = yaml.safe_load(f)

info = data.get("info") or {}
talks = data["talks"]
name = html.escape(info.get("name") or "Talks")
contact = html.escape(info.get("contact") or "")
blurb = "".join(
    f"<p>{html.escape(p).replace(chr(10), '<br>')}</p>"
    for p in str(info.get("blurb") or "").split("\n\n") if p.strip()
)

talks.sort(key=lambda t: str(t["date"]), reverse=True)


def nice_date(d):
    """2026-10-09 -> October 9, 2026"""
    if not isinstance(d, datetime.date):
        d = datetime.date.fromisoformat(str(d))
    return f"{d:%B} {d.day}, {d.year}"


def slugify(text):
    text = unicodedata.normalize("NFKD", str(text)).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def paragraphs(text):
    return "".join(
        f"<p>{html.escape(p).replace(chr(10), '<br>')}</p>"
        for p in str(text or "").split("\n\n") if p.strip()
    )


def page(title, body, root):
    """Wrap body in the shared site header and footer.
    root is the path back to the site root, e.g. "../" or "../../"."""
    return f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link href="{root}style.css" rel="stylesheet">
  </head>

  <body>
    <header class="site-header">
      <a class="site-name" href="{root}index.html">MSGSS</a>
      <nav>
        <a href="{root}index.html">Home</a>
        <a href="{root}seminar/">Seminar</a>
        <a href="{root}travel-grant.html">Travel Grant</a>
        <a href="{root}docs/">Documents</a>
      </nav>
    </header>

    <main>
{body}
    </main>

    <footer class="site-footer">
      <a href="mailto:msgss@dal.ca">msgss@dal.ca</a> ·
      <a href="https://www.instagram.com/msgss.dal">Instagram</a> ·
      <a href="https://github.com/msgss-dal">GitHub</a>
    </footer>
  </body>
</html>
"""


# Each talk gets a page at seminar/talks/<date>-<speaker>.html
# (with -2, -3, ... added if two talks would get the same name).
used = set()
for t in talks:
    base = f'{t["date"]}-{slugify(t["speaker"])}'
    slug, n = base, 2
    while slug in used:
        slug, n = f"{base}-{n}", n + 1
    used.add(slug)
    t["_slug"] = slug

# ---- Seminar page: list of all talks ----
parts = []
year = None
for t in talks:
    y = str(t["date"])[:4]
    if y != year:
        year = y
        parts.append(f"<h2>{year}</h2>")
    title = html.escape(t.get("title") or "TBA")
    meta = f'{nice_date(t["date"])} &middot; {html.escape(t["speaker"])}'
    parts.append(
        f'<article><h3><a href="talks/{t["_slug"]}.html">{title}</a></h3>'
        f'<p class="meta">{meta}</p>{paragraphs(t.get("abstract"))}</article>'
    )

body = f"""<h1>{name}</h1>
{blurb}
<p><b>Location:</b> {html.escape(str(info.get("location") or "TBA"))}<br>
<b>Time:</b> {html.escape(str(info.get("time") or "TBA"))}<br>
<b>Want to give a presentation?</b> Email <a href="mailto:{contact}">{contact}</a></p>
{chr(10).join(parts)}"""

os.makedirs("seminar", exist_ok=True)
with open("seminar/index.html", "w", encoding="utf-8") as f:
    f.write(page(name, body, "../"))

# ---- One page per talk ----
os.makedirs("seminar/talks", exist_ok=True)
# Remove all old talk pages first, so every build starts fresh and
# deleted/renamed talks don't leave stale pages behind.
for old in glob.glob("seminar/talks/*.html"):
    os.remove(old)

for t in talks:
    title = html.escape(t.get("title") or "TBA")
    body = f"""<p><a href="../index.html">&larr; All talks</a></p>
<h1>{title}</h1>
<p class="meta">{html.escape(t["speaker"])} &middot; {nice_date(t["date"])}</p>
{paragraphs(t.get("abstract")) or "<p><i>Abstract TBA.</i></p>"}"""
    with open(f'seminar/talks/{t["_slug"]}.html', "w", encoding="utf-8") as f:
        f.write(page(f"{title} &middot; {name}", body, "../../"))
