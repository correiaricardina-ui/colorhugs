#!/usr/bin/env python3
"""Constrói *Quem És Tu?* a partir das suas fontes (D-314, D-318).

    python3 scripts/build-book-pdf.py

Produz **dois PDF de uma só fonte**:

`quem-es-tu-leitura.pdf`
    Vinte páginas A5 pela ordem de leitura. É o ficheiro para ver no ecrã e para
    rever antes de imprimir.

`quem-es-tu-impressao.pdf`
    A folha de instruções, e a seguir cinco folhas A4 já impostas para dobrar ao
    meio e agrafar. **A família nunca toca no modo de livro da impressora** — a
    imposição já está feita no ficheiro.

**O texto não vive aqui.** As dezasseis cenas vêm de `livro-historia.md` e as
quatro páginas de paratexto de `livro-paratexto.md`. Nos dois ficheiros a regra
de leitura é a mesma: **o que está em citação é o que vai para a página**; o resto
é comentário para quem escreve. Uma tradução muda o markdown e volta a correr
isto.

**As ilustrações não são tocadas.** São colocadas, e mais nada. O nivelamento de
paleta é um passo anterior e separado (`level-book-palette.py`, D-316).
"""

import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MATERIALS = os.path.join(ROOT, "docs", "materials")
ART = os.path.join(ROOT, "artwork", "livro")
BRANDING = os.path.join(ROOT, "public", "assets", "branding")
FONTS = os.path.join(ROOT, "assets", "fonts")

# A página é A5 ao alto. As cenas são 5:4 ao baixo e assentam a 120 mm; a cena 4
# é ao alto e assenta a 107 por 134, que é o que cabe na mesma página com a
# mesma margem e o mesmo bloco de texto (D-317).
SCENE_W_MM = 120
SCENE_4_W_MM = 107

PAGE_COUNT = 20  # dezasseis cenas mais capa, ficha técnica, elenco e contracapa


# --------------------------------------------------------------------------
# Fonte do texto
# --------------------------------------------------------------------------

def quoted_blocks(path, heading_re):
    """Devolve {chave: [parágrafos]} lendo só as linhas em citação.

    O comentário editorial e as notas de ilustração ficam de fora por
    construção, sem precisarem de marcação própria.
    """
    out, key, para, buf = {}, None, [], []
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\n")
            m = heading_re.match(line)
            if m:
                if key and (buf or para):
                    if buf:
                        para.append(" ".join(buf))
                    out[key] = para
                key, para, buf = m.group(1), [], []
                continue
            if key is None:
                continue
            if line.startswith(">"):
                body = line[1:].strip()
                if body:
                    buf.append(body)
                elif buf:
                    para.append(" ".join(buf))
                    buf = []
            elif line.strip() == "" and buf:
                para.append(" ".join(buf))
                buf = []
    if key:
        if buf:
            para.append(" ".join(buf))
        out[key] = para
    return out


def inline(text):
    """Marcação mínima: negrito, itálico e travessão de diálogo."""
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", text)
    return text


def load_text():
    scenes = quoted_blocks(
        os.path.join(MATERIALS, "livro-historia.md"),
        re.compile(r"^##\s+Cena\s+(\d+)"),
    )
    para = quoted_blocks(
        os.path.join(MATERIALS, "livro-paratexto.md"),
        re.compile(r"^##\s+P[áa]gina\s+(\d+)"),
    )
    missing = [n for n in range(1, 17) if str(n) not in scenes]
    if missing:
        sys.exit(f"cenas sem texto em livro-historia.md: {missing}")
    return scenes, para


# --------------------------------------------------------------------------
# Páginas
# --------------------------------------------------------------------------

# As ilustrações entram no PDF a 200 dpi no tamanho em que são colocadas. A
# 297 dpi o ficheiro fica em 30 MB, e **um ficheiro pesado é um obstáculo real
# para quem o vai descarregar em casa** — a 200 dpi fica em metade, e numa
# impressora doméstica, com cor chapada e contorno grosso, não se distingue. Os
# ficheiros originais não são tocados: as cópias vivem numa pasta temporária.
PLACED_MM = {"capa": 148, "cena-04": SCENE_4_W_MM}
PRINT_DPI = 200
_WORK = None


