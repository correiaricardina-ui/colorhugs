#!/usr/bin/env python3
"""Constrói o baralho terapêutico da linha de psicólogos (D-332).

    python3 scripts/build-therapy-deck.py

Lê as frases de `docs/materials/baralho-terapeutico.md` — as listas numeradas
sob cada naipe — e produz `docs/materials/baralho/baralho-terapeutico.pdf`, com
frentes e versos espelhados para impressão frente e verso.

**Herda a geometria do baralho das famílias** (D-200): 90×120 mm, quatro por
folha A4. Uma clínica que já tem um dos baralhos arruma o outro da mesma
maneira.

**Os naipes distinguem-se pelo verso; as cartas dentro de um naipe não.** É a
qualificação necessária à regra dos versos iguais: aqui é preciso encontrar um
naipe sem virar o monte, e continua a ser preciso que nenhuma carta se reconheça
individualmente estando voltada.
"""

import os
import re

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MATERIALS = os.path.join(ROOT, "docs", "materials")
FONTS = os.path.join(ROOT, "assets", "fonts")
BRANDING = os.path.join(ROOT, "public", "assets", "branding")
EMOTIONS = os.path.join(ROOT, "artwork", "emotions")

# As sete figuras, para os naipes que as integrem. **Um naipe que precise do
# outro baralho para funcionar contraria a regra de que nenhuma peça pressupõe
# outra** (D-327), e fica inútil para quem só tenha este.
FIGURES = {
    "Zangado": "angry.png", "Triste": "sad.png", "Assustado": "scared.png",
    "Envergonhado": "ashamed.png", "Calmo": "calm.png", "Feliz": "happy.png",
    "Aborrecido": "bored.png",
}
SOURCE = os.path.join(MATERIALS, "baralho-terapeutico.md")
OUT = os.path.join(MATERIALS, "baralho")

DPI = 300
MM = DPI / 25.4
A4 = (round(210 * MM), round(297 * MM))
CARD = (round(90 * MM), round(120 * MM))

INK = (58, 51, 43)
FAINT = (150, 140, 126)
PAPER = (255, 253, 249)

CREDIT = "© ColorHugs · colorhugs.pt · Material licenciado"

# Naipe: (título no markdown, cor da faixa)
SUITS = [
    ("Fizeste, não és", (214, 120, 128)),
    ("Reparação", (122, 158, 196)),
    ("Quase", (196, 166, 104)),
    ("Conversa", (126, 168, 142)),
]


def phrases():
    """As listas numeradas sob cada `## Naipe N — Nome`."""
    text = open(SOURCE, encoding="utf-8").read()
    out = {}
    for block in re.split(r"\n(?=## )", text):
        m = re.match(r"## Naipe \d+ — (.+)", block)
        if not m:
            continue
        head = block.split("### Carta de instrução")[0]
        familias = re.findall(r"^\d+\.\s+(.+)$",
                              head.split("### Famílias no naipe")[1], re.M) \
            if "### Famílias no naipe" in head else []
        items = re.findall(r"^\d+\.\s+(.+)$",
                           head.split("### Famílias no naipe")[0], re.M)
        out[m.group(1).strip()] = (
            [i.strip() for i in items],
            quoted(block, "frente"),
            quoted(block, "verso"),
            [f.strip() for f in familias],
        )
    return out


def quoted(block, side):
    """Os parágrafos em citação sob «Carta de instrução — <lado>».

    A mesma regra de leitura que os livros usam: **o que está em citação vai
    para a página, o resto é comentário para quem escreve.**
    """
    m = re.search(r"### Carta de instrução — " + side + r"\n(.*?)(?=\n###|\n## |\Z)",
                  block, re.S)
    if not m:
        return []
    paras, buf = [], []
    for line in m.group(1).splitlines():
        if line.startswith(">"):
            body = line[1:].strip()
            if body:
                buf.append(body)
            elif buf:
                paras.append(" ".join(buf))
                buf = []
        elif buf:
            paras.append(" ".join(buf))
            buf = []
    if buf:
        paras.append(" ".join(buf))
    # **A ordem importa e da primeira vez estava trocada.** Tirar o itálico
    # primeiro come um dos asteriscos de um par de negrito e deixa os restantes
    # a imprimir na carta. O negrito sai primeiro; o itálico passa a aspas
    # angulares, que é a marcação certa em português e a única que se lê num
    # cartão sem mudar de tipo de letra.
    limpo = []
    for para in paras:
        para = re.sub(r"\*\*(.+?)\*\*", r"\1", para)
        para = re.sub(r"\*(.+?)\*", r"«\1»", para)
        limpo.append(para.replace("*", ""))
    return limpo


def wrap(draw, text, font, width):
    linhas, actual = [], ""
    for palavra in text.split():
        teste = (actual + " " + palavra).strip()
        if draw.textlength(teste, font=font) <= width:
            actual = teste
        else:
            linhas.append(actual)
            actual = palavra
    if actual:
        linhas.append(actual)
    return linhas


