#!/usr/bin/env python3
"""
The ashamed family's schema — the loop that hiding keeps closed.

**The first schema in the project that is not a graph.** Anger's is one episode
over time; sadness's is one episode carried two ways; fear's is a series of
episodes. Shame's mechanism has no time axis worth drawing: it is a circle that
closes on itself, and what keeps it closed is that the prediction is never
tested.

Four boxes, one loop, and one arrow leaving it. The arrow that leaves is the
whole intervention: **someone sees and stays.**

Two rules held: no numbers anywhere (D-201, trivially here), and the child's
version carries no sentence written about her rather than to her (D-189).

    python3 scripts/figure-shame-loop.py
"""

import pathlib

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/materials/figuras"

INK = "#1B2A5B"
LOOP = "#D06AA0"     # the ashamed family's own pink, darkened to carry a line
OUTWARD = "#3FA96B"  # the way out
SOFT = "#8B6FE0"

f = FontProperties(fname="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
fb = FontProperties(fname="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")


def box(ax, x, y, text, colour, w=3.0, h=1.25, bold=False):
    ax.add_patch(
        FancyBboxPatch(
            (x - w / 2, y - h / 2), w, h,
            boxstyle="round,pad=0.16,rounding_size=0.35",
            linewidth=2.4, edgecolor=colour, facecolor="white", zorder=3,
        )
    )
    ax.text(
        x, y, text, fontproperties=fb if bold else f, fontsize=12.5,
        color=INK, ha="center", va="center", linespacing=1.35, zorder=4,
    )


def arrow(ax, start, end, colour, rad=0.28, lw=2.6):
    ax.add_patch(
        FancyArrowPatch(
            start, end,
            connectionstyle=f"arc3,rad={rad}",
            arrowstyle="-|>", mutation_scale=20,
            linewidth=lw, color=colour, zorder=2,
        )
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(11.5, 6.6), dpi=200)
    ax.set_xlim(-9.2, 8.8)
    ax.set_ylim(-4.3, 4.1)
    ax.axis("off")

    # **The order is the argument, and the first draft had it wrong**: hiding
    # comes before nobody being able to contradict it, not after. The event
    # enters the loop from outside; it does not repeat.
    box(ax, -7.2, 2.6, "aconteceu\nalguma coisa", INK, w=3.0)
    arrow(ax, (-5.6, 2.6), (-4.3, 2.6), INK, rad=0.0, lw=2.2)

    box(ax, -2.5, 2.6, "a vergonha diz:\n«se souberem,\nninguém me quer»", LOOP,
        w=3.7, h=1.8)
    box(ax, 2.6, 2.6, "escondo", LOOP, w=2.6, bold=True)
    box(ax, 2.6, -2.6, "ninguém pode\ndizer-me o contrário", LOOP, w=3.7)
    box(ax, -2.5, -2.6, "e fica tudo\nna mesma", LOOP, w=3.0)

    arrow(ax, (-0.6, 2.6), (1.25, 2.6), LOOP, rad=0.0)
    arrow(ax, (2.6, 1.75), (2.6, -1.75), LOOP, rad=0.0)
    arrow(ax, (0.7, -2.6), (-0.95, -2.6), LOOP, rad=0.0)
    arrow(ax, (-2.5, -1.75), (-2.5, 1.6), LOOP, rad=0.0)

    ax.text(
        -3.0, 0.0, "e outra vez,\ne outra vez",
        fontproperties=f, fontsize=11.5, color=LOOP, ha="right", va="center",
    )

    # The way out leaves at the point where the loop is kept closed.
    arrow(ax, (4.0, 2.6), (5.3, 2.6), OUTWARD, rad=0.0)
    box(ax, 7.0, 2.6, "alguém vê\ne fica", OUTWARD, w=2.8, bold=True)
    arrow(ax, (7.0, 1.85), (7.0, -1.75), OUTWARD, rad=0.0)
    box(ax, 7.0, -2.6, "a vergonha\nfica mais pequena", OUTWARD, w=3.4)

    ax.text(
        7.0, -3.75, "a única saída passa por ser vista",
        fontproperties=fb, fontsize=12, color=OUTWARD, ha="center", va="top",
    )

    clinical = ax.text(
        -2.5, -3.75,
        "esconder alivia no momento — e é o que impede\na previsão de alguma vez ser desmentida",
        fontproperties=f, fontsize=11.5, color=SOFT, ha="center", va="top",
        linespacing=1.4,
    )

    fig.text(
        0.5, 0.015, "Esquema ilustrativo. Não representa medições.",
        fontproperties=f, fontsize=10.5, color="#7A839B", ha="center", va="top",
    )

    plt.tight_layout()
    plt.savefig(OUT / "envergonhado-ciclo.png", bbox_inches="tight",
                facecolor="white")

    clinical.set_visible(False)
    plt.savefig(OUT / "envergonhado-ciclo-crianca.png", bbox_inches="tight",
                facecolor="white")

    print("wrote envergonhado-ciclo.png and envergonhado-ciclo-crianca.png")


if __name__ == "__main__":
    main()
