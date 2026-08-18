#!/usr/bin/env python3
"""
Build a teacher document.

    python3 scripts/build-teacher-pages.py sala
    python3 scripts/build-teacher-pages.py vocabulario

**One builder, two documents.** The second was going to be a copy of the first
with a different cover; a copy is two files that drift apart the first time a
margin changes.

**A separate builder, and deliberately so.** The workbook builder knows about
families, evidence gradings, session records and child sheets; none of that
exists here. Bending it to also produce a teacher document would have meant
threading a second mode through every function in it.

Governed by D-289: **o professor não trata, nomeia.** There is no worksheet in
this document, no question addressed to a child, and no box to fill in. What
there is, on every page, is the same five headings — and the same order, because
a teacher with thirty children does not read seven different structures.

"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MATERIALS = os.path.join(ROOT, "docs", "materials")
ASSETS = os.path.join(ROOT, "public", "assets")
BRANDING = os.path.join(ASSETS, "branding")

BAND = ["#2F6FD0", "#E0619A", "#8B6FE0", "#EF7D3D", "#3FA96B", "#D9911A", "#E0566A"]

CSS = """
@page { size: A4; }

body {
  font-family: "Nunito", system-ui, sans-serif;
  color: #1B2A5B;
  font-size: 11.5pt;
  line-height: 1.5;
  margin: 0;
}

.sheet {
  page-break-after: always;
  display: flex;
  flex-direction: column;
}
.sheet:last-child { page-break-after: auto; }

h2 {
  font-size: 20pt;
  margin: 0 0 5mm;
  color: #1B2A5B;
}

