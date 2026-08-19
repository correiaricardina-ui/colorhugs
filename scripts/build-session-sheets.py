#!/usr/bin/env python3
"""Constrói as três folhas de sessão (D-339).

    python3 scripts/build-session-sheets.py

Três folhas A4 para usar na consulta, cada uma num PDF próprio:

`casa-das-sete.pdf`
    A casa em corte, vazia, para a criança pôr ou desenhar quem lá vive.

`antes-durante-depois.pdf`
    Três caixas para sequenciar um episódio real.

`duas-listas.pdf`
    A mesma pergunta em duas metades iguais, para o adulto e a criança
    responderem em separado antes de compararem.

**São as peças que abrem e ficam abertas**, e só podem existir nesta linha:
numa folha que vai para casa isso está proibido, porque não há ninguém para
apanhar o que se abriu. Aqui há.

**Caixas e não linhas, e nada impresso dentro de uma caixa.** É a regra dos
cadernos e vale aqui: uma linha diz quanto se espera que se escreva, e uma caixa
não diz nada.
"""

import os

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(ROOT, "assets", "fonts")
SESSAO = os.path.join(ROOT, "artwork", "sessao")
BRANDING = os.path.join(ROOT, "public", "assets", "branding")
OUT = os.path.join(ROOT, "docs", "materials", "folhas")

DPI = 200
MM = DPI / 25.4
A4 = (round(210 * MM), round(297 * MM))

INK = (58, 51, 43)
FAINT = (168, 155, 138)
BOX = (120, 110, 96)
ROOF = (150, 96, 62)

FAMILY = "Peças de sessão"
FAMILY_COLOUR = (150, 128, 96)
CREDIT = "© ColorHugs · colorhugs.pt · Material licenciado"

SOURCE = os.path.join(ROOT, "docs", "materials", "folhas-instrucoes.md")


def page():
    im = Image.new("RGB", A4, "white")
    return im, ImageDraw.Draw(im)


def fonts():
    return (
        ImageFont.truetype(os.path.join(FONTS, "Baloo2-Bold.ttf"), round(7.5 * MM)),
        ImageFont.truetype(os.path.join(FONTS, "Nunito-Medium.ttf"), round(3.6 * MM)),
        ImageFont.truetype(os.path.join(FONTS, "Nunito-Medium.ttf"), round(2.9 * MM)),
    )


def header(draw, title, subtitle):
    """O cabeçalho comum às três folhas.

    **É o que as faz reconhecer-se como da mesma família** sem lhes pôr número:
    o nome da família por cima, o traço da cor da família por baixo do título, e
    o mesmo rodapé. **Numerá-las diria que há ordem, e não há** (D-327).
    """
    big, small, tiny = fonts()
    draw.text((round(18 * MM), round(13 * MM)), FAMILY.upper(), font=tiny,
              fill=FAMILY_COLOUR)
    draw.text((round(18 * MM), round(18 * MM)), title, font=big, fill=INK)
    draw.rounded_rectangle(
        [round(18 * MM), round(29.5 * MM), round(46 * MM), round(30.7 * MM)],
        radius=round(0.6 * MM), fill=FAMILY_COLOUR,
    )
    draw.text((round(18 * MM), round(34 * MM)), subtitle, font=small, fill=FAINT)


def credit(im, draw):
    _, _, tiny = fonts()
    w = draw.textlength(CREDIT, font=tiny)
    draw.text(((A4[0] - w) / 2, A4[1] - round(13 * MM)), CREDIT, font=tiny, fill=FAINT)


def box(draw, x0, y0, x1, y1, radius=4):
    draw.rounded_rectangle([round(x0 * MM), round(y0 * MM), round(x1 * MM),
                            round(y1 * MM)], radius=round(radius * MM),
                           outline=BOX, width=3)


def label(draw, text, x, y):
    _, small, _ = fonts()
    draw.text((round(x * MM), round(y * MM)), text, font=small, fill=FAINT)


# --------------------------------------------------------------------------

