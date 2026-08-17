#!/usr/bin/env python3
"""
The sad family's schema — the figure that explains what families get wrong.

**It is not the arousal curve, and it could not be** (D-201, D-214). Anger rises
fast and comes down slowly, and its figure is one line with a shape. Sadness
does not do that, and drawing it as a curve would say something false about it
before a word was read.

What this draws instead is **the same sadness carried two ways**: alone, and
with company. Two lines from the same point.

The thing it has to get right, and the thing it would be easy to get wrong:
**the accompanied line must not end sooner.** The evidence on telling someone is
consistent about the bond and equivocal about the feeling lifting, and a figure
where company makes sadness finish faster would promise exactly what D-214 says
may not be promised. So the two lines end together, and what differs is how far
down the accompanied one goes — *easier to carry*, not *over sooner*.

**No numbers on any axis** (D-201). A graph with a scale looks like data.

Two versions, as the angry schema needed (D-189): the clinician's carries a line
about the child, and the child's page does not — a sentence *about* her talks
over her head on a page she reads herself.

    python3 scripts/figure-sadness-paths.py
"""

import pathlib

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/materials/figuras"

INK = "#1B2A5B"
ALONE = "#4A78B8"  # the sad family's own blue, darkened to carry a line
TOGETHER = "#E08A4B"  # warm, and clearly not a second shade of the first
SOFT = "#8B6FE0"

f = FontProperties(fname="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
fb = FontProperties(fname="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    t = np.linspace(0, 10, 700)

    # **Sadness does not spike.** The first draft rose almost vertically and
    # read as anger in another colour. It arrives over a while, settles, and
    # thins slowly — and it does not reach zero inside the picture, because it
    # usually does not reach zero inside a week either.
    arrive = 1 / (1 + np.exp(-(t - 2.3) * 1.9))
    thin = 0.42 + 0.58 * np.exp(-np.clip(t - 3.9, 0, None) / 5.0)
    # Small waves: a child who feels better for an hour and worse again in the
    # evening should be able to find that in the picture.
    waves = 1 + 0.055 * np.sin((t - 2.3) * 1.9) * np.clip(t - 2.8, 0, 1)

    alone = arrive * thin * waves
    # Same arrival, same ending, lower to carry.
    together = alone * (1 - 0.30 * np.clip((t - 2.4) / 3.5, 0, 1))

    fig, ax = plt.subplots(figsize=(9, 4.8), dpi=200)

    ax.plot(t, alone, color=ALONE, lw=5, solid_capstyle="round", zorder=3)
    ax.plot(t, together, color=TOGETHER, lw=5, solid_capstyle="round", zorder=4)
    ax.fill_between(t, together, alone, color=TOGETHER, alpha=0.10, zorder=2)

    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(INK)
        ax.spines[s].set_linewidth(2)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1.3, 13.6)
    ax.set_ylim(0, 1.62)

    ax.set_xlabel("tempo", fontproperties=f, fontsize=14, color=INK, labelpad=10)
    ax.set_ylabel("tristeza", fontproperties=f, fontsize=14, color=INK, labelpad=12)

    ax.axvline(0.9, 0, 1.20 / 1.60, color=INK, lw=1.4, ls=(0, (4, 4)), alpha=0.5, zorder=1)
    ax.text(
        1.05, 1.24, "acontece\nalguma coisa",
        fontproperties=f, fontsize=13, color=INK, ha="left", va="bottom",
        linespacing=1.35,
    )

    # Labels beyond the end of the lines, not on top of them, and far enough
    # from the axis that "com companhia" is not sitting on the baseline.
    ax.text(
        10.3, alone[-1], "sozinha",
        fontproperties=fb, fontsize=15, color=ALONE, ha="left", va="center",
    )
    ax.text(
        10.3, together[-1] - 0.02, "com companhia",
        fontproperties=fb, fontsize=15, color=TOGETHER, ha="left", va="center",
    )

    # The whole argument of the figure, in one line.
    ax.text(
        4.9, 1.16, "mais fácil de carregar —\nnão mais depressa a passar",
        fontproperties=fb, fontsize=14, color=TOGETHER, ha="left", va="bottom",
        linespacing=1.4,
    )
    ax.annotate(
        "", xy=(5.6, 0.72), xytext=(5.4, 1.12),
        arrowprops=dict(arrowstyle="-", lw=1.6, color=TOGETHER, alpha=0.55,
                        connectionstyle="arc3,rad=0.25"),
    )

    # The clinician's line: the error the figure exists to correct.
    clinical = ax.text(
        4.4, 0.13,
        "aqui é onde se tenta animar, e é\no que faz a linha de baixo desaparecer",
        fontproperties=f, fontsize=12, color=SOFT, ha="left", va="bottom",
        linespacing=1.4,
    )

    ax.text(
        0, -0.30, "Esquema ilustrativo. Não representa medições.",
        transform=ax.transAxes, fontproperties=f, fontsize=11, color="#7A839B",
    )

    plt.tight_layout()
    plt.savefig(OUT / "triste-caminhos.png", bbox_inches="tight", facecolor="white")

    # The child's version: the same picture without the sentence addressed to
    # whoever is applying it (D-189).
    clinical.set_visible(False)
    plt.savefig(OUT / "triste-caminhos-crianca.png", bbox_inches="tight", facecolor="white")

    print("wrote triste-caminhos.png and triste-caminhos-crianca.png")


if __name__ == "__main__":
    main()
