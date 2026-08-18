#!/usr/bin/env python3
"""Constrói *Antes de Precisar* — o livro dos pais (D-325).

    python3 scripts/build-parents-book-pdf.py

Dois PDF de uma só fonte, `docs/materials/livro-pais.md`:

`antes-de-precisar-leitura.pdf`
    Páginas A5 pela ordem de leitura, para ecrã ou para imprimir simplesmente
    frente e verso.

`antes-de-precisar-impressao.pdf`
    A folha de instruções e as folhas A4 já impostas para dobrar e agrafar,
    pela mesma mecânica do livro ilustrado.

**A parte de cima do markdown não é o livro.** O ficheiro começa com a estrutura,
a espinha e as regras de escrita, que são notas para quem escreve. O livro
começa em `# O que este livro não faz`, e é daí que este construtor lê.

**Cada capítulo abre com a figura da sua família**, tirada do baralho. Não se
gera arte nenhuma: as sete existem.
"""

import os
import re
import subprocess
import sys

import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MATERIALS = os.path.join(ROOT, "docs", "materials")
EMOTIONS = os.path.join(ROOT, "artwork", "emotions")
FONTS = os.path.join(ROOT, "assets", "fonts")
BRANDING = os.path.join(ROOT, "public", "assets", "branding")

SOURCE = os.path.join(MATERIALS, "livro-pais.md")
START = "# O que este livro não faz"

TITLE = "Antes de Precisar"
SUBTITLE = "Os sete sentimentos, e o que um adulto pode fazer com eles"

# A figura que abre cada capítulo, pela ordem do livro: o depósito primeiro.
OPENERS = {
    "1": "calm.png",
    "2": "happy.png",
    "3": "angry.png",
    "4": "sad.png",
    "5": "scared.png",
    "6": "ashamed.png",
    "7": "bored.png",
}


_WORK = None


def transparent(name):
    """Cópia da figura do baralho com o fundo branco tornado transparente.

    As cartas foram desenhadas para fundo branco e trazem o rebordo de
    autocolante. Colocadas numa página creme, **cada uma aparece dentro do seu
    quadrado branco** — sete rectângulos numa capa que não os tem. O desenho não
    se toca: retira-se o fundo.
    """
    global _WORK
    import tempfile

    from PIL import Image

    if _WORK is None:
        _WORK = tempfile.mkdtemp(prefix="colorhugs-livro-pais-")
    out = os.path.join(_WORK, name)
    if os.path.exists(out):
        return out

    im = Image.open(os.path.join(EMOTIONS, name)).convert("RGBA")
    px = im.load()
    w, h = im.size
    # Preenchimento a partir das bordas: só o branco ligado ao exterior sai. O
    # branco dos olhos fica, porque não toca na berma.
    fila = [(x, y) for x in range(w) for y in (0, h - 1)]
    fila += [(x, y) for y in range(h) for x in (0, w - 1)]
    visto = set()
    while fila:
        x, y = fila.pop()
        if (x, y) in visto or not (0 <= x < w and 0 <= y < h):
            continue
        visto.add((x, y))
        r, g, b, a = px[x, y]
        if r < 232 or g < 232 or b < 232:
            continue
        px[x, y] = (r, g, b, 0)
        fila += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    im.save(out)
    return out


def chapters():
    """O livro, partido em capítulos, a partir do markdown."""
    if not os.path.exists(SOURCE):
        sys.exit(f"{SOURCE}: o livro não está escrito")
    text = open(SOURCE, encoding="utf-8").read()
    if START not in text:
        sys.exit(f"{SOURCE}: falta a abertura «{START}»")
    body = START + text.split(START, 1)[1]

    out = []
    for block in re.split(r"\n(?=# )", body):
        heading = block.split("\n", 1)[0].lstrip("# ").strip()
        rest = block.split("\n", 1)[1] if "\n" in block else ""
        rest = rest.replace("\n---\n", "\n")
        number = re.match(r"(\d+)\.", heading)
        out.append({
            "number": number.group(1) if number else None,
            "title": re.sub(r"^\d+\.\s*", "", heading),
            "html": markdown.markdown(rest.strip()),
        })
    return out


