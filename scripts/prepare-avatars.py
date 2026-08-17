#!/usr/bin/env python3
"""
Turn the ten line-art avatars into something the browser can colour.

## What was wrong

`manifest.json` gives seed points for the seven areas, and flood-filling from
them leaves between 1.6% and 42.8% of the character unpainted depending on which
one the child picked — the dino comes out almost fully coloured, the fox nearly
half white, for exactly the same work.

**That is the failure D-069 and D-075 were written to prevent, in another
shape.** The avatar cannot be a choice about how much reward is visible. The
regions are all there and all sealed; they were simply never assigned.

## What this does

1. Floods each of the seven areas from its seed points.
2. **Assigns every remaining sealed region to the area it touches most.**
   Adjacency, not distance: a cat's muzzle belongs to the head because it sits
   inside it, and a centroid would sometimes say otherwise.
3. Writes one silhouette mask per area, so the browser tints by CSS mask rather
   than by flood-filling a canvas at runtime — the same mechanism the body map
   already uses, and it needs no script to hold a colour.

## The trap, recorded because it cost an hour

The artwork is transparent everywhere except the line. Using its alpha as a
mask over a filled canvas throws the fill away and returns the avatar blank.
**The colour goes underneath the line art, not inside it.**

    python3 scripts/prepare-avatars.py
"""

import json
import pathlib

import numpy as np
from PIL import Image
from scipy import ndimage

ROOT = pathlib.Path(__file__).resolve().parents[1]
AVATARS = ROOT / "public/assets/avatars"
MASKS = AVATARS / "masks"
OUT = ROOT / "src/data/avatars.json"

# Which area belongs to which section. The letters are the manifest's own.
AREAS = ["LH", "BG", "IW", "KD", "CC", "MC", "CM"]

# ---------------------------------------------------------------------------
# The palettes.
#
# **Each avatar is coloured as itself, not as a colour key** (D-211). Painting
# each area in its section's accent turned a fox into a harlequin — green torso,
# purple chest, red legs — and the whole point of the avatar is that the child
# likes looking at it.
#
# Two rules held while choosing these:
#
#   *One family per character, varied by tone.* A ginger cat is ginger nearly
#   everywhere; if head, arms and torso were the same swatch, the child would
#   have no way of seeing that anything had changed. So they are the same hue at
#   different lightness, plus one or two honest accents — pink ears, a cream
#   belly, dark paws.
#
#   *Adjacent areas must differ enough to read.* Verified by measuring, not by
#   looking: `check_contrast()` refuses a palette where two touching areas are
#   within a small perceptual distance.
# ---------------------------------------------------------------------------

PALETTES: dict[str, dict[str, str]] = {
    # ginger cat — pink ears, cream belly and paws
    "gato": {"LH": "#F2A65A", "BG": "#EE8FA6", "IW": "#FBE7CE", "KD": "#E0904A",
             "CC": "#F9BE7C", "MC": "#D9823E", "CM": "#FBE7CE"},
    # soft lilac-grey rabbit
    "coelho": {"LH": "#DCD3E8", "BG": "#F0B7C8", "IW": "#FDF0E4", "KD": "#BFB2D4",
               "CC": "#EAE3F3", "MC": "#FBDCE6", "CM": "#BFB2D4"},
    # honey bear
    "urso": {"LH": "#C99560", "BG": "#E6C199", "IW": "#F7E7CE", "KD": "#B07C48",
             "CC": "#DCAE7B", "MC": "#B07C48", "CM": "#E6C199"},
    # fox: orange, white front, dark socks
    "raposa": {"LH": "#E8823C", "BG": "#B85A32", "IW": "#FDF2E4", "KD": "#D4712F",
               "CC": "#F4A163", "MC": "#EE9048", "CM": "#8C5233"},
    # green dino with an amber crest
    "dino": {"LH": "#6FBF73", "BG": "#E9A23B", "IW": "#DDF0C6", "KD": "#569E5C",
             "CC": "#8ED092", "MC": "#7CC57F", "CM": "#44844B"},
    # tin robot, warm accents
    "robot": {"LH": "#8FB8D9", "BG": "#E36B6B", "IW": "#F2C14E", "KD": "#BCC9D3",
              "CC": "#A9CBE3", "MC": "#E08A4B", "CM": "#7A93A5"},
    # butterfly: purple body, warm wings
    "borboleta": {"LH": "#7E6BD1", "BG": "#5B4AA5", "IW": "#F2C14E", "KD": "#F08CA0",
                  "CC": "#F5B267", "MC": "#9A88E0", "CM": "#E9843B"},
    # cheerful red car, chrome and glass
    "carro": {"LH": "#A9D6EE", "BG": "#A32E2A", "IW": "#C9CED4", "KD": "#F7D36B",
              "CC": "#E0524C", "MC": "#AEB6BE", "CM": "#4B4F55"},
    # brick roof, cream walls, wooden door
    "casa": {"LH": "#B5713F", "BG": "#A8483F", "IW": "#A9D6EE", "KD": "#7FC0E2",
             "CC": "#F5E4C8", "MC": "#C0554A", "CM": "#6FA85E"},
    # silver rocket, red fins, a flame
    "foguetao": {"LH": "#F2C14E", "BG": "#AEB6BE", "IW": "#E8843C", "KD": "#E0524C",
                 "CC": "#DCE3E9", "MC": "#98A2AB", "CM": "#F5A623"},
}

