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
EMOTIONS = os.path.join(ROOT, "artwork", "emotions")
SESSAO = os.path.join(ROOT, "artwork", "sessao")
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


_LIMPAS = {}


def limpa(nome):
    """A figura sem o fundo branco nem o rebordo de autocolante."""
    if nome in _LIMPAS:
        return _LIMPAS[nome]
    im = Image.open(os.path.join(EMOTIONS, nome)).convert("RGBA")
    px = im.load()
    w, h = im.size
    fila = [(x, y) for x in range(w) for y in (0, h - 1)]
    fila += [(x, y) for y in range(h) for x in (0, w - 1)]
    visto = set()
    while fila:
        x, y = fila.pop()
        if (x, y) in visto or not (0 <= x < w and 0 <= y < h):
            continue
        visto.add((x, y))
        r, g, b, a = px[x, y]
        if r < 236 or g < 236 or b < 236:
            continue
        px[x, y] = (r, g, b, 0)
        fila += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    _LIMPAS[nome] = im.crop(im.getbbox())
    return _LIMPAS[nome]


def pecas(im, draw, x0, y, familias, largura=24, colunas=4):
    """As peças, desenhadas para ficarem de pé (D-365).

    **Uma figura recortada plana não fica de pé no tabuleiro** — cai, e uma peça
    que cai a cada jogada é uma peça que se perde. Cada peça é a figura mais a
    sua imagem invertida por cima, unidas por uma dobra: dobrada ao meio fica de
    dois lados, abre em tenda, e assenta.
    """
    _, small, tiny, negro = fontes()
    draw.text((round(x0 * MM), round(y * MM)), "As peças", font=negro, fill=INK)
    draw.text((round(x0 * MM), round((y + 5.5) * MM)),
              "Recortar pelo traço, dobrar pela linha do meio e abrir para ficar "
              "de pé.", font=small, fill=FAINT)
    passo = round(2.2 * MM)
    alvo = round(largura * MM)
    for i, familia in enumerate(familias):
        c = i % colunas
        fig = limpa(familia)
        e = min(alvo / fig.width, alvo / fig.height)
        f2 = fig.resize((round(fig.width * e), round(fig.height * e)), Image.LANCZOS)
        espelho = f2.transpose(Image.FLIP_TOP_BOTTOM)

        cx = round((x0 + c * (largura + 16)) * MM)
        topo = round((y + 14) * MM)
        im.paste(espelho, (cx, topo), espelho)
        dobra = topo + espelho.height
        im.paste(f2, (cx, dobra), f2)

        caixa = [cx - round(3 * MM), topo - round(3 * MM),
                 cx + f2.width + round(3 * MM), dobra + f2.height + round(3 * MM)]
        for xx in range(caixa[0], caixa[2], passo * 2):
            draw.line([xx, caixa[1], xx + passo, caixa[1]], fill=FAINT, width=2)
            draw.line([xx, caixa[3], xx + passo, caixa[3]], fill=FAINT, width=2)
        for yy in range(caixa[1], caixa[3], passo * 2):
            draw.line([caixa[0], yy, caixa[0], yy + passo], fill=FAINT, width=2)
            draw.line([caixa[2], yy, caixa[2], yy + passo], fill=FAINT, width=2)
        # A dobra, a tracejado forte, atravessando a peça toda.
        for xx in range(caixa[0], caixa[2], round(3 * MM)):
            draw.line([xx, dobra, xx + round(1.6 * MM), dobra], fill=BOX, width=3)


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
        ("Uma partida demora à volta de minuto e meio. Jogam-se várias.", False),
    ], 44)

    # **O percurso é arte quando existe** (D-361). Catorze rectângulos iguais em
    # serpentina são um diagrama; um caminho desenhado é um caminho. O
    # construtor cai na grelha enquanto a arte não existir.
    percurso = os.path.join(SESSAO, "percurso.png")
    if os.path.exists(percurso):
        arte = Image.open(percurso).convert("RGBA")
        largura_mm = 174
        arte = arte.resize((round(largura_mm * MM),
                            round(arte.height * largura_mm * MM / arte.width)),
                           Image.LANCZOS)
        im.paste(arte, ((A4[0] - arte.width) // 2, round(88 * MM)), arte)
    else:
        lado, gap = 24, 5
        x0, y0 = 24, 76
        casas = []
        for linha in range(3):
            for coluna in range(5):
                c = coluna if linha % 2 == 0 else 4 - coluna
                casas.append((x0 + c * (lado + gap), y0 + linha * (lado + gap)))
        casas = casas[:15]
        for i, (cx, cy) in enumerate(casas):
            extremo = i in (0, len(casas) - 1)
            draw.rounded_rectangle(
                [round(cx * MM), round(cy * MM), round((cx + lado) * MM),
                 round((cy + lado) * MM)],
                radius=round(4 * MM), outline=BOX, width=6 if extremo else 3)
        fim_percurso = y0 + 3 * (lado + gap) + 6

    credito(im, draw)
    return im


def outra_vez_pecas():
    """O dado e as peças do «Outra vez», em folha própria.

    **Não cabiam na folha do percurso, e encolhê-los era pior** (D-363). Um cubo
    de papel de 20 mm é difícil de dobrar, pior de colar e mau de lançar na mão
    de uma criança de seis anos; os dados das estratégias têm 48 mm. Com faces
    de 38 mm a planificação ocupa 152 mm de altura, e depois do percurso só
    sobravam 106. **Papel é barato; um dado que não se consegue montar não é.**

    **As peças também cresceram por medida e não por gosto:** a pedra do
    percurso tem 29 mm, e o recorte anterior tinha 30 — a peça era maior do que
    o sítio onde tem de assentar.
    """
    im, draw = pagina("Outra vez — o dado e as peças",
                      "Recortar pelo traço cheio, dobrar pelo tracejado, colar pelas abas.")
    _, small, tiny, negro = fontes()

    faces = ["1", "2", "3", "1", "2", "volta"]
    cruz = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (1, 3)]
    L, aba, ox, oy = 36, 8, 52, 48
    ocupadas = set(cruz)

    def caixa(c, l):
        return (round((ox + c * L) * MM), round((oy + l * L) * MM),
                round((ox + (c + 1) * L) * MM), round((oy + (l + 1) * L) * MM))

    for c, l in cruz:
        bx0, by0, bx1, by1 = caixa(c, l)
        a, recuo = round(aba * MM), round(6 * MM)
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

    grande = ImageFont.truetype(os.path.join(FONTS, "Baloo2-Bold.ttf"), round(12 * MM))
    for (c, l), texto in zip(cruz, faces):
        bx0, by0, bx1, by1 = caixa(c, l)
        draw.rectangle([bx0, by0, bx1, by1], outline=CUT, width=4)
        cx, cy = (bx0 + bx1) / 2, (by0 + by1) / 2
        if texto.isdigit():
            w = draw.textlength(texto, font=grande)
            draw.text((cx - w / 2, cy - round(7 * MM)), texto, font=grande, fill=INK)
        else:
            r = round(9 * MM)
            draw.arc([cx - r, cy - r, cx + r, cy + r], 20, 320, fill=INK,
                     width=round(2 * MM))
            p1 = (cx + r * 0.94, cy - r * 0.34)
            draw.polygon([p1, (p1[0] - round(4.4 * MM), p1[1] - round(2.4 * MM)),
                          (p1[0] - round(1.6 * MM), p1[1] + round(4 * MM))], fill=INK)
            w = draw.textlength(texto, font=small)
            draw.text((cx - w / 2, by1 - round(9 * MM)), texto, font=small, fill=FAINT)

    for c, l in cruz:
        bx0, by0, bx1, by1 = caixa(c, l)
        if (c, l + 1) in ocupadas:
            tracejado(draw, bx0, by1, bx1, by1, FOLD)
        if (c + 1, l) in ocupadas:
            tracejado(draw, bx1, by0, bx1, by1, FOLD)

    # A peça tem de assentar na pedra do percurso, que mede 29 mm.
    pecas(im, draw, 22, 196, ["angry.png", "happy.png", "calm.png", "sad.png"],
          largura=26)

    credito(im, draw)
    return im


def coracao_pequeno(draw, cx, cy, largura, cor):
    """Um coração a traço, para os cantos da moldura."""
    import math

    pontos = []
    for i in range(80):
        t = 2 * math.pi * i / 80
        x = 16 * math.sin(t) ** 3
        y = (13 * math.cos(t) - 5 * math.cos(2 * t)
             - 2 * math.cos(3 * t) - math.cos(4 * t))
        pontos.append((round((cx + x * largura / 32) * MM),
                       round((cy - y * largura / 32) * MM)))
    draw.polygon(pontos, outline=cor, width=3)


def a_vez():
    """O tabuleiro do «A vez»: as regras e os doze quadrados.

    **A espera é imposta pela sorte e não por um adulto.** É a diferença que faz
    esta peça funcionar: ninguém está a mandar esperar, a espera apenas
    acontece — e é isso que se pratica.
    """
    im, draw = pagina("A vez", "Um desenho a dois. Às vezes a vez é agora, às vezes não.")
    _, small, tiny, negro = fontes()

    regras(draw, [
        ("Dois jogadores e um desenho só, feito por ambos.", False),
        ("Antes de cada vez, tira-se uma carta do monte, virada para baixo.", False),
        ("Sai «agora»: desenha-se uma coisa e marca-se um quadrado.", True),
        ("Sai «espera»: passa a vez, e não se desenha nada.", True),
        ("Quando o monte acaba, baralha-se e continua-se.", False),
        ("Acaba quando os doze quadrados estiverem marcados.", False),
    ], 44)

    # **Os quadrados em cima, o desenho em baixo** (D-365). Doze quadradinhos
    # para desenhar dentro davam doze desenhos pequenos; assim **o desenho é um
    # desenho**, e os quadrados passam a marcar o que já se fez.
    draw.text((round(20 * MM), round(80 * MM)), "O QUE JÁ SE FEZ", font=tiny,
              fill=FAMILY_COLOUR)
    lado, gap = 11, 4
    gx0, gy0 = 20, 86
    for i in range(12):
        cx = gx0 + i * (lado + gap)
        draw.rounded_rectangle(
            [round(cx * MM), round(gy0 * MM), round((cx + lado) * MM),
             round((gy0 + lado) * MM)],
            radius=round(2 * MM), outline=BOX, width=3)

    # A moldura do desenho: uma linha dupla, com folga entre as duas.
    mx0, my0, mx1, my1 = 20, 108, 190, 268
    draw.rounded_rectangle(
        [round(mx0 * MM), round(my0 * MM), round(mx1 * MM), round(my1 * MM)],
        radius=round(7 * MM), outline=FAMILY_COLOUR, width=5)
    draw.rounded_rectangle(
        [round((mx0 + 3) * MM), round((my0 + 3) * MM), round((mx1 - 3) * MM),
         round((my1 - 3) * MM)],
        radius=round(5 * MM), outline=FAMILY_COLOUR, width=2)
    for cx, cy in ((mx0 + 10, my0 + 10), (mx1 - 10, my0 + 10),
                   (mx0 + 10, my1 - 10), (mx1 - 10, my1 - 10)):
        coracao_pequeno(draw, cx, cy, 7, FAMILY_COLOUR)

    rot = "O DESENHO"
    w = draw.textlength(rot, font=tiny)
    draw.rectangle([round((mx0 + 16) * MM), round((my0 - 2) * MM),
                    round((mx0 + 16) * MM) + w + round(4 * MM),
                    round((my0 + 4) * MM)], fill="white")
    draw.text((round((mx0 + 18) * MM), round((my0 - 1.6) * MM)), rot,
              font=tiny, fill=FAMILY_COLOUR)

    credito(im, draw)
    return im


CARTA = (56, 52)


def carta_a_vez(agora):
    cw, ch = CARTA
    card = Image.new("RGB", (round(cw * MM), round(ch * MM)), "white")
    draw = ImageDraw.Draw(card)
    pad = round(2.5 * MM)
    draw.rounded_rectangle([pad, pad, card.width - pad, card.height - pad],
                           radius=round(4 * MM), fill=(255, 253, 249),
                           outline=INK, width=4)

    arte = os.path.join(SESSAO, "carta-agora.png" if agora else "carta-espera.png")
    if os.path.exists(arte):
        fig = Image.open(arte).convert("RGBA")
        alvo = round(26 * MM)
        e = alvo / fig.height
        f2 = fig.resize((round(fig.width * e), alvo), Image.LANCZOS)
        card.paste(f2, (card.width // 2 - f2.width // 2, round(7 * MM)), f2)

    _, small, tiny, negro = fontes()
    palavra = "agora" if agora else "espera"
    w = draw.textlength(palavra, font=negro)
    draw.text((card.width / 2 - w / 2, round((ch - 15) * MM)), palavra,
              font=negro, fill=INK)

    marca = "© ColorHugs · colorhugs.pt"
    mini = ImageFont.truetype(os.path.join(FONTS, "Nunito-Medium.ttf"),
                              round(2.4 * MM))
    w = draw.textlength(marca, font=mini)
    draw.text((card.width / 2 - w / 2, round((ch - 7) * MM)), marca,
              font=mini, fill=FAINT)
    return card


def carta_a_vez_verso():
    """O verso, **igual nas doze**.

    Se o verso dissesse qual é a carta, o jogo acabava: o monte está virado para
    baixo e a espera tem de ser uma surpresa. **E impresso só de um lado, o
    desenho da frente vê-se por transparência no papel de impressora** — é a
    outra razão para haver verso.
    """
    cw, ch = CARTA
    card = Image.new("RGB", (round(cw * MM), round(ch * MM)), "white")
    draw = ImageDraw.Draw(card)
    pad = round(2.5 * MM)
    draw.rounded_rectangle([pad, pad, card.width - pad, card.height - pad],
                           radius=round(4 * MM), fill=FAMILY_COLOUR,
                           outline=INK, width=4)

    disc = round(30 * MM)
    cx, cy = card.width // 2, round(23 * MM)
    pale = tuple(round(255 - (255 - c) * 0.10) for c in FAMILY_COLOUR)
    draw.ellipse([cx - disc // 2, cy - disc // 2, cx + disc // 2, cy + disc // 2],
                 fill=pale)
    logo = Image.open(os.path.join(ROOT, "public", "assets", "branding",
                                   "colorhugs-logo.webp")).convert("RGBA")
    w = round(23 * MM)
    logo = logo.resize((w, round(logo.height * w / logo.width)), Image.LANCZOS)
    card.paste(logo, (cx - logo.width // 2, cy - logo.height // 2), logo)

    f = ImageFont.truetype(os.path.join(FONTS, "Baloo2-Bold.ttf"), round(5 * MM))
    w = draw.textlength("A vez", font=f)
    draw.text((card.width / 2 - w / 2, round(40 * MM)), "A vez", font=f,
              fill=(255, 255, 255))
    return card


def folha_a_vez(cartas, espelhar=False):
    im = Image.new("RGB", A4, "white")
    draw = ImageDraw.Draw(im)
    _, small, tiny, negro = fontes()
    draw.text((round(18 * MM), round(13 * MM)), FAMILY.upper(), font=tiny,
              fill=FAMILY_COLOUR)
    draw.text((round(18 * MM), round(18 * MM)),
              "A vez — as cartas" + (" (verso)" if espelhar else ""),
              font=fontes()[0], fill=INK)
    cw, ch = CARTA
    mx = (210 - 3 * cw) / 4
    my = 34
    gy = (297 - my - 14 - 4 * ch) / 3
    for i, c in enumerate(cartas):
        col, lin = i % 3, i // 3
        if espelhar:
            col = 2 - col
        im.paste(c, (round((mx + col * (cw + mx)) * MM),
                     round((my + lin * (ch + gy)) * MM)))
    w = draw.textlength(CREDIT, font=tiny)
    draw.text(((A4[0] - w) / 2, A4[1] - round(9 * MM)), CREDIT, font=tiny, fill=FAINT)
    return im


JOGOS = {"outra-vez": outra_vez, "outra-vez-pecas": outra_vez_pecas,
         "a-vez": a_vez}


def main():
    os.makedirs(OUT, exist_ok=True)
    for nome, constroi in JOGOS.items():
        im = constroi()
        im.save(os.path.join(OUT, f"{nome}.pdf"), resolution=DPI)
        im.save(os.path.join(OUT, f"{nome}.png"))
        print(f"{nome}.pdf")

    # As doze cartas do «A vez», frente e verso, num só ficheiro.
    frentes = [carta_a_vez(i % 2 == 0) for i in range(12)]
    versos = [carta_a_vez_verso()] * 12
    paginas = [folha_a_vez(frentes), folha_a_vez(versos, espelhar=True)]
    alvo = os.path.join(OUT, "a-vez-cartas.pdf")
    paginas[0].save(alvo, save_all=True, append_images=paginas[1:],
                    resolution=DPI, format="PDF")
    for i, pg in enumerate(paginas):
        pg.save(os.path.join(OUT, f"a-vez-cartas-{i + 1}.png"))
    print("a-vez-cartas.pdf · 2 folhas")


if __name__ == "__main__":
    main()
