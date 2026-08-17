#!/usr/bin/env python3
"""
Build a practitioner workbook as a printable PDF.

The markdown is where the content is written and reviewed; **the PDF is what a
colleague actually buys.** A licensed material that arrives as a `.md` file is
a draft, however good the writing.

    python3 scripts/build-workbook-pdf.py angry

Produces **two files from one source** (D-172): the whole workbook, and the
child's sheets alone. Handing a sheet to a child should not mean printing a page
that carries evidence gradings.

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
ASSETS = os.path.join(ROOT, "public", "assets")
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
/*
  Margins are set by Chromium at print time, not here, because the running
  header and footer live in that margin. The cover is printed separately with
  no margin at all — see `render`.
*/

* { box-sizing: border-box; }

body {
  margin: 0;
  color: #1B2A5B;
  font-family: "DejaVu Sans", system-ui, sans-serif;
  font-size: 9.2pt;
  line-height: 1.55;
}

.band { display: flex; gap: 5px; margin: 0 0 14mm; }
.band span { height: 7px; flex: 1; border-radius: 4px; }

h1 { font-size: 17pt; margin: 0 0 4mm; line-height: 1.25; }
h2 {
  font-size: 12.5pt;
  margin: 10mm 0 3mm;
  padding-top: 4mm;
  border-top: 1.5px solid rgba(27,42,91,0.14);
  page-break-after: avoid;
  break-after: avoid;
}
/* A heading alone at the foot of a page is a heading pointing at nothing. */
h2 + p, h2 + ul, h2 + table, h3 + p, h3 + ul { break-before: avoid; }
h3 {
  font-size: 10.2pt;
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
  font-size: 9.2pt;
}
blockquote p:last-child { margin-bottom: 0; }

table {
  width: 100%;
  border-collapse: collapse;
  margin: 4mm 0 6mm;
  font-size: 8.8pt;
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

/* The clinical record: rows to write on, not a score. Two columns means the
   right-hand one is the writing space; three means the middle is a label. */
/*
   The clinical record. Its tables have no headings, so the empty header row was
   printing as a grey stripe — and the writing cells had no border at all, which
   is a form to fill in with nowhere to write.
*/
table thead:empty,
table tr:empty { display: none; }
/* A heading row whose cells are all blank prints as a grey stripe. */
table thead:has(th:empty) { visibility: collapse; }
table th:first-child { width: 38%; }
.record table { border: 1px solid rgba(27,42,91,0.22); }
.record th, .record td {
  border: 1px solid rgba(27,42,91,0.18);
  padding: 2.4mm 3mm;
}
.record td:last-child:empty { height: 9mm; background: #FAF9FE; }
/* The session-note table is one wide column of writing space. */
.record table + table td:empty { height: 12mm; }
.record h3 { margin-top: 6mm; }

/*
   One guide, one page. A colleague looking up sheet nine should not find the
   limits section halfway down it — and a guide split across two pages is worse
   still, because the record box lands away from the guidance it belongs to.
*/
.guide { break-before: page; break-inside: avoid; font-size: 8.4pt; }
.guide h3 { margin-top: 0; margin-bottom: 2mm; }
.guide h3 + table { margin-top: 0; }
.guide table { margin-top: 1.5mm; margin-bottom: 3mm; font-size: 8.4pt; }
.guide th, .guide td { padding: 1.6mm 2.5mm; }
.guide p { margin-bottom: 1.5mm; }
.guide ul { margin-bottom: 3mm; }
.guide li { margin-bottom: 1mm; }
/* The record must land on the same page as the guidance it belongs to. */
.guide .record td:last-child:empty { height: 7mm; }
.guide .record table + table td:empty { height: 9mm; }
.guide + h2, .guide ~ h2 { break-before: page; }

img { max-width: 100%; }
figure { margin: 6mm 0; page-break-inside: avoid; text-align: center; }

em { color: #4A5578; }

/* ---- the sheets ------------------------------------------------------
   A sheet fills a page and is printed alone. Everything on it is sized for a
   child's hand: rows tall enough to write in, lines far enough apart.
*/
.sheet { page-break-before: always; page-break-inside: avoid; }
.sheet h2 {
  border: 0;
  margin: 0 0 1mm;
  padding: 0;
  font-size: 20pt;
}
.sheet .age {
  display: inline-block;
  margin-bottom: 5mm;
  padding: 1mm 3mm;
  border-radius: 99px;
  background: #F3F1FA;
  color: #5B4F8A;
  font-size: 8.5pt;
  font-weight: 700;
}
/* The sheets are read by a child and set larger than the workbook around
   them. */
.sheet { font-size: 10.5pt; line-height: 1.65; }
.sheet .lead { font-size: 11.5pt; margin-bottom: 6mm; }
.sheet h3 { margin: 5mm 0 1.5mm; font-size: 11pt; }
/*
   The guidance page is dense prose rather than fields, so it sets tighter. It
   was spilling a few lines onto a fifth page, which put one paragraph alone on
   a sheet — worse than a slightly closer page.
*/
.sheet[data-kind="guidance"] { font-size: 9.8pt; line-height: 1.55; }
.sheet[data-kind="guidance"] .lead { font-size: 10.5pt; margin-bottom: 4mm; }
.sheet[data-kind="guidance"] h3 { margin: 4mm 0 1.2mm; }
.sheet[data-kind="guidance"] .lines { min-height: 26mm; }

/* Fields, not data: the rows are empty and tall enough to write in. */
/* Rows tall enough for a child's handwriting, and enough of them to fill the
   sheet — a half-empty worksheet reads as an unfinished one. */
/* Rows tall enough to draw in, and enough of them to fill the sheet. */
table.fill td { height: 26mm; border: 1px solid rgba(27,42,91,0.28); }
/* A one-row table is not a table with room: the ladder's single row has to
   take a drawing, so it gets the height four rows would have had. */
table.fill.one-row td { height: 62mm; }
table.fill th {
  background: #F3F1FA;
  border: 1px solid rgba(27,42,91,0.28);
  font-size: 9.5pt;
}
/* Each column says what goes in it, and that it may be drawn. */
table.fill th em {
  display: block;
  margin-top: 0.8mm;
  font-weight: 400;
  font-size: 8pt;
  color: #7A839B;
}

/*
   Boxes rather than ruled lines.
   
   Ruled lines only accept writing, and that shuts out the youngest children —
   and, more to the point, any child with a written-language difficulty, who is
   exactly the child a psychologist has in front of her. An empty box takes a
   sentence or a drawing without choosing between them (D-185).

   `data-lines` survives as the measure of how much room to give: the box is
   about as tall as that many written lines would have been.
*/
/*
   One treatment everywhere: a warm fill *and* an outline.

   The fill alone was gentler but vanished in a black-and-white photocopy, which
   is how much of this will be printed. The outline alone was a cold grey
   rectangle. Together they survive the photocopier and still look like they
   belong to this project (D-186).

   A motif in the corner was tried and rejected: it looked good and it quietly
   took that corner away from the child.
*/
.lines {
  margin: 3mm 0 0;
  display: flex;
  min-height: 22mm;
}
.lines > div { flex: 1; }
.lines div {
  border: 1.5px solid rgba(27,42,91,0.28);
  border-radius: 5mm;
  background: #F7F5FD;
}

.ask { margin-top: 6mm; font-weight: 700; }

/*
  The artwork is where the child draws, so it takes every millimetre the rest of
  the page does not need. The sheet is a column; the figure is the part that
  stretches.
*/
/*
   A definite height, not a minimum: the drawing figure sizes itself against it,
   and a percentage height inside a flex column needs the parent to be definite
   or the image grows until the sheet spills onto a second page. It did.
   A4 less the printed margins is 260mm.
*/
.sheet { display: flex; flex-direction: column; height: 256mm; overflow: hidden; }
/* Prompts keep their natural size; boxes take everything that is left. */
.sheet > .ask, .sheet > h2, .sheet > h3, .sheet > .lead,
.sheet > .cards, .sheet > p { flex: 0 0 auto; }
figure.art {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 4mm 0;
  min-height: 0;
}
figure.art img { max-height: 100%; max-width: 100%; object-fit: contain; }
/* A tall figure may use the full width; the bubbles are portrait. */
figure.art.tall img { max-height: 100%; width: auto; }
/* The processed artwork is transparent; nothing should sit behind it. */
figure.art img { background: transparent; }
.boxed { flex: 1; display: flex; flex-direction: column; justify-content: center; }

.box-labels {
  display: flex;
  gap: 4mm;
  margin-top: -3mm;
}
.box-labels span {
  flex: 1;
  text-align: center;
  font-weight: 700;
  font-size: 11pt;
}
.under-arrow {
  margin-top: 2mm;
  text-align: center;
  font-size: 9.5pt;
  color: #5B4F8A;
}

/*
  The identity page asks for a first name and an age, and nothing else. No
  surname, no school, no address: a sheet a child carries between a clinic and a
  home should not be able to identify her to whoever finds it.
*/
.id-fields { display: flex; gap: 8mm; margin: 4mm 0 2mm; }
.id-fields label {
  flex: 1;
  font-weight: 700;
  font-size: 10.5pt;
  color: #5B4F8A;
}
.id-fields label span {
  display: block;
  margin-top: 2mm;
  height: 11mm;
  border-bottom: 1px solid rgba(27,42,91,0.28);
}
.identity .lead { margin-bottom: 2mm; }


/* Emotion cards on a sheet: the same figure the child met on screen, so the
   paper and the app are recognisably one thing. */
.cards { display: flex; gap: 6mm; margin: 4mm 0 2mm; }
.cards figure { flex: 1; margin: 0; text-align: center; }
/* A stretched figure is a fat figure: the card keeps its proportions and the
   caption box below it takes the leftover height instead. */
.cards img { object-fit: contain; align-self: center; }
.cards.three img { max-height: 38mm; }
.cards { flex: 1; }
.cards.five { gap: 3mm; }
.cards.five img { max-height: 30mm; }
.cards.five figcaption { font-size: 8.5pt; }
/* Four fine words instead of three (sad), and six figures on the company
   sheet. Smaller than .three so the row still leaves the child room to write
   beneath it. */
.cards.four img { max-height: 30mm; }
.cards.four figcaption { font-size: 9.5pt; }
.cards.six { flex-wrap: wrap; gap: 3mm; }
.cards.six figure { flex: 0 0 30%; }
.cards.six img { max-height: 30mm; }
.cards.six figcaption { font-size: 9pt; }
.cards.one { justify-content: center; }
.cards.one img { max-height: 62mm; }
.cards figcaption {
  margin-top: 1mm;
  font-weight: 700;
  font-size: 10.5pt;
}
.cards figure { display: flex; flex-direction: column; }
.cards .lines { margin-top: 2mm; flex: 1; }

/* The hint says what the box is for, quietly enough to write over. */
.lines div { position: relative; }
.hint {
  position: absolute;
  top: 2mm;
  left: 3mm;
  color: #A6ADBE;
  font-size: 8.5pt;
  font-style: italic;
}

/*
   EXPERIMENT (D-186). Two ways of softening a box, to be compared on paper.

   `soft`   — nothing inside; only the outline changes, warmer and rounder.
   `corner` — one small motif in a corner, well clear of the middle.

   The middle of every box stays empty either way: that is where the child
   draws, and anything printed there competes with her and tells her where she
   may not go.
*/


/* Psychoeducation pages: a card beside the text, then a figure. Not fields,
   so they set closer than a worksheet. */
.pe { display: flex; gap: 6mm; align-items: center; margin: 3mm 0 2mm; }
.pe-card { flex: 0 0 44mm; margin: 0; }
.pe-card img { width: 100%; }
.pe-text { flex: 1; font-size: 11pt; }
.pe-text p { margin-bottom: 2.5mm; }
.pe-curve { flex: 1; margin: 2mm 0; display: flex; align-items: center;
            justify-content: center; min-height: 0; }
.pe-curve img { max-height: 100%; max-width: 100%; object-fit: contain; }
/* The schema was drawn for the workbook and carries a line addressed to the
   clinician — *mesmo que ela ache que não*. On the child's page that line talks
   over her head, so the figure is cropped to the curve itself. */
.pe-curve { overflow: hidden; }
.pe-close { font-size: 11pt; margin-top: 2mm; }

ul.tips { margin: 2mm 0 3mm; padding-left: 5mm; font-size: 10pt; }
ul.tips li { margin-bottom: 2mm; }
/* The letter reads, it does not instruct: longer measure, warmer leading, and
   no bulleted advice. */
.sheet[data-kind="letter"] { font-size: 11pt; line-height: 1.75; }
.sheet[data-kind="letter"] p { margin-bottom: 4mm; }
.sheet[data-kind="letter"] h3 { margin: 5mm 0 1mm; }
.sheet[data-kind="letter"] .sign {
  margin-top: 5mm;
  font-size: 10pt;
  font-style: italic;
  color: #5B4F8A;
}

ul.prompts { margin-top: 4mm; font-size: 11pt; }
ul.prompts li { margin-bottom: 2.5mm; }

.footnote {
  margin-top: 10mm;
  padding-top: 4mm;
  border-top: 1px solid rgba(27,42,91,0.12);
  font-size: 8.5pt;
  color: #7A839B;
  text-align: center;
}
"""


