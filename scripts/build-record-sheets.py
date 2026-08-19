#!/usr/bin/env python3
"""Constrói as folhas da família «Peças de registo» (D-366).

    python3 scripts/build-record-sheets.py

**São folhas para a técnica escrever**, não para a criança usar — é isso que as
separa das *Peças de sessão* e a razão de terem família própria.

Cada folha lê o seu markdown pela regra do projecto: **o que está em citação vai
para a página; o resto é comentário para quem escreve.** Os campos por preencher
estão marcados com `[…]` no markdown e saem como caixas.
"""

import os
import re

from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MATERIALS = os.path.join(ROOT, "docs", "materials")
FONTS = os.path.join(ROOT, "assets", "fonts")
OUT = os.path.join(MATERIALS, "folhas")

FAMILIA = "Peças de registo"
COR = "#5a6b7a"

FOLHAS = [("devolucao-escola", "Devolução à escola",
           "Sugestões práticas para a sala de aula.", "A4"),
          ("grelha-acomodacao", "Grelha de acomodação",
           "O que se faz em casa para ajudar, e o que uma versão mais pequena "
           "poderia ser.", "A4 landscape"),
          ("registo-degraus", "Registo dos degraus",
           "Os degraus por ordem, e o que aconteceu em cada um.", "A4"),
          ("bloco-registo", "Bloco de registo",
           "Nota de uma sessão. Cortar ao meio: uma metade por sessão.",
           "A4 duplo"),
          ("oito-sessoes", "Oito sessões",
           "Um exemplo trabalhado. Não é um plano de tratamento.", "A4 texto")]

CSS = """
@font-face { font-family: "T"; font-weight: 500;
  src: url("file://%(f)s/Nunito-Medium.ttf") format("truetype"); }
@font-face { font-family: "T"; font-weight: 700;
  src: url("file://%(f)s/Nunito-Bold.ttf") format("truetype"); }
@font-face { font-family: "D"; font-weight: 700;
  src: url("file://%(f)s/Baloo2-Bold.ttf") format("truetype"); }
@page { size: A4; margin: 13mm 18mm 11mm; }
body { font-family: "T", sans-serif; font-weight: 500; font-size: 9pt;
       line-height: 1.4; color: #33383d; }
.fam { font-size: 7pt; letter-spacing: 1.4px; color: %(c)s;
       text-transform: uppercase; }
h1 { font-family: "D", sans-serif; font-size: 15pt; margin: 1mm 0 0 0; }
.sub { color: #7d858c; margin: 1mm 0 0 0; }
.rule { width: 26mm; height: 1.1mm; background: %(c)s; border-radius: .6mm;
        margin: 2mm 0 3mm; }
.meia .rule { margin: 1.6mm 0 2mm; }
h2 { font-size: 7.6pt; letter-spacing: 1.2px; text-transform: uppercase;
     color: %(c)s; margin: 3mm 0 1mm 0; font-weight: 700; }
p { margin: 0 0 1.6mm 0; }
strong { font-weight: 700; }
.campo { border: 1.2pt solid #b9c1c8; border-radius: 2mm; height: 6mm;
         margin: 0 0 1.4mm 0; }
.campo.alto { height: 16mm; }
.dica { font-size: 7.6pt; color: #8b949b; font-style: italic;
        margin: 0 0 1.2mm 0; }
.marcar { display: inline-flex; align-items: center; gap: 2mm;
          margin: 0 6mm 1.5mm 0; font-size: 8.4pt; }
.marcar .quad { width: 4.5mm; height: 4.5mm; border: 1.2pt solid #b9c1c8;
                border-radius: 1mm; }
table { width: 100%%; border-collapse: separate; border-spacing: 0 1.3mm; }
th { font-size: 7.4pt; letter-spacing: .8px; text-transform: uppercase;
     color: %(c)s; text-align: left; padding: 0 0 .6mm 1.5mm; font-weight: 700; }
td { border: 1.2pt solid #b9c1c8; border-radius: 2mm; height: 10mm; }
td + td { border-left: 1.2pt solid #b9c1c8; }
th.estreita, td.estreita { width: 16mm; }
td.baixa { height: 9mm; }
.linha { display: flex; gap: 3mm; }
.linha > div { flex: 1; }
.rot { font-size: 7pt; color: #96a0a8; margin: 0 0 .8mm 1mm; }
.nao { background: #f4f6f7; border-left: 3px solid %(c)s; padding: 2.5mm 4mm;
       margin: 1mm 0 0 0; }
.nao p { margin: 0 0 1.4mm 0; }
.meia { height: 130mm; overflow: hidden; }
.meia h1 { font-size: 12.5pt; }
.meia .campo.alto { height: 10mm; }
.meia .dica { margin: 0 0 .6mm 0; font-size: 7.2pt; }
.meia .sub { display: none; }
.meia h2 { margin: 1.8mm 0 .6mm 0; }
.corte { border-top: 1.2pt dashed #c8cfd4; margin: 4mm 0; }
.marca { font-size: 6.6pt; color: #b0b8bd; margin-top: 2mm; }
.texto h2 { margin: 5mm 0 1.4mm 0; font-size: 8.4pt; }
.fase { font-size: 7.6pt; letter-spacing: 1.2px; text-transform: uppercase;
        color: #96a0a8; border-top: 1pt solid #dfe4e8; padding-top: 2mm;
        margin: 5mm 0 2mm 0; break-after: avoid; page-break-after: avoid; }
.sessao { background: #f7f9fa; border-radius: 3mm; padding: 3mm 4mm;
          margin: 0 0 2.6mm 0; break-inside: avoid; }
.sessao h3 { font-family: "D", sans-serif; font-size: 10pt; margin: 0 0 1.6mm 0;
             color: #33383d; }
.linhaet { display: flex; gap: 3mm; margin: 0 0 1.6mm 0; }
.et { flex: 0 0 26mm; font-size: 7.2pt; letter-spacing: .8px;
      text-transform: uppercase; color: %(c)s; font-weight: 700;
      padding-top: .6mm; }
.texto p { margin: 0 0 2.4mm 0; }
.texto { font-size: 9.4pt; line-height: 1.5; }
.pe { position: fixed; bottom: 0; left: 0; right: 0; font-size: 6.8pt;
      color: #b08a5a; display: flex; justify-content: space-between; }
"""

