#!/usr/bin/env python3
"""
Build a practitioner workbook as a printable PDF.

The markdown is where the content is written and reviewed; **the PDF is what a
colleague actually buys.** A licensed material that arrives as a `.md` file is
a draft, however good the writing.

    python3 scripts/build-workbook-pdf.py angry

Markdown → HTML → PDF, printed by headless Chromium. Chosen over a PDF library
because the layout is typographic — running headers, page breaks that do not
strand a heading, tables, callouts — and CSS says all of that in a few lines
where a drawing API would take hundreds.

**The cover is page one, full bleed, with no header or footer.** It is already a
complete composition (`scripts/figure-workbook-cover.py`); framing it would be
framing a frame.

**The family name appears on this document, unlike on a colouring page.** D-120
keeps a child's own choice off anything she carries home; a workbook is not a
record of a child, it is material about a feeling, and the practitioner needs to
see at a glance which one they are holding.
"""

import os
import re
import sys

import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MATERIALS = os.path.join(ROOT, "docs", "materials")
BRANDING = os.path.join(ROOT, "public", "assets", "branding")

# The same seven section accents as the colouring pages (D-138), so every
# printed ColorHugs object reads as one family.
BAND = ["#2F6FD0", "#E0619A", "#8B6FE0", "#EF7D3D", "#3FA96B", "#D9911A", "#E0566A"]

FAMILIES = {
    "angry": "Zangado",
    "sad": "Triste",
    "scared": "Assustado",
    "ashamed": "Envergonhado",
    "happy": "Feliz",
    "calm": "Calmo",
    "bored": "Tédio",
}

CSS = """
@page {
  size: A4;
  margin: 22mm 20mm 20mm;
  @bottom-center { content: counter(page); }
}
@page :first { margin: 0; }

* { box-sizing: border-box; }

body {
  margin: 0;
  color: #1B2A5B;
  font-family: "DejaVu Sans", system-ui, sans-serif;
  font-size: 10.5pt;
  line-height: 1.65;
}

/* The cover fills the sheet. It is already a finished composition. */
.cover { page-break-after: always; }
.cover img { display: block; width: 100%; height: auto; }

.band { display: flex; gap: 5px; margin: 0 0 14mm; }
.band span { height: 7px; flex: 1; border-radius: 4px; }

h1 { font-size: 19pt; margin: 0 0 4mm; line-height: 1.25; }
h2 {
  font-size: 14pt;
  margin: 10mm 0 3mm;
  padding-top: 4mm;
  border-top: 1.5px solid rgba(27,42,91,0.14);
  page-break-after: avoid;
  break-after: avoid;
}
/* A heading alone at the foot of a page is a heading pointing at nothing. */
h2 + p, h2 + ul, h2 + table, h3 + p, h3 + ul { break-before: avoid; }
h3 {
  font-size: 11.5pt;
  margin: 7mm 0 2mm;
  color: #5B4F8A;
  page-break-after: avoid;
}
p { margin: 0 0 3.5mm; }
strong { color: #16234C; }

ul { margin: 0 0 4mm; padding-left: 5mm; }
li { margin-bottom: 1.8mm; }

/* Callouts: the literacy line the child reads, and the warnings. */
blockquote {
  margin: 5mm 0;
  padding: 4mm 5mm;
  border-left: 4px solid #8B6FE0;
  background: #F7F5FD;
  border-radius: 0 8px 8px 0;
  font-size: 10.5pt;
}
blockquote p:last-child { margin-bottom: 0; }

table {
  width: 100%;
  border-collapse: collapse;
  margin: 4mm 0 6mm;
  font-size: 9.5pt;
  page-break-inside: avoid;
}
th, td {
  text-align: left;
  vertical-align: top;
  padding: 2.6mm 3mm;
  border-bottom: 1px solid rgba(27,42,91,0.12);
}
th { background: #F3F1FA; font-weight: 700; }

/*
   The markdown uses --- as a section rule, not a page break. Forcing a break
   at every one left half-empty pages and stranded headings; the h2 rule above
   already separates sections visually.
*/
hr { border: 0; height: 0; margin: 6mm 0 0; }

/* The clinician's sheet: rows to write on, not a score. */
table.sheet td:last-child { height: 11mm; }

img { max-width: 100%; }
figure { margin: 6mm 0; page-break-inside: avoid; text-align: center; }

em { color: #4A5578; }

.footnote {
  margin-top: 10mm;
  padding-top: 4mm;
  border-top: 1px solid rgba(27,42,91,0.12);
  font-size: 8.5pt;
  color: #7A839B;
  text-align: center;
}
"""


def build_html(family_id: str) -> str:
    title = FAMILIES[family_id]
    source = os.path.join(MATERIALS, f"{title.lower()}-caderno.md")
    if not os.path.exists(source):
        raise SystemExit(f"{source}: no workbook written for {family_id} yet")

    with open(source, encoding="utf-8") as f:
        text = f.read()

    # The cover replaces the markdown title block, so drop it rather than
    # printing the same words twice.
    text = re.sub(r"\A#\s.*?\n---\n", "", text, count=1, flags=re.S)

    body = markdown.markdown(text, extensions=["tables", "sane_lists"])

    # Resolve image paths against the materials folder so Chromium can load them.
    body = body.replace('src="figuras/', f'src="file://{MATERIALS}/figuras/')

    cover = os.path.join(MATERIALS, "figuras", f"{family_id}-capa.png")
    band = "".join(f'<span style="background:{c}"></span>' for c in BAND)

    return f"""<!doctype html>
<html lang="pt-PT"><head><meta charset="utf-8">
<title>{title} — Caderno de aplicação</title>
<style>{CSS}</style></head>
<body>
  <div class="cover"><img src="file://{cover}" alt=""></div>
  <div class="band">{band}</div>
  <h1>{title} — Caderno de aplicação</h1>
  {body}
  <p class="footnote">colorhugs.pt · Material licenciado · Uso profissional</p>
</body></html>"""


def build(family_id: str) -> str:
    from playwright.sync_api import sync_playwright

    html = build_html(family_id)
    scratch = os.path.join(MATERIALS, f".{family_id}-workbook.html")
    with open(scratch, "w", encoding="utf-8") as f:
        f.write(html)

    target = os.path.join(MATERIALS, f"{FAMILIES[family_id].lower()}-caderno.pdf")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file://{scratch}", wait_until="networkidle")
        page.pdf(
            path=target,
            format="A4",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            display_header_footer=False,
        )
        browser.close()
    os.remove(scratch)
    return target


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "angry"
    if which not in FAMILIES:
        raise SystemExit(f"unknown family: {which}")
    print(build(which))
