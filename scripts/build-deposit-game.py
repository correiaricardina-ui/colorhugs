#!/usr/bin/env python3
"""Constrói O Depósito (D-348).

    python3 scripts/build-deposit-game.py

Duas folhas A4: `deposito-tabuleiro.pdf` com o depósito e as regras, e
`deposito-cartas.pdf` com as doze cartas de dia e as fichas para recortar.

As cartas e as regras vêm de `docs/materials/deposito.md` — as listas numeradas
sob cada secção de dias, e as regras em citação.

**A escolha do dia bom é o coração da peça** (D-348): encher o depósito ou
reparar uma carta que ficou por resolver, nunca as duas. Sem essa escolha isto
seria um percurso que ilustra a lógica do depósito sem a fazer sentir.
"""

import os
import re

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(ROOT, "assets", "fonts")
EMOTIONS = os.path.join(ROOT, "artwork", "emotions")
SESSAO = os.path.join(ROOT, "artwork", "sessao")
OUT = os.path.join(ROOT, "docs", "materials", "folhas")
SOURCE = os.path.join(ROOT, "docs", "materials", "deposito.md")

DPI = 200
MM = DPI / 25.4
A4 = (round(210 * MM), round(297 * MM))
A4L = (round(297 * MM), round(210 * MM))
A3L = (round(420 * MM), round(297 * MM))

# Medida de carta de jogar. **42×46 mm era pequeno de mais para uma criança
# manusear num jogo de mesa**, e os lugares do tabuleiro passam a ter
# exactamente este tamanho.
CARTA = (63, 88)



INK = (58, 51, 43)
FAINT = (168, 155, 138)
BOX = (120, 110, 96)
CUT = (120, 110, 96)
FAMILY = "Peças de sessão"
FAMILY_COLOUR = (150, 128, 96)
CREDIT = "© ColorHugs · colorhugs.pt · Material licenciado"

FIGURAS = {
    "Calmo": "calm.png", "Feliz": "happy.png", "Zangado": "angry.png",
    "Triste": "sad.png", "Assustado": "scared.png",
    "Envergonhado": "ashamed.png", "Aborrecido": "bored.png",
}

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


def fonte(nome, mm):
    return ImageFont.truetype(os.path.join(FONTS, nome), round(mm * MM))


def leitura():
    texto = open(SOURCE, encoding="utf-8").read()
    regras = []
    m = re.search(r"## As regras.*?\n(.*?)(?=\n## )", texto, re.S)
    buf = []
    for linha in m.group(1).splitlines():
        if linha.startswith(">"):
            corpo = linha[1:].strip()
            if corpo:
                buf.append(corpo)
            elif buf:
                regras.append(" ".join(buf))
                buf = []
        elif buf:
            regras.append(" ".join(buf))
            buf = []
    if buf:
        regras.append(" ".join(buf))
    regras = [re.sub(r"\*\*(.+?)\*\*", r"\1", r).replace("*", "") for r in regras]

    cartas = []
    for item in re.findall(r"^\d+\.\s+(.+)$", texto, re.M):
        partes = [p.strip() for p in item.split("·")]
        if len(partes) < 2 or partes[0] not in FIGURAS:
            continue
        custo = None
        if len(partes) == 3:
            custo = int(re.sub(r"\D", "", partes[2]))
        cartas.append((partes[0], partes[1], custo))
    if len(cartas) != 24:
        raise SystemExit(f"{len(cartas)} cartas, deviam ser vinte e quatro")
    return regras, cartas


def cabeca(draw, titulo, subtitulo):
    draw.text((round(18 * MM), round(13 * MM)), FAMILY.upper(),
              font=fonte("Nunito-Medium.ttf", 2.9), fill=FAMILY_COLOUR)
    draw.text((round(18 * MM), round(18 * MM)), titulo,
              font=fonte("Baloo2-Bold.ttf", 7.5), fill=INK)
    draw.rounded_rectangle(
        [round(18 * MM), round(29.5 * MM), round(46 * MM), round(30.7 * MM)],
        radius=round(0.6 * MM), fill=FAMILY_COLOUR)
    draw.text((round(18 * MM), round(34 * MM)), subtitulo,
              font=fonte("Nunito-Medium.ttf", 3.6), fill=FAINT)


