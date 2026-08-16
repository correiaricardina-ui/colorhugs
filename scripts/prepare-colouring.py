#!/usr/bin/env python3
"""
Prepare colouring pages, and refuse the ones that do not work on screen.

Every published page gets two routes: **colour it on screen, or download the
PDF.** Neither is a fallback for the other — some children have a printer and
crayons and no patience for a screen, and some have the opposite.

## The six-region rule

Tap-and-fill colouring gives a child exactly as many colours as the drawing has
sealed regions. A hand drawn as a single outline is one region: one colour, and
nothing else to do. So a page in the official ColorHugs library needs **at
least six** fillable areas, with every internal dividing line touching the
outer outline at both ends.

This applies to the **official library only** (D-129). Imagine & Create cannot
guarantee it — no model does — and a child's own drawing in Kids Draw for Kids
almost never has six sealed regions, often none. Those are coloured with the
brush instead, and downloading is offered prominently, because paper is where
they work best.

**On paper the rule does not apply at all.** With crayons, a one-region hand is
a whole hand to colour however you like. The limit belongs to the screen, and
rejecting good art because of it would be a mistake.

A rule nobody checks is not a rule, so this script refuses to export a page
that fails, rather than reporting it and carrying on.
"""

import os
import sys

import numpy as np
from datetime import date
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from scipy import ndimage

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.environ.get("COLORHUGS_PAGE_SRC", os.path.join(ROOT, "artwork", "colouring"))
DST = os.path.join(ROOT, "public", "assets", "colouring")

# The three How Do I Feel? paths, plus the general Explore & Color library for
# pages that answer to no activity — they are simply good pages to colour.
PATHS = ("strategies", "moments", "now", "library")

MIN_REGIONS = 6

# A fillable area must be worth filling. Without a floor the count is trivially
# gamed: the first hand to pass this check did so only because the generator
# had drawn the numerals 1–5 beside the fingers, and five hollow digits counted
# as five areas. The hand itself was still one region and still gave a child
# one colour.
MIN_AREA_SHARE = 0.005

MAX_EDGE = 1400

# A4 at 300 dpi, with a margin wide enough for small hands and cheap printers.
A4 = (2480, 3508)
MARGIN = 190

# Room at the foot of the page for the mark and the small print. Kept out of
# the drawing's box so nothing crowds the art.
FOOTER_HEIGHT = 300

LOGO = os.path.join(ROOT, "public", "assets", "branding", "colorhugs-logo.webp")
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# The only words on the page, and deliberately language-neutral: a domain and a
# copyright line read the same in every locale. A translatable sentence here
# would need seven versions of every PDF, for ever — the D-081 trap in another
# form. And by D-120 nothing may name the feeling the child chose.
FOOTER_TEXT = "colorhugs.pt"

# The band across the head of the page: the seven section accents, in the order
# of the seven areas, taken from globals.css. It frames the sheet without a
# single word — so it costs no translation, and by D-120 it cannot report what
# the child chose. It is also the only colour on the page, which suits a sheet
# that exists to be coloured: the paper starts with a little colour and the
# child adds the rest.
BAND_COLOURS = [
    "#2F6FD0",  # Learning Hub
    "#E0619A",  # Brain Gym
    "#8B6FE0",  # My Inner World
    "#EF7D3D",  # Kids Draw
    "#3FA96B",  # Color & Create
    "#D9911A",  # My ColorHugs
    "#E0566A",  # Community
]
BAND_HEIGHT = 46
BAND_GAP = 70


def sealed_regions(grey, alpha=None):
    """Fillable areas: enclosed white regions that are not the background."""
    white = grey > 128
    if alpha is not None:
        white &= alpha > 128
    labels, count = ndimage.label(white)
    background = labels[2, 2]
    total = white.size
    return [
        i
        for i in range(1, count + 1)
        if i != background and (labels == i).sum() > total * MIN_AREA_SHARE
    ]


def cut_white(img):
    """Transparent background, line kept. No die-cut rim: this is a page."""
    rgb = img.convert("RGB")
    grey = np.asarray(rgb.convert("L"))
    alpha = np.where(grey < 250, 255 - grey, 0).astype(np.uint8)
    out = Image.merge(
        "RGBA",
        (
            Image.new("L", rgb.size, 0),
            Image.new("L", rgb.size, 0),
            Image.new("L", rgb.size, 0),
            Image.fromarray(alpha).filter(ImageFilter.GaussianBlur(0.4)),
        ),
    )
    return out


def fit(img, box):
    """Scale to fill the box, up or down, keeping the proportions.

    `Image.thumbnail` only ever shrinks. The source drawings are around 1250px
    and the printable area is over 2000, so thumbnail left them a stamp in the
    middle of an A4 sheet. A colouring page has to fill the paper — a child
    colours with a crayon, not a needle.
    """
    scale = min(box[0] / img.width, box[1] / img.height)
    return img.resize(
        (max(1, round(img.width * scale)), max(1, round(img.height * scale))),
        Image.LANCZOS,
    )