def work_dir():
    global _WORK
    if _WORK is None:
        import tempfile
        _WORK = tempfile.mkdtemp(prefix="colorhugs-livro-")
    return _WORK


def at_print_size(path):
    """Cópia da ilustração reamostrada para o tamanho em que é colocada."""
    from PIL import Image

    # A marca não passa por aqui. Tem transparência, e convertê-la para RGB
    # transformou o fundo transparente em preto nas páginas 2 e 20 — invisível
    # no ficheiro e imediato na página.
    if not os.path.abspath(path).startswith(os.path.abspath(ART)):
        return path

    stem = os.path.splitext(os.path.basename(path))[0]
    out = os.path.join(work_dir(), stem + ".png")
    if os.path.exists(out):
        return out
    im = Image.open(path).convert("RGB")
    mm = PLACED_MM.get(stem, SCENE_W_MM)
    target = round(mm / 25.4 * PRINT_DPI)
    if target < im.width:
        im = im.resize((target, round(im.height * target / im.width)),
                       Image.LANCZOS)
    im.save(out, "PNG", optimize=True)
    return out


def img(path):
    return "file://" + at_print_size(path)


def page_cover(para):
    body = "".join(f"<p>{inline(p)}</p>" for p in para.get("1", []))
    return f"""
<section class="page cover">
  <img class="art" src="{img(os.path.join(ART, 'capa.png'))}">
  <div class="cover-title">{body}</div>
</section>"""


def page_imprint(para):
    body = "".join(f"<p>{inline(p)}</p>" for p in para.get("2", []))
    return f"""
<section class="page plain imprint">
  <div class="block">{body}</div>
  <img class="mark" src="{img(os.path.join(BRANDING, 'colorhugs-parents.webp'))}">
</section>"""


def page_scene(n, paras):
    src = os.path.join(ART, f"cena-{n:02d}.png")
    if not os.path.exists(src):
        sys.exit(f"falta a ilustração {src}")
    cls = "art tall" if n == 4 else "art"
    body = "".join(f"<p>{inline(p)}</p>" for p in paras)
    return f"""
<section class="page scene">
  <div class="art-slot"><img class="{cls}" src="{img(src)}"></div>
  <div class="words">{body}</div>
  <div class="folio">{n + 2}</div>
</section>"""


def page_cast(para):
    body = "".join(f"<p>{inline(p)}</p>" for p in para.get("19", []))
    return f"""
<section class="page plain cast">
  <div class="block">{body}</div>
</section>"""


def page_back(para):
    body = "".join(f"<p>{inline(p)}</p>" for p in para.get("20", []))
    return f"""
<section class="page plain back">
  <div class="block">{body}</div>
  <img class="mark" src="{img(os.path.join(BRANDING, 'colorhugs-parents.webp'))}">
</section>"""


# Instâncias estáticas e não o ficheiro variável. Com a fonte variável o
# Chromium incorpora o texto como Type 3 — contornos desenhados em vez de
# glifos — e o PDF fica maior e pior de ver em alguns leitores. As estáticas
# são geradas a partir do variável por `scripts/make-book-fonts.py`.
FACES = """
@font-face { font-family: "ColorHugs Text"; font-weight: 500;
  src: url("file://%(f)s/Nunito-Medium.ttf") format("truetype"); }
@font-face { font-family: "ColorHugs Text"; font-weight: 700;
  src: url("file://%(f)s/Nunito-Bold.ttf") format("truetype"); }
@font-face { font-family: "ColorHugs Display"; font-weight: 700;
  src: url("file://%(f)s/Baloo2-Bold.ttf") format("truetype"); }
"""


