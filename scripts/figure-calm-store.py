#!/usr/bin/env python3
"""
The calm family's schema — the store, and where it is spent.

**It is the only schema in the project that is not about one family.** The other
five explain a mechanism: the arousal curve, the two paths, the avoidance cycle,
the hiding loop, the strip of time. **Calm has no mechanism to explain** — there
is nothing to bring down, nothing that maintains it, and nothing to correct.

What it has instead is the one thing no other family has: **it points outwards.**
The store is filled here and spent elsewhere. So the figure is the only place in
the whole material where the seven families are visibly one system rather than
seven separate things.

A body map was considered and rejected: **calm is general deactivation and
usually has no location** (D-276), and asking a child to point at it is asking
her to find something that has no place.

Two versions, further apart than usual. The clinician's carries the mechanism of
each arrow; the child's carries three short lines and no explanation.

    python3 scripts/figure-calm-store.py
"""

import pathlib

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/materials/figuras"

INK = "#1B2A5B"
STORE = "#3FA96B"
SCARED = "#8B6FE0"
ANGRY = "#C0554A"
SAD = "#4A78B8"
SOFT = "#8B6FE0"

f = FontProperties(fname="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
fb = FontProperties(fname="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")


def box(ax, x, y, w, h, text, colour, bold=False, size=12.5):
    ax.add_patch(
        FancyBboxPatch(
            (x - w / 2, y - h / 2), w, h,
            boxstyle="round,pad=0.16,rounding_size=0.35",
            linewidth=2.6, edgecolor=colour, facecolor="white", zorder=3,
        )
    )
    ax.text(
        x, y, text, fontproperties=fb if bold else f, fontsize=size, color=INK,
        ha="center", va="center", linespacing=1.35, zorder=4,
    )


def arrow(ax, start, end, colour):
    ax.add_patch(
        FancyArrowPatch(
            start, end, connectionstyle="arc3,rad=0.0",
            arrowstyle="-|>", mutation_scale=20, linewidth=2.6,
            color=colour, zorder=2,
        )
    )


def draw(child: bool) -> None:
    fig, ax = plt.subplots(figsize=(10.6, 6.4), dpi=200)
    ax.set_xlim(-6.6, 7.2)
    ax.set_ylim(-4.4, 3.6)
    ax.axis("off")

    box(
        ax, -3.6, 0.0, 4.4, 2.5,
        "o que se junta aqui\n\nsítios · alturas\no tom do corpo",
        STORE, bold=False,
    )
    ax.text(-3.6, 1.55, "CALMO", fontproperties=fb, fontsize=13, color=STORE,
            ha="center", va="bottom")

    rows = [
        (2.3, SCARED, "Assustado",
         "para conseguir ficar\num bocadinho" if not child
         else "para conseguir ficar"),
        (0.0, ANGRY, "Zangado",
         "para o corpo descer\ndepois do pico" if not child
         else "para o corpo descer"),
        (-2.3, SAD, "Triste",
         "para saber onde é\no seu sítio" if not child
         else "para saber onde é o meu sítio"),
    ]

    for y, colour, name, note in rows:
        # From the edge of the store to just short of each box, so the head is
        # visible: the first version drew the arrows into the boxes and the
        # points disappeared under the borders.
        arrow(ax, (-1.32, y * 0.30), (0.85, y * 0.92), colour)
        box(ax, 3.6, y, 5.2, 1.5, f"{name}\n{note}", colour, size=12)

    if not child:
        ax.text(
            0.3, -3.75,
            "esta é a única família que aponta para fora de si própria: enche-se aqui e gasta-se noutro lado",
            fontproperties=f, fontsize=11.5, color=SOFT, ha="center", va="top",
        )

    fig.text(
        0.5, 0.012, "Esquema ilustrativo. Não representa medições.",
        fontproperties=f, fontsize=10.5, color="#7A839B", ha="center", va="top",
    )

    plt.tight_layout()
    name = "calmo-deposito-crianca.png" if child else "calmo-deposito.png"
    plt.savefig(OUT / name, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    draw(child=False)
    draw(child=True)
    print("wrote calmo-deposito.png and calmo-deposito-crianca.png")


if __name__ == "__main__":
    main()