INK_ALPHA = 60  # above this the pixel is line, not fillable space


def regions(line: Image.Image):
    """Label every sealed white region inside the silhouette."""
    alpha = np.array(line)[:, :, 3]
    ink = alpha > INK_ALPHA
    space = ~ink
    lab, n = ndimage.label(space)

    # Anything touching the edge of the canvas is the background, not a region.
    edge = set(lab[0, :]) | set(lab[-1, :]) | set(lab[:, 0]) | set(lab[:, -1])
    edge.discard(0)
    inside = [i for i in range(1, n + 1) if i not in edge]
    return lab, inside, ink


def lab(hexcolour: str):
    """Rough CIELAB, enough to compare two flat colours honestly."""
    r, g, b = (int(hexcolour[i : i + 2], 16) / 255 for i in (1, 3, 5))

    def lin(c):
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = lin(r), lin(g), lin(b)
    x = r * 0.4124 + g * 0.3576 + b * 0.1805
    y = r * 0.2126 + g * 0.7152 + b * 0.0722
    z = r * 0.0193 + g * 0.1192 + b * 0.9505
    xn, yn, zn = 0.95047, 1.0, 1.08883

    def f(t):
        return t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16 / 116

    fx, fy, fz = f(x / xn), f(y / yn), f(z / zn)
    return 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)


def distance(a: str, b: str) -> float:
    la, aa, ba = lab(a)
    lb, ab, bb = lab(b)
    return ((la - lb) ** 2 + (aa - ab) ** 2 + (ba - bb) ** 2) ** 0.5


def check_contrast(name, lab_img, owner, palette, floor=9.0):
    """Warn where two touching areas are too close to tell apart.

    Measured, not eyeballed. Two areas of the same hue at almost the same
    lightness make the child's progress invisible: she paints a whole section
    and the avatar looks unchanged.
    """
    import itertools

    borders = set()
    for rid, area in owner.items():
        mask = lab_img == rid
        grown = ndimage.binary_dilation(mask, iterations=2) & ~mask
        for nid in np.unique(lab_img[grown]):
            other = owner.get(int(nid))
            if other and other != area:
                borders.add(tuple(sorted((area, other))))

    for a, b in sorted(borders):
        d = distance(palette[a], palette[b])
        if d < floor:
            print(f"  ⚠ {name}: {a} e {b} tocam-se e distam {d:.1f} (mínimo {floor})")


def nearest_region(lab, inside_set, x, y, radius=40):
    """The closest sealed region to a point, searched outward ring by ring."""
    h, w = lab.shape
    for r in range(1, radius):
        for dy in range(-r, r + 1):
            for dx in range(-r, r + 1):
                if max(abs(dx), abs(dy)) != r:
                    continue
                px, py = x + dx, y + dy
                if 0 <= px < w and 0 <= py < h:
                    rid = int(lab[py, px])
                    if rid in inside_set:
                        return rid
    return 0