def rodape(im, draw):
    """O rodapé, ao pé da folha — seja ela ao alto ou ao baixo.

    **O tabuleiro passou a ao baixo e o rodapé continuou a ser posto na altura
    da folha ao alto**, ou seja fora da página. Passa a medir a folha em que
    está a ser escrito.
    """
    f = fonte("Nunito-Medium.ttf", 2.9)
    w = draw.textlength(CREDIT, font=f)
    draw.text(((im.width - w) / 2, im.height - round(11 * MM)), CREDIT,
              font=f, fill=FAINT)


def quebra(draw, texto, f, largura):
    linhas, actual = [], ""
    for palavra in texto.split():
        teste = (actual + " " + palavra).strip()
        if draw.textlength(teste, font=f) <= largura:
            actual = teste
        else:
            linhas.append(actual)
            actual = palavra
    if actual:
        linhas.append(actual)
    return linhas


def tabuleiro():
    """O tabuleiro, em A3 ao baixo, com um lugar para cada coisa.

    **Os lugares têm o tamanho real das cartas que lá assentam** (D-353): um
    lugar mais pequeno do que a carta é uma sugestão, não um lugar, e um maior
    deixa a mesa outra vez a fazer o trabalho.

    **As regras saíram daqui.** Um tabuleiro com dez linhas de texto impressas ao
    lado não é um tabuleiro: é uma folha de instruções com um desenho.
    """
    im = Image.new("RGB", A3L, "white")
    draw = ImageDraw.Draw(im)

    draw.text((round(20 * MM), round(16 * MM)), FAMILY.upper(),
              font=fonte("Nunito-Medium.ttf", 3.2), fill=FAMILY_COLOUR)
    draw.text((round(20 * MM), round(22 * MM)), "O Depósito",
              font=fonte("Baloo2-Bold.ttf", 11), fill=INK)
    draw.rounded_rectangle(
        [round(20 * MM), round(39 * MM), round(58 * MM), round(40.4 * MM)],
        radius=round(0.7 * MM), fill=FAMILY_COLOUR)

    frasco = os.path.join(SESSAO, "deposito-frasco.png")
    if os.path.exists(frasco):
        arte = Image.open(frasco).convert("RGBA")
        altura = round(202 * MM)
        arte = arte.resize((round(arte.width * altura / arte.height), altura),
                           Image.LANCZOS)
        im.paste(arte, (round(20 * MM), round(50 * MM)), arte)

    etiqueta = fonte("Nunito-Bold.ttf", 4)
    nota = fonte("Nunito-Medium.ttf", 3.2)
    cw, ch = CARTA
    x = 196

    def carta_vazia(cx, cy, tracejado=False):
        caixa = [round(cx * MM), round(cy * MM),
                 round((cx + cw) * MM), round((cy + ch) * MM)]
        if tracejado:
            passo = round(2.6 * MM)
            for xx in range(caixa[0], caixa[2], passo * 2):
                draw.line([xx, caixa[1], xx + passo, caixa[1]], fill=BOX, width=3)
                draw.line([xx, caixa[3], xx + passo, caixa[3]], fill=BOX, width=3)
            for yy in range(caixa[1], caixa[3], passo * 2):
                draw.line([caixa[0], yy, caixa[0], yy + passo], fill=BOX, width=3)
                draw.line([caixa[2], yy, caixa[2], yy + passo], fill=BOX, width=3)
        else:
            draw.rounded_rectangle(caixa, radius=round(3 * MM), outline=BOX, width=3)

    # **A jarra ocupa quase toda a altura e a coluna da direita encolhe para a
    # largura de três cartas** (D-354). A primeira versão deixava um terço da
    # folha em branco, e um tabuleiro com vazios parece por acabar.
    draw.text((round(x * MM), round(50 * MM)), "O monte", font=etiqueta, fill=INK)
    draw.text((round(x * MM), round(56 * MM)),
              "As doze cartas do dia, viradas para baixo.", font=nota, fill=FAINT)
    carta_vazia(x, 62)

    xr = x + cw + 12
    draw.text((round(xr * MM), round(50 * MM)), "A reserva", font=etiqueta, fill=INK)
    draw.text((round(xr * MM), round(56 * MM)),
              "As fichas que ainda não entraram.", font=nota, fill=FAINT)
    draw.rounded_rectangle(
        [round(xr * MM), round(62 * MM), round((x + 3 * cw + 12) * MM),
         round((62 + ch) * MM)], radius=round(3 * MM), outline=BOX, width=3)

    y2 = 62 + ch + 16
    draw.text((round(x * MM), round(y2 * MM)), "Por resolver", font=etiqueta, fill=INK)
    draw.text((round(x * MM), round((y2 + 6) * MM)),
              "As que o depósito não chegou para pagar. Se forem mais de três, "
              "empilham-se.", font=nota, fill=FAINT)
    for i in range(3):
        carta_vazia(x + i * (cw + 6), y2 + 12, tracejado=True)

    logo = Image.open(os.path.join(ROOT, "public", "assets", "branding",
                                   "colorhugs-logo.webp")).convert("RGBA")
    larg = round(46 * MM)
    logo = logo.resize((larg, round(logo.height * larg / logo.width)), Image.LANCZOS)
    im.paste(logo, (round((x + 3 * cw + 12) * MM) - logo.width,
                    round(252 * MM)), logo)

    rodape(im, draw)
    return im