def instruction_card(title, paras, colour, tinted=False):
    """A carta de instrução, que usa os dois lados.

    **Uma carta de instrução que obrigue a ir procurar as instruções a outro
    sítio não é uma carta de instrução.** A frente diz o que o naipe faz e como
    se joga; o verso leva a regra dura e o que o naipe não faz.
    """
    card = Image.new("RGB", CARD, "white")
    draw = ImageDraw.Draw(card)
    pad = round(4 * MM)
    fill = tuple(round(255 - (255 - c) * 0.14) for c in colour) if tinted else PAPER
    draw.rounded_rectangle(
        [pad, pad, CARD[0] - pad, CARD[1] - pad],
        radius=round(6 * MM), fill=fill, outline=INK, width=4,
    )

    head = ImageFont.truetype(os.path.join(FONTS, "Baloo2-Bold.ttf"), round(5.6 * MM))
    x = round(10 * MM)
    box = CARD[0] - round(20 * MM)
    y = round(11 * MM)
    draw.text((x, y), title, font=head, fill=INK)
    y += round(11 * MM)

    # O corpo desce até caber. Uma carta de instrução vale pelo que diz, não
    # pelo tamanho da letra — mas abaixo de 2,6 mm deixa de se ler à mesa.
    size = round(3.5 * MM)
    while size >= round(2.6 * MM):
        font = ImageFont.truetype(os.path.join(FONTS, "Nunito-Medium.ttf"), size)
        linhas = []
        for para in paras:
            linhas += wrap(draw, para, font, box) + [""]
        altura = len(linhas) * size * 1.42
        if y + altura < CARD[1] - round(15 * MM):
            break
        size -= round(0.15 * MM)

    for linha in linhas:
        if linha:
            draw.text((x, y), linha, font=font, fill=INK)
        y += size * 1.42

    tiny = ImageFont.truetype(os.path.join(FONTS, "Nunito-Medium.ttf"), round(2.6 * MM))
    w = draw.textlength(CREDIT, font=tiny)
    draw.text(((CARD[0] - w) / 2, CARD[1] - round(11 * MM)), CREDIT, font=tiny, fill=FAINT)
    return card


def card_front(text, colour, instruction=False):
    card = Image.new("RGB", CARD, "white")
    draw = ImageDraw.Draw(card)
    pad = round(4 * MM)
    draw.rounded_rectangle(
        [pad, pad, CARD[0] - pad, CARD[1] - pad],
        radius=round(6 * MM), fill=PAPER, outline=INK, width=4,
    )

    face = "Nunito-Medium.ttf" if not instruction else "Nunito-Bold.ttf"
    # O corpo desce até caber: as frases vão de três palavras a catorze, e um
    # baralho em que uma carta tem letra visivelmente menor parece um erro.
    size = round(8 * MM)
    box = CARD[0] - round(22 * MM)
    while size > round(4 * MM):
        font = ImageFont.truetype(os.path.join(FONTS, face), size)
        linhas = wrap(draw, text, font, box)
        if len(linhas) <= 4:
            break
        size -= round(0.4 * MM)

    alto = len(linhas) * size * 1.34
    y = (CARD[1] - alto) / 2 - round(4 * MM)
    for linha in linhas:
        w = draw.textlength(linha, font=font)
        draw.text(((CARD[0] - w) / 2, y), linha, font=font, fill=INK)
        y += size * 1.34

    draw.rounded_rectangle(
        [round(30 * MM), CARD[1] - round(17 * MM),
         CARD[0] - round(30 * MM), CARD[1] - round(15 * MM)],
        radius=round(1 * MM), fill=colour,
    )

    tiny = ImageFont.truetype(os.path.join(FONTS, "Nunito-Medium.ttf"), round(2.6 * MM))
    w = draw.textlength(CREDIT, font=tiny)
    draw.text(((CARD[0] - w) / 2, CARD[1] - round(11 * MM)), CREDIT, font=tiny, fill=FAINT)
    return card


def transparent(name):
    """A figura sem o fundo branco e sem o rebordo de autocolante.

    O rebordo é branco e está ligado ao fundo, por isso sai com ele. **Aqui isso
    é o que se quer**: sobre o creme da carta, o campo branco rectangular via-se
    como uma caixa por trás da figura, e o rebordo não faz falta nenhuma numa
    carta que não é para recortar.

    O preenchimento entra pelas bermas, por isso o branco dos olhos fica — não
    toca no exterior.
    """
    im = Image.open(os.path.join(EMOTIONS, name)).convert("RGBA")
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
        if r < 232 or g < 232 or b < 232:
            continue
        px[x, y] = (r, g, b, 0)
        fila += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return im.crop(im.getbbox())