def casa_das_sete():
    """A casa em corte, e a parte de fora.

    **A casa é arte gerada e não desenhada em código** (D-340). A primeira
    versão era um esquema traçado com linhas e lia-se como tal; esta é da mesma
    família do resto do projecto.

    É traço e não cor. No livro a casa é colorida, mas ali ninguém escreve por
    cima — **aqui a criança desenha, escreve ou põe os bonecos recortados, que
    já são coloridos**, e uma casa cheia de cor briga com o lápis dela.

    **O fora não é decoração.** Na primeira cena do livro o sétimo está à porta,
    e quem queira pôr alguém fora de casa precisa de ter onde.
    """
    im, draw = page()
    header(draw, "Quem vive nesta casa",
           "Pôr ou desenhar. Não há lugares certos, e há sítio fora da casa.")

    casa = Image.open(os.path.join(SESSAO, "casa-vazia.png")).convert("RGBA")
    largura = round(180 * MM)
    casa = casa.resize((largura, round(casa.height * largura / casa.width)),
                       Image.LANCZOS)
    x = (A4[0] - casa.width) // 2
    y = round(54 * MM)
    im.paste(casa, (x, y), casa)

    # **A linha do chão continua até às margens da folha.** Na arte ela pára na
    # largura do desenho, e o que fica por baixo lê-se como página em branco em
    # vez de se ler como o lado de fora. Estendida, a folha tem um dentro e um
    # fora, que é a razão de a casa ter uma porta.
    cinza = np.asarray(casa.convert("L"))
    alfa = np.asarray(casa.split()[-1])
    escuro = (cinza < 120) & (alfa > 128)
    linhas = escuro[int(casa.height * 0.80):].sum(axis=1)
    chao = int(casa.height * 0.80) + int(linhas.argmax())
    draw.line([round(12 * MM), y + chao, A4[0] - round(12 * MM), y + chao],
              fill=INK, width=round(0.9 * MM))

    label(draw, "fora", 14, (y + chao) / MM + 7)

    credit(im, draw)
    return im


def antes_durante_depois():
    im, draw = page()
    header(draw, "Antes, durante, depois",
           "Uma coisa que aconteceu mesmo. Não se pergunta porquê.")

    caixas = [("Antes", 50), ("Durante", 122), ("Depois", 194)]
    for texto, y in caixas:
        label(draw, texto, 20, y - 8)
        box(draw, 18, y, 192, y + 62)

    credit(im, draw)
    return im


def duas_listas():
    """A mesma pergunta, duas metades iguais, corte a meio.

    **Respondem em separado e só depois comparam.** A primeira versão pôs as
    duas colunas lado a lado na mesma metade da folha, e assim cada um vê o que
    o outro escreve — a peça deixava de ter objecto. São duas metades iguais,
    uma por cima da outra, e corta-se.
    """
    im, draw = page()
    header(draw, "Duas listas",
           "Cortar ao meio. Cada um responde sem ver o outro, e só depois comparam.")

    for topo in (46, 162):
        label(draw, "A pergunta", 20, topo)
        box(draw, 18, topo + 5, 192, topo + 23)
        label(draw, "A resposta", 20, topo + 30)
        box(draw, 18, topo + 35, 192, topo + 105)

    corte = 152
    step = round(3 * MM)
    for x in range(round(12 * MM), round(198 * MM), step * 2):
        draw.line([x, round(corte * MM), x + step, round(corte * MM)],
                  fill=FAINT, width=2)

    credit(im, draw)
    return im


# --------------------------------------------------------------------------
# O caderno
# --------------------------------------------------------------------------

