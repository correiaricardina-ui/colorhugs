#!/usr/bin/env python3
"""
Measure the banner artwork and write its real proportions.

**Why this exists.** `SectionBanner` framed every banner at 1568x644 and cropped
whatever did not fit. Three of the eleven banners are not that shape — My Inner
World, Brain Gym and Kids Draw are 1568x784 — so eighteen per cent of each was
cut away, top and bottom. On My Inner World that removed the top of the heart
and pushed the ribbon against the edge.

Cropping approved artwork to fit a frame is redrawing it by another means
(rule 6, D-003). **The frame takes the artwork's shape, not the other way
round.**

Measured rather than typed: the number that was wrong before was a typed one.

    python3 scripts/measure-banners.py
"""

import json
import pathlib
import struct

ROOT = pathlib.Path(__file__).resolve().parents[1]
BANNERS = ROOT / "public/assets/banners"
OUT = ROOT / "src/data/banner-sizes.json"


def webp_size(path: pathlib.Path) -> tuple[int, int]:
    """Read width and height from a WebP header, without Pillow.

    The script has to run wherever the site is built, and a build step that
    needs an image library installed is a build step that stops working on
    someone else's machine.
    """
    data = path.read_bytes()
    if data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        raise ValueError(f"{path.name} is not a WebP file")

    chunk = data[12:16]

    if chunk == b"VP8X":
        w = int.from_bytes(data[24:27], "little") + 1
        h = int.from_bytes(data[27:30], "little") + 1
        return w, h

    if chunk == b"VP8L":
        bits = int.from_bytes(data[21:25], "little")
        w = (bits & 0x3FFF) + 1
        h = ((bits >> 14) & 0x3FFF) + 1
        return w, h

    if chunk == b"VP8 ":
        w, h = struct.unpack("<HH", data[26:30])
        return w & 0x3FFF, h & 0x3FFF

    raise ValueError(f"{path.name}: unknown WebP chunk {chunk!r}")


def main() -> None:
    sizes: dict[str, dict[str, int]] = {}
    for file in sorted(BANNERS.glob("*.webp")):
        w, h = webp_size(file)
        sizes[f"/assets/banners/{file.name}"] = {"w": w, "h": h}
        print(f"{file.name:26} {w}x{h}  {w / h:.3f}")

    OUT.write_text(json.dumps(sizes, indent=2, sort_keys=True) + "\n")
    print(f"\nwrote {OUT.relative_to(ROOT)} — {len(sizes)} banners")


if __name__ == "__main__":
    main()
