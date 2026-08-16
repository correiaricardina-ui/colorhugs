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
from PIL import Image, ImageFilter
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


def to_pdf(img, target):
    """One page, A4, centred, black on white.

    No title and no feeling name — by D-120 the file must not report what the
    child chose. Only the quiet ColorHugs mark belongs here, and it is added to
    the artwork rather than drawn as text.
    """
    page = Image.new("RGB", A4, "white")
    art = img.convert("RGBA")
    box = (A4[0] - 2 * MARGIN, A4[1] - 2 * MARGIN)
    art.thumbnail(box, Image.LANCZOS)
    flat = Image.new("RGB", art.size, "white")
    flat.paste(art, (0, 0), art)
    page.paste(flat, ((A4[0] - art.width) // 2, (A4[1] - art.height) // 2))
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
