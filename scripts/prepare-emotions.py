#!/usr/bin/env python3
"""
Prepare the How Do I Feel? artwork.

Two families, processed differently on purpose (D-083):

  * **Emotion cards** keep the white die-cut rim. They are cards.
  * **The body map figure** has no rim. It is interface, not a collectable.

The figure is also split into five zone silhouettes so the browser can colour
it without a canvas flood fill: each zone is exported as its own transparent
shape, tinted with CSS and stacked beneath the outline. One outline plus five
shapes covers every colour state (D-070's economy, a simpler mechanism).

Source directory: COLORHUGS_EMOTION_SRC, defaulting to /home/claude/src-emotions.
"""

import json
import os

import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

SRC = os.environ.get("COLORHUGS_EMOTION_SRC", "/home/claude/src-emotions")
DST = os.environ.get(
    "COLORHUGS_ASSET_DIR", "/home/claude/ch/colorhugs/public/assets"
)

CARDS = ["happy", "calm", "sad", "scared", "angry", "ashamed", "bored"]
MAX_CARD = 700
MAX_FIGURE = 900

# Five zones, in the order a child reads the body. The neck sliver is grouped
# with the head so nothing is left permanently white (D-075).
ZONES = ["head", "chest", "stomach", "arms", "legs"]


def cut_white(img: Image.Image, rim_ratio: float | None) -> Image.Image:
    """Remove the white studio background.

    `rim_ratio` keeps a white band of that fraction of the width around the
    artwork — the die-cut rim. `None` removes the background entirely.
    """
    rgb = img.convert("RGB")
    w, h = rgb.size
    pad = 12
    padded = Image.new("RGB", (w + 2 * pad, h + 2 * pad), (255, 255, 255))
    padded.paste(rgb, (pad, pad))
    a = np.array(padded)

    flat = a.min(axis=2) > 243
    lab, _ = ndimage.label(flat)
    border = set(lab[0, :]) | set(lab[-1, :]) | set(lab[:, 0]) | set(lab[:, -1])
    border.discard(0)
    bg = np.isin(lab, list(border))

    if rim_ratio:
        rim = max(6, round(w * rim_ratio))
        core = ~bg
        band = ndimage.binary_dilation(
            core, ndimage.generate_binary_structure(2, 2), iterations=rim
        )
        bg = bg & ~band

    alpha = np.where(bg, 0, 255).astype(np.uint8)
    out = Image.fromarray(a).convert("RGBA")
    out.putalpha(Image.fromarray(alpha).filter(ImageFilter.GaussianBlur(0.7)))
    box = out.getbbox()
    return out.crop(box) if box else out


def downscale(img: Image.Image, longest: int) -> Image.Image:
    w, h = img.size
    if max(w, h) <= longest:
        return img
    s = longest / max(w, h)
    return img.resize((round(w * s), round(h * s)), Image.LANCZOS)


def assign_zones(regions):
    """Map sealed white regions to the five zones by position and size.

    Regions arrive as (area, label_id, centroid_y, centroid_x) with centroids
    normalised 0–1. The figure is symmetrical and upright, so position is
    enough — but the assignment is asserted afterwards rather than trusted.
    """
    regions = sorted(regions, key=lambda r: -r[0])
    zones = {z: [] for z in ZONES}

    for _area, rid, cy, cx in regions:
        offset = abs(cx - 0.5)
        if cy < 0.34:
            # Head, and the neck sliver directly beneath it (D-075: nothing is
            # left permanently white).
            zones["head"].append(rid)
        elif offset > 0.25:
            # Only the arms sit that far out. The legs are off-centre too, but
            # by roughly 0.18 — which is why this threshold is not 0.12.
            zones["arms"].append(rid)
        elif cy < 0.55:
            zones["chest"].append(rid)
        elif cy < 0.70:
            zones["stomach"].append(rid)
        else:
            zones["legs"].append(rid)

    return zones


