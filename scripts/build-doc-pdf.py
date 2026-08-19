#!/usr/bin/env python3
"""Compõe um documento do projecto em PDF (D-374).

    python3 scripts/build-doc-pdf.py docs/CATALOGO-HOW-DO-I-FEEL.md

**Para ler e para mostrar, não para editar.** Os documentos do projecto vivem em
markdown, que é onde se trabalham; isto compõe-os para serem vistos.

Trata o subconjunto de markdown que estes documentos usam: títulos, parágrafos,
negrito, itálico, código, listas, tabelas e separadores.
"""

import html as _html
import os
import re
import sys

from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(ROOT, "assets", "fonts")
BRANDING = os.path.join(ROOT, "public", "assets", "branding")

CSS = """
@font-face { font-family: "T"; font-weight: 500;
  src: url("file://%(f)s/Nunito-Medium.ttf") format("truetype"); }
@font-face { font-family: "T"; font-weight: 700;
  src: url("file://%(f)s/Nunito-Bold.ttf") format("truetype"); }
@font-face { font-family: "D"; font-weight: 700;
  src: url("file://%(f)s/Baloo2-Bold.ttf") format("truetype"); }
@page { size: A4; margin: 18mm 20mm 18mm; }
body { font-family: "T", sans-serif; font-weight: 500; font-size: 9.6pt;
       line-height: 1.5; color: #3a332b; }
h1 { font-family: "D", sans-serif; font-size: 21pt; margin: 0 0 1mm 0; }
h2 { font-family: "D", sans-serif; font-size: 12.5pt; margin: 7mm 0 2mm 0;
     color: #2f2a24; break-after: avoid; }
h3 { font-size: 9pt; letter-spacing: 1px; text-transform: uppercase;
     color: #968060; margin: 4mm 0 1.5mm 0; break-after: avoid; }
p { margin: 0 0 2.6mm 0; }
strong { font-weight: 700; }
em { font-style: italic; }
code { background: #f4efe7; padding: 0 1.6mm; border-radius: 1mm;
       font-family: "T", sans-serif; font-size: 8.6pt; color: #6a6055; }
ul { margin: 0 0 2.6mm 0; padding-left: 5mm; }
li { margin: 0 0 1.2mm 0; }
hr { border: 0; border-top: 1pt solid #e6ded2; margin: 6mm 0; }
table { width: 100%%; border-collapse: collapse; margin: 0 0 3.5mm 0;
        font-size: 8.8pt; break-inside: avoid; }
th { text-align: left; font-weight: 700; font-size: 7.6pt; letter-spacing: .8px;
     text-transform: uppercase; color: #968060; padding: 0 3mm 1.4mm 0;
     border-bottom: 1pt solid #dfd6c8; }
td { padding: 1.6mm 3mm 1.6mm 0; border-bottom: .6pt solid #efe8dd;
     vertical-align: top; }
td.c, th.c { text-align: center; padding-right: 0; }
.capa { text-align: center; padding: 34mm 0 0 0; break-after: page; }
.capa img { width: 46mm; }
.capa h1 { font-size: 26pt; margin: 8mm 0 2mm; }
.capa .sub { color: #8a8175; font-size: 11pt; }
.capa .selo { margin-top: 30mm; }

"""


def inline(t):
    t = _html.escape(t)
    t = re.sub(r"`(.+?)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", t)
    return t


