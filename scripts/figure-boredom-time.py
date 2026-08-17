#!/usr/bin/env python3
"""
The bored family's schema — what happens to the empty time.

**The fourth different shape in five families.** Anger's is one episode over
time; sadness's is one episode carried two ways; fear's is a series of episodes;
shame's is a loop. Boredom's is none of those: what matters is **what fills a
stretch of empty time**, so the figure is a strip of time with blocks in it.

Two strips. In the first, the emptiness is filled the moment it appears and the
discomfort ends at once — and nothing of hers ever happens. In the second, the
discomfort lasts a little longer, there is a stretch of nothing, and then
something that came from her.

**The honest part is at the end.** The figure must not promise that the invention
always arrives, because it does not and the evidence is thin (D-260). The last
block is drawn with a dashed edge and the clinician's line says so.

No numbers on anything (D-201).

    python3 scripts/figure-boredom-time.py
"""

import pathlib

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyBboxPatch

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/materials/figuras"

INK = "#1B2A5B"
DISCOMFORT = "#C9A227"  # the uncomfortable bit, in the family's own khaki
FILLED = "#8A93A8"      # what somebody else put there
EMPTY = "#B9C2D0"       # the stretch of nothing
HERS = "#3FA96B"        # what came from her
SOFT = "#8B6FE0"

f = FontProperties(fname="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
fb = FontProperties(fname="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")


def block(ax, x, w, y, colour, label, dashed=False, h=0.72):
    ax.add_patch(
        FancyBboxPatch(
            (x, y - h / 2), w, h,
            boxstyle="round,pad=0.02,rounding_size=0.12",
            linewidth=2.4, edgecolor=colour,
            facecolor=colour, alpha=0.16 if dashed else 0.22,
            linestyle=(0, (5, 4)) if dashed else "solid",
            zorder=3,
        )
    )
    ax.text(
        x + w / 2, y, label, fontproperties=f, fontsize=11.5, color=INK,
        ha="center", va="center", linespacing=1.3, zorder=4,
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(11, 4.8), dpi=200)
    ax.set_xlim(-0.4, 10.9)
    ax.set_ylim(-1.9, 2.6)
    ax.axis("off")

    # Strip one: filled at once.
    ax.text(-0.3, 1.95, "quando se enche logo", fontproperties=fb, fontsize=14,
            color=FILLED, ha="left", va="bottom")
    block(ax, 0.0, 0.9, 1.35, DISCOMFORT, "custa\num bocadinho")
    block(ax, 1.0, 7.6, 1.35, FILLED, "uma coisa que alguém pôs lá")

    # Strip two: left alone.
    ax.text(-0.3, 0.35, "quando se deixa estar", fontproperties=fb, fontsize=14,
            color=HERS, ha="left", va="bottom")
    block(ax, 0.0, 1.6, -0.25, DISCOMFORT, "custa mais\ne dura mais")
    block(ax, 1.7, 3.1, -0.25, EMPTY, "nada")
    block(ax, 4.9, 3.7, -0.25, HERS, "uma coisa que veio dela", dashed=True)

    ax.annotate(
        "", xy=(10.6, -1.15), xytext=(0.0, -1.15),
        arrowprops=dict(arrowstyle="-|>", mutation_scale=18, lw=1.8, color=INK),
    )
    ax.text(5.3, -1.45, "tempo", fontproperties=f, fontsize=12, color=INK,
            ha="center", va="top")

    clinical = ax.text(
        5.3, -1.78,
        "a parte que custa é o princípio, não o todo — e o que vem no fim não vem sempre nem por encomenda",
        fontproperties=f, fontsize=11.5, color=SOFT, ha="center", va="top",
    )

    fig.text(
        0.5, 0.008, "Esquema ilustrativo. Não representa medições.",
        fontproperties=f, fontsize=10.5, color="#7A839B", ha="center", va="top",
    )

    plt.tight_layout()
    plt.savefig(OUT / "tedio-tempo.png", bbox_inches="tight", facecolor="white")

    clinical.set_visible(False)
    plt.savefig(OUT / "tedio-tempo-crianca.png", bbox_inches="tight",
                facecolor="white")

    print("wrote tedio-tempo.png and tedio-tempo-crianca.png")


if __name__ == "__main__":
    main()
