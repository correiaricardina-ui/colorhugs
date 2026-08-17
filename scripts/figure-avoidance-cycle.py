#!/usr/bin/env python3
"""
The scared family's schema — what avoidance does over time.

**Not the arousal curve and not the two paths.** Anger's figure is one episode.
Sadness's is one episode carried two ways. Fear's problem is not inside an
episode at all: it is what happens **across** them, and no picture of a single
episode can show it.

So this draws **four encounters with the same thing**, twice over. Avoiding gives
relief inside each one and a taller peak in the next. Staying — even a little,
even badly — gives a harder minute and a lower peak next time.

It is the one figure in the project whose claim is *estabelecida* rather than
*razoável* (D-235), and it is also the one families most reliably get backwards,
because **the version that makes things worse is the one that feels better
immediately**.

Two rules held, both from D-201: **no numbers on any axis**, and the child's
version carries no sentence written about her.

    python3 scripts/figure-avoidance-cycle.py
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
AVOID = "#C0554A"    # the line that grows
APPROACH = "#3FA96B" # the line that settles
SOFT = "#8B6FE0"

f = FontProperties(fname="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
fb = FontProperties(fname="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")


def episodes(peaks, cut=None):
    """Four humps along one time axis, each with its own height.

    `cut` truncates each hump early — what avoidance does: the feeling stops
    because the situation stopped, not because the fear came down.
    """
    t = np.linspace(0, 4, 1200)
    y = np.zeros_like(t)
    for i, peak in enumerate(peaks):
        centre = i + 0.5
        local = np.exp(-((t - centre) ** 2) / 0.020)
        if cut is not None:
            local = np.where(t > centre + cut, 0, local)
        y = np.maximum(y, local * peak)
    return t, y


def panel(ax, peaks, colour, title, note, cut=None):
    t, y = episodes(peaks, cut)
    ax.plot(t, y, color=colour, lw=4.5, solid_capstyle="round", zorder=3)
    ax.fill_between(t, y, color=colour, alpha=0.08, zorder=1)

    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(INK)
        ax.spines[s].set_linewidth(1.8)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-0.1, 4.35)
    ax.set_ylim(0, 1.35)

    ax.set_title(title, fontproperties=fb, fontsize=15, color=colour, pad=12)
    ax.set_xlabel("uma vez, outra vez, outra vez…", fontproperties=f,
                  fontsize=11.5, color=INK, labelpad=8)
    ax.text(-0.055, 0.5, "medo", fontproperties=f, fontsize=12, color=INK,
            rotation=90, ha="right", va="center", transform=ax.transAxes)
    # Below the axis label, not on top of it: the first version printed the two
    # over each other and neither could be read.
    ax.text(0.5, -0.22, note, fontproperties=fb, fontsize=12, color=colour,
            ha="center", va="top", transform=ax.transAxes, linespacing=1.4)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    fig, (left, right) = plt.subplots(1, 2, figsize=(11, 4.6), dpi=200)

    # Avoiding: cut short each time, and higher each time.
    panel(
        left, [0.62, 0.76, 0.90, 1.05], AVOID,
        "quando se foge",
        "alívio logo — e maior da próxima vez",
        cut=0.10,
    )
    # Staying: the full hump, coming down on its own, lower each time.
    panel(
        right, [1.05, 0.86, 0.66, 0.46], APPROACH,
        "quando se fica um bocadinho",
        "custa mais no momento — e menor da próxima vez",
    )

    clinical = fig.text(
        0.5, -0.10,
        "A versão que piora é a que sabe melhor no momento. É por isso que ninguém a escolhe de propósito.",
        fontproperties=f, fontsize=12, color=SOFT, ha="center", va="top",
    )
    fig.text(
        0.5, -0.18, "Esquema ilustrativo. Não representa medições.",
        fontproperties=f, fontsize=10.5, color="#7A839B", ha="center", va="top",
    )

    plt.tight_layout()
    plt.savefig(OUT / "assustado-evitamento.png", bbox_inches="tight",
                facecolor="white")

    # The child's version: the same picture without the line addressed to
    # whoever is applying it (D-189).
    clinical.set_visible(False)
    plt.savefig(OUT / "assustado-evitamento-crianca.png", bbox_inches="tight",
                facecolor="white")

    print("wrote assustado-evitamento.png and assustado-evitamento-crianca.png")


if __name__ == "__main__":
    main()