def to_pdf(img, target):
    """One page, A4, the drawing filling the sheet, with the mark beneath.

    No title and no feeling name — by D-120 the file must not report what the
    child chose. A parent finding this PDF learns nothing about her.
    """
    page = Image.new("RGB", A4, "white")
    draw = ImageDraw.Draw(page)

    # Header band. Keeping the mark at the foot rather than repeating it here
    # leaves the drawing measurably larger, and the sheet exists to be painted.
    width = A4[0] - 2 * MARGIN
    segment = width / len(BAND_COLOURS)
    for index, colour in enumerate(BAND_COLOURS):
        x = MARGIN + index * segment
        draw.rounded_rectangle(
            [x, MARGIN, x + segment - 6, MARGIN + BAND_HEIGHT],
            radius=20,
            fill=colour,
        )

    art_top = MARGIN + BAND_HEIGHT + BAND_GAP
    box = (width, A4[1] - art_top - MARGIN - FOOTER_HEIGHT)

    # Trim the empty margin the generator happened to leave before scaling, so
    # how much of the sheet a drawing fills depends on the drawing and not on
    # how it was framed. The jumping child sat in the top two thirds of its
    # square and printed noticeably smaller than the elephant, which filled its
    # own. Same reasoning as normalising the emotion cards (D-122).
    #
    # PDF only. The WebP stays square, because the canvas sets its size from the
    # image and assumes a square frame.
    trimmed = img.convert("RGBA")
    bbox = trimmed.convert("L").point(lambda v: 255 if v < 200 else 0).getbbox()
    if bbox:
        pad = round(max(trimmed.size) * 0.02)
        trimmed = trimmed.crop(
            (
                max(0, bbox[0] - pad),
                max(0, bbox[1] - pad),
                min(trimmed.width, bbox[2] + pad),
                min(trimmed.height, bbox[3] + pad),
            )
        )

    art = fit(trimmed, box)
    flat = Image.new("RGB", art.size, "white")
    flat.paste(art, (0, 0), art)
    page.paste(flat, ((A4[0] - art.width) // 2, art_top + (box[1] - art.height) // 2))

    footer_top = A4[1] - MARGIN - FOOTER_HEIGHT

    if os.path.exists(LOGO):
        logo = fit(Image.open(LOGO).convert("RGBA"), (900, 170))
        page.paste(logo, ((A4[0] - logo.width) // 2, footer_top), logo)
        text_y = footer_top + logo.height + 40
    else:
        text_y = footer_top + 60

    try:
        font = ImageFont.truetype(FONT, 46)
    except OSError:
        font = ImageFont.load_default()

    line = f"{FOOTER_TEXT}   ·   © {date.today().year} ColorHugs"
    width = draw.textlength(line, font=font)
    draw.text(
        ((A4[0] - width) / 2, text_y), line, fill=(120, 128, 150), font=font
    )

    page.save(target, "PDF", resolution=300)


def main():
    failures = []
    made = 0

    for path in PATHS:
        src_dir = os.path.join(SRC, path)
        dst_dir = os.path.join(DST, path)
        if not os.path.isdir(src_dir):
            continue
        os.makedirs(dst_dir, exist_ok=True)

        for name in sorted(os.listdir(src_dir)):
            if not name.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
                continue
            stem = os.path.splitext(name)[0]
            img = Image.open(os.path.join(src_dir, name))
            grey = np.asarray(img.convert("L"))

            regions = sealed_regions(grey)
            ink = (grey < 128).mean() * 100

            if len(regions) < MIN_REGIONS:
                failures.append(
                    f"{path}/{stem}: {len(regions)} fillable area(s), needs "
                    f"{MIN_REGIONS}. Add internal dividing lines, each touching "
                    f"the outer outline at both ends."
                )
                continue

            cut = cut_white(img)
            cut.thumbnail((MAX_EDGE, MAX_EDGE), Image.LANCZOS)
            cut.save(
                os.path.join(dst_dir, f"{stem}.webp"), "WEBP", quality=92, method=6
            )
            to_pdf(img, os.path.join(dst_dir, f"{stem}.pdf"))
            made += 1
            print(f"  {path}/{stem:22} {len(regions):3} areas   ink {ink:4.1f}%   + pdf")

    if failures:
        print("\n  Not exported:\n")
        for line in failures:
            print(f"    {line}")
        print(
            "\n  A page with too few areas gives a child one colour and nothing\n"
            "  else to do. It is fine on paper and not fine on screen."
        )
        return 1

    print(f"\n  {made} page(s) exported, each with a WebP and a PDF.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