def capa():
    """A capa do caderno.

    **É material de técnico, e a capa diz isso pelo registo e não por um aviso.**
    Sóbria, tipográfica, com o selo profissional — que é o lockup dos
    profissionais, ao contrário das cartas e das folhas de criança, onde entra a
    marca simples.

    **As três miniaturas não são decoração.** São as três folhas desenhadas em
    pequeno — a casa, as três caixas, as duas metades — e dizem o que está lá
    dentro sem ser preciso abrir. Numa secretária com material de vários
    conjuntos, é isso que faz encontrar o certo.
    """
    im, draw = page()
    big, small, tiny = fonts()

    draw.rectangle([0, 0, A4[0], round(6 * MM)], fill=FAMILY_COLOUR)

    titulo = ImageFont.truetype(os.path.join(FONTS, "Baloo2-Bold.ttf"),
                                round(15 * MM))
    draw.text((round(24 * MM), round(38 * MM)), "Peças de sessão",
              font=titulo, fill=INK)
    draw.rounded_rectangle(
        [round(24 * MM), round(60 * MM), round(60 * MM), round(61.4 * MM)],
        radius=round(0.7 * MM), fill=FAMILY_COLOUR)
    draw.text((round(24 * MM), round(66 * MM)),
              "Três folhas, dois dados, dois jogos, sete folhas de bonecos, e as instruções.",
              font=small, fill=(110, 100, 88))
    draw.text((round(24 * MM), round(73 * MM)),
              "Cada peça funciona sozinha. Não há ordem entre elas.",
              font=small, fill=(110, 100, 88))

    # As três miniaturas.
    # Quatro miniaturas em vez de três: o dado é peça da família e tem de se ver
    # na capa como as outras.
    y0, alt, larg, passo = 108, 46, 37, 43
    for i, nome in enumerate(("Quem vive nesta casa", "Antes, durante, depois",
                              "Duas listas", "Bonecos de tamanhos")):
        x0 = 22 + i * passo
        draw.rounded_rectangle(
            [round(x0 * MM), round(y0 * MM), round((x0 + larg) * MM),
             round((y0 + alt) * MM)],
            radius=round(3 * MM), outline=(214, 205, 192), width=3)
        if i == 0:
            casa = Image.open(os.path.join(SESSAO, "casa-vazia.png")).convert("RGBA")
            w = round(27 * MM)
            casa = casa.resize((w, round(casa.height * w / casa.width)), Image.LANCZOS)
            im.paste(casa, (round((x0 + 5) * MM), round((y0 + 12) * MM)), casa)
        elif i == 1:
            for k in range(3):
                draw.rounded_rectangle(
                    [round((x0 + 6) * MM), round((y0 + 9 + k * 11) * MM),
                     round((x0 + 31) * MM), round((y0 + 17 + k * 11) * MM)],
                    radius=round(1.4 * MM), outline=BOX, width=3)
        elif i == 2:
            for k in range(2):
                draw.rounded_rectangle(
                    [round((x0 + 6) * MM), round((y0 + 9 + k * 20) * MM),
                     round((x0 + 31) * MM), round((y0 + 24 + k * 20) * MM)],
                    radius=round(1.4 * MM), outline=BOX, width=3)
            p2 = round(2 * MM)
            for xx in range(round((x0 + 4) * MM), round((x0 + 33) * MM), p2 * 2):
                draw.line([xx, round((y0 + 27) * MM), xx + p2,
                           round((y0 + 27) * MM)], fill=FAINT, width=2)
        else:
            fig = Image.open(os.path.join(
                ROOT, "artwork", "emotions", "angry.png")).convert("RGBA")
            diff = Image.new("L", fig.size)
            diff.putdata([0 if p[:3] > (246, 246, 246) else 255
                          for p in fig.getdata()])
            fig = fig.crop(diff.getbbox())
            for alt, cx, cy in ((20, 15, 8), (9, 9, 30), (5, 27, 33)):
                h2 = round(alt * MM)
                f2 = fig.resize((round(fig.width * h2 / fig.height), h2),
                                Image.LANCZOS)
                im.paste(f2, (round((x0 + cx) * MM) - f2.width // 2,
                              round((y0 + cy) * MM)), f2)
        larg_txt = draw.textlength(nome, font=tiny)
        draw.text((round((x0 + larg / 2) * MM) - larg_txt / 2,
                   round((y0 + alt + 4) * MM)), nome, font=tiny, fill=(130, 120, 106))

    selo = Image.open(os.path.join(BRANDING, "colorhugs-professional.webp"))
    selo = selo.convert("RGBA")
    larg = round(42 * MM)
    selo = selo.resize((larg, round(selo.height * larg / selo.width)), Image.LANCZOS)
    im.paste(selo, ((A4[0] - selo.width) // 2, round(196 * MM)), selo)

    draw.line([round(24 * MM), round(258 * MM), A4[0] - round(24 * MM),
               round(258 * MM)], fill=(226, 218, 206), width=2)
    draw.text((round(24 * MM), round(263 * MM)), "Material licenciado · uso profissional",
              font=tiny, fill=FAINT)
    larg_txt = draw.textlength("colorhugs.pt", font=tiny)
    draw.text((A4[0] - round(24 * MM) - larg_txt, round(263 * MM)), "colorhugs.pt",
              font=tiny, fill=FAINT)
    return im


def instrucoes():
    """As páginas de instruções, lidas de `folhas-instrucoes.md`.

    **A mesma regra dos livros: o que está em citação vai para a página.** O
    comentário editorial fica no markdown e não chega à mesa.
    """
    import re

    texto = open(SOURCE, encoding="utf-8").read()
    seccoes = []
    for bloco in re.split(r"\n(?=## )", texto):
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
            seccoes.append((m.group(1).strip(), paras))

    big, small, tiny = fonts()
    corpo = ImageFont.truetype(os.path.join(FONTS, "Nunito-Medium.ttf"),
                               round(3.4 * MM))
    negro = ImageFont.truetype(os.path.join(FONTS, "Nunito-Bold.ttf"),
                               round(3.4 * MM))
    sub = ImageFont.truetype(os.path.join(FONTS, "Baloo2-Bold.ttf"),
                             round(5.2 * MM))

    paginas, im, draw = [], None, None
    y = 0
    margem, largura = 18, 174

    def nova(primeira=False):
        nonlocal im, draw, y
        if im is not None:
            credit(im, draw)
            paginas.append(im)
        im, draw = page()
        draw.text((round(margem * MM), round(13 * MM)), FAMILY.upper(),
                  font=tiny, fill=FAMILY_COLOUR)
        if primeira:
            draw.text((round(margem * MM), round(18 * MM)),
                      "Instruções e exploração", font=big, fill=INK)
            draw.rounded_rectangle(
                [round(margem * MM), round(29.5 * MM),
                 round((margem + 28) * MM), round(30.7 * MM)],
                radius=round(0.6 * MM), fill=FAMILY_COLOUR)
            y = 40
        else:
            y = 24

    nova(primeira=True)

    for titulo, paras in seccoes:
        if titulo.lower() != "abertura":
            if y > 210:
                nova()
            draw.text((round(margem * MM), round(y * MM)), titulo, font=sub, fill=INK)
            y += 10
        for para in paras:
            # **Negrito parágrafo a parágrafo e não palavra a palavra.** Compor
            # negrito no meio de uma linha exige medir cada troço; num texto de
            # instruções o ganho não paga a complexidade, e o que carrega o
            # sentido é a frase inteira.
            forte = para.startswith("**")
            limpo = para.replace("**", "").replace("*", "")
            fonte = negro if forte else corpo
            for linha in wrap_text(draw, limpo, fonte, round(largura * MM)):
                if y > 262:
                    nova()
                draw.text((round(margem * MM), round(y * MM)), linha,
                          font=fonte, fill=INK if forte else (78, 70, 60))
                y += 5.4
            y += 3.2

    credit(im, draw)
    paginas.append(im)
    return paginas


def wrap_text(draw, texto, fonte, largura_px):
    linhas, actual = [], ""
    for palavra in texto.split():
        teste = (actual + " " + palavra).strip()
        if draw.textlength(teste, font=fonte) <= largura_px:
            actual = teste
        else:
            linhas.append(actual)
            actual = palavra
    if actual:
        linhas.append(actual)
    return linhas


SHEETS = {
    "casa-das-sete": casa_das_sete,
    "antes-durante-depois": antes_durante_depois,
    "duas-listas": duas_listas,
}


def main():
    os.makedirs(OUT, exist_ok=True)
    folhas = []
    for name, build in SHEETS.items():
        im = build()
        im.save(os.path.join(OUT, f"{name}.pdf"), resolution=DPI)
        im.save(os.path.join(OUT, f"{name}.png"))
        folhas.append(im)
        print(f"{name}.pdf")

    # O dado é a quarta peça da família e entra no caderno pela mesma razão que
    # as folhas: junta-se, não se prende.
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "dado", os.path.join(ROOT, "scripts", "build-strategy-die.py"))
    dado = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dado)
    dado.main()
    for familia, _, _ in dado.dados():
        folhas.append(Image.open(
            os.path.join(OUT, f"dado-{familia.lower()}.png")).convert("RGB"))

    spec = importlib.util.spec_from_file_location(
        "jogos", os.path.join(ROOT, "scripts", "build-session-games.py"))
    jogos = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(jogos)
    jogos.main()
    for nome in jogos.JOGOS:
        folhas.append(Image.open(os.path.join(OUT, f"{nome}.png")).convert("RGB"))

    # **Os bonecos passam a peça desta família** (D-351). O Depósito saiu: é
    # produto à parte, com identidade própria.
    spec = importlib.util.spec_from_file_location(
        "bonecos", os.path.join(ROOT, "scripts", "build-size-figures.py"))
    bon = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bon)
    bon.main()
    for familia in bon.FAMILIES:
        folhas.append(Image.open(os.path.join(
            ROOT, "docs", "materials", "bonecos",
            f"bonecos-{familia}.png")).convert("RGB"))

    # **O caderno junta-as e não as prende.** Cada folha continua a existir no
    # seu PDF e a imprimir-se sozinha; o caderno é conveniência de arrumação,
    # não é um percurso (D-327).
    paginas = [capa()] + instrucoes() + folhas
    alvo = os.path.join(OUT, "pecas-de-sessao.pdf")
    paginas[0].save(alvo, save_all=True, append_images=paginas[1:],
                    resolution=DPI, format="PDF")
    print(f"pecas-de-sessao.pdf · {len(paginas)} páginas")


if __name__ == "__main__":
    main()
