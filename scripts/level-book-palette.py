#!/usr/bin/env python3
"""Nivela a paleta de fundo das cenas do livro (D-313, D-316).

Corrige apenas as cores planas de chão e parede. Não toca nas personagens, nos
contornos, nos objectos de cenário nem em nada que não seja fundo.

Método: para cada cena mede-se a cor dominante do chão e da parede, calcula-se o
desvio para a mediana do livro, e aplica-se esse desvio com um peso que vale 1
nos píxeis iguais à cor de fundo e cai para 0 à medida que o píxel se afasta
dela. As arestas antialiased transitam suavemente e nada mais se move.

Uso:
    python3 scripts/level-book-palette.py            # aplica às cenas fora de pack
    python3 scripts/level-book-palette.py --report   # só mede, não escreve
"""

import argparse
import glob
import os
import sys

import numpy as np
from PIL import Image

ART = "artwork/livro"

# As sete cores canónicas das personagens. Servem para excluir personagens da
# detecção de fundo — a cena 4 é ao alto e tem o vermelho no topo, a cena 12 tem
# o amarelo, e sem esta exclusão a parede é detectada como sendo a personagem.
CAST = np.array([
    [230,  60,  55],   # vermelho
    [ 95, 185, 240],   # azul claro
    [175, 140, 225],   # lilás
    [245, 150, 180],   # rosa
    [188, 153,  66],   # caqui
    [126, 211, 171],   # verde-menta
    [252, 196,   5],   # amarelo-ouro
])

# Cenas fora de pack, medidas em D-313 e reconfirmadas antes de corrigir.
OUT_OF_PACK = ["cena-09", "cena-11", "cena-12", "cena-14"]

TOL = 55.0        # raio, em distância euclidiana RGB, dentro do qual o desvio
                  # se aplica por inteiro
                  # se aplica por inteiro
FEATHER = 20.0    # largura da transição para fora desse raio
SAME_SURFACE = 34.0  # abaixo desta distância, chão e parede são tratados como a
                     # mesma superfície e recebem um só desvio. Corrigi-los em
                     # separado quando são cores próximas parte a mesma parede
                     # entre dois desvios diferentes e produz manchas visíveis
                     # — apareceu na parede direita da cena 14.


def dominant(a, y0, y1, exclude_cast=False):
    """Cor plana dominante numa faixa horizontal da imagem.

    `exclude_cast` só se usa na faixa da parede. Na faixa do chão retira mais do
    que devia e a detecção passa a apanhar um objecto de cenário em vez do chão
    — foi o que aconteceu nas cenas 12 e 14 na primeira passagem.
    """
    h = a.shape[0]
    p = a[int(h * y0):int(h * y1)].reshape(-1, 3)

    if exclude_cast:
        d = np.linalg.norm(p[:, None, :] - CAST[None, :, :], axis=2)
        p = p[d.min(axis=1) > 60]
        p = p[p.sum(1) > 300]          # fora contornos
    if len(p) < 500:
        return None

    q = (p // 4).astype(int)
    key = q[:, 0] * 4096 + q[:, 1] * 64 + q[:, 2]
    vals, counts = np.unique(key, return_counts=True)
    sel = p[key == vals[counts.argmax()]]
    return np.median(sel, axis=0)


def measure(path):
    a = np.asarray(Image.open(path).convert("RGB")).astype(float)
    return dominant(a, 0.88, 0.99), dominant(a, 0.02, 0.14, exclude_cast=True)


def level(a, sources, deltas):
    """Aplica os desvios a partir da imagem original, uma só vez por píxel.

    Os dois desvios — chão e parede — têm de ser calculados sobre a imagem
    original e aplicados em conjunto. Aplicá-los em sequência corrige o chão
    duas vezes nas cenas em que o chão e a parede são cores próximas, e foi o
    que fez as cenas 12 e 14 passarem para o outro lado da mediana na primeira
    passagem: 58.5 de distância antes, 75.4 depois.

    Cada píxel pertence à fonte de que está mais perto, e só a essa.
    """
    # Cada píxel pertence à cor de que está mais perto, e as sete cores do
    # elenco entram nessa disputa como fontes intocáveis.
    #
    # O caqui é [188 153 66] e o chão da cena 14 é [212 150 90] — 34 de
    # distância, dentro do raio de correcção. Um raio fixo de protecção não
    # chega: a personagem tem variação interna e os píxeis do bordo caem para
    # fora do raio. Mediu-se 21.4 de desvio no caqui da cena 14 sem protecção
    # nenhuma, e ainda 15.8 com um raio fixo de 26. **A cor das personagens não
    # muda nunca** (folha de personagens), e a fronteira tem de ser decidida por
    # proximidade e não por raio.
    all_sources = list(sources) + list(CAST.astype(float))
    dists = np.stack([np.linalg.norm(a - s[None, None, :], axis=2) for s in all_sources])
    owner = dists.argmin(axis=0)

    out = a.copy()
    for i, delta in enumerate(deltas):
        d = dists[i]
        w = np.clip((TOL + FEATHER - d) / FEATHER, 0.0, 1.0)
        w = np.where(owner == i, w, 0.0)
        out += w[:, :, None] * delta[None, None, :]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--suffix", default="")
    args = ap.parse_args()

    scenes = sorted(glob.glob(os.path.join(ART, "cena-*.png")))
    if not scenes:
        sys.exit(f"sem cenas em {ART}")

    floors, walls = {}, {}
    for f in scenes:
        name = os.path.splitext(os.path.basename(f))[0]
        floors[name], walls[name] = measure(f)

    keep = [n for n in floors if n not in OUT_OF_PACK]
    tgt_floor = np.median([floors[n] for n in keep if floors[n] is not None], axis=0)
    tgt_wall = np.median([walls[n] for n in keep if walls[n] is not None], axis=0)

    print(f"mediana do livro  chão {tgt_floor}  parede {tgt_wall}")
    print(f"(calculada sobre {len(keep)} cenas, excluindo as fora de pack)\n")

    for name in sorted(floors):
        d = np.linalg.norm(floors[name] - tgt_floor)
        mark = "  <-- corrigir" if name in OUT_OF_PACK else ""
        print(f"{name}  chão {floors[name]}  distância {d:5.1f}{mark}")

    if args.report:
        return

    print()
    for name in OUT_OF_PACK:
        path = os.path.join(ART, f"{name}.png")
        a = np.asarray(Image.open(path).convert("RGB")).astype(float)

        sources = [floors[name]]
        deltas = [tgt_floor - floors[name]]
        if walls[name] is not None and np.linalg.norm(walls[name] - floors[name]) > SAME_SURFACE:
            sources.append(walls[name])
            deltas.append(tgt_wall - walls[name])

        a = level(a, sources, deltas)

        out = os.path.join(ART, f"{name}{args.suffix}.png")
        Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).save(out)

        nf, nw = measure(out)
        print(f"{name}  chão {floors[name]} -> {nf}   "
              f"distância {np.linalg.norm(floors[name]-tgt_floor):.1f} -> "
              f"{np.linalg.norm(nf-tgt_floor):.1f}")


if __name__ == "__main__":
    main()