CSS = """
@font-face { font-family: "ColorHugs Text"; font-weight: 500;
  src: url("file://%(f)s/Nunito-Medium.ttf") format("truetype"); }
@font-face { font-family: "ColorHugs Text"; font-weight: 700;
  src: url("file://%(f)s/Nunito-Bold.ttf") format("truetype"); }
@font-face { font-family: "ColorHugs Display"; font-weight: 700;
  src: url("file://%(f)s/Baloo2-Bold.ttf") format("truetype"); }

@page { size: 148mm 210mm; margin: 17mm 15mm 16mm; }
@page :first { margin: 0; }

* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  font-family: "ColorHugs Text", system-ui, sans-serif;
  font-weight: 500; font-size: 10.6pt; line-height: 1.58; color: #3a332b;
  -webkit-print-color-adjust: exact;
}
p { margin: 0 0 3.2mm 0; text-align: left; hyphens: none; }
strong { font-weight: 700; }
em { font-style: italic; }

/* Capa ------------------------------------------------------------------- */
.cover {
  width: 148mm; height: 210mm; page-break-after: always;
  background: #f6ece0; padding: 30mm 16mm 16mm;
  display: flex; flex-direction: column; align-items: center;
  text-align: center;
}
.cover h1 {
  font-family: "ColorHugs Display", sans-serif; font-weight: 700;
  font-size: 33pt; line-height: 1.08; margin: 0 0 6mm 0; color: #4a3a28;
}
.cover .sub { font-size: 10.4pt; color: #6a6055; margin: 0 auto auto;
  max-width: 92mm; text-align: center; }
.cover .row { display: flex; gap: 3mm; margin: 6mm 0 8mm; }
.cover .row img { width: 13mm; height: auto; }
.cover .mark { width: 32mm; }

/* Capítulos -------------------------------------------------------------- */
.chapter { page-break-before: always; }
.chapter:first-of-type { page-break-before: avoid; }
.opener { text-align: center; margin: 0 0 8mm 0; }
.opener img { width: 26mm; height: auto; display: block; margin: 0 auto 3mm; }
.opener .num { font-size: 8.6pt; letter-spacing: 1.4px; color: #a08d76;
  text-transform: uppercase; }
.opener h2 {
  font-family: "ColorHugs Display", sans-serif; font-weight: 700;
  font-size: 17pt; line-height: 1.15; margin: 1.5mm 0 0 0; color: #4a3a28;
}
.chapter > p:first-of-type { font-size: 10.9pt; }
"""


def build_html(cover_only=False):
    caps = chapters()
    figures = "".join(
        f'<img src="file://{transparent(f)}" alt="">' for f in OPENERS.values()
    )
    parts = [f"""
<section class="cover">
  <h1>{TITLE}</h1>
  <p class="sub">{SUBTITLE}</p>
  <div class="row">{figures}</div>
  <img class="mark" src="file://{os.path.join(BRANDING, 'colorhugs-parents.webp')}" alt="">
</section>"""]

    for c in caps:
        opener = ""
        if c["number"]:
            fig = OPENERS.get(c["number"])
            img = f'<img src="file://{transparent(fig)}" alt="">' if fig else ""
            opener = (f'<div class="opener">{img}'
                      f'<div class="num">Capítulo {c["number"]}</div>'
                      f'<h2>{c["title"]}</h2></div>')
        else:
            opener = f'<div class="opener"><h2>{c["title"]}</h2></div>'
        parts.append(f'<section class="chapter">{opener}{c["html"]}</section>')

    if cover_only:
        parts = parts[:1]
    else:
        parts = parts[1:]
    return ("<!doctype html><html lang='pt-PT'><meta charset='utf-8'>"
            f"<style>{CSS % {'f': FONTS}}</style><body>"
            + "".join(parts) + "</body></html>")