SHEET_RE = re.compile(r'<section class="sheet".*?</section>', re.S)


def load_sheets(
    family_id: str, audience: str | None = None, show_age: bool = True
) -> str:
    """The sheets, as HTML, from the one file that defines them.

    `audience` selects which are wanted. **What to say to the parents is not in
    the child's book**: it is written for whoever applies the material, and a
    page addressed over a child's head does not belong in something she carries
    home (D-188). The workbook takes everything.
    """
    path = os.path.join(MATERIALS, f"{FAMILIES[family_id].lower()}-fichas.html")
    if not os.path.exists(path):
        # **Refuse, do not return nothing** (D-229). Returning an empty string
        # produced a one-page parents' letter with a header, a footer and no
        # letter, and a three-page exploration book with nothing to explore —
        # files that look finished and are not, which is the fault D-004 exists
        # to prevent, arriving through the build instead of through the data.
        raise SystemExit(
            f"{path}: the sheets for {FAMILIES[family_id]} are not written yet. "
            f"The workbook can be built without them; the child's book and the "
            f"parents' letter cannot."
        )
    with open(path, encoding="utf-8") as f:
        raw = f.read()

    # The file explains itself in an HTML comment; comments are not content.
    raw = re.sub(r"<!--.*?-->", "", raw, flags=re.S)

    out = []
    for sheet in SHEET_RE.findall(raw):
        if audience is not None:
            marked = re.search(r'data-for="([^"]+)"', sheet)
            if (marked.group(1) if marked else "child") != audience:
                continue
        # The age chip is written as an attribute so the sheet source stays
        # readable; it becomes a real element here.
        #
        # **Only in the workbook, never in the child's book** (D-247). The range
        # is a decision for whoever applies the material — and one she may need
        # to override, since a sheet marked 7 to 9 is often exactly right for a
        # six-year-old in front of her. Printed on the sheet the child holds, it
        # does the opposite of helping: a child who reads *7 aos 9 anos* on a
        # page she was given at six has been told she is early, and a child of
        # ten has been told she is late.
        age = re.search(r'data-age="([^"]+)"', sheet)
        if age and show_age:
            sheet = sheet.replace(
                "</h2>", f'</h2><span class="age">{age.group(1)}</span>', 1
            )
        # Ruled writing space, from a count rather than repeated empty divs.
        # An empty box, sized from the number of lines it replaces, and
        # carrying its own hint of what goes in it.
        def box(m):
            """A box that grows.

            `data-lines` is no longer a height in millimetres but a **share**:
            a box asking for three lines gets three times the leftover space of
            one asking for one. The sheet then fills itself, whatever else is on
            it, and a child gets room to draw rather than room to sign her name.
            """
            extra, attrs, lines, hint = m.groups()
            hint = hint or "Escreve ou desenha aqui"
            return (
                f'<div class="lines{extra}" style="flex:{lines}" {attrs.strip()}>'
                f'<div><span class="hint">{hint}</span></div></div>'
            )

        sheet = re.sub(
            r'<div class="lines([^"]*)"([^>]*?)'
            r'data-lines="(\d+)"(?:\s+data-hint="([^"]*)")?[^>]*></div>',
            box,
            sheet,
        )
        out.append(
            sheet.replace("ASSETS/", f"file://{ASSETS}/").replace(
                "FIGURAS/", f"file://{MATERIALS}/figuras/"
            )
        )
    return "\n".join(out)


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

    body = markdown.markdown(
        text, extensions=["tables", "sane_lists", "md_in_html"]
    )

    # Resolve image paths against the materials folder so Chromium can load them.
    body = body.replace('src="figuras/', f'src="file://{MATERIALS}/figuras/')

    # The worksheets are not bound into the workbook: they live in the child's
    # exploration book, and a licence gives both. Printing them twice makes two
    # copies that can drift apart (D-194).
    #
    # **The practitioner pages are the exception, and they were reaching nobody**
    # (D-231). A sheet marked `data-for="practitioner"` is written for whoever
    # applies the material: it is kept out of the child's book because it talks
    # over her head, and out of the parents' letter because it is not addressed
    # to them. It was therefore appearing in no document at all — written,
    # built, and delivered nowhere.
    sheets_file = os.path.join(
        MATERIALS, f"{FAMILIES[family_id].lower()}-fichas.html"
    )
    practitioner = (
        load_sheets(family_id, "practitioner")
        if os.path.exists(sheets_file)
        else ""
    )
    if practitioner:
        # Last, as an annex. No heading is added: the sheet carries its own
        # title, and a second one would print the same words twice.
        body += practitioner

    band = "".join(f'<span style="background:{c}"></span>' for c in BAND)

    # **The closing footnote goes inside the last sheet, not after it.**
    # Standing on its own after a full-page annex, it opened a page of its own
    # and printed a single grey line on an otherwise blank sheet — in both
    # families, and unnoticed since the angry build.
    footnote = '<p class="footnote">colorhugs.pt · Material licenciado · Uso profissional</p>'
    if practitioner and body.rstrip().endswith("</section>"):
        cut = body.rstrip()[: -len("</section>")]
        body = cut + footnote + "</section>"
        footnote = ""

    return f"""<!doctype html>
<html lang="pt-PT"><head><meta charset="utf-8">
<title>{title} — Caderno de aplicação</title>
<style>{CSS}</style></head>
<body>
  <div class="band">{band}</div>
  <h1>{title} — Caderno de aplicação</h1>
  {body}
  {footnote}
</body></html>"""


