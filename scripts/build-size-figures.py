#!/usr/bin/env python3
"""Constrói os bonecos de tamanhos (D-331).

    python3 scripts/build-size-figures.py

Uma folha A4 por família, com a figura em três tamanhos para recortar.

**Uma folha por família e não uma folha com as sete.** A clínica imprime a que
serve àquele caso naquele dia, e nenhuma peça pressupõe as outras (D-327). Sete
famílias ao mesmo tempo obrigariam a uma folha enorme ou a figuras pequenas de
mais para uma criança recortar.

**Três tamanhos, e três não é pouco — é o limite.** Três degraus grosseiros
dizem *ficou pequeno*, *ficou como é*, *ficou enorme*, e não se convertem em
número. Cinco degraus já pediriam uma escala, e uma escala é o que este material
não pode ser.

O rebordo branco das figuras, que noutros contextos é um defeito, aqui é a
margem de corte. Fica.
"""

import os

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMOTIONS = os.path.join(ROOT, "artwork", "emotions")
FONTS = os.path.join(ROOT, "assets", "fonts")
OUT = os.path.join(ROOT, "docs", "materials", "bonecos")

DPI = 200
MM = DPI / 25.4
A4 = (round(210 * MM), round(297 * MM))

INK = (58, 51, 43)
FAINT = (168, 155, 138)
CUT = (205, 195, 180)

FAMILY = "Peças de sessão"
FAMILY_COLOUR = (150, 128, 96)
CREDIT = "© ColorHugs · colorhugs.pt · Material licenciado"

FAMILIES = {
    "zangado": ("angry.png", "Zangado"),
    "triste": ("sad.png", "Triste"),
    "assustado": ("scared.png", "Assustado"),
    "envergonhado": ("ashamed.png", "Envergonhado"),
    "calmo": ("calm.png", "Calmo"),
    "feliz": ("happy.png", "Feliz"),
    "aborrecido": ("bored.png", "Aborrecido"),
}

# Alturas em milímetros. O grande é cerca de três vezes e meia o médio, que é a
# proporção que a cena 4 do livro fixou para o Zangado enorme — a criança que
# leu a história reconhece o tamanho.
BIG_MM, MID_MM, SMALL_MM = 138, 52, 30


def figure(name, height_mm):
    im = Image.open(os.path.join(EMOTIONS, name)).convert("RGBA")
    # A imagem tem margem branca à volta; recorta-se ao conteúdo para que a
    # altura pedida seja a altura da figura e não a da folha em que ela vinha.
    bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
    diff = Image.new("L", im.size)
    diff.putdata([0 if p[:3] > (246, 246, 246) else 255
                  for p in im.convert("RGBA").getdata()])
    box = diff.getbbox() or (0, 0, im.width, im.height)
    im = im.crop(box)
    h = round(height_mm * MM)
    return im.resize((round(im.width * h / im.height), h), Image.LANCZOS)


def sheet(family_id):
    name, label = FAMILIES[family_id]
    page = Image.new("RGB", A4, "white")
    draw = ImageDraw.Draw(page)

    title = ImageFont.truetype(os.path.join(FONTS, "Baloo2-Bold.ttf"), round(7 * MM))
    small = ImageFont.truetype(os.path.join(FONTS, "Nunito-Medium.ttf"), round(3.4 * MM))
    tiny = ImageFont.truetype(os.path.join(FONTS, "Nunito-Medium.ttf"), round(2.9 * MM))

    # **O mesmo cabeçalho das outras peças da família** (D-351): o nome da
    # família por cima, o traço da cor por baixo do título, o mesmo rodapé.
    draw.text((round(18 * MM), round(13 * MM)), FAMILY.upper(), font=tiny,
              fill=FAMILY_COLOUR)
    draw.text((round(18 * MM), round(18 * MM)), f"Bonecos — {label}",
              font=title, fill=INK)
    draw.rounded_rectangle(
        [round(18 * MM), round(29.5 * MM), round(46 * MM), round(30.7 * MM)],
        radius=round(0.6 * MM), fill=FAMILY_COLOUR)
    draw.text(
        (round(18 * MM), round(34 * MM)),
        "Recortar. Não é uma escala e não se regista.",
        font=small, fill=FAINT,
    )

    # **As figuras são quase quadradas.** A primeira disposição pôs o grande à
    # esquerda e os outros dois numa coluna à direita, e as caixas de corte
    # sobrepuseram-se — a 112 mm de altura o grande ocupa 105 de largura e não
    # sobra coluna. O grande fica sozinho em cima, os dois pequenos lado a lado
    # por baixo.
    placed = []
    for mm, cx_mm, top_mm in ((BIG_MM, 105, 46), (MID_MM, 68, 198), (SMALL_MM, 142, 214)):
        f = figure(name, mm)
        x = round(cx_mm * MM) - f.width // 2
        y = round(top_mm * MM)
        page.paste(f, (x, y), f)
        placed.append((x, y, f.width, f.height))

    m = round(5 * MM)
    boxes = [(x - m, y - m, x + w + m, y + h + m) for x, y, w, h in placed]
    for i, a in enumerate(boxes):
        for b in boxes[i + 1:]:
            if a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]:
                raise SystemExit("caixas de corte sobrepostas — corrigir a disposição")

    step = round(2.4 * MM)
    for x0, y0, x1, y1 in boxes:
        for x in range(x0, x1, step * 2):
            draw.line([x, y0, min(x + step, x1), y0], fill=CUT, width=2)
            draw.line([x, y1, min(x + step, x1), y1], fill=CUT, width=2)
        for yy in range(y0, y1, step * 2):
            draw.line([x0, yy, x0, min(yy + step, y1)], fill=CUT, width=2)
            draw.line([x1, yy, x1, min(yy + step, y1)], fill=CUT, width=2)

    width = draw.textlength(CREDIT, font=tiny)
    draw.text(((A4[0] - width) / 2, A4[1] - round(13 * MM)), CREDIT,
              font=tiny, fill=FAINT)
    return page


def main():
    os.makedirs(OUT, exist_ok=True)
    pages = [sheet(f) for f in FAMILIES]
    target = os.path.join(OUT, "bonecos-tamanhos.pdf")
    pages[0].save(target, save_all=True, append_images=pages[1:],
                  resolution=DPI, format="PDF")
    for family_id, page in zip(FAMILIES, pages):
        page.save(os.path.join(OUT, f"bonecos-{family_id}.png"))
    print(f"{len(pages)} folhas · {target}")


if __name__ == "__main__":
    main()