CSS = FACES % {"f": FONTS} + """
@page { size: 148mm 210mm; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  font-family: "ColorHugs Text", system-ui, sans-serif;
  font-weight: 500;
  color: #3a332b;
  -webkit-print-color-adjust: exact;
}
.page {
  width: 148mm; height: 210mm;
  padding: 14mm;
  page-break-after: always;
  position: relative;
  display: flex; flex-direction: column;
  background: #fffdf9;
}
.page:last-child { page-break-after: auto; }

/* Cenas ------------------------------------------------------------------ */
.scene .art-slot { display: flex; justify-content: center; }
.scene .art { width: 120mm; height: auto; display: block; }
.scene .art.tall { width: 107mm; }
.scene .words { padding-top: 7mm; }
.scene .words p {
  margin: 0 0 3.2mm 0;
  font-size: 11.8pt; line-height: 1.52; font-weight: 500;
  text-align: left; hyphens: none;
}
.folio {
  position: absolute; bottom: 7mm; left: 0; right: 0;
  text-align: center; font-size: 7.4pt; color: #a89c8c;
}

/* Capa ------------------------------------------------------------------- */
.cover { padding: 0; justify-content: flex-start; }
.cover .art { width: 148mm; height: 210mm; object-fit: cover;
  display: block; }
.cover-title {
  position: absolute; top: 22mm; left: 14mm; right: 14mm;
  text-align: center;
}
.cover-title p {
  margin: 0; font-family: "ColorHugs Display", sans-serif;
  font-size: 44pt; font-weight: 700; line-height: 1.05;
  letter-spacing: 0.2px; color: #4a3a28;
}

/* Páginas de texto ------------------------------------------------------- */
.plain { justify-content: center; }
.plain .block p { margin: 0 0 3.4mm 0; font-size: 9.8pt; line-height: 1.55;
  font-weight: 500; }
.plain .mark { position: absolute; bottom: 12mm; left: 50%;
  transform: translateX(-50%); width: 30mm; }
.imprint .block p:first-child { font-family: "ColorHugs Display", sans-serif;
  font-size: 19pt; font-weight: 700; margin-bottom: 5mm; }
.cast .block p:first-child { font-family: "ColorHugs Display", sans-serif;
  font-size: 20pt; font-weight: 700; margin-bottom: 7mm; text-align: center; }
.cast .block p { font-size: 11pt; line-height: 1.6; }
.back .block p { font-size: 11pt; line-height: 1.55; }
.back .block p:nth-child(3) { margin-top: 9mm; }
.back .block p:nth-child(n+3) { font-size: 9.4pt; color: #6a6055; }
"""


def build_reading_html(scenes, para):
    pages = [page_cover(para), page_imprint(para)]
    for n in range(1, 17):
        pages.append(page_scene(n, scenes[str(n)]))
    pages.append(page_cast(para))
    pages.append(page_back(para))
    if len(pages) != PAGE_COUNT:
        sys.exit(f"{len(pages)} páginas, deviam ser {PAGE_COUNT}")
    return (
        "<!doctype html><html lang='pt-PT'><meta charset='utf-8'>"
        f"<style>{CSS}</style><body>" + "".join(pages) + "</body></html>"
    )


INSTRUCTIONS = """
<!doctype html><html lang='pt-PT'><meta charset='utf-8'><style>
""" + FACES % {"f": FONTS} + """
@page { size: A4 landscape; margin: 16mm 20mm; }
body { font-family: "ColorHugs Text", system-ui, sans-serif; color: #3a332b;
       font-weight: 500; font-size: 10.5pt; line-height: 1.55;
       column-count: 2; column-gap: 14mm; }
h1 { column-span: all; }
h1 { font-family: "ColorHugs Display", sans-serif; font-size: 22pt;
     margin: 0 0 2mm 0; }
h2 { font-family: "ColorHugs Display", sans-serif; }
h2 { font-size: 12pt; margin: 8mm 0 2mm 0; }
p { margin: 0 0 3mm 0; }
ol { margin: 0 0 3mm 0; padding-left: 6mm; }
li { margin-bottom: 2.5mm; }
.warn { background: #fdf3e7; border-left: 3px solid #e0b070;
        padding: 4mm 5mm; margin: 5mm 0; }
.small { font-size: 9.5pt; color: #6a6055; margin-top: 10mm; }
</style><body>
<h1>Quem És Tu?</h1>
<p>Como imprimir este livro em casa. <strong>Esta folha não faz parte do
livro</strong> — não a agrafe com as outras.</p>

<h2>O que vai sair</h2>
<p><strong>A página 1 deste ficheiro é esta folha</strong>, e não entra no livro.
O livro são as <strong>páginas 2 a 11</strong>: cinco folhas A4, impressas dos dois
lados. Dobradas ao meio e agrafadas na dobra, dão um livro A5 de vinte páginas
pela ordem certa.</p>

<h2>Antes de imprimir tudo</h2>
<div class="warn">
<p><strong>Imprima primeiro só as páginas 2 e 3, frente e verso, e confirme.</strong>
De um lado deve aparecer a capa à direita. Do outro, virando a folha como se
virasse uma página, deve ficar por trás da capa a página com o título e o texto
pequeno.</p>
<p>Se sair de cabeça para baixo, mude a opção de frente e verso — a impressora
está a virar pelo lado errado — e repita.</p>
</div>

<h2>Depois</h2>
<ol>
  <li>Imprima as páginas 2 a 11, frente e verso, <strong>sem
      redimensionar</strong> e sem ajustar à margem.</li>
  <li>Empilhe as folhas pela ordem em que saíram, sem as rodar.</li>
  <li>Dobre o conjunto ao meio, de uma vez.</li>
  <li>Agrafe duas vezes na dobra.</li>
</ol>

<h2>Se a impressora não fizer frente e verso sozinha</h2>
<p>Imprima primeiro as páginas <strong>2, 4, 6, 8 e 10</strong>. Volte a pôr
essas folhas na gaveta e imprima as páginas <strong>3, 5, 7, 9 e 11</strong>.
Faça o ensaio com as páginas 2 e 3 antes de fazer com todas.</p>

<p class="small">ColorHugs · colorhugs.pt · Pode imprimir este livro as vezes
que quiser, para as crianças de casa.</p>
</body></html>
"""