AVISO = ("Rascunho técnico, sujeito a revisão jurídica. Não usar antes dessa "
         "revisão.")


def seccoes(nome):
    texto = open(os.path.join(MATERIALS, f"{nome}.md"), encoding="utf-8").read()
    out = []
    for bloco in re.split(r"\n(?=##+ )", texto):
        fase = re.match(r"### (.+)", bloco)
        if fase:
            out.append(("§" + fase.group(1).strip(), []))
            continue
        m = re.match(r"## (.+)", bloco)
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


def campos(texto):
    """Uma linha de caixas rotuladas.

    `[Nome]` dá uma caixa com rótulo; `[]` sozinho dá uma caixa alta sem rótulo,
    para o texto que a psicóloga escreve.
    """
    rotulos = re.findall(r"`\[(.*?)\]`", texto)
    if not rotulos:
        return None
    if rotulos == [""]:
        return "<div class='campo alto'></div>"
    return ("<div class='linha'>" + "".join(
        f"<div><div class='rot'>{r}</div><div class='campo'></div></div>"
        for r in rotulos) + "</div>")


def tabela(texto):
    """`{{A | B | C · 6}}` vira uma grelha vazia com seis linhas."""
    m = re.match(r"\{\{(.+?)\}\}", texto.strip())
    if not m:
        return None
    corpo = m.group(1)
    cabecas, _, linhas = corpo.rpartition("·")
    n = int(linhas.strip())
    colunas = [c.strip() for c in cabecas.split("|") if c.strip()]
    def largura(c):
        # **Uma coluna de números não precisa da mesma largura de uma frase.**
        curtas = {"nº", "degrau", "data"}
        return " class='estreita'" if c.lower() in curtas else ""

    cab = "".join(f"<th{largura(c)}>{c}</th>" for c in colunas)
    celulas = "".join(
        "<tr>" + "".join(f"<td{largura(c)}></td>" for c in colunas) + "</tr>"
        for _ in range(n))
    return f"<table><tr>{cab}</tr>{celulas}</table>"


