"""
ColorHugs — asset preparation.

The supplied artwork is flat RGB with either a WHITE or a BLACK studio
background. Sticker UI needs transparency, so we:

  1. pad the canvas with the detected background colour;
  2. flood-fill the background from the borders (connected components);
  3. for WHITE backgrounds, erode the background mask so the sticker's
     white die-cut rim is preserved (it is the same colour as the bg);
  4. feather the alpha channel by <1px to avoid hard edges;
  5. trim to the artwork bounding box;
  6. downscale to a sane web size.

The artwork itself is never redrawn, recoloured or restyled.
"""
import os
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

SRC = os.environ.get("COLORHUGS_SOURCE_DIR", "/mnt/project")
DST = "/home/claude/colorhugs/public/assets"

# source file -> destination path (relative to DST)
MAP = {
    # ---------- branding ----------
    "ColorHugs_Principal.png": "branding/colorhugs-logo.png",
    # ---------- banners ----------
    "Faixa_parents.png": "banners/parents-safety.webp",
    "Faixa_community.png": "banners/community.webp",
    "Faixa_principal.png": "banners/home.png",
    "faixa_larning_hub.png": "banners/learning-hub.png",
    "Faixa_Brain_Gym.png": "banners/brain-gym.png",
    "Faixa_My_Inner_World.png": "banners/my-inner-world.png",
    "Faixa_Kids_Draw_for_Kids.png": "banners/kids-draw.png",
    "faixa_color_and_create.png": "banners/color-and-create.png",
    "Faixa_My_ColorHugs.png": "banners/my-colorhugs.png",
    "Faixa_Free.png": "banners/free.png",
    "Faixa_premium.png": "banners/premium.png",
    # ---------- section stickers ----------
    "Learning_Hub.png": "stickers/sections/learning-hub.png",
    "Brain_Gym.png": "stickers/sections/brain-gym.png",
    "Community.png": "stickers/sections/community.png",
    "My_Inner_Word.png": "stickers/sections/my-inner-world.png",
    "Kids_Draw_for_Kids.png": "stickers/sections/kids-draw.png",
    "Color_and_Create.png": "stickers/sections/color-and-create.png",
    "My_ColorHugs.png": "stickers/sections/my-colorhugs.png",
    "ParentSafety.png": "stickers/sections/parents-safety.png",
    # ---------- plan badges ----------
    "Free.png": "stickers/plans/free.png",
    "Premium.png": "stickers/plans/premium.png",
    # ---------- learning hub ----------
    "learninghub_word.png": "stickers/learning-hub/word-explorer.png",
    "learninghub_number.png": "stickers/learning-hub/number-adventure.png",
    "learninghub_storytime.png": "stickers/learning-hub/story-time.png",
    "learninghub_schoolchallenge.png": "stickers/learning-hub/school-challenge.png",
    # ---------- brain gym ----------
    "braingymn_focusmission.png": "stickers/brain-gym/focus-mission.png",
    "braingym_memory.png": "stickers/brain-gym/memory-challenge.png",
    "braingymn_thinksolve.png": "stickers/brain-gym/think-and-solve.png",
    "braingym_speddybrain.png": "stickers/brain-gym/speedy-brain.png",
    # ---------- my inner world ----------
    "innerworld_howdoifeel.png": "stickers/my-inner-world/how-do-i-feel.png",
    "innerworld_calmmybody.png": "stickers/my-inner-world/calm-my-body.png",
    "innerwordl_myworries.png": "stickers/my-inner-world/my-worries.png",
    "innerworld_mysuperpowers.png": "stickers/my-inner-world/my-superpowers.png",
    # ---------- kids draw for kids ----------
    "kidsdraws_idea.png": "stickers/kids-draw/draw-your-own-idea.png",
    "kidsdraws_missions.png": "stickers/kids-draw/drawing-missions.png",
    "kidsdraws_surprise.png": "stickers/kids-draw/surprise-mission.png",
    "kidsdraw_silly.png": "stickers/kids-draw/silly-and-creative.png",
    "kidsdraw_add.png": "stickers/kids-draw/add-something.png",
    "kidsdraw_follow.png": "stickers/kids-draw/follow-the-clues.png",
    "kidsdraws_where.png": "stickers/kids-draw/where-does-it-go.png",
    "kidsdraw_listen.png": "stickers/kids-draw/listen-and-draw.png",
    "Kidsdraw_memory.png": "stickers/kids-draw/memory-mission.png",
    "Kiddraw_see.png": "stickers/kids-draw/see-kids-drawings.png",
    "kidsdraw_submit.png": "stickers/kids-draw/submit-my-drawing.png",
    # ---------- color & create ----------
    "ExploreColor.png": "stickers/color-and-create/explore-and-color.png",
    "ImagineCreate.png": "stickers/color-and-create/imagine-and-create.png",
    # ---------- my colorhugs ----------
    "colorhugs_mystickerbook.png": "stickers/my-colorhugs/my-sticker-book.png",
    "colorhugs_progress.png": "stickers/my-colorhugs/my-progress.png",
    "colorhugs_nextgoal.png": "stickers/my-colorhugs/next-goal.png",
    "colorhug_trophy.png": "stickers/my-colorhugs/my-trophy-shelf.png",
    # ---------- community ----------
    "communityfavorite.png": "stickers/community/community-favorite.png",
}