def capa():
    """A face da caixa.

    **Um produto que se vende sozinho precisa de uma cara**, e a cara diz três
    coisas antes de qualquer texto: o que é o jogo, para quantas pessoas, e que é
    cooperativo. **Sem vencedor é a coisa mais invulgar deste jogo e tem de estar
    à frente**, não escondida nas regras.
    """
    im = Image.new("RGB", A4, "white")
    draw = ImageDraw.Draw(im)

    draw.rectangle([0, 0, A4[0], round(6 * MM)], fill=FAMILY_COLOUR)

    titulo = ImageFont.truetype(os.path.join(FONTS, "Baloo2-Bold.ttf"), round(18 * MM))
    w = draw.textlength("O Depósito", font=titulo)
    draw.text(((A4[0] - w) / 2, round(28 * MM)), "O Depósito", font=titulo, fill=INK)

    sub = fonte("Nunito-Medium.ttf", 4.2)
    for i, linha in enumerate((
            "Jogo cooperativo. Ganha-se em conjunto ou não se ganha.",
            "Duas ou três pessoas · a partir dos seis anos · dez minutos")):
        w = draw.textlength(linha, font=sub)
        draw.text(((A4[0] - w) / 2, round((52 + i * 7) * MM)), linha,
                  font=sub, fill=(110, 100, 88))

    frasco = os.path.join(SESSAO, "deposito-frasco.png")
    if os.path.exists(frasco):
        arte = Image.open(frasco).convert("RGBA")
        altura = round(120 * MM)
        arte = arte.resize((round(arte.width * altura / arte.height), altura),
                           Image.LANCZOS)
        im.paste(arte, ((A4[0] - arte.width) // 2, round(74 * MM)), arte)

    # As sete, em fila, pequenas: dizem de que família é o jogo.
    ordem = ["Calmo", "Feliz", "Zangado", "Triste", "Assustado",
             "Envergonhado", "Aborrecido"]
    alt = round(14 * MM)
    larguras = []
    figs = []
    for nome in ordem:
        f = limpa(FIGURAS[nome])
        f = f.resize((round(f.width * alt / f.height), alt), Image.LANCZOS)
        figs.append(f)
        larguras.append(f.width)
    total = sum(larguras) + round(4 * MM) * (len(figs) - 1)
    x = (A4[0] - total) // 2
    for f in figs:
        im.paste(f, (x, round(202 * MM)), f)
        x += f.width + round(4 * MM)

    selo = Image.open(os.path.join(
        ROOT, "public", "assets", "branding", "colorhugs-professional.webp")
    ).convert("RGBA")
    larg = round(38 * MM)
    selo = selo.resize((larg, round(selo.height * larg / selo.width)), Image.LANCZOS)
    im.paste(selo, ((A4[0] - selo.width) // 2, round(226 * MM)), selo)

    tiny = fonte("Nunito-Medium.ttf", 2.9)
    draw.line([round(24 * MM), round(268 * MM), A4[0] - round(24 * MM),
               round(268 * MM)], fill=(226, 218, 206), width=2)
    draw.text((round(24 * MM), round(273 * MM)),
              "Material licenciado · uso profissional", font=tiny, fill=FAINT)
    w = draw.textlength("colorhugs.pt", font=tiny)
    draw.text((A4[0] - round(24 * MM) - w, round(273 * MM)), "colorhugs.pt",
              font=tiny, fill=FAINT)
    return im


def regras_folha(regras):
    """As regras, em folha própria."""
    im = Image.new("RGB", A4, "white")
    draw = ImageDraw.Draw(im)
    cabeca(draw, "O Depósito — como se joga",
           "Duas ou três pessoas, todas do mesmo lado.")

    y = 46
    corpo = fonte("Nunito-Medium.ttf", 3.6)
    negro = fonte("Nunito-Bold.ttf", 3.6)
    for regra in regras:
        corte = regra.find(".")
        cabecalho, resto = regra[:corte + 1], regra[corte + 1:].strip()
        for linha in quebra(draw, cabecalho, negro, round(174 * MM)):
            draw.text((round(18 * MM), round(y * MM)), linha, font=negro, fill=INK)
            y += 5.8
        for linha in quebra(draw, resto, corpo, round(174 * MM)):
            draw.text((round(18 * MM), round(y * MM)), linha, font=corpo,
                      fill=(96, 88, 78))
            y += 5.8
        y += 4

    y += 6
    draw.text((round(18 * MM), round(y * MM)), "O que está na caixa",
              font=negro, fill=INK)
    y += 8
    for item in ("O tabuleiro, com o depósito e os três lugares.",
                 "Vinte e quatro cartas de dia: doze boas e doze difíceis.",
                 "Vinte fichas.",
                 "Esta folha."):
        draw.text((round(18 * MM), round(y * MM)), "·  " + item, font=corpo,
                  fill=(96, 88, 78))
        y += 5.8

    y += 8
    draw.text((round(18 * MM), round(y * MM)), "Quase nunca se resolve tudo",
              font=negro, fill=INK)
    y += 8
    for linha in quebra(draw,
                        "Cerca de uma partida em dez acaba sem nada por resolver. "
                        "É de propósito: um jogo em que dava para resolver tudo "
                        "ensinaria que o depósito chega sempre, e não chega.",
                        corpo, round(174 * MM)):
        draw.text((round(18 * MM), round(y * MM)), linha, font=corpo,
                  fill=(96, 88, 78))
        y += 5.8

    rodape(im, draw)
    return im


def coracao(draw, cx, cy, largura, cor=CUT, espessura=4):
    """Um coração a traço, num contorno fechado.

    **A primeira versão foi montada com dois círculos e um triângulo**, e via-se
    a costura: as linhas interiores atravessavam a forma e a ficha lia-se como
    três peças mal encaixadas. É uma curva só, calculada, e fecha sobre si mesma.
    """
    import math

    pontos = []
    passos = 120
    for i in range(passos):
        t = 2 * math.pi * i / passos
        x = 16 * math.sin(t) ** 3
        y = (13 * math.cos(t) - 5 * math.cos(2 * t)
             - 2 * math.cos(3 * t) - math.cos(4 * t))
        pontos.append((x, y))
    escala = largura / 32.0
    caminho = [(round((cx + x * escala) * MM), round((cy - y * escala) * MM))
               for x, y in pontos]
    draw.polygon(caminho, fill="white", outline=cor, width=espessura)


def ficha(largura_px):
    """Uma ficha. **Todas iguais, e o coração é multicolor** (D-356).

    **Uma ficha não é uma emoção — é um bocado de depósito.** Pintá-la de
    vermelho diz que o que ali está guardado é zanga, e o depósito não se enche
    com zanga: enche-se nos dias calmos e felizes. **Um coração de uma cor só
    nomeia um sentimento que não está lá.** Multicolor diz o que é: uma mistura,
    sem pertencer a ninguém.

    Usa a arte quando ela existe; enquanto não existir, desenha o coração
    calculado, a branco.
    """
    arte = os.path.join(SESSAO, "ficha-coracao.png")
    if os.path.exists(arte):
        base = Image.open(arte).convert("RGBA")
    else:
        lado = 400
        base = Image.new("RGBA", (lado, lado), (0, 0, 0, 0))
        d = ImageDraw.Draw(base)
        import math
        pontos = []
        for i in range(160):
            t = 2 * math.pi * i / 160
            x = 16 * math.sin(t) ** 3
            y = (13 * math.cos(t) - 5 * math.cos(2 * t)
                 - 2 * math.cos(3 * t) - math.cos(4 * t))
            pontos.append((lado / 2 + x * lado / 38, lado / 2 - y * lado / 38))
        d.polygon(pontos, fill=(255, 255, 255, 255), outline=(0, 0, 0, 255), width=9)
    e = largura_px / base.width
    return base.resize((largura_px, round(base.height * e)), Image.LANCZOS)


def fichas():
    """A folha das fichas: vinte e uma, todas iguais."""
    im = Image.new("RGB", A4, "white")
    draw = ImageDraw.Draw(im)
    cabeca(draw, "O Depósito — fichas",
           "Recortar as vinte e uma. São todas iguais.")

    largura, gap, x0, y0 = 32, 5, 24, 54
    uma = ficha(round(largura * MM))
    for i in range(21):
        c, l = i % 5, i // 5
        im.paste(uma, (round((x0 + c * (largura + gap)) * MM),
                       round((y0 + l * (largura + gap)) * MM)), uma)

    nota = fonte("Nunito-Medium.ttf", 3.2)
    draw.text((round(24 * MM), round((y0 + 5 * (largura + gap) + 6) * MM)),
              "Uma ficha não é um sentimento — é um bocado de depósito. Por isso "
              "são todas iguais e nenhuma é de uma cor só.", font=nota, fill=FAINT)

    rodape(im, draw)
    return im


def carta_frente(familia, frase, custo):
    cw, ch = CARTA
    card = Image.new("RGB", (round(cw * MM), round(ch * MM)), "white")
    draw = ImageDraw.Draw(card)
    pad = round(3 * MM)
    draw.rounded_rectangle([pad, pad, card.width - pad, card.height - pad],
                           radius=round(4 * MM), fill=(255, 253, 249),
                           outline=INK, width=4)

    fig = limpa(FIGURAS[familia])
    alvo = round(30 * MM)
    e = min(alvo / fig.width, alvo / fig.height)
    f2 = fig.resize((round(fig.width * e), round(fig.height * e)), Image.LANCZOS)
    card.paste(f2, (card.width // 2 - f2.width // 2, round(9 * MM)), f2)

    corpo = fonte("Nunito-Medium.ttf", 3.4)
    linhas = quebra(draw, frase, corpo, round((cw - 12) * MM))
    y = round(44 * MM)
    for linha in linhas:
        w = draw.textlength(linha, font=corpo)
        draw.text((card.width / 2 - w / 2, y), linha, font=corpo, fill=INK)
        y += round(4.6 * MM)

    if custo is None:
        f = fonte("Nunito-Bold.ttf", 3.8)
        texto = "dia bom"
        w = draw.textlength(texto, font=f)
        draw.text((card.width / 2 - w / 2, round((ch - 18) * MM)), texto,
                  font=f, fill=FAMILY_COLOUR)
    else:
        f = fonte("Baloo2-Bold.ttf", 9)
        texto = f"−{custo}"
        w = draw.textlength(texto, font=f)
        draw.text((card.width / 2 - w / 2, round((ch - 23) * MM)), texto,
                  font=f, fill=INK)

    # **A marca vai também na frente** (D-354). Uma carta fotografada ou
    # fotocopiada perde o verso e deixa de dizer de onde veio.
    tiny = fonte("Nunito-Medium.ttf", 2.4)
    marca = "© ColorHugs · colorhugs.pt"
    w = draw.textlength(marca, font=tiny)
    draw.text((card.width / 2 - w / 2, round((ch - 8.5) * MM)), marca,
              font=tiny, fill=(150, 140, 126))
    return card


def carta_verso():
    """O verso, **igual nas vinte e quatro**.

    No baralho terapêutico o verso identifica o naipe de propósito. **Aqui é o
    contrário: se o verso disser se a carta é de dia bom ou de dia difícil, o
    jogo acaba**, porque o monte está virado para baixo e não se pode saber o que
    vem a seguir.
    """
    cw, ch = CARTA
    card = Image.new("RGB", (round(cw * MM), round(ch * MM)), "white")
    draw = ImageDraw.Draw(card)
    pad = round(3 * MM)
    draw.rounded_rectangle([pad, pad, card.width - pad, card.height - pad],
                           radius=round(4 * MM), fill=FAMILY_COLOUR,
                           outline=INK, width=4)

    disc = round(38 * MM)
    cx, cy = card.width // 2, round(38 * MM)
    pale = tuple(round(255 - (255 - c) * 0.10) for c in FAMILY_COLOUR)
    draw.ellipse([cx - disc // 2, cy - disc // 2, cx + disc // 2, cy + disc // 2],
                 fill=pale)
    logo = Image.open(os.path.join(ROOT, "public", "assets", "branding",
                                   "colorhugs-logo.webp")).convert("RGBA")
    w = round(29 * MM)
    logo = logo.resize((w, round(logo.height * w / logo.width)), Image.LANCZOS)
    card.paste(logo, (cx - logo.width // 2, cy - logo.height // 2), logo)

    f = fonte("Baloo2-Bold.ttf", 5.5)
    texto = "O Depósito"
    w = draw.textlength(texto, font=f)
    draw.text((card.width / 2 - w / 2, round(66 * MM)), texto, font=f,
              fill=(255, 255, 255))
    return card


def folha_cartas(cartas_im, espelhar=False):
    """Seis cartas por folha A4, duas colunas e três filas."""
    im = Image.new("RGB", A4, "white")
    cw, ch = CARTA
    mx = (210 - 2 * cw) / 3
    my = (297 - 3 * ch) / 4
    for i, c in enumerate(cartas_im):
        col, lin = i % 2, i // 2
        if espelhar:
            col = 1 - col
        im.paste(c, (round((mx + col * (cw + mx)) * MM),
                     round((my + lin * (ch + my)) * MM)))
    return im


def main():
    os.makedirs(OUT, exist_ok=True)
    regras, lista = leitura()
    frentes = [carta_frente(*c) for c in lista]
    verso = carta_verso()
    paginas = [("deposito-capa", capa()),
               ("deposito-tabuleiro", tabuleiro()),
               ("deposito-regras", regras_folha(regras))]
    paginas.append(("deposito-fichas", fichas()))

    # **As cartas num só ficheiro, frente e verso alternados** (D-354): é o que
    # uma impressora frente e verso precisa, e oito ficheiros soltos eram oito
    # oportunidades de imprimir na ordem errada.
    baralho = []
    for i in range(0, len(frentes), 6):
        lote = frentes[i:i + 6]
        baralho.append(folha_cartas(lote))
        baralho.append(folha_cartas([verso] * len(lote), espelhar=True))
    alvo = os.path.join(OUT, "deposito-cartas.pdf")
    baralho[0].save(alvo, save_all=True, append_images=baralho[1:],
                    resolution=DPI, format="PDF")
    print(f"deposito-cartas.pdf · {len(baralho)} folhas")
    for nome, pagina in paginas:
        pagina.save(os.path.join(OUT, f"{nome}.pdf"), resolution=DPI)
        pagina.save(os.path.join(OUT, f"{nome}.png"))
        print(f"{nome}.pdf")


if __name__ == "__main__":
    main()