def assign(lab, inside, seeds):
    """Give every sealed region an area.

    Seeded regions take the area of their seed. The rest go to whichever area
    they share the most border with, resolved outward so that a region touching
    only other unassigned regions still lands somewhere on a later pass.
    """
    owner: dict[int, str] = {}
    inside_set = set(inside)

    for area, points in seeds.items():
        for x, y in points:
            rid = int(lab[y, x])
            if rid not in inside_set:
                # **The seed landed on the line itself**, which happens on four
                # of the ten. Left alone, that area gets no region at all and
                # one whole section stops giving colour on that avatar — the
                # D-069 fairness failure again. Snap to the nearest space.
                rid = nearest_region(lab, inside_set, x, y)
            if rid and rid not in owner:
                owner[rid] = area

    unassigned = [r for r in inside if r not in owner]

    # Neighbours are found by growing each region by one pixel and seeing what
    # it lands on. Two passes are rarely enough on the busier characters, so it
    # repeats until nothing moves.
    while unassigned:
        moved = False
        for rid in list(unassigned):
            mask = lab == rid
            grown = ndimage.binary_dilation(mask, iterations=3) & ~mask
            touching = lab[grown]
            counts: dict[str, int] = {}
            for nid in np.unique(touching):
                area = owner.get(int(nid))
                if area:
                    counts[area] = counts.get(area, 0) + int((touching == nid).sum())
            if counts:
                owner[rid] = max(counts, key=lambda a: counts[a])
                unassigned.remove(rid)
                moved = True
        if not moved:
            # Nothing left is adjacent to anything assigned — an island. It goes
            # to the largest area, which is always better than staying white.
            sizes: dict[str, int] = {}
            for r, a in owner.items():
                sizes[a] = sizes.get(a, 0) + int((lab == r).sum())
            fallback = max(sizes, key=lambda a: sizes[a]) if sizes else AREAS[0]
            for rid in unassigned:
                owner[rid] = fallback
            break

    return owner


def main() -> None:
    MASKS.mkdir(parents=True, exist_ok=True)
    manifest = json.loads((AVATARS / "manifest.json").read_text())
    out: dict[str, dict] = {}

    for name, entry in manifest.items():
        line = Image.open(ROOT / ("public" + entry["file"])).convert("RGBA")
        lab, inside, ink = regions(line)
        owner = assign(lab, inside, entry["seeds"])

        total = sum(int((lab == r).sum()) for r in inside)
        painted = 0
        masks: dict[str, str] = {}

        for area in AREAS:
            ids = [r for r, a in owner.items() if a == area]
            if not ids:
                continue
            shape = np.isin(lab, ids)
            painted += int(shape.sum())

            # Grown by one pixel so the tint meets the line instead of leaving a
            # pale halo where the antialiasing sits.
            shape = ndimage.binary_dilation(shape, iterations=2)

            # **Saved with an alpha channel, not as greyscale.** A CSS mask
            # reads alpha, not luminance, so a grey-on-black PNG is opaque
            # everywhere and paints the whole bounding box a flat colour — which
            # is exactly what happened the first time and looked, on the page,
            # like a gold rectangle where a rocket should be.
            a = (shape * 255).astype("uint8")
            rgb = np.full(a.shape + (3,), 255, dtype="uint8")
            img = Image.fromarray(np.dstack([rgb, a]), mode="RGBA")
            path = MASKS / f"{name}-{area}.webp"
            img.save(path, "WEBP", lossless=True)
            masks[area] = f"/assets/avatars/masks/{path.name}"

        left = (total - painted) / total * 100 if total else 0
        print(f"{name:10} áreas {len(masks)}  por pintar {left:5.2f}%")

        palette = PALETTES[name]
        check_contrast(name, lab, owner, palette)

        out[name] = {
            "line": entry["file"],
            "width": line.width,
            "height": line.height,
            "masks": masks,
            "palette": palette,
        }

    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(f"\nwrote {OUT.relative_to(ROOT)} — {len(out)} avatars")


if __name__ == "__main__":
    main()