def family_card(label, colour):
    """A figura de uma família, na cor do naipe que a integra."""
    card = Image.new("RGB", CARD, "white")
    draw = ImageDraw.Draw(card)
    pad = round(4 * MM)
    draw.rounded_rectangle(
        [pad, pad, CARD[0] - pad, CARD[1] - pad],
        radius=round(6 * MM), fill=PAPER, outline=INK, width=4,
    )

    im = transparent(FIGURES[label])
    h = round(58 * MM)
    im = im.resize((round(im.width * h / im.height), h), Image.LANCZOS)
    card.paste(im, ((CARD[0] - im.width) // 2, round(16 * MM)), im)

    font = ImageFont.truetype(os.path.join(FONTS, "Baloo2-Bold.ttf"), round(7 * MM))
    w = draw.textlength(label, font=font)
    draw.text(((CARD[0] - w) / 2, CARD[1] - round(33 * MM)), label, font=font, fill=INK)

    draw.rounded_rectangle(
        [round(30 * MM), CARD[1] - round(17 * MM),
         CARD[0] - round(30 * MM), CARD[1] - round(15 * MM)],
        radius=round(1 * MM), fill=colour,
    )
    tiny = ImageFont.truetype(os.path.join(FONTS, "Nunito-Medium.ttf"), round(2.6 * MM))
    w = draw.textlength(CREDIT, font=tiny)
    draw.text(((CARD[0] - w) / 2, CARD[1] - round(11 * MM)), CREDIT, font=tiny, fill=FAINT)
    return card


def card_back(name, colour):
    """O verso: painel da cor do naipe, o logótipo e o nome do naipe.

    **O logótipo assenta sobre um campo claro e não sobre a cor cheia.** É o
    logótipo colorido, e a cor por baixo dele apaga-lhe metade — sobre o painel
    saturado ficava turvo. O campo claro é a mesma cor do naipe muito diluída,
    para que continue a pertencer-lhe.
    """
    card = Image.new("RGB", CARD, "white")
    draw = ImageDraw.Draw(card)
    pad = round(4 * MM)
    draw.rounded_rectangle(
        [pad, pad, CARD[0] - pad, CARD[1] - pad],
        radius=round(6 * MM), fill=colour, outline=INK, width=4,
    )

    disc = round(52 * MM)
    cx, cy = CARD[0] // 2, round(50 * MM)
    pale = tuple(round(255 - (255 - c) * 0.10) for c in colour)
    draw.ellipse([cx - disc // 2, cy - disc // 2, cx + disc // 2, cy + disc // 2],
                 fill=pale)

    logo = Image.open(os.path.join(BRANDING, "colorhugs-logo.webp")).convert("RGBA")
    w = round(40 * MM)
    logo = logo.resize((w, round(logo.height * w / logo.width)), Image.LANCZOS)
    card.paste(logo, (cx - logo.width // 2, cy - logo.height // 2), logo)

    font = ImageFont.truetype(os.path.join(FONTS, "Baloo2-Bold.ttf"), round(6.5 * MM))
    linhas = wrap(draw, name, font, CARD[0] - round(24 * MM))
    y = round(88 * MM)
    for linha in linhas:
        w = draw.textlength(linha, font=font)
        draw.text(((CARD[0] - w) / 2, y), linha, font=font, fill=(255, 255, 255))
        y += round(9 * MM)
    return card


def sheet(cards, mirror=False):
    page = Image.new("RGB", A4, "white")
    cols, rows = 2, 2
    mx = (A4[0] - cols * CARD[0]) // (cols + 1)
    my = (A4[1] - rows * CARD[1]) // (rows + 1)
    for i, card in enumerate(cards):
        c, r = i % cols, i // cols
        if mirror:
            c = cols - 1 - c
        page.paste(card, (mx + c * (CARD[0] + mx), my + r * (CARD[1] + my)))
    return page


def main():
    os.makedirs(OUT, exist_ok=True)
    data = phrases()
    fronts, backs = [], []
    for name, colour in SUITS:
        items, frente, verso, familias = data.get(name, ([], [], [], []))
        if not items:
            continue
        if frente:
            fronts.append(instruction_card(name, frente, colour))
            backs.append(instruction_card("Antes de usar", verso, colour, tinted=True)
                         if verso else card_back(name, colour))
        for label in familias:
            fronts.append(family_card(label, colour))
            backs.append(card_back(name, colour))
        for text in items:
            fronts.append(card_front(text, colour))
            backs.append(card_back(name, colour))

    if not fronts:
        raise SystemExit("nenhum naipe escrito ainda em baralho-terapeutico.md")

    pages = []
    for i in range(0, len(fronts), 4):
        pages.append(sheet(fronts[i:i + 4]))
        pages.append(sheet(backs[i:i + 4], mirror=True))

    target = os.path.join(OUT, "baralho-terapeutico.pdf")
    pages[0].save(target, save_all=True, append_images=pages[1:],
                  resolution=DPI, format="PDF")
    print(f"{len(fronts)} cartas · {len(pages)} folhas · {target}")


if __name__ == "__main__":
    main()
