#!/usr/bin/env python3
"""
Build the two assembled teacher pieces: the poster and the schema cards.

**Neither has any new content.** The poster is the seven families and their fine
words, which exist; the cards are the six schema figures, which exist and are
currently trapped inside a workbook page. Somebody explaining the avoidance cycle
to a parent wants it on the table, not on page seven of a PDF.

    python3 scripts/build-teacher-extras.py poster
    python3 scripts/build-teacher-extras.py cartoes

**The poster is A3 and the cards are A5 two-up on A4.** A3 because a poster read
from four metres has to be, and A5 because a card held in one hand while talking
has to be — printed two to a page so a colleague with an ordinary printer gets
them without a print shop.

**The cards use the child's version of each figure** (D-189): a table card is
looked at *with* somebody, and the sentence written to the clinician does not
belong on a surface a child can see.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MATERIALS = os.path.join(ROOT, "docs", "materials")
ASSETS = os.path.join(ROOT, "public", "assets")
FIGURAS = os.path.join(MATERIALS, "figuras")
BRANDING = os.path.join(ASSETS, "branding")

BAND = ["#2F6FD0", "#E0619A", "#8B6FE0", "#EF7D3D", "#3FA96B", "#D9911A", "#E0566A"]

# Family, card file, accent, and the fine words. The accents are the same seven
# used everywhere else (D-138), so a poster on a wall reads as the same object
# as the deck on the table.
FAMILIES = [
    ("Zangado", "angry", "#E0566A", "chateado · irritado · furioso"),
    ("Triste", "sad", "#2F6FD0", "desiludido · sozinho · com saudades · magoado"),
    ("Assustado", "scared", "#8B6FE0", "nervoso · preocupado · tímido"),
    ("Envergonhado", "ashamed", "#E0619A", "culpado · arrependido · embaraçado"),
    ("Aborrecido", "bored", "#D9911A", "farto · impaciente · sem vontade"),
    ("Calmo", "calm", "#3FA96B", "tranquilo · descansado · seguro"),
    ("Feliz", "happy", "#EF7D3D", "contente · entusiasmado · orgulhoso · aliviado"),
]

# The six schemas, in the order a clinician meets them. Each card carries the
# child's version of the figure and one line saying what it shows.
CARDS = [
    ("Zangado", "#E0566A", "zangado-curva-crianca.png",
     "A activação sobe depressa e desce devagar. No pico, a conversa não entra — "
     "o que se diz nesse minuto é para depois."),
    ("Triste", "#2F6FD0", "triste-caminhos-crianca.png",
     "As duas linhas acabam no mesmo sítio. Com companhia, a tristeza não passa "
     "mais depressa — fica mais fácil de carregar."),
    ("Assustado", "#8B6FE0", "assustado-evitamento-crianca.png",
     "Quando se foge, há alívio logo e o medo vem maior da próxima vez. Quando "
     "se fica um bocadinho, custa mais no momento e vem menor."),
    ("Envergonhado", "#E0619A", "envergonhado-ciclo-crianca.png",
     "Enquanto ninguém souber, ninguém pode desmentir. A saída passa por alguém "
     "ver e ficar."),
    ("Aborrecido", "#D9911A", "tedio-tempo-crianca.png",
     "Quando se enche o vazio logo, o desconforto acaba e nada sai dali. A parte "
     "que custa é o princípio, não o todo."),
    ("Feliz", "#EF7D3D", "feliz-formas-crianca.png",
     "Quando a carga está toda na espera, quase não se aproveita e o buraco a "
     "seguir é fundo. O buraco é normal."),
]

POSTER_CSS = """
@page { size: A3; margin: 16mm; }
/* **A poster is read from four metres**, and the first version printed at the
   size of a page — everything true, everything unreadable across a classroom.
   The body fills the sheet and the type is scaled to the distance. */
html, body { height: 100%; }
body {
  font-family: "Nunito", system-ui, sans-serif;
  color: #1B2A5B;
  margin: 0;
  display: flex;
  flex-direction: column;
}
.band { display: flex; gap: 3mm; margin-bottom: 9mm; }
.band span { height: 5mm; flex: 1; border-radius: 3mm; }

