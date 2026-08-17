#!/usr/bin/env python3
"""
The happy family's schema — the two shapes a good thing can take.

**It is the only figure in the material that draws a positive feeling**, and it
exists because of the two complaints in D-283, which are the same mechanism in
two tenses: the joy that is never inhabited, and the emptiness afterwards.

Two panels.

The first is what families get wrong twice over: the charge is all in the
**before**, the thing itself is barely a bump, and the drop afterwards is read as
proof that something failed. **The dip is normal and the figure says so.**

The second is not *the right way* — nothing here promises a technique. It is what
it looks like when the charge is spread: less in the anticipation, more in the
thing, and a gentler return.

**No numbers on any axis** (D-201), and the baseline is drawn, because the whole
point of the after is that it goes *below* where it started and comes back.

    python3 scripts/figure-joy-shapes.py
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
ALL_BEFORE = "#E0A32E"
SPREAD = "#E0619A"
SOFT = "#8B6FE0"

f = FontProperties(fname="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
fb = FontProperties(fname="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")


def panel(ax, y, colour, title, note):
    t = np.linspace(0, 10, 900)
    ax.plot(t, y, color=colour, lw=4.5, solid_capstyle="round", zorder=4)
    ax.fill_between(t, y, 0, color=colour, alpha=0.10, zorder=2)

    # The baseline matters: the after goes below where it started.
    ax.axhline(0, color=INK, lw=1.6, alpha=0.55, zorder=3)

    # The moment itself.
    ax.axvline(5.4, -0.55 / 1.75, 1.35 / 1.75, color=INK, lw=1.4,
               ls=(0, (4, 4)), alpha=0.45, zorder=1)
    ax.text(5.4, 1.42, "a coisa acontece", fontproperties=f, fontsize=11.5,
            color=INK, ha="center", va="bottom")

    for s in ("top", "right", "bottom"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_color(INK)
    ax.spines["left"].set_linewidth(2)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-0.4, 10.9)
    ax.set_ylim(-0.55, 1.75)

    ax.set_title(title, fontproperties=fb, fontsize=14, color=colour, pad=26)
    ax.text(-0.05, 0.62, "alegria", fontproperties=f, fontsize=11.5, color=INK,
            rotation=90, ha="right", va="center", transform=ax.transAxes)
    ax.text(0.5, -0.13, note, fontproperties=fb, fontsize=12, color=colour,
            ha="center", va="top", transform=ax.transAxes)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    t = np.linspace(0, 10, 900)

    # **Blended, not masked.** The first version cut the curves at the moment
    # with a hard mask and produced a vertical jump — a discontinuity reads as a
    # drawing error, and the drop here is meant to be steep, not instantaneous.
    def gate(centre, steep):
        return 1 / (1 + np.exp(-(t - centre) * steep))

    # All the charge in the anticipation: a long climb, a small bump at the
    # moment itself, and a deep dip afterwards.
    w = gate(5.4, 3.4)
    before = 1.15 * np.exp(-((t - 4.9) ** 2) / 3.2) * (1 - w)
    during = 0.26 * np.exp(-((t - 5.9) ** 2) / 0.55) * w
    after = -0.42 * np.exp(-((t - 7.1) ** 2) / 2.2) * gate(6.1, 2.6)
    shape_a = before + during + after

    # The charge spread: a smaller climb, the thing itself the highest point,
    # and a shallower return.
    wb = gate(5.4, 2.2)
    before_b = 0.62 * np.exp(-((t - 4.4) ** 2) / 4.0) * (1 - wb)
    during_b = 1.05 * np.exp(-((t - 6.2) ** 2) / 1.8) * wb
    after_b = -0.15 * np.exp(-((t - 8.6) ** 2) / 2.4) * gate(7.8, 2.2)
    shape_b = before_b + during_b + after_b

    fig, (left, right) = plt.subplots(1, 2, figsize=(11.4, 4.9), dpi=200)
    panel(left, shape_a, ALL_BEFORE, "quando está tudo no antes",
          "quase não a aproveitou — e o buraco a seguir é fundo")
    panel(right, shape_b, SPREAD, "quando se reparte",
          "menos na espera, mais na coisa — e a volta é mais suave")

    clinical = fig.text(
        0.5, -0.10,
        "o buraco depois é normal e não é sinal de que correu mal — e a criança que «não aproveitou» não estava a rejeitar nada: nunca chegou a estar lá",
        fontproperties=f, fontsize=11.5, color=SOFT, ha="center", va="top",
    )
    fig.text(
        0.5, -0.19, "Esquema ilustrativo. Não representa medições.",
        fontproperties=f, fontsize=10.5, color="#7A839B", ha="center", va="top",
    )

    plt.tight_layout()
    plt.savefig(OUT / "feliz-formas.png", bbox_inches="tight", facecolor="white")

    clinical.set_visible(False)
    plt.savefig(OUT / "feliz-formas-crianca.png", bbox_inches="tight",
                facecolor="white")

    print("wrote feliz-formas.png and feliz-formas-crianca.png")


if __name__ == "__main__":
    main()
