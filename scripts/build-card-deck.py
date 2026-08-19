#!/usr/bin/env python3
"""
The physical deck — cards to print, cut and handle in session.

**No new artwork.** Seven family cards and twenty-four fine cards are already
drawn; this only lays them out. Thirty-one cards at 90x120mm — larger than a
playing card, because small hands hold them — four to a sheet, with cut marks
and a uniform back.

    python3 scripts/build-card-deck.py            # PT-PT
    python3 scripts/build-card-deck.py en

**The back is the same on every card.** If the backs differed by family, a child
could tell a card face-down — which quietly ruins any dynamic that depends on
turning one over.

**The deck carries the words**, unlike every other piece of artwork in the
project (D-081): a printed deck is made for one language and reprinted for the
next, so there is nothing to gain by leaving them off and a great deal of
usefulness to lose.
"""

import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMOTIONS = os.path.join(ROOT, "public", "assets", "emotions")
BRANDING = os.path.join(ROOT, "public", "assets", "branding")
OUT = os.path.join(ROOT, "docs", "materials", "baralho")

REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
TEXT = os.path.join(ROOT, "assets", "fonts", "Nunito-Medium.ttf")

# **A marca vai na face de cada carta e não só no verso** (D-330). Uma carta
# fotocopiada ou fotografada perde o verso e deixa de dizer de onde veio.
#
# É composta na carta e não desenhada dentro da ilustração, por isso não
# contraria a regra de não haver texto dentro da arte: os PNG das personagens
# ficam intactos e continuam a servir todas as línguas.
CREDIT = "© ColorHugs · colorhugs.pt"

DPI = 300
MM = DPI / 25.4
A4 = (round(210 * MM), round(297 * MM))

# Bigger than a playing card, because small hands hold them.
#
# 90x120mm gives four to a sheet rather than nine, so the deck runs to eight
# sheets of fronts instead of four — worth it. A card a four-year-old can pick
# up, turn over and put down without dropping the pile is more useful than a
# deck that prints economically.
CARD = (round(90 * MM), round(120 * MM))
COLS, ROWS = 2, 2
MARGIN_X = (A4[0] - COLS * CARD[0]) / 2
MARGIN_Y = (A4[1] - ROWS * CARD[1]) / 2

INK = (27, 42, 91)
MUTED = (150, 156, 175)

FAMILIES = ["happy", "calm", "sad", "scared", "angry", "ashamed", "bored"]

TINTS = {
    "happy": "#FFCF15",
    "calm": "#A6E5C2",
    "sad": "#7DC0F5",
    "scared": "#C9ADE9",
    "angry": "#E8302C",
    "ashamed": "#FC89AE",
    "bored": "#B0A454",
}


def tint(family, amount=0.86):
    raw = TINTS[family]
    base = tuple(int(raw[i : i + 2], 16) for i in (1, 3, 5))
    return tuple(round(c + (255 - c) * amount) for c in base)


def labels(locale):
    with open(os.path.join(ROOT, "src", "i18n", f"{locale}.json"), encoding="utf-8") as f:
        strings = json.load(f)["feelings"]
    return strings["families"], strings["fine"]


def fit(img, box):
    scale = min(box[0] / img.width, box[1] / img.height)
    return img.resize(
        (max(1, round(img.width * scale)), max(1, round(img.height * scale))),
        Image.LANCZOS,
    )


