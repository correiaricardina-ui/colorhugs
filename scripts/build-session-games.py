#!/usr/bin/env python3
"""Constrói os dois jogos pequenos (D-347).

    python3 scripts/build-session-games.py

`outra-vez.pdf` — o jogo em que se perde. Um percurso curto, um dado, e duas
faces que mandam voltar ao princípio.

`a-vez.pdf` — o jogo em que se espera. Um desenho a dois, e um baralho pequeno
que decide se a vez é agora ou se é preciso esperar.

**São dois jogos e não duas variantes do mesmo**, e a razão é o andamento.
Perder tem de acontecer **muitas vezes e depressa**, ou não se pratica nada;
esperar tem de acontecer **devagar**, ou não há espera nenhuma. Um jogo não pode
ser rápido e lento ao mesmo tempo.
"""

import os

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(ROOT, "assets", "fonts")
FIGURAS = os.path.join(ROOT, "artwork", "sessao", "dados")
OUT = os.path.join(ROOT, "docs", "materials", "folhas")

DPI = 200
MM = DPI / 25.4
A4 = (round(210 * MM), round(297 * MM))

INK = (58, 51, 43)
FAINT = (168, 155, 138)
BOX = (120, 110, 96)
CUT = (120, 110, 96)
FOLD = (198, 188, 174)
FAMILY = "Peças de sessão"
FAMILY_COLOUR = (150, 128, 96)
CREDIT = "© ColorHugs · colorhugs.pt · Material licenciado"


def fontes():
    return (
        ImageFont.truetype(os.path.join(FONTS, "Baloo2-Bold.ttf"), round(7.5 * MM)),
        ImageFont.truetype(os.path.join(FONTS, "Nunito-Medium.ttf"), round(3.6 * MM)),
        ImageFont.truetype(os.path.join(FONTS, "Nunito-Medium.ttf"), round(2.9 * MM)),
        ImageFont.truetype(os.path.join(FONTS, "Nunito-Bold.ttf"), round(3.6 * MM)),
    )


def pagina(titulo, subtitulo):
    im = Image.new("RGB", A4, "white")
    draw = ImageDraw.Draw(im)
    big, small, tiny, _ = fontes()
    draw.text((round(18 * MM), round(13 * MM)), FAMILY.upper(), font=tiny,
              fill=FAMILY_COLOUR)
    draw.text((round(18 * MM), round(18 * MM)), titulo, font=big, fill=INK)
    draw.rounded_rectangle(
        [round(18 * MM), round(29.5 * MM), round(46 * MM), round(30.7 * MM)],
        radius=round(0.6 * MM), fill=FAMILY_COLOUR)
    draw.text((round(18 * MM), round(34 * MM)), subtitulo, font=small, fill=FAINT)
    return im, draw


def credito(im, draw):
    _, _, tiny, _ = fontes()
    w = draw.textlength(CREDIT, font=tiny)
    draw.text(((A4[0] - w) / 2, A4[1] - round(13 * MM)), CREDIT, font=tiny, fill=FAINT)


def regras(draw, linhas, y):
    _, small, _, negro = fontes()
    for texto, forte in linhas:
        draw.text((round(18 * MM), round(y * MM)), texto,
                  font=negro if forte else small, fill=INK if forte else (96, 88, 78))
        y += 5.6
    return y


def tracejado(draw, x0, y0, x1, y1, cor, passo=2.4):
    passo = round(passo * MM)
    if x0 == x1:
        for y in range(y0, y1, passo * 2):
            draw.line([x0, y, x0, min(y + passo, y1)], fill=cor, width=3)
    else:
        for x in range(x0, x1, passo * 2):
            draw.line([x, y0, min(x + passo, x1), y0], fill=cor, width=3)


# --------------------------------------------------------------------------

