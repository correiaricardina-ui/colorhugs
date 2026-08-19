#!/usr/bin/env python3
"""Constrói as três folhas de enquadramento, consentimento e licença (D-359).

    python3 scripts/build-consent-sheets.py

Lê `docs/materials/enquadramento-consentimento.md` e imprime **apenas o que está
em citação** — a regra de leitura de todo o projecto. O comentário editorial, a
justificação de haver três folhas e a lista do que falta verificar ficam no
markdown e não chegam à família.

**As três saem em ficheiros separados**, porque não se entregam à mesma pessoa: o
enquadramento e o consentimento vão para a família, os termos de licença ficam
com a técnica.
"""

import os
import re

from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MATERIALS = os.path.join(ROOT, "docs", "materials")
FONTS = os.path.join(ROOT, "assets", "fonts")
BRANDING = os.path.join(ROOT, "public", "assets", "branding")
SOURCE = os.path.join(MATERIALS, "enquadramento-consentimento.md")
OUT = os.path.join(MATERIALS, "folhas")

AVISO = ("Rascunho técnico, sujeito a revisão jurídica. "
         "Não usar com famílias antes dessa revisão.")

CSS = """
@font-face { font-family: "T"; font-weight: 500;
  src: url("file://%(f)s/Nunito-Medium.ttf") format("truetype"); }
@font-face { font-family: "T"; font-weight: 700;
  src: url("file://%(f)s/Nunito-Bold.ttf") format("truetype"); }
@font-face { font-family: "D"; font-weight: 700;
  src: url("file://%(f)s/Baloo2-Bold.ttf") format("truetype"); }
@page { size: A4; margin: 18mm 20mm 16mm; }
body { font-family: "T", sans-serif; font-weight: 500; font-size: 10.4pt;
       line-height: 1.55; color: #3a332b; }
.fam { font-size: 7.4pt; letter-spacing: 1.4px; color: #968060;
       text-transform: uppercase; }
h1 { font-family: "D", sans-serif; font-size: 17pt; margin: 2mm 0 0 0; }
.rule { width: 28mm; height: 1.2mm; background: #968060; border-radius: .6mm;
        margin: 3mm 0 6mm; }
p { margin: 0 0 3.6mm 0; }
strong { font-weight: 700; }
code { font-family: "T", sans-serif; font-weight: 500; background: #f4efe7;
       padding: 0 2mm; border-radius: 1mm; color: #6a6055; }
.aviso { margin-top: 8mm; padding: 4mm 5mm; background: #fdf3e7;
         border-left: 3px solid #e0b070; font-size: 9pt; }
.pe { position: fixed; bottom: 0; left: 0; right: 0; font-size: 7.4pt;
      color: #a89b8a; display: flex; justify-content: space-between; }
"""


def folhas():
    texto = open(SOURCE, encoding="utf-8").read()
    out = []
    for bloco in re.split(r"\n(?=# Folha )", texto):
        m = re.match(r"# Folha \d+ — (.+)", bloco)
        if not m:
            continue
        paras, buf = [], []
        for linha in bloco.splitlines():
            if linha.startswith(">"):
                corpo = linha[1:].strip()
                if corpo:
                    buf.append(corpo)
                elif buf:
                    paras.append(" ".join(buf))
                    buf = []
            elif buf:
                paras.append(" ".join(buf))
                buf = []
        if buf:
            paras.append(" ".join(buf))
        if paras:
            out.append((m.group(1).strip(), paras))
    return out


def html(titulo, paras):
    corpo = ""
    for p in paras:
        p = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", p)
        p = re.sub(r"`(.+?)`", r"<code>\1</code>", p)
        p = p.replace("*", "")
        corpo += f"<p>{p}</p>"
    return (f"<!doctype html><html lang='pt-PT'><meta charset='utf-8'>"
            f"<style>{CSS % {'f': FONTS}}</style><body>"
            f"<div class='fam'>ColorHugs · material licenciado</div>"
            f"<h1>{titulo}</h1><div class='rule'></div>{corpo}"
            f"<div class='aviso'>{AVISO}</div>"
            f"<div class='pe'><span>colorhugs.pt</span>"
            f"<span>© ColorHugs · Ricardina Correia</span></div>"
            f"</body></html>")


def main():
    os.makedirs(OUT, exist_ok=True)
    nomes = ["enquadramento", "consentimento", "licenca"]
    with sync_playwright() as p:
        navegador = p.chromium.launch()
        for nome, (titulo, paras) in zip(nomes, folhas()):
            alvo = os.path.join(OUT, f"{nome}.pdf")
            rascunho = alvo + ".html"
            with open(rascunho, "w", encoding="utf-8") as f:
                f.write(html(titulo, paras))
            pagina = navegador.new_page()
            pagina.goto("file://" + rascunho, wait_until="networkidle")
            pagina.pdf(path=alvo, format="A4", print_background=True,
                       prefer_css_page_size=True)
            pagina.close()
            os.remove(rascunho)
            print(f"{nome}.pdf")
        navegador.close()


if __name__ == "__main__":
    main()