h1 { font-size: 60pt; margin: 0 0 3mm; text-align: center; }
.sub { text-align: center; font-size: 20pt; color: #4C5A85; margin: 0 0 12mm; }

.grid {
  flex: 1;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 6mm 12mm;
  align-content: stretch;
}
/* The seventh sits alone on the last row and is centred across both columns,
   because a lone card hugging the left margin reads as a mistake. */
.fam:nth-child(7) { grid-column: 1 / -1; justify-self: center; width: calc(50% - 5mm); }

.fam {
  display: flex;
  gap: 6mm;
  align-items: center;
  border-left: 4mm solid var(--accent);
  padding: 4mm 0 4mm 6mm;
}
.fam img { width: 44mm; height: auto; }
.fam .name { font-size: 30pt; font-weight: 800; margin: 0 0 2mm; }
.fam .words { font-size: 17pt; color: #4C5A85; margin: 0; line-height: 1.35; }

.foot {
  margin-top: 10mm;
  text-align: center;
  font-size: 13pt;
  color: #7A839B;
}
.foot img { width: 42mm; display: block; margin: 0 auto 4mm; }
"""

CARDS_CSS = """
@page { size: A4; margin: 0; }
body {
  font-family: "Nunito", system-ui, sans-serif;
  color: #1B2A5B;
  margin: 0;
}
/* Two A5 cards per A4 sheet, with a cut line between them. */
.sheet { page-break-after: always; height: 297mm; display: flex; flex-direction: column; }
.sheet:last-child { page-break-after: auto; }

.card {
  height: 148.5mm;
  box-sizing: border-box;
  padding: 12mm 14mm;
  display: flex;
  flex-direction: column;
  border-top: 5mm solid var(--accent);
}
.card + .card { border-top: 5mm solid var(--accent); }
.cut { border-top: 0.5px dashed #C7CDDB; }

.card h2 { font-size: 20pt; margin: 0 0 1mm; }
.card .kicker {
  font-size: 9.5pt; text-transform: uppercase; letter-spacing: 0.08em;
  color: #8A93A8; margin: 0 0 4mm;
}
.card figure { margin: 0; flex: 1; display: flex; align-items: center; justify-content: center; }
.card figure img { max-width: 100%; max-height: 62mm; object-fit: contain; }
.card p.note { font-size: 11pt; margin: 3mm 0 0; line-height: 1.45; }
.card .brand { font-size: 8.5pt; color: #A6AEC0; margin: 2mm 0 0; }
"""


def poster_html() -> str:
    band = "".join(f'<span style="background:{c}"></span>' for c in BAND)
    fams = "".join(
        f"""<div class="fam" style="--accent:{accent}">
  <img src="file://{ASSETS}/emotions/{slug}.webp" alt="">
  <div>
    <p class="name">{name}</p>
    <p class="words">{words}</p>
  </div>
</div>"""
        for name, slug, accent, words in FAMILIES
    )
    return f"""<!doctype html>
<html lang="pt-PT"><head><meta charset="utf-8"><style>{POSTER_CSS}</style></head>
<body>
  <div class="band">{band}</div>
  <h1>Como Me Sinto?</h1>
  <p class="sub">Sete famílias de sentimentos, e as palavras que vivem dentro delas</p>
  <div class="grid">{fams}</div>
  <div class="foot">
    <img src="file://{BRANDING}/colorhugs-logo.webp" alt="">
    colorhugs.pt · Ricardina Correia · Psicologia Pediátrica
  </div>
</body></html>"""


def cards_html() -> str:
    def card(name, accent, fig, note):
        return f"""<div class="card" style="--accent:{accent}">
  <p class="kicker">O que acontece por dentro</p>
  <h2>{name}</h2>
  <figure><img src="file://{FIGURAS}/{fig}" alt=""></figure>
  <p class="note">{note}</p>
  <p class="brand">colorhugs.pt · Material licenciado</p>
</div>"""

    sheets = []
    for i in range(0, len(CARDS), 2):
        pair = CARDS[i : i + 2]
        inner = card(*pair[0]) + '<div class="cut"></div>' + (
            card(*pair[1]) if len(pair) > 1 else ""
        )
        sheets.append(f'<section class="sheet">{inner}</section>')
    return f"""<!doctype html>
<html lang="pt-PT"><head><meta charset="utf-8"><style>{CARDS_CSS}</style></head>
<body>{"".join(sheets)}</body></html>"""


def render(html: str, target: str, fmt: str) -> None:
    from playwright.sync_api import sync_playwright

    scratch = target + ".html"
    with open(scratch, "w", encoding="utf-8") as fh:
        fh.write(html)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file://{scratch}", wait_until="networkidle")
        page.pdf(path=target, format=fmt, print_background=True)
        browser.close()
    os.remove(scratch)


def main() -> None:
    which = sys.argv[1] if len(sys.argv) > 1 else "poster"
    if which == "poster":
        out = os.path.join(MATERIALS, "professores-poster.pdf")
        render(poster_html(), out, "A3")
    elif which == "cartoes":
        out = os.path.join(MATERIALS, "professores-cartoes.pdf")
        render(cards_html(), out, "A4")
    else:
        raise SystemExit("try: poster | cartoes")
    print(out)


if __name__ == "__main__":
    main()