IDENTITY = """
<section class="sheet identity">
  <h2>Estas fichas são de…</h2>
  <p class="lead">Escreve o teu nome e desenha-te aqui.</p>

  <div class="id-fields">
    <label>Nome<span></span></label>
    <label>Idade<span></span></label>
  </div>

  <!--
    A hand mirror, not the plush frame used by the externalising sheet: the
    same picture on two sheets makes the second look like a repeat, and these
    two ask for opposite things — one for her own face, one for the Anger's.
    A mirror is also what you look into to draw yourself.
  -->
  <figure class="art tall"><img src="ASSETS/worksheets/mirror.png" alt=""></figure>
</section>
"""


def sheets_html(family_id: str) -> str:
    """The child's exploration book.

    No colour band and no licensing footnote: this is what goes on the table
    between a clinician and a child, and nothing on it is addressed to anyone
    else. Its cover carries the plain ColorHugs logo, never the endorsed
    professional lockup — the endorsement is for a colleague (D-190).
    """
    title = FAMILIES[family_id]
    return f"""<!doctype html>
<html lang="pt-PT"><head><meta charset="utf-8">
<title>{title} — Caderno de exploração</title>
<style>{CSS}
.sheet:first-of-type {{ page-break-before: avoid; }}
</style></head>
<body>{IDENTITY.replace("ASSETS/", f"file://{ASSETS}/")}{load_sheets(family_id, "child", show_age=False)}</body></html>"""


