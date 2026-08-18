#!/usr/bin/env python3
"""Gera as instâncias estáticas das fontes do livro.

    python3 scripts/make-book-fonts.py

**Porquê não usar os ficheiros variáveis directamente.** O Chromium incorpora
uma fonte variável no PDF como Type 3 — cada glifo desenhado como contorno em
vez de entrar como glifo de uma fonte incorporada. O ficheiro cresce e alguns
leitores mostram texto pior. Com instâncias estáticas o PDF leva subconjuntos
TrueType normais.

As fontes de origem são `Nunito.ttf` e `Baloo2.ttf`, ambas SIL Open Font
License, com a licença ao lado em `assets/fonts/`.
"""

import os

from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

FONTS = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "fonts"
)

INSTANCES = [
    ("Nunito.ttf", {"wght": 500}, "Nunito-Medium.ttf"),
    ("Nunito.ttf", {"wght": 700}, "Nunito-Bold.ttf"),
    ("Baloo2.ttf", {"wght": 700}, "Baloo2-Bold.ttf"),
]


def main():
    for src, axes, name in INSTANCES:
        font = TTFont(os.path.join(FONTS, src))
        out = instancer.instantiateVariableFont(
            font, axes, inplace=False, updateFontNames=True
        )
        target = os.path.join(FONTS, name)
        out.save(target)
        print(f"{name}  {os.path.getsize(target) // 1024} KB")


if __name__ == "__main__":
    main()