RUNNING = """<style>
 .run { width: 100%; margin: 0 15mm; box-sizing: border-box;
        font-family: system-ui, sans-serif; font-size: 7.2pt; color: #a08d76;
        display: flex; justify-content: space-between; }
</style>"""


def render(html, target, footer=True):
    from playwright.sync_api import sync_playwright

    scratch = target + ".html"
    with open(scratch, "w", encoding="utf-8") as f:
        f.write(html)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("file://" + scratch, wait_until="networkidle")
        page.pdf(
            path=target, print_background=True, prefer_css_page_size=True,
            display_header_footer=footer,
            header_template="<div></div>",
            footer_template=RUNNING + '<div class="run">'
            f"<span>{TITLE} · colorhugs.pt</span>"
            '<span class="pageNumber"></span></div>',
        )
        browser.close()
    os.remove(scratch)
    return target


def main():
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "bookpdf", os.path.join(ROOT, "scripts", "build-book-pdf.py")
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    reading = os.path.join(MATERIALS, "antes-de-precisar-leitura.pdf")

    # **A capa imprime-se à parte, sem rodapé corrido.** O Chromium aplica o
    # rodapé a todas as páginas ou a nenhuma, e numa capa ele aparece por cima
    # da composição — foi o que saiu na primeira tentativa, com o número de
    # página colado ao endereço.
    cover_pdf = os.path.join(MATERIALS, ".capa-pais.pdf")
    body_pdf = os.path.join(MATERIALS, ".corpo-pais.pdf")
    render(build_html(cover_only=True), cover_pdf, footer=False)
    render(build_html(), body_pdf)
    subprocess.run(["pdfunite", cover_pdf, body_pdf, reading], check=True)
    os.remove(cover_pdf)
    os.remove(body_pdf)

    from pypdf import PdfReader

    pages = len(PdfReader(reading).pages)
    if pages % 4:
        # **Um caderno agrafado ao centro exige múltiplo de quatro.** Em vez de
        # falhar, acrescentam-se páginas em branco no fim, que é o que uma
        # gráfica faria — e o livro impresso acaba com uma ou duas folhas
        # limpas em vez de acabar a meio de uma folha.
        blanks = 4 - pages % 4
        print(f"  {pages} páginas — acrescentadas {blanks} em branco no fim")
        from pypdf import PdfWriter

        w = PdfWriter()
        for p in PdfReader(reading).pages:
            w.add_page(p)
        for _ in range(blanks):
            w.add_blank_page(width=w.pages[0].mediabox.width,
                             height=w.pages[0].mediabox.height)
        with open(reading, "wb") as f:
            w.write(f)
        pages += blanks

    mod.PAGE_COUNT = pages
    instr = os.path.join(MATERIALS, ".instrucoes-pais.pdf")
    sheets = pages // 4
    mod.render(
        mod.INSTRUCTIONS
        .replace("Quem És Tu?", TITLE)
        .replace("as <strong>páginas 2 a 11</strong>: cinco folhas A4",
                 f"as <strong>páginas 2 a {pages // 2 + 1}</strong>: "
                 f"{sheets} folhas A4")
        .replace("de vinte páginas", f"de {pages} páginas")
        .replace("Imprima as páginas 2 a 11", f"Imprima as páginas 2 a {pages // 2 + 1}")
        .replace("<strong>2, 4, 6, 8 e 10</strong>",
                 "<strong>pares</strong>")
        .replace("<strong>3, 5, 7, 9 e 11</strong>",
                 "<strong>ímpares a partir da 3</strong>")
        .replace("Cinco folhas A4", f"{sheets} folhas A4"),
        instr, fmt="A4",
    )

    printing = os.path.join(MATERIALS, "antes-de-precisar-impressao.pdf")
    mod.impose(reading, printing, instr)
    os.remove(instr)

    if _WORK:
        import shutil
        shutil.rmtree(_WORK, ignore_errors=True)

    for f in (reading, printing):
        print(f"{os.path.basename(f)}  {os.path.getsize(f) // 1024} KB")


if __name__ == "__main__":
    main()