def prepare_figure(path: str, out_dir: str) -> dict:
    os.makedirs(out_dir, exist_ok=True)
    img = Image.open(path)
    cut = downscale(cut_white(img, rim_ratio=None), MAX_FIGURE)

    grey = np.array(cut.convert("L"))
    alpha = np.array(cut.split()[-1])
    # White inside the figure: light, and not transparent background.
    inside = (grey > 128) & (alpha > 128)

    # The outline is exported as **line only**, everything else transparent.
    #
    # Cutting the background is not enough: the white inside the figure is
    # sealed, so it is not connected to the border and survives the cut as
    # opaque white — which would sit on top of the coloured zones and hide
    # every one of them. Alpha therefore comes from darkness, keeping the
    # anti-aliased edge rather than hard-thresholding it into jaggies.
    line = Image.merge(
        "RGBA",
        (
            Image.new("L", cut.size, 0),
            Image.new("L", cut.size, 0),
            Image.new("L", cut.size, 0),
            Image.fromarray(np.where(alpha > 8, 255 - grey, 0).astype(np.uint8)),
        ),
    )
    line.save(os.path.join(out_dir, "outline.webp"), "WEBP", quality=95, method=6)
    lab, n = ndimage.label(inside)
    h, w = inside.shape
    total = inside.size

    regions = []
    for i in range(1, n + 1):
        m = lab == i
        s = int(m.sum())
        if s < total * 0.0005:
            continue
        ys, xs = np.where(m)
        regions.append((s, i, ys.mean() / h, xs.mean() / w))

    zones = assign_zones(regions)

    missing = [z for z, ids in zones.items() if not ids]
    if missing:
        raise SystemExit(
            f"Sealing test failed: no region found for {missing}. "
            "Regenerate the figure — every internal line must touch the "
            "outer outline at both ends."
        )

    # Arms and legs are pairs. One region where there should be two means the
    # left and right have merged, which is the leak this test exists to catch.
    for paired in ("arms", "legs"):
        if len(zones[paired]) != 2:
            raise SystemExit(
                f"Sealing test failed: {paired} resolved to "
                f"{len(zones[paired])} region(s), expected 2 (left and right)."
            )

    manifest = {"outline": "/assets/body/outline.webp", "size": list(cut.size), "zones": {}}

    for zone, ids in zones.items():
        mask = np.isin(lab, ids)
        # Grow each zone under its own outline so no white hairline shows
        # between the fill and the black line.
        mask = ndimage.binary_dilation(
            mask, ndimage.generate_binary_structure(2, 2), iterations=3
        )
        shape = Image.new("RGBA", cut.size, (255, 255, 255, 0))
        shape.putalpha(
            Image.fromarray(np.where(mask, 255, 0).astype(np.uint8)).filter(
                ImageFilter.GaussianBlur(0.6)
            )
        )
        # White pixels, shaped by alpha: the browser tints these with CSS.
        white = Image.new("RGBA", cut.size, (255, 255, 255, 255))
        white.putalpha(shape.split()[-1])
        rel = f"/assets/body/zone-{zone}.webp"
        white.save(os.path.join(out_dir, f"zone-{zone}.webp"), "WEBP", quality=92, method=6)
        manifest["zones"][zone] = {"file": rel, "regions": len(ids)}

    with open(os.path.join(out_dir, "manifest.json"), "w") as f:
        json.dump(manifest, f, indent=2)

    return manifest


def normalise_cards(images: dict[str, Image.Image], side: int) -> dict[str, Image.Image]:
    """Put every card on the same square canvas at the same character scale.

    Trimming each card to its own bounding box — the pipeline used for section
    stickers, where each is a different subject — is wrong here. These seven
    are the *same character*, and a child compares them side by side: if happy
    renders smaller than bored, the child is reading a size difference that
    means nothing.

    The originals cannot simply be kept either. They were generated at two
    canvas sizes and framed differently, from 0.64 to 0.85 of the frame height.

    Scale is normalised by **ink area** — the character's mass — rather than by
    height or width, because raised arms make happy wide and short while bored
    slumps narrow and tall. Area is the one measure that means the same thing
    across all seven poses.
    """
    areas = {
        name: int((np.asarray(img)[..., 3] > 128).sum()) for name, img in images.items()
    }
    target = float(np.median(list(areas.values())))

    # Area-normalised size each card wants, before anything is made to fit.
    wanted = {
        name: (
            img.size[0] * (target / areas[name]) ** 0.5,
            img.size[1] * (target / areas[name]) ** 0.5,
        )
        for name, img in images.items()
    }

    # One shared factor brings the largest inside the canvas. Shrinking only
    # the ones that overflow would undo the normalisation it just did — which
    # is the bug this comment exists to stop someone reintroducing.
    largest = max(max(w, h) for w, h in wanted.values())
    fit = min(1.0, (side - 8) / largest)

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
    cards_dir = os.path.join(DST, "emotions")
    os.makedirs(cards_dir, exist_ok=True)

    cut = {}
    for name in CARDS:
        src = os.path.join(SRC, f"{name}.png")
        if not os.path.exists(src):
            print(f"  {name:9} MISSING SOURCE")
            continue
        cut[name] = cut_white(Image.open(src), rim_ratio=0.016)

    for name, img in normalise_cards(cut, MAX_CARD).items():
        img.save(os.path.join(cards_dir, f"{name}.webp"), "WEBP", quality=92, method=6)
        ink = int((np.asarray(img)[..., 3] > 128).sum())
        print(f"  {name:9} {img.size[0]}x{img.size[1]}  ink {ink / (MAX_CARD ** 2) * 100:5.1f}%")

    figure = os.path.join(SRC, "body-figure.png")
    if os.path.exists(figure):
        manifest = prepare_figure(figure, os.path.join(DST, "body"))
        print("\n  body figure:", manifest["size"])
        for zone, meta in manifest["zones"].items():
            print(f"    {zone:8} {meta['regions']} sealed region(s)")


if __name__ == "__main__":
    main()
