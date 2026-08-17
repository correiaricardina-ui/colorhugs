#!/usr/bin/env python3
"""
Cover for a practitioner workbook.

**Drawn, not generated.** A cover is typography — title, subtitle, lockup — and
type is what image generators do worst. Garbled Portuguese on a document
carrying a clinician's signature is not a risk worth taking, and a drawn cover
regenerates when a word changes.

The illustration is the family's own emotion card, so the workbook is
recognisable from across a desk and matches what the child sees on screen.

Run with the family id:

    python3 scripts/figure-workbook-cover.py angry
"""

import os
import sys
from datetime import date

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRANDING = os.path.join(ROOT, "public", "assets", "branding")
EMOTIONS = os.path.join(ROOT, "public", "assets", "emotions")
OUT = os.path.join(ROOT, "docs", "materials", "figuras")

REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

A4 = (2480, 3508)
MARGIN = 210

INK = (27, 42, 91)
MUTED = (122, 131, 155)

# Same seven section accents as the colouring pages, so every printed ColorHugs
# sheet is recognisable as one family of objects.
BAND = ["#2F6FD0", "#E0619A", "#8B6FE0", "#EF7D3D", "#3FA96B", "#D9911A", "#E0566A"]

FAMILIES = {
    "angry": {"title": "Zangado", "tint": "#E63B33"},
    "sad": {"title": "Triste", "tint": "#6FB2E8"},
    "scared": {"title": "Assustado", "tint": "#A98BDD"},
    "ashamed": {"title": "Envergonhado", "tint": "#F495B0"},
    "happy": {"title": "Feliz", "tint": "#F5B700"},
    "calm": {"title": "Calmo", "tint": "#8FD9A8"},
    "bored": {"title": "Tédio", "tint": "#A89B5C"},
}

SUBTITLE = "Caderno de aplicação"
CHILD_SUBTITLE = "Caderno de exploração"
STRAPLINE = "Material licenciado · Uso profissional"
DISCLAIMER = (
    "Ferramenta psicoeducativa. Não diagnostica, não avalia\n"
    "e não substitui acompanhamento psicológico."
)

# Families whose workbook is written. Generating a cover for one that is not
# would put a finished-looking object in front of a colleague before the
# content behind it exists.
WRITTEN = {"angry", "sad", "scared", "ashamed"}


def fit(img, box):
    scale = min(box[0] / img.width, box[1] / img.height)
    return img.resize(
        (max(1, round(img.width * scale)), max(1, round(img.height * scale))),
        Image.LANCZOS,
    )


def centred(draw, text, y, font, fill, spacing=18):
    for line in text.split("\n"):
        width = draw.textlength(line, font=font)
        draw.text(((A4[0] - width) / 2, y), line, font=font, fill=fill)
        y += font.size + spacing
    return y


def build(family_id: str, child: bool = False) -> str:
    """The cover.

    `child=True` builds the cover of the child's exploration book. Two things
    change, and both matter:

    * **The plain ColorHugs logo, never the endorsed professional lockup**
      (D-063, D-065). The endorsement is addressed to a colleague; a child
      holding her own book has no use for a credential.
    * **No licensing strapline and no clinical disclaimer.** They are addressed
      over her head, and the child's material does not do that (D-189).
    """
    family = FAMILIES[family_id]
    page = Image.new("RGB", A4, "white")
    draw = ImageDraw.Draw(page)

    # Header band, as on every printable page.
    width = A4[0] - 2 * MARGIN
    segment = width / len(BAND)
    for index, colour in enumerate(BAND):
        x = MARGIN + index * segment
        draw.rounded_rectangle(
            [x, MARGIN, x + segment - 8, MARGIN + 52], radius=24, fill=colour
        )

    # The emotion card, on a soft disc of its own colour so it sits on the page
    # rather than floating. Ten per cent tint: enough to hold it, not enough to
    # compete with the card's own outline.
    card = fit(Image.open(os.path.join(EMOTIONS, f"{family_id}.webp")).convert("RGBA"),
               (880, 880))
    disc_r = 560
    cx, cy = A4[0] // 2, 1120
    tint = tuple(int(family["tint"][i : i + 2], 16) for i in (1, 3, 5))
    soft = tuple(round(c + (255 - c) * 0.90) for c in tint)
    draw.ellipse([cx - disc_r, cy - disc_r, cx + disc_r, cy + disc_r], fill=soft)
    page.paste(card, (cx - card.width // 2, cy - card.height // 2), card)

    # Title block. Positions are fixed rather than flowed, so a longer family
    # name — "Envergonhado" — cannot push the lockup into the text beneath it.
    centred(draw, family["title"], 1830, ImageFont.truetype(BOLD, 150), INK, 10)
    centred(
        draw,
        CHILD_SUBTITLE if child else SUBTITLE,
        2020,
        ImageFont.truetype(REGULAR, 78),
        INK,
        10,
    )
    if not child:
        centred(draw, STRAPLINE, 2140, ImageFont.truetype(REGULAR, 46), MUTED, 10)

    # The endorsed professional lockup — never the plain child-facing one, and
    # never on a child's screen (D-063, D-065).
    mark = "colorhugs-logo.webp" if child else "colorhugs-professional.webp"
    lockup = fit(Image.open(os.path.join(BRANDING, mark)).convert("RGBA"), (700, 560))
    page.paste(lockup, ((A4[0] - lockup.width) // 2, 2400), lockup)

    if not child:
        centred(draw, DISCLAIMER, 3060, ImageFont.truetype(REGULAR, 42), MUTED, 12)
    centred(
        draw,
        f"colorhugs.pt   ·   © {date.today().year}",
        3230,
        ImageFont.truetype(REGULAR, 40),
        MUTED,
    )

    os.makedirs(OUT, exist_ok=True)
    suffix = "-capa-crianca" if child else "-capa"
    target = os.path.join(OUT, f"{family_id}{suffix}.png")
    page.save(target)
    return target


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "angry"
    if which not in WRITTEN and "--force" not in sys.argv:
        raise SystemExit(
            f"{which}: no workbook written yet. Use --force only to preview a layout."
        )
    print(build(which))
    print(build(which, child=True))
