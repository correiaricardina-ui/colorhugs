#!/usr/bin/env python3
"""Constrói a versão de ecrã de *Quem És Tu?* (D-321).

    python3 scripts/build-book-web.py

Produz uma pasta autónoma em `docs/materials/livro-ecra/` que se abre com dois
cliques no `index.html`, sem servidor e sem ligação à internet.

**Sai da mesma fonte que os PDF.** O texto vem de `livro-historia.md` e
`livro-paratexto.md` pela mesma regra — o que está em citação vai para o ecrã —
e as ilustrações são as mesmas. Não há aqui um segundo original a divergir do
primeiro.

**O que esta versão não tem, e é deliberado:** nenhum script de terceiros,
nenhuma fonte remota, nenhum pedido de rede, nenhum registo do que foi lido,
nenhum armazenamento no navegador, nenhum botão de compra e nenhum preço. Um
livro que se abre num computador de casa não precisa de saber quem o abriu.
"""

import html
import os
import re
import shutil
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

MATERIALS = os.path.join(ROOT, "docs", "materials")
ART = os.path.join(ROOT, "artwork", "livro")
FONTS = os.path.join(ROOT, "assets", "fonts")
OUT = os.path.join(MATERIALS, "livro-ecra")

SCREEN_W = 1200  # largura máxima das ilustrações no ecrã


def load():
    """Reutiliza o leitor do construtor de PDF, para não haver duas gramáticas."""
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "bookpdf", os.path.join(ROOT, "scripts", "build-book-pdf.py")
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def seen_descriptions():
    """O «O que se vê» de cada cena, para texto alternativo.

    Foi escrito para quem ilustra, e descreve exactamente o que está na imagem —
    que é o que um leitor de ecrã precisa de ouvir. **Não se escreve um segundo
    texto alternativo**, que divergiria deste na primeira alteração.
    """
    out, key = {}, None
    path = os.path.join(MATERIALS, "livro-historia.md")
    for line in open(path, encoding="utf-8"):
        m = re.match(r"^##\s+Cena\s+(\d+)", line)
        if m:
            key = m.group(1)
            continue
        if key and line.startswith("**O que se vê.**"):
            out[key] = re.sub(r"\*\*|\*", "", line.replace("**O que se vê.**", "")).strip()
    return out


def copy_image(src_name, dst_dir):
    im = Image.open(os.path.join(ART, src_name)).convert("RGB")
    if im.width > SCREEN_W:
        im = im.resize((SCREEN_W, round(im.height * SCREEN_W / im.width)),
                       Image.LANCZOS)
    im.save(os.path.join(dst_dir, src_name), "PNG", optimize=True)


def screens(mod, scenes, para, alts):
    """Capa, dezasseis cenas, elenco, contracapa. A ficha técnica fica fora do
    percurso de leitura e abre num painel — uma página de direitos de autor no
    meio de uma história é uma interrupção sem motivo."""
    items = [{
        "kind": "cover",
        "img": "capa.png",
        "alt": "As sete personagens juntas. O Aborrecido está à frente.",
        "text": [mod.inline(p) for p in para.get("1", [])],
    }]
    for n in range(1, 17):
        items.append({
            "kind": "scene",
            "img": f"cena-{n:02d}.png",
            "alt": alts.get(str(n), ""),
            "text": [mod.inline(p) for p in scenes[str(n)]],
        })
    items.append({"kind": "cast", "img": None, "alt": "",
                  "text": [mod.inline(p) for p in para.get("19", [])]})
    items.append({"kind": "back", "img": None, "alt": "",
                  "text": [mod.inline(p) for p in para.get("20", [])]})
    return items