def converte(md):
    linhas = md.split("\n")
    out, i = [], 0
    while i < len(linhas):
        l = linhas[i]
        if l.startswith("|"):
            bloco = []
            while i < len(linhas) and linhas[i].startswith("|"):
                bloco.append(linhas[i])
                i += 1
            out.append(tabela(bloco))
            continue
        if re.match(r"^#{1,3} ", l):
            n = len(l) - len(l.lstrip("#"))
            out.append(f"<h{n}>{inline(l[n + 1:])}</h{n}>")
        elif l.startswith("- "):
            # **Um item pode atravessar várias linhas.** A primeira versão lia
            # só a primeira e o resto do item saía como parágrafo, com os
            # asteriscos do negrito partidos à vista.
            itens = []
            while i < len(linhas) and linhas[i].startswith("- "):
                partes = [linhas[i][2:]]
                i += 1
                while (i < len(linhas) and linhas[i].strip()
                       and not re.match(r"^(#|\||-{3}|- )", linhas[i])):
                    partes.append(linhas[i].strip())
                    i += 1
                itens.append(f"<li>{inline(' '.join(partes))}</li>")
            out.append("<ul>" + "".join(itens) + "</ul>")
            continue
        elif l.strip() == "---":
            out.append("<hr>")
        elif l.strip():
            para = [l]
            i += 1
            while i < len(linhas) and linhas[i].strip() and not re.match(
                    r"^(#|\||-{3}|- )", linhas[i]):
                para.append(linhas[i])
                i += 1
            out.append(f"<p>{inline(' '.join(para))}</p>")
            continue
        i += 1
    return "".join(out)


def tabela(bloco):
    linhas = [[c.strip() for c in l.strip("|").split("|")] for l in bloco]
    alinha = []
    if len(linhas) > 1 and set(linhas[1][0]) <= set("-: "):
        alinha = [":-:" in c or c.strip().startswith(":-") and c.strip().endswith("-:")
                  for c in linhas[1]]
        cabeca, corpo = linhas[0], linhas[2:]
    else:
        cabeca, corpo = linhas[0], linhas[1:]
    if not alinha:
        alinha = [False] * len(cabeca)

    def cl(j):
        return " class='c'" if j < len(alinha) and alinha[j] else ""

    th = "".join(f"<th{cl(j)}>{inline(c)}</th>" for j, c in enumerate(cabeca))
    tr = "".join(
        "<tr>" + "".join(f"<td{cl(j)}>{inline(c)}</td>" for j, c in enumerate(l))
        + "</tr>" for l in corpo)
    return f"<table><tr>{th}</tr>{tr}</table>"


def main():
    origem = sys.argv[1]
    md = open(os.path.join(ROOT, origem), encoding="utf-8").read()
    linhas = md.split("\n")
    titulo = linhas[0].lstrip("# ").strip()
    resto = "\n".join(linhas[1:])
    sub = ""
    for l in linhas[1:6]:
        if l.strip() and not l.startswith("#"):
            sub = l.strip()
            break

    capa = (f"<div class='capa'>"
            f"<img src='file://{BRANDING}/colorhugs-professional.webp'>"
            f"<h1>{inline(titulo)}</h1>"
            f"<div class='sub'>{inline(sub)}</div>"
            f"<div class='selo'>colorhugs.pt · material licenciado</div></div>")

    doc = (f"<!doctype html><html lang='pt-PT'><meta charset='utf-8'>"
           f"<style>{CSS % {'f': FONTS}}</style><body>{capa}"
           f"{converte(resto)}</body></html>")

    alvo = os.path.join(ROOT, "docs", os.path.basename(origem).replace(".md", ".pdf"))
    rascunho = alvo + ".html"
    with open(rascunho, "w", encoding="utf-8") as f:
        f.write(doc)
    with sync_playwright() as p:
        navegador = p.chromium.launch()
        pagina = navegador.new_page()
        pagina.goto("file://" + rascunho, wait_until="networkidle")
        # **O rodapé é o da impressão e não um elemento fixo em CSS** (D-375).
        # Um `position: fixed` repete-se no topo das páginas seguintes, por cima
        # do texto — foi o que aconteceu na primeira versão.
        rodape = (
            "<div style=\"width:100%;font-size:7pt;color:#b3a894;"
            "font-family:sans-serif;padding:0 20mm;display:flex;"
            "justify-content:space-between;\">"
            f"<span>{_html.escape(titulo)}</span>"
            "<span>© ColorHugs · Ricardina Correia · "
            "<span class='pageNumber'></span></span></div>")
        pagina.pdf(path=alvo, format="A4", print_background=True,
                   prefer_css_page_size=True, display_header_footer=True,
                   header_template="<div></div>", footer_template=rodape)
        navegador.close()
    os.remove(rascunho)
    print(alvo)


if __name__ == "__main__":
    main()
