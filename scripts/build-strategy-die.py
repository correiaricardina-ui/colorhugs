#!/usr/bin/env python3
"""Constrói os dados por família (D-344, D-345).

    python3 scripts/build-strategy-die.py

Uma folha A4 por dado, com a planificação de um cubo para recortar, dobrar e
colar. As faces e a pergunta de cada dado vêm de `docs/materials/dados-familias.md`.

**São dois dados e não sete**, e a razão está escrita nesse ficheiro: a estrutura
*escolhe uma destas* existe em duas famílias e não nas outras cinco. **Os dois
não fazem a mesma pergunta** — um pergunta o que se quer experimentar, o outro o
que faz companhia — e essa diferença é a distinção que separa as duas famílias.

**O dado propõe; não manda.** É a tensão desta peça e resolve-se por regra e não
por desenho: as cinco estratégias são oferecidas e não prescritas, e um dado que
caísse numa delas e obrigasse a cumpri-la contrariava isso. **Quem lança pode
aceitar, recusar ou voltar a lançar**, e a face «outra coisa» existe para a
criança pôr lá a sua.

**Palavras e não pictogramas.** Cinco ícones novos custariam cinco gerações e
seriam adivinhados de maneiras diferentes por cada criança; as palavras saem do
ficheiro e traduzem-se sem redesenhar nada.
"""

import os

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(ROOT, "assets", "fonts")
OUT = os.path.join(ROOT, "docs", "materials", "folhas")
FIGURAS = os.path.join(ROOT, "artwork", "sessao", "dados")

DPI = 200
MM = DPI / 25.4
A4 = (round(210 * MM), round(297 * MM))

INK = (58, 51, 43)
FAINT = (168, 155, 138)
CUT = (120, 110, 96)
FOLD = (198, 188, 174)
FAMILY = "Peças de sessão"
FAMILY_COLOUR = (150, 128, 96)
CREDIT = "© ColorHugs · colorhugs.pt · Material licenciado"

LADO = 48          # milímetros
ABA = 9

SOURCE = os.path.join(ROOT, "docs", "materials", "dados-familias.md")


def dados():
    """Lê cada `## Dado do <Família>`: a pergunta e as seis faces."""
    import re

    texto = open(SOURCE, encoding="utf-8").read()
    out = []
    for bloco in re.split(r"\n(?=## )", texto):
        m = re.match(r"## Dado do (\w+)", bloco)
        if not m:
            continue
        pergunta = re.search(r"\*\*Pergunta:\*\*\s*(.+)", bloco)
        faces = re.findall(r"^\d+\.\s+(.+)$", bloco, re.M)
        if len(faces) != 6:
            raise SystemExit(f"{m.group(1)}: {len(faces)} faces, deviam ser seis")
        out.append((m.group(1), pergunta.group(1).strip() if pergunta else "",
                    [f.strip() for f in faces]))
    return out

# Posições na cruz, em unidades de face: (coluna, linha).
CRUZ = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (1, 3)]


def wrap(draw, texto, fonte, largura):
    linhas, actual = [], ""
    for palavra in texto.split():
        teste = (actual + " " + palavra).strip()
        if draw.textlength(teste, font=fonte) <= largura:
            actual = teste
        else:
            linhas.append(actual)
            actual = palavra
    if actual:
        linhas.append(actual)
    return linhas


def dashed(draw, x0, y0, x1, y1, cor, passo=2.2):
    passo = round(passo * MM)
    if x0 == x1:
        for y in range(y0, y1, passo * 2):
            draw.line([x0, y, x0, min(y + passo, y1)], fill=cor, width=3)
    else:
        for x in range(x0, x1, passo * 2):
            draw.line([x, y0, min(x + passo, x1), y0], fill=cor, width=3)


def figura(familia, indice):
    """A imagem daquela face, se existir.

    **Uma face sem imagem fica só com a palavra, e o dado constrói-se na
    mesma.** É deliberado: uma imagem que se sabe que não se lê a 26 mm não deve
    ser fixada no ficheiro só para a face não ficar vazia.
    """
    caminho = os.path.join(FIGURAS, f"{familia.lower()}-{indice}.png")
    return Image.open(caminho).convert("RGBA") if os.path.exists(caminho) else None