PAGE = """<!doctype html>
<html lang="pt-PT">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Quem És Tu?</title>
<style>
@font-face { font-family: "ColorHugs Text"; font-weight: 500;
  src: url("fontes/Nunito-Medium.ttf") format("truetype"); font-display: swap; }
@font-face { font-family: "ColorHugs Text"; font-weight: 700;
  src: url("fontes/Nunito-Bold.ttf") format("truetype"); font-display: swap; }
@font-face { font-family: "ColorHugs Display"; font-weight: 700;
  src: url("fontes/Baloo2-Bold.ttf") format("truetype"); font-display: swap; }

* { box-sizing: border-box; }
html, body { height: 100%; margin: 0; }
body {
  font-family: "ColorHugs Text", system-ui, sans-serif;
  font-weight: 500; color: #3a332b; background: #f4ece1;
  display: flex; flex-direction: column;
}
.reader {
  flex: 1; display: flex; align-items: center; justify-content: center;
  padding: 3vh 4vw; gap: 4vw; min-height: 0;
}
figure { margin: 0; flex: 0 1 auto; min-width: 0; }
figure img {
  max-width: 100%; max-height: 82vh; display: block; border-radius: 10px;
  box-shadow: 0 6px 26px rgba(90, 70, 45, .18);
}
.words { flex: 0 1 30rem; min-width: 0; }
.words p { font-size: clamp(1.02rem, 1.5vw, 1.32rem); line-height: 1.55;
  margin: 0 0 .9em 0; }

.cover-screen { flex-direction: column; gap: 0; }
.cover-screen figure { position: relative; }
.cover-screen .words {
  position: absolute; top: 6%; left: 0; right: 0; text-align: center; flex: none;
}
.cover-screen .words p {
  font-family: "ColorHugs Display", sans-serif; font-weight: 700;
  font-size: clamp(2rem, 4.4vw, 3.4rem); margin: 0; color: #4a3a28;
}

.panel-screen { max-width: 42rem; margin: 0 auto; }
.panel-screen .words { flex: 1 1 auto; }
.cast-screen .words p:first-child {
  font-family: "ColorHugs Display", sans-serif; font-weight: 700;
  font-size: clamp(1.5rem, 3vw, 2rem); margin-bottom: .9em; text-align: center;
}
.back-screen .words p:nth-child(n+3) { font-size: .95rem; color: #6a6055; }

nav {
  display: flex; align-items: center; justify-content: center; gap: 1.1rem;
  padding: .7rem 1rem 1.2rem;
}
button {
  font: inherit; font-size: 1rem; padding: .5rem 1.1rem; border-radius: 999px;
  border: 1.5px solid #cbb9a0; background: #fffaf3; color: #3a332b;
  cursor: pointer;
}
button:hover:not(:disabled) { background: #fff; border-color: #a8917a; }
button:disabled { opacity: .35; cursor: default; }
button:focus-visible, a:focus-visible { outline: 3px solid #7a9ec4;
  outline-offset: 2px; }
.count { font-variant-numeric: tabular-nums; font-size: .95rem;
  color: #6a6055; min-width: 5.5rem; text-align: center; }
.imprint-open { background: none; border: none; color: #6a6055;
  text-decoration: underline; padding: .4rem; }

dialog {
  border: none; border-radius: 12px; padding: 2rem 2.2rem; max-width: 34rem;
  color: #3a332b; background: #fffdf9;
}
dialog::backdrop { background: rgba(60, 48, 34, .45); }
dialog p { margin: 0 0 .9em 0; font-size: .98rem; line-height: 1.55; }
dialog p:first-child { font-family: "ColorHugs Display", sans-serif;
  font-weight: 700; font-size: 1.35rem; }
dialog img { display: block; margin: 1.4rem auto 0; width: 8rem; }

@media (max-width: 820px) {
  .reader { flex-direction: column; gap: 1.4rem; padding: 2vh 5vw; }
  figure img { max-height: 52vh; }
}
@media (prefers-reduced-motion: no-preference) {
  .reader > * { animation: in .28s ease-out; }
  @keyframes in { from { opacity: 0; transform: translateY(6px); } }
}
</style>
</head>
<body>

<main class="reader" id="reader" aria-live="polite"></main>

<nav>
  <button id="prev" type="button">&#8592; Anterior</button>
  <span class="count" id="count"></span>
  <button id="next" type="button">Seguinte &#8594;</button>
  <button class="imprint-open" id="open-imprint" type="button">Ficha técnica</button>
</nav>

<dialog id="imprint">
  __IMPRINT__
  <img src="imagens/marca.png" alt="ColorHugs">
  <form method="dialog"><button type="submit">Fechar</button></form>
</dialog>

<script>
const SCREENS = __DATA__;
const reader = document.getElementById('reader');
const count  = document.getElementById('count');
const prev   = document.getElementById('prev');
const next   = document.getElementById('next');
let i = 0;

function render() {
  const s = SCREENS[i];
  reader.className = 'reader ' + s.kind + '-screen'
    + (s.kind === 'cast' || s.kind === 'back' ? ' panel-screen' : '');
  const fig = s.img
    ? '<figure><img src="imagens/' + s.img + '" alt="' + s.alt + '"></figure>'
    : '';
  const words = '<div class="words">'
    + s.text.map(t => '<p>' + t + '</p>').join('') + '</div>';
  reader.innerHTML = s.kind === 'cover' ? '<figure><img src="imagens/'
      + s.img + '" alt="' + s.alt + '">' + words + '</figure>'
    : fig + words;
  count.textContent = (i + 1) + ' de ' + SCREENS.length;
  prev.disabled = i === 0;
  next.disabled = i === SCREENS.length - 1;
  document.title = 'Quem És Tu? — ' + (i + 1) + ' de ' + SCREENS.length;
}

function go(step) {
  const n = i + step;
  if (n < 0 || n >= SCREENS.length) return;
  i = n;
  render();
}

prev.addEventListener('click', () => go(-1));
next.addEventListener('click', () => go(1));
document.addEventListener('keydown', e => {
  if (document.getElementById('imprint').open) return;
  if (e.key === 'ArrowRight' || e.key === 'PageDown') go(1);
  if (e.key === 'ArrowLeft'  || e.key === 'PageUp')   go(-1);
  if (e.key === 'Home') { i = 0; render(); }
  if (e.key === 'End')  { i = SCREENS.length - 1; render(); }
});
document.getElementById('open-imprint').addEventListener('click',
  () => document.getElementById('imprint').showModal());

render();
</script>
</body>
</html>
"""