# --------------------------------------------------------------------------
# Imposição
# --------------------------------------------------------------------------

def imposition(n_pages):
    """Ordem de caderno agrafado ao centro, duas páginas A5 por face A4.

    Para vinte páginas: 20|1, 2|19, 18|3, 4|17, ... **A conta tem de fechar em
    múltiplo de quatro**, e é por isso que o livro tem vinte páginas e não
    dezanove nem vinte e uma.
    """
    if n_pages % 4:
        sys.exit(f"{n_pages} páginas não é múltiplo de quatro")
    faces = []
    for i in range(n_pages // 4):
        faces.append((n_pages - 2 * i, 1 + 2 * i))       # frente da folha
        faces.append((2 + 2 * i, n_pages - 1 - 2 * i))   # verso da folha
    return faces


def impose(reading_pdf, out_pdf, instructions_pdf):
    from pypdf import PdfReader, PdfWriter, Transformation
    from pypdf.generic import RectangleObject

    src = PdfReader(reading_pdf)
    if len(src.pages) != PAGE_COUNT:
        sys.exit(f"o PDF de leitura tem {len(src.pages)} páginas")

    a5_w = src.pages[0].mediabox.width
    a5_h = src.pages[0].mediabox.height

    writer = PdfWriter()
    for page in PdfReader(instructions_pdf).pages:
        writer.add_page(page)

    for left, right in imposition(PAGE_COUNT):
        sheet = writer.add_blank_page(width=a5_w * 2, height=a5_h)
        for slot, number in ((0, left), (1, right)):
            p = src.pages[number - 1]
            p.add_transformation(Transformation().translate(tx=slot * a5_w, ty=0))
            p.mediabox = RectangleObject((0, 0, a5_w * 2, a5_h))
            sheet.merge_page(p)
    with open(out_pdf, "wb") as f:
        writer.write(f)


# --------------------------------------------------------------------------

def render(html, target, fmt="A5"):
    from playwright.sync_api import sync_playwright

    scratch = target + ".html"
    with open(scratch, "w", encoding="utf-8") as f:
        f.write(html)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("file://" + scratch, wait_until="networkidle")
        page.pdf(path=target, format=fmt, print_background=True,
                 margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
                 prefer_css_page_size=True)
        browser.close()
    os.remove(scratch)
    return target


def main():
    scenes, para = load_text()
    reading = os.path.join(MATERIALS, "quem-es-tu-leitura.pdf")
    render(build_reading_html(scenes, para), reading)

    instr = os.path.join(MATERIALS, ".instrucoes.pdf")
    render(INSTRUCTIONS, instr, fmt="A4")

    printing = os.path.join(MATERIALS, "quem-es-tu-impressao.pdf")
    impose(reading, printing, instr)
    os.remove(instr)

    if _WORK:
        import shutil
        shutil.rmtree(_WORK, ignore_errors=True)

    for f in (reading, printing):
        print(f"{os.path.basename(f)}  {os.path.getsize(f) // 1024} KB")


if __name__ == "__main__":
    main()