def folha(familia, pergunta, FACES, aberta):
    im = Image.new("RGB", A4, "white")
    draw = ImageDraw.Draw(im)

    big = ImageFont.truetype(os.path.join(FONTS, "Baloo2-Bold.ttf"), round(7.5 * MM))
    small = ImageFont.truetype(os.path.join(FONTS, "Nunito-Medium.ttf"), round(3.6 * MM))
    tiny = ImageFont.truetype(os.path.join(FONTS, "Nunito-Medium.ttf"), round(2.9 * MM))
    face = ImageFont.truetype(os.path.join(FONTS, "Nunito-Bold.ttf"), round(4.1 * MM))

    draw.text((round(18 * MM), round(13 * MM)), FAMILY.upper(), font=tiny,
              fill=FAMILY_COLOUR)
    draw.text((round(18 * MM), round(18 * MM)), f"Dado do {familia}",
              font=big, fill=INK)
    draw.rounded_rectangle(
        [round(18 * MM), round(29.5 * MM), round(46 * MM), round(30.7 * MM)],
        radius=round(0.6 * MM), fill=FAMILY_COLOUR)
    draw.text((round(18 * MM), round(34 * MM)),
              "Recortar pelo traço cheio, dobrar pelo tracejado, colar pelas abas.",
              font=small, fill=FAINT)
    draw.text((round(18 * MM), round(40 * MM)),
              f"O dado propõe: {pergunta} Pode aceitar-se, recusar-se ou voltar a lançar.",
              font=small, fill=FAINT)

    ox, oy = 33, 56   # canto superior esquerdo da cruz, em milímetros
    ocupadas = set(CRUZ)

    def caixa(c, l):
        return (round((ox + c * LADO) * MM), round((oy + l * LADO) * MM),
                round((ox + (c + 1) * LADO) * MM), round((oy + (l + 1) * LADO) * MM))

    # As abas, primeiro, para ficarem por baixo do contorno das faces.
    for c, l in CRUZ:
        x0, y0, x1, y1 = caixa(c, l)
        a = round(ABA * MM)
        recuo = round(6 * MM)
        if (c, l - 1) not in ocupadas:
            draw.polygon([(x0 + recuo, y0 - a), (x1 - recuo, y0 - a),
                          (x1, y0), (x0, y0)], outline=CUT, width=3)
        if (c, l + 1) not in ocupadas:
            draw.polygon([(x0, y1), (x1, y1), (x1 - recuo, y1 + a),
                          (x0 + recuo, y1 + a)], outline=CUT, width=3)
        if (c - 1, l) not in ocupadas:
            draw.polygon([(x0 - a, y0 + recuo), (x0, y0), (x0, y1),
                          (x0 - a, y1 - recuo)], outline=CUT, width=3)
        if (c + 1, l) not in ocupadas:
            draw.polygon([(x1, y0), (x1 + a, y0 + recuo), (x1 + a, y1 - recuo),
                          (x1, y1)], outline=CUT, width=3)

    for (c, l), texto in zip(CRUZ, FACES):
        x0, y0, x1, y1 = caixa(c, l)
        draw.rectangle([x0, y0, x1, y1], outline=CUT, width=4)

        # **A sexta face nomeia-se e fica vazia.** Uma face em branco não se
        # percebe; uma face escrita não deixa lá pôr nada. O rótulo sobe para o
        # cimo, em cinzento, e o resto da face é da criança.
        ultima = aberta and texto == FACES[-1]
        fonte = tiny if ultima else face
        cor = FAINT if ultima else INK

        # **Imagem em cima, palavra por baixo.** O dado serve crianças a partir
        # dos cinco anos e muitas não leem: quem lê, lê; quem não lê, reconhece;
        # e a palavra fica a ensinar a quem está a aprender (D-346).
        fig = None if ultima else figura(familia, FACES.index(texto) + 1)
        if fig is not None:
            alvo = round(25 * MM)
            escala = min(alvo / fig.width, alvo / fig.height)
            fig = fig.resize((round(fig.width * escala), round(fig.height * escala)),
                             Image.LANCZOS)
            im.paste(fig, ((x0 + x1) // 2 - fig.width // 2,
                           y0 + round(7 * MM) + (alvo - fig.height) // 2), fig)

        linhas = wrap(draw, texto, fonte, round((LADO - 8) * MM))
        alt = len(linhas) * round(6.4 * MM)
        if ultima:
            y = y0 + round(6 * MM)
        elif fig is not None:
            y = y0 + round(34 * MM)
        else:
            y = (y0 + y1) / 2 - alt / 2
        for linha in linhas:
            w = draw.textlength(linha, font=fonte)
            draw.text(((x0 + x1) / 2 - w / 2, y), linha, font=fonte, fill=cor)
            y += round(6.4 * MM)

    # As dobras: os limites entre duas faces vizinhas.
    for c, l in CRUZ:
        x0, y0, x1, y1 = caixa(c, l)
        if (c, l + 1) in ocupadas:
            dashed(draw, x0, y1, x1, y1, FOLD)
        if (c + 1, l) in ocupadas:
            dashed(draw, x1, y0, x1, y1, FOLD)

    w = draw.textlength(CREDIT, font=tiny)
    draw.text(((A4[0] - w) / 2, A4[1] - round(13 * MM)), CREDIT, font=tiny, fill=FAINT)

    return im


def main():
    os.makedirs(OUT, exist_ok=True)
    for familia, pergunta, faces in dados():
        # **Só o dado do Zangado tem face aberta.** As seis do Triste são um
        # conjunto fechado no caderno; acrescentar «outra coisa» seria pôr uma
        # sétima onde o material fixou seis.
        aberta = faces[-1].lower().startswith("outra")
        im = folha(familia, pergunta, faces, aberta)
        nome = f"dado-{familia.lower()}"
        im.save(os.path.join(OUT, f"{nome}.pdf"), resolution=DPI)
        im.save(os.path.join(OUT, f"{nome}.png"))
        print(f"{nome}.pdf")


if __name__ == "__main__":
    main()