RUNNING = """
<style>
  .run {
    width: 100%;
    margin: 0 18mm;
    box-sizing: border-box;
    font-family: system-ui, sans-serif;
    font-size: 7.5pt;
    color: #8A93A8;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .run .rule { border-top: 0.5px solid #D8DCE6; padding-top: 2mm; width: 100%;
               display: flex; justify-content: space-between; }
  .run .top { border-bottom: 0.5px solid #D8DCE6; padding-bottom: 2mm;
              width: 100%; display: flex; justify-content: space-between; }
</style>
"""


def parents_html(family_id: str) -> str:
    """One page, for the family to take home.

    It closes itself: nothing on it asks a question that needs someone there to
    receive the answer (D-095). Everything that opens stays in the workbook.
    """
    title = FAMILIES[family_id]
    return f"""<!doctype html>
<html lang="pt-PT"><head><meta charset="utf-8">
<title>{title} — Para os pais</title>
<style>{CSS}
.sheet:first-of-type {{ page-break-before: avoid; }}
</style></head>
<body>{load_sheets(family_id, "parents")}</body></html>"""


def render(html: str, target: str, title: str, cover: str | None = None) -> str:
    """Print to PDF, with a running header and footer on every page.

    The cover is rendered on its own with no margin and no running elements —
    it is a finished composition, and a header across it would be a caption on a
    painting. The two are then joined.
    """
    from playwright.sync_api import sync_playwright

    scratch = target + ".html"
    with open(scratch, "w", encoding="utf-8") as f:
        f.write(html)

    body_pdf = target if cover is None else target + ".body.pdf"
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file://{scratch}", wait_until="networkidle")
        page.pdf(
            path=body_pdf,
            format="A4",
            print_background=True,
            margin={
                "top": "20mm",
                "right": "18mm",
                "bottom": "17mm",
                "left": "18mm",
            },
            display_header_footer=True,
            header_template=RUNNING
            + f'<div class="run"><div class="top"><span>{title}</span>'
            + "<span>ColorHugs</span></div></div>",
            footer_template=RUNNING
            + '<div class="run"><div class="rule">'
            + "<span>colorhugs.pt · Material licenciado</span>"
            + '<span class="pageNumber"></span></div></div>',
        )
        if cover is not None:
            page.set_content(
                f'<body style="margin:0"><img src="file://{cover}" '
                'style="display:block;width:100%">'
            )
            page.wait_for_timeout(400)
            page.pdf(
                path=target + ".cover.pdf",
                format="A4",
                print_background=True,
                margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            )
        browser.close()
    os.remove(scratch)

    if cover is not None:
        import subprocess

        subprocess.run(
            ["pdfunite", target + ".cover.pdf", body_pdf, target], check=True
        )
        os.remove(target + ".cover.pdf")
        os.remove(body_pdf)
    return target