# Banners are full-bleed rectangles: keep their background.
KEEP_BACKGROUND = lambda rel: rel.startswith("banners/")

# The banner slot renders at this aspect with object-cover.
BANNER_ASPECT = 1568 / 644

# Some banners are die-cut compositions on a flat background rather than
# full-bleed scenes. Cropping those would clip the artwork, so they are padded
# with their own background colour to the exact banner aspect instead. Padding
# adds nothing to the image and removes nothing from it.
PAD_TO_BANNER_ASPECT = {
    "banners/parents-safety.webp",
    "banners/community.webp",
}

MAX_STICKER = 1000   # px, longest edge
MAX_BANNER = 1600


def detect_bg(arr):
    """Return 'white', 'black' or None based on the four corners."""
    h, w, _ = arr.shape
    corners = np.array([arr[1, 1], arr[1, w - 2], arr[h - 2, 1], arr[h - 2, w - 2]], float)
    m = corners.mean()
    if m < 40:
        return "black"
    if m > 240:
        return "white"
    return None


def cut_background(img: Image.Image) -> Image.Image:
    arr = np.array(img.convert("RGB"))
    kind = detect_bg(arr)
    if kind is None:
        return img.convert("RGBA")

    h, w = arr.shape[:2]
    rim = max(6, round(w * 0.016))          # thickness of the white die-cut rim
    pad = rim + 4
    fill = (0, 0, 0) if kind == "black" else (255, 255, 255)

    padded = Image.new("RGB", (w + 2 * pad, h + 2 * pad), fill)
    padded.paste(img.convert("RGB"), (pad, pad))
    a = np.array(padded)

    if kind == "black":
        flat = a.max(axis=2) < 42
    else:
        flat = a.min(axis=2) > 243

    # keep only background regions connected to the outer border
    lab, n = ndimage.label(flat)
    border_ids = set(lab[0, :]) | set(lab[-1, :]) | set(lab[:, 0]) | set(lab[:, -1])
    border_ids.discard(0)
    bg = np.isin(lab, list(border_ids))

    if kind == "white":
        # The sticker's white die-cut rim is the same colour as the studio
        # background, so it was flood-filled away. Rebuild it as a band of
        # fixed thickness measured from the artwork itself (not from the
        # canvas edge, which would leave a rectangular frame).
        core = ~bg
        band = ndimage.binary_dilation(
            core, ndimage.generate_binary_structure(2, 2), iterations=rim
        )
        bg = bg & ~band
    else:
        # push 1px into the artwork to remove the dark anti-aliasing fringe
        bg = ndimage.binary_dilation(bg, ndimage.generate_binary_structure(2, 2), iterations=1)

    alpha = np.where(bg, 0, 255).astype(np.uint8)
    out = Image.fromarray(a).convert("RGBA")
    mask = Image.fromarray(alpha).filter(ImageFilter.GaussianBlur(0.7))
    out.putalpha(mask)

    box = out.getbbox()
    return out.crop(box) if box else out


def pad_to_aspect(img: Image.Image, aspect: float) -> Image.Image:
    """Centre the image on a canvas of the target aspect, filled with its own
    background colour. Nothing is cropped, scaled or stretched."""
    rgb = img.convert("RGB")
    w, h = rgb.size
    fill = rgb.getpixel((1, 1))
    if w / h > aspect:
        new_w, new_h = w, round(w / aspect)
    else:
        new_w, new_h = round(h * aspect), h
    canvas = Image.new("RGB", (new_w, new_h), fill)
    canvas.paste(rgb, ((new_w - w) // 2, (new_h - h) // 2))
    return canvas


def downscale(img: Image.Image, longest: int) -> Image.Image:
    w, h = img.size
    if max(w, h) <= longest:
        return img
    s = longest / max(w, h)
    return img.resize((round(w * s), round(h * s)), Image.LANCZOS)


def main():
    report = []
    for src, rel in MAP.items():
        p = os.path.join(SRC, src)
        if not os.path.exists(p):
            report.append((src, rel, "MISSING SOURCE"))
            continue
        img = Image.open(p)
        if KEEP_BACKGROUND(rel):
            base = img.convert("RGB")
            if rel in PAD_TO_BANNER_ASPECT:
                base = pad_to_aspect(base, BANNER_ASPECT)
            out = downscale(base, MAX_BANNER)
            dest = os.path.join(DST, rel).replace(".png", ".webp")
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            out.save(dest, quality=86, method=6)
        else:
            out = downscale(cut_background(img), MAX_STICKER)
            dest = os.path.join(DST, rel).replace(".png", ".webp")
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            out.save(dest, quality=88, method=6, exact=False)
        kb = os.path.getsize(dest) // 1024
        report.append((src, rel, f"{out.size[0]}x{out.size[1]} {kb}KB"))

    used = set(MAP.keys())
    unused = sorted(set(os.listdir(SRC)) - used)
    for s, r, st in report:
        print(f"{s:34} -> {r:52} {st}")
    print("\nUNUSED SOURCE FILES:", unused)


if __name__ == "__main__":
    main()