def outra_vez():
    """O jogo em que se perde.

    **Sorte pura e nenhuma perícia.** É a condição que torna perder suportável:
    quem perde não perdeu por ser pior a alguma coisa, e não há competência
    nenhuma a defender. Duas das seis faces mandam voltar ao princípio, e por
    isso perde-se muitas vezes numa sessão.
    """
    im, draw = pagina("Outra vez", "Um percurso curto. Perde-se muitas vezes, e é de propósito.")
    _, small, tiny, negro = fontes()

    y = regras(draw, [
        ("Dois jogadores. Cada um escolhe uma figura e põe-na no início.", False),
        ("À vez, lança-se o dado e anda-se as casas que saírem.", False),
        ("Se sair «volta», volta-se ao princípio — e joga-se outra vez.", True),
        ("Ganha quem chegar ao fim. Depois recomeça-se.", False),
        ("Uma partida demora um minuto ou dois. Jogam-se várias.", False),
    ], 44)

    # O percurso: catorze casas em serpentina.
    lado, gap = 24, 5
    x0, y0 = 24, 76
    casas = []
    for linha in range(3):
        for coluna in range(5):
            c = coluna if linha % 2 == 0 else 4 - coluna
            casas.append((x0 + c * (lado + gap), y0 + linha * (lado + gap)))
    casas = casas[:14]

    for i, (cx, cy) in enumerate(casas):
        primeira, ultima = i == 0, i == len(casas) - 1
        draw.rounded_rectangle(
            [round(cx * MM), round(cy * MM), round((cx + lado) * MM),
             round((cy + lado) * MM)],
            radius=round(4 * MM), outline=BOX,
            width=6 if (primeira or ultima) else 3)
        if primeira or ultima:
            rot = "Início" if primeira else "Fim"
            w = draw.textlength(rot, font=negro)
            draw.text((round((cx + lado / 2) * MM) - w / 2,
                       round((cy + lado / 2 - 2) * MM)), rot, font=negro, fill=INK)

    # O dado, na parte de baixo.
    draw.text((round(18 * MM), round(172 * MM)), "O dado", font=negro, fill=INK)
    draw.text((round(18 * MM), round(178 * MM)),
              "Recortar pelo traço cheio, dobrar pelo tracejado, colar pelas abas.",
              font=small, fill=FAINT)

    faces = ["1", "2", "3", "1", "volta", "volta"]
    cruz = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (1, 3)]
    L, aba, ox, oy = 21, 6, 84, 190
    ocupadas = set(cruz)

    def caixa(c, l):
        return (round((ox + c * L) * MM), round((oy + l * L) * MM),
                round((ox + (c + 1) * L) * MM), round((oy + (l + 1) * L) * MM))

    for c, l in cruz:
        bx0, by0, bx1, by1 = caixa(c, l)
        a, recuo = round(aba * MM), round(4 * MM)
        if (c, l - 1) not in ocupadas:
            draw.polygon([(bx0 + recuo, by0 - a), (bx1 - recuo, by0 - a),
                          (bx1, by0), (bx0, by0)], outline=CUT, width=3)
        if (c, l + 1) not in ocupadas:
            draw.polygon([(bx0, by1), (bx1, by1), (bx1 - recuo, by1 + a),
                          (bx0 + recuo, by1 + a)], outline=CUT, width=3)
        if (c - 1, l) not in ocupadas:
            draw.polygon([(bx0 - a, by0 + recuo), (bx0, by0), (bx0, by1),
                          (bx0 - a, by1 - recuo)], outline=CUT, width=3)
        if (c + 1, l) not in ocupadas:
            draw.polygon([(bx1, by0), (bx1 + a, by0 + recuo), (bx1 + a, by1 - recuo),
                          (bx1, by1)], outline=CUT, width=3)

    grande = ImageFont.truetype(os.path.join(FONTS, "Baloo2-Bold.ttf"), round(7.5 * MM))
    for (c, l), texto in zip(cruz, faces):
        bx0, by0, bx1, by1 = caixa(c, l)
        draw.rectangle([bx0, by0, bx1, by1], outline=CUT, width=4)
        fonte = grande if texto.isdigit() else negro
        w = draw.textlength(texto, font=fonte)
        draw.text(((bx0 + bx1) / 2 - w / 2, (by0 + by1) / 2 - round(4 * MM)),
                  texto, font=fonte, fill=INK)

    for c, l in cruz:
        bx0, by0, bx1, by1 = caixa(c, l)
        if (c, l + 1) in ocupadas:
            tracejado(draw, bx0, by1, bx1, by1, FOLD)
        if (c + 1, l) in ocupadas:
            tracejado(draw, bx1, by0, bx1, by1, FOLD)

    credito(im, draw)
    return im


def a_vez():
    """O jogo em que se espera.

    **A espera é imposta pela sorte e não por um adulto.** É a diferença que faz
    esta peça funcionar: ninguém está a mandar esperar, a espera apenas
    acontece — e é isso que se pratica.
    """
    im, draw = pagina("A vez", "Um desenho a dois. Às vezes a vez é agora, às vezes não.")
    _, small, tiny, negro = fontes()

    regras(draw, [
        ("Dois jogadores e um desenho só, feito por ambos.", False),
        ("Antes de cada vez, tira-se uma carta do monte, virada para baixo.", False),
        ("Sai «agora»: preenche-se um quadrado. Sai «espera»: passa a vez.", True),
        ("Quando o monte acaba, baralha-se e continua-se.", False),
        ("Acaba quando os doze quadrados estiverem preenchidos.", False),
    ], 44)

    # O desenho partilhado: doze quadrados.
    lado, gap, x0, y0 = 32, 7, 32, 76
    for i in range(12):
        c, l = i % 4, i // 4
        cx = x0 + c * (lado + gap)
        cy = y0 + l * (lado + gap)
        draw.rounded_rectangle(
            [round(cx * MM), round(cy * MM), round((cx + lado) * MM),
             round((cy + lado) * MM)],
            radius=round(3 * MM), outline=BOX, width=3)

    # As cartas: seis «agora», seis «espera».
    draw.text((round(18 * MM), round(200 * MM)), "As cartas", font=negro, fill=INK)
    draw.text((round(18 * MM), round(206 * MM)),
              "Recortar as doze. Metade diz agora, metade diz espera.",
              font=small, fill=FAINT)

    cw, ch, cgap, cx0, cy0 = 40, 19, 4, 22, 214
    palavras = ["agora", "espera"] * 6
    for i, palavra in enumerate(palavras):
        c, l = i % 4, i // 4
        px = cx0 + c * (cw + cgap)
        py = cy0 + l * (ch + cgap)
        draw.rounded_rectangle(
            [round(px * MM), round(py * MM), round((px + cw) * MM),
             round((py + ch) * MM)],
            radius=round(2.5 * MM), outline=CUT, width=3)
        w = draw.textlength(palavra, font=negro)
        draw.text((round((px + cw / 2) * MM) - w / 2,
                   round((py + ch / 2 - 2.4) * MM)), palavra, font=negro, fill=INK)

    credito(im, draw)
    return im


JOGOS = {"outra-vez": outra_vez, "a-vez": a_vez}


def main():
    os.makedirs(OUT, exist_ok=True)
    for nome, constroi in JOGOS.items():
        im = constroi()
        im.save(os.path.join(OUT, f"{nome}.pdf"), resolution=DPI)
        im.save(os.path.join(OUT, f"{nome}.png"))
        print(f"{nome}.pdf")


if __name__ == "__main__":
    main()