def build(family_id: str) -> str:
    from playwright.sync_api import sync_playwright

    html = build_html(family_id)
    scratch = os.path.join(MATERIALS, f".{family_id}-workbook.html")
    with open(scratch, "w", encoding="utf-8") as f:
        f.write(html)
    os.remove(scratch)

    stem = FAMILIES[family_id].lower()
    title = FAMILIES[family_id]
    workbook = render(
        html,
        os.path.join(MATERIALS, f"{stem}-caderno.pdf"),
        f"{title} — Caderno de aplicação",
        cover=os.path.join(MATERIALS, "figuras", f"{family_id}-capa.png"),
    )

    # The workbook stands on its own while a family is being written; the
    # child's book and the parents' letter are made of sheets and cannot.
    sheets_file = os.path.join(MATERIALS, f"{stem}-fichas.html")
    if not os.path.exists(sheets_file):
        print(f"  {stem}-fichas.html not written yet — workbook only.")
        return workbook

    sheets = render(
        sheets_html(family_id),
        os.path.join(MATERIALS, f"{stem}-exploracao.pdf"),
        f"{title} — Caderno de exploração",
        cover=os.path.join(MATERIALS, "figuras", f"{family_id}-capa-crianca.png"),
    )
    parents = render(
        parents_html(family_id),
        os.path.join(MATERIALS, f"{stem}-pais.pdf"),
        f"{title} — Para os pais",
    )
    return "\n".join((workbook, sheets, parents))


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "angry"
    if which not in FAMILIES:
        raise SystemExit(f"unknown family: {which}")
    print(build(which))