def html(titulo, subtitulo, blocos, duplo=False, texto=False):
    corpo = ""
    for nome, paras in blocos:
        if nome.startswith("§"):
            corpo += f"<div class='fase'>{nome[1:]}</div>"
            continue
        if nome.lower().startswith("o cabeçalho"):
            corpo += "".join(campos(p) or "" for p in paras)
            continue
        sessao = nome.lower().startswith("sessão")
        corpo += (f"<div class='sessao'><h3>{nome}</h3>" if sessao
                  else f"<h2>{nome}</h2>")
        classe = "nao" if nome.lower().startswith("o que não vai") else ""
        interior = ""
        for p in paras:
            grelha = tabela(p)
            if grelha:
                interior += grelha
                continue
            caixas = campos(p)
            if caixas:
                interior += caixas
                continue
            # **Todas as ocorrências e não só a primeira.** `re.match` apanhava
            # a primeira caixa do parágrafo e as outras desapareciam.
            marcar = re.findall(r"\(\((.+?)\)\)", p)
            if marcar:
                interior += "".join(
                    f"<div class='marcar'><div class='quad'></div>"
                    f"<span>{m}</span></div>" for m in marcar)
                continue
            dica = re.match(r"_(.+)_$", p)
            if dica:
                interior += f"<p class='dica'>{dica.group(1)}</p>"
                continue
            # **Um parágrafo que abre com «**Etiqueta.**» vira uma linha
            # etiquetada.** É o que separa o raciocínio dos acontecimentos, que
            # é o que num exemplo trabalhado se quer copiar (D-371).
            et = re.match(r"\*\*(.+?)\.\*\*\s+(.+)$", p, re.S)
            if sessao and et:
                resto = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>",
                               et.group(2))
                resto = resto.replace("***", "").replace("*", "")
                # **O texto vai dentro de um só elemento.** Solto, cada troço a
                # negrito virava uma coluna do flex e saltava para o lado.
                interior += (f"<p class='linhaet'><span class='et'>"
                             f"{et.group(1)}</span><span>{resto}</span></p>")
                continue
            p = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", p)
            p = re.sub(r"`(.+?)`", r"\1", p).replace("*", "")
            interior += f"<p>{p}</p>"
        corpo += (f"<div class='{classe}'>{interior}</div>" if classe
                  else interior)
        if sessao:
            corpo += "</div>"
    if texto:
        corpo = f"<div class='texto'>{corpo}</div>"
    cabeca = (f"<div class='fam'>{FAMILIA} · ColorHugs</div>"
              f"<h1>{titulo}</h1><p class='sub'>{subtitulo}</p>"
              f"<div class='rule'></div>")
    if duplo:
        # **Um bloco corta-se.** Duas metades iguais na mesma folha, com a linha
        # de corte a meio, e a marca em cada uma — porque cada metade sai da
        # folha sozinha.
        meia = (f"<div class='meia'>{cabeca}{corpo}"
                f"<div class='marca'>colorhugs.pt · material licenciado</div>"
                f"</div>")
        interior = meia + "<div class='corte'></div>" + meia
        return ("<!doctype html><html lang='pt-PT'><meta charset='utf-8'>"
                f"<style>{CSS % {'f': FONTS, 'c': COR}}</style><body>"
                f"{interior}</body></html>")
    return ("<!doctype html><html lang='pt-PT'><meta charset='utf-8'>"
            f"<style>{CSS % {'f': FONTS, 'c': COR}}</style><body>"
            f"{cabeca}{corpo}"
            f"<div class='pe'><span>{'Caso fictício. Exemplo trabalhado, não é um plano de tratamento.' if texto else AVISO}</span>"
            f"<span>© ColorHugs · colorhugs.pt</span></div></body></html>")


def main():
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        navegador = p.chromium.launch()
        for nome, titulo, subtitulo, formato in FOLHAS:
            alvo = os.path.join(OUT, f"{nome}.pdf")
            rascunho = alvo + ".html"
            pagina_css = ("@page { size: A4 landscape; margin: 12mm 16mm 10mm; }"
                          if "landscape" in formato else "")
            if "duplo" in formato:
                pagina_css = "@page { size: A4; margin: 12mm 16mm; }"
            with open(rascunho, "w", encoding="utf-8") as f:
                f.write(html(titulo, subtitulo, seccoes(nome),
                             duplo="duplo" in formato,
                             texto="texto" in formato)
                        .replace("</style>", pagina_css + "</style>"))
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
