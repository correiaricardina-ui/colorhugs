#!/usr/bin/env python3
"""
Prepare the fine-word cards — the premium layer inside each emotion family.

Named `family__word`, so the file says which family it belongs to and nothing
else has to. Twenty-four in total, unevenly spread across the seven families,
because **the count is per language and per family, not a fixed number**
(D-101): angry has three, happy four, bored four.

Same treatment as the family cards: the white studio background removed, the
die-cut rim kept, and **scale normalised by the mass of the largest connected
piece**, so a card with a detached prop is not shrunk to compensate (D-158).

Normalisation happens **within a family, not across the deck**. A fine word is
only ever seen beside its own siblings and its own mother, never beside a card
from another family, so that is the set that has to match.
"""

import os
import re

import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.environ.get("COLORHUGS_FINE_SRC", os.path.join(ROOT, "artwork", "fine"))
DST = os.path.join(ROOT, "public", "assets", "emotions", "fine")

SIDE = 700
RIM_RATIO = 0.016


def cut_white(img, rim_ratio=RIM_RATIO):
    rgb = img.convert("RGB")
    width, height = rgb.size
    pad = 12
    padded = Image.new("RGB", (width + 2 * pad, height + 2 * pad), (255, 255, 255))
    padded.paste(rgb, (pad, pad))
    array = np.array(padded)

    flat = array.min(axis=2) > 243
    labels, _ = ndimage.label(flat)
    border = (
        set(labels[0, :]) | set(labels[-1, :]) | set(labels[:, 0]) | set(labels[:, -1])
    )
    border.discard(0)
    background = np.isin(labels, list(border))

    # The die-cut rim is the same white as the studio background, so it is
    # flood-filled away with it. Rebuild it as a band of fixed thickness
    # measured from the artwork, not from the canvas edge.
    rim = max(6, round(width * rim_ratio))
    band = ndimage.binary_dilation(
        ~background, ndimage.generate_binary_structure(2, 2), iterations=rim
    )
    background = background & ~band

    out = Image.fromarray(array).convert("RGBA")
    out.putalpha(
        Image.fromarray(np.where(background, 0, 255).astype(np.uint8)).filter(
            ImageFilter.GaussianBlur(0.7)
        )
    )
    box = out.getbbox()
    return out.crop(box) if box else out


def body_mass(img):
    """Largest connected piece only — steam puffs and motion marks float free."""
    solid = np.asarray(img)[..., 3] > 128
    labels, count = ndimage.label(solid)
    if count == 0:
        return 1
    return int(ndimage.sum(solid, labels, range(1, count + 1)).max())


def normalise(images, side=SIDE):
    masses = {name: body_mass(img) for name, img in images.items()}
    target = float(np.median(list(masses.values())))

    wanted = {
        name: (
            img.size[0] * (target / masses[name]) ** 0.5,
            img.size[1] * (target / masses[name]) ** 0.5,
        )
        for name, img in images.items()
    }
    fit = min(1.0, (side - 8) / max(max(w, h) for w, h in wanted.values()))

    out = {}
    for name, img in images.items():
        w, h = wanted[name]
        scaled = img.resize(
            (max(1, round(w * fit)), max(1, round(h * fit))), Image.LANCZOS
        )
        canvas = Image.new("RGBA", (side, side), (255, 255, 255, 0))
        canvas.paste(
            scaled, ((side - scaled.width) // 2, (side - scaled.height) // 2), scaled
        )
        out[name] = canvas
    return out


def main():
    os.makedirs(DST, exist_ok=True)
    families = {}

    for name in sorted(os.listdir(SRC)):
        if not name.lower().endswith(".png"):
            continue
        stem = os.path.splitext(name)[0]
        if not re.fullmatch(r"[a-z]+__[a-z-]+", stem):
            raise SystemExit(f"{name}: expected family__word.png")
        family = stem.split("__")[0]
        families.setdefault(family, {})[stem] = cut_white(
            Image.open(os.path.join(SRC, name))
        )

    total = 0
    for family, cards in sorted(families.items()):
        print(f"  {family}")
        for stem, img in normalise(cards).items():
            img.save(os.path.join(DST, f"{stem}.webp"), "WEBP", quality=92, method=6)
            array = np.asarray(img).astype(int)
            lum = array[..., :3].mean(axis=2)
            sat = array[..., :3].max(axis=2) - array[..., :3].min(axis=2)
            body = (sat > 25) & (lum > 30) & (lum < 250) & (array[..., 3] > 128)
            word = stem.split("__")[1]
            print(f"    {word:14} colour {body.mean() * 100:5.1f}%   mean L {lum[body].mean():5.1f}")
            total += 1

    print(f"\n  {total} fine cards in {len(families)} families")


if __name__ == "__main__":
    main()