def main():
    mod = load()
    scenes, para = mod.load_text()
    alts = seen_descriptions()

    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "imagens"))
    os.makedirs(os.path.join(OUT, "fontes"))

    for name in ["capa.png"] + [f"cena-{n:02d}.png" for n in range(1, 17)]:
        copy_image(name, os.path.join(OUT, "imagens"))

    mark = os.path.join(ROOT, "public", "assets", "branding",
                        "colorhugs-parents.webp")
    Image.open(mark).save(os.path.join(OUT, "imagens", "marca.png"))

    for f in ("Nunito-Medium.ttf", "Nunito-Bold.ttf", "Baloo2-Bold.ttf"):
        shutil.copy(os.path.join(FONTS, f), os.path.join(OUT, "fontes", f))
    for f in os.listdir(FONTS):
        if f.startswith("OFL"):
            shutil.copy(os.path.join(FONTS, f), os.path.join(OUT, "fontes", f))

    items = screens(mod, scenes, para, alts)
    imprint = "".join(f"<p>{mod.inline(p)}</p>" for p in para.get("2", []))

    import json
    page = (PAGE.replace("__DATA__", json.dumps(items, ensure_ascii=False))
                .replace("__IMPRINT__", imprint))
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(page)

    total = sum(
        os.path.getsize(os.path.join(dp, f))
        for dp, _, fs in os.walk(OUT) for f in fs
    )
    print(f"{OUT}  {len(items)} ecrãs  {total // 1024} KB")


if __name__ == "__main__":
    main()