def card_front(path, label, family):
    """One card: the figure on its family's colour, the word beneath it."""
    card = Image.new("RGB", CARD, "white")
    draw = ImageDraw.Draw(card)

    pad = round(4 * MM)
    draw.rounded_rectangle(
        [pad, pad, CARD[0] - pad, CARD[1] - pad],
        radius=round(6 * MM),
        fill=tint(family),
        outline=INK,
        width=4,
    )

    art = fit(
        Image.open(path).convert("RGBA"),
        (CARD[0] - round(18 * MM), round(72 * MM)),
    )
    card.paste(art, ((CARD[0] - art.width) // 2, round(12 * MM)), art)

    # The word is set to fit rather than at a fixed size: "Entusiasmado" is more
    # than twice the width of "Feliz", and a deck where one card's word is
    # visibly smaller looks like a mistake rather than a long word.
    size = round(9 * MM)
    while size > 16:
        font = ImageFont.truetype(BOLD, size)
        if draw.textlength(label, font=font) <= CARD[0] - round(14 * MM):
            break
        size -= 2
    width = draw.textlength(label, font=font)
    draw.text(
        ((CARD[0] - width) / 2, CARD[1] - round(26 * MM)), label, font=font, fill=INK
    )

    credit(draw)
    return card


def credit(draw):
    """A linha da marca, ao pé da carta.

    **Discreta de propósito.** A carta é manuseada por crianças pequenas e o
    logótipo a cores ao pé da figura é ruído — uma linha composta faz o mesmo
    trabalho de proveniência com uma fracção da tinta e da atenção.
    """
    font = ImageFont.truetype(TEXT, round(3.1 * MM))
    width = draw.textlength(CREDIT, font=font)
    draw.text(
        ((CARD[0] - width) / 2, CARD[1] - round(11.5 * MM)),
        CREDIT,
        font=font,
        fill=(120, 128, 158),
    )


def card_back():
    """The same on every card, so none can be told apart face-down."""
    card = Image.new("RGB", CARD, "white")
    draw = ImageDraw.Draw(card)
    pad = round(4 * MM)
    draw.rounded_rectangle(
        [pad, pad, CARD[0] - pad, CARD[1] - pad],
        radius=round(6 * MM),
        fill=(247, 245, 253),
        outline=INK,
        width=4,
    )
    mark = fit(
        Image.open(os.path.join(BRANDING, "colorhugs-logo.webp")).convert("RGBA"),
        (CARD[0] - round(28 * MM), round(46 * MM)),
    )
    card.paste(mark, ((CARD[0] - mark.width) // 2, (CARD[1] - mark.height) // 2), mark)
    return card


def sheet(cards, mirror=False):
    """Nine cards on A4, with cut marks in the margin.

    `mirror` reverses the column order, so a sheet of backs printed on the
    reverse of a sheet of fronts lines up.
    """
    page = Image.new("RGB", A4, "white")
    draw = ImageDraw.Draw(page)

    for index, card in enumerate(cards):
        col, row = index % COLS, index // COLS
        if mirror:
            col = COLS - 1 - col
        x = round(MARGIN_X + col * CARD[0])
        y = round(MARGIN_Y + row * CARD[1])
        page.paste(card, (x, y))

    # Cut marks live in the margin, never on the card.
    reach = round(4 * MM)
    for col in range(COLS + 1):
        x = round(MARGIN_X + col * CARD[0])
        draw.line([(x, MARGIN_Y - reach), (x, MARGIN_Y)], fill=MUTED, width=2)
        bottom = round(MARGIN_Y + ROWS * CARD[1])
        draw.line([(x, bottom), (x, bottom + reach)], fill=MUTED, width=2)
    for row in range(ROWS + 1):
        y = round(MARGIN_Y + row * CARD[1])
        draw.line([(MARGIN_X - reach, y), (MARGIN_X, y)], fill=MUTED, width=2)
        right = round(MARGIN_X + COLS * CARD[0])
        draw.line([(right, y), (right + reach, y)], fill=MUTED, width=2)

    return page


def build(locale="pt-PT"):
    family_labels, fine_labels = labels(locale)
    os.makedirs(OUT, exist_ok=True)

    cards = []
    for family in FAMILIES:
        cards.append(
            card_front(
                os.path.join(EMOTIONS, f"{family}.webp"), family_labels[family], family
            )
        )
    for key, label in fine_labels.items():
        family = key.split("__")[0]
        cards.append(
            card_front(os.path.join(EMOTIONS, "fine", f"{key}.webp"), label, family)
        )

    pages = []
    back = card_back()
    per_sheet = COLS * ROWS
    for start in range(0, len(cards), per_sheet):
        batch = cards[start : start + per_sheet]
        pages.append(sheet(batch))
        pages.append(sheet([back] * len(batch), mirror=True))

    target = os.path.join(OUT, f"baralho-{locale}.pdf")
    pages[0].save(
        target, "PDF", resolution=DPI, save_all=True, append_images=pages[1:]
    )
    print(f"{len(cards)} cartas · {len(pages)} folhas · {target}")
    return target


if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "pt-PT")