h3 {
  page-break-after: avoid;
  font-size: 12pt;
  margin: 5mm 0 1.5mm;
  color: #4C5A85;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

p { margin: 0 0 2.6mm; }
p.lead { font-size: 12.5pt; margin-bottom: 5mm; }

ul { margin: 0 0 2mm; padding-left: 6mm; }
li { margin-bottom: 1.3mm; }

/*
  The character card beside the framing paragraph — the same composition the
  child's sheets use, so a teacher who has seen the deck recognises the page.
*/
.pe { display: flex; gap: 6mm; align-items: flex-start; margin-bottom: 3mm; }
.pe-card img { width: 30mm; height: auto; }
.pe-text { flex: 1; }
.pe-text p { margin: 0; }

/*
  **The line a teacher can actually use**, and the reason this document exists
  in the shape it does: five seconds, in the middle of a lesson, is what there
  is. It is set apart because it is what gets photocopied and stuck inside a
  planner.
*/
.teacher-line {
  page-break-inside: avoid;
  background: #F4F1FB;
  border-left: 3px solid #8B6FE0;
  padding: 3mm 5mm;
  margin: 1mm 0 2mm;
  font-size: 12.5pt;
}

/* Kept whole: the last page's callout was splitting across the page break, and
   an escalation instruction cut in half is the one place that cannot happen. */
.callout {
  page-break-inside: avoid;
  background: #FDF2F4;
  border-left: 3px solid #E0566A;
  padding: 4mm 5mm;
  margin-top: 4mm;
}
.callout p { margin: 0; font-size: 11pt; }
/* The same box in green, for the ones that are advice rather than a limit. A
   teacher who sees every aside in warning red stops reading the red ones. */
.callout.ok { background: #EEF8F1; border-left-color: #3FA96B; }

table.vocab {
  width: 100%;
  border-collapse: collapse;
  margin: 2mm 0 4mm;
  font-size: 11pt;
}
table.vocab th {
  text-align: left;
  font-size: 9.5pt;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #4C5A85;
  border-bottom: 1px solid #D8DCE6;
  padding: 0 3mm 1.5mm 0;
}
table.vocab td {
  padding: 2mm 3mm 2mm 0;
  border-bottom: 0.5px solid #E8EBF2;
  vertical-align: top;
}

p.sign { margin-top: auto; font-size: 10pt; color: #7A839B; font-style: italic; }

.band { display: flex; gap: 2mm; margin-bottom: 6mm; }
.band span { height: 3mm; flex: 1; border-radius: 2mm; }

/* The cover, printed with the band and nothing else. */
.cover {
  page-break-after: always;
  min-height: 245mm;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}
.cover h1 { font-size: 30pt; margin: 0 0 2mm; }
.cover .sub { font-size: 14pt; color: #4C5A85; margin-bottom: 10mm; }
.cover .rule { font-size: 13pt; color: #8B6FE0; font-weight: 700; margin-bottom: 12mm; }
.cover img.logo { width: 46mm; margin: 0 auto; }
.cover .foot { font-size: 10pt; color: #7A839B; margin-top: 12mm; }
"""

RUNNING = """
<style>
  .run { width: 100%; margin: 0 14mm; box-sizing: border-box;
         font-family: system-ui, sans-serif; font-size: 8pt; color: #8A93A8; }
  .run .rule { border-top: 0.5px solid #D8DCE6; padding-top: 2mm;
               display: flex; justify-content: space-between; }
</style>
"""

HEADER = RUNNING + '<div class="run"></div>'
FOOTER = (
    RUNNING
    + '<div class="run"><div class="rule">'
    + "<span>colorhugs.pt · Material licenciado · Para professores</span>"
    + '<span class="pageNumber"></span></div></div>'
)


DOCS = {
    "sala": {
        "stem": "professores-sala",
        "title": "Como Me Sinto?",
        "sub": "Sete emoções na sala de aula",
        "rule": "O professor não trata — nomeia.",
    },
    "vocabulario": {
        "stem": "professores-vocabulario",
        "title": "As Palavras dos Sentimentos",
        "sub": "Vocabulário emocional para a sala de aula",
        "rule": "Isto é conteúdo de língua, e não é terapia.",
    },
}


def cover_html(doc: dict) -> str:
    band = "".join(f'<span style="background:{c}"></span>' for c in BAND)
    logo = f"file://{BRANDING}/colorhugs.webp"
    return f"""<section class="cover">
  <div class="band">{band}</div>
  <h1>{doc["title"]}</h1>
  <p class="sub">{doc["sub"]}</p>
  <p class="rule">{doc["rule"]}</p>
  <img class="logo" src="{logo}" alt="">
  <p class="foot">colorhugs.pt · Ricardina Correia · Psicologia Pediátrica</p>
</section>"""


def load(doc: dict) -> str:
    src = os.path.join(MATERIALS, doc["stem"] + ".html")
    with open(src, encoding="utf-8") as fh:
        raw = fh.read()
    parts = re.findall(r"<section class=\"sheet\".*?</section>", raw, re.S)
    if not parts:
        raise SystemExit(f"no sections found in {doc['stem']}.html")
    body = "\n".join(parts)
    return body.replace("ASSETS/", f"file://{ASSETS}/")


def render(html: str, target: str) -> None:
    """Print to PDF with Playwright, the same way the workbooks are printed.

    A first version shelled out to a Node script that does not exist in this
    repository — the workbooks use Playwright directly, and copying their
    approach means one browser toolchain rather than two.
    """
    from playwright.sync_api import sync_playwright

    scratch = target + ".html"
    with open(scratch, "w", encoding="utf-8") as fh:
        fh.write(html)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file://{scratch}", wait_until="networkidle")
        page.pdf(
            path=target,
            format="A4",
            print_background=True,
            margin={"top": "16mm", "right": "16mm", "bottom": "16mm", "left": "16mm"},
            display_header_footer=True,
            header_template=HEADER,
            footer_template=FOOTER,
        )
        browser.close()
    os.remove(scratch)


def main() -> None:
    which = sys.argv[1] if len(sys.argv) > 1 else "sala"
    if which not in DOCS:
        raise SystemExit(f"unknown document: {which} (try {', '.join(DOCS)})")
    doc = DOCS[which]

    html = f"""<!doctype html>
<html lang="pt-PT"><head><meta charset="utf-8">
<title>{doc["title"]} — {doc["sub"]}</title>
<style>{CSS}</style></head>
<body>{cover_html(doc)}{load(doc)}</body></html>"""

    out = os.path.join(MATERIALS, doc["stem"] + ".pdf")
    render(html, out)
    print(out)


if __name__ == "__main__":
    main()
