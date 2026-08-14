# ColorHugs — Asset Map

Every supplied artwork file and where it now lives. Nothing was redrawn,
recoloured or replaced. Filenames were normalised to kebab-case and grouped by
section so new activities drop in without touching the interface.

## Processing applied

`scripts/prepare-assets.py` does three things, and nothing else:

1. **Background removal.** The supplied files are flat RGB with either a white
   or a black studio background. Sticker UI needs transparency, so the
   background is flood-filled from the borders. For white-background files the
   sticker's white die-cut rim is the same colour as the background, so the rim
   is rebuilt as a fixed-width band measured from the artwork itself.
2. **Trim** to the artwork bounding box, so no sticker carries dead space.
3. **Resize and convert to WebP** (stickers ≤1000px, banners ≤1600px). Total
   asset weight dropped from ~9 MB to ~7.6 MB with alpha added.

Originals are untouched. Re-run the script to regenerate `/public/assets`.

## Branding

| Source | Destination |
| --- | --- |
| `ColorHugs_Principal.png` | `branding/colorhugs-logo.webp` |
| `Faixa_principal.png` | `banners/home.webp` |

## Sections

| Section | Sticker | Banner |
| --- | --- | --- |
| Learning Hub | `Learning_Hub.png` | `faixa_larning_hub.png` |
| Brain Gym | `Brain_Gym.png` | `Faixa_Brain_Gym.png` |
| My Inner World | `My_Inner_Word.png` | `Faixa_My_Inner_World.png` |
| Kids Draw for Kids | `Kids_Draw_for_Kids.png` | `Faixa_Kids_Draw_for_Kids.png` |
| Color & Create | `Color_and_Create.png` | `faixa_color_and_create.png` |
| My ColorHugs | `My_ColorHugs.png` | `Faixa_My_ColorHugs.png` |
| Community | `Community.png` | `Faixa_community.png` |
| Parents & Safety | `ParentSafety.png` | `Faixa_parents.png` |

## Activities

| Section | Activity | Source |
| --- | --- | --- |
| Learning Hub | Word Explorer | `learninghub_word.png` |
| Learning Hub | Number Adventure | `learninghub_number.png` |
| Learning Hub | Story Time | `learninghub_storytime.png` |
| Learning Hub | School Challenge | `learninghub_schoolchallenge.png` |
| Brain Gym | Focus Mission | `braingymn_focusmission.png` |
| Brain Gym | Memory Challenge | `braingym_memory.png` |
| Brain Gym | Think & Solve | `braingymn_thinksolve.png` |
| Brain Gym | Speedy Brain | `braingym_speddybrain.png` |
| My Inner World | How Do I Feel? | `innerworld_howdoifeel.png` |
| My Inner World | Calm My Body | `innerworld_calmmybody.png` |
| My Inner World | My Worries | `innerwordl_myworries.png` |
| My Inner World | My Superpowers | `innerworld_mysuperpowers.png` |
| Kids Draw | Draw Your Own Idea | `kidsdraws_idea.png` |
| Kids Draw | Drawing Missions | `kidsdraws_missions.png` |
| Kids Draw | Silly & Creative (L1) | `kidsdraw_silly.png` |
| Kids Draw | Add Something (L2) | `kidsdraw_add.png` |
| Kids Draw | Follow the Clues (L3) | `kidsdraw_follow.png` |
| Kids Draw | Where Does It Go? (L4) | `kidsdraws_where.png` |
| Kids Draw | Listen & Draw (L5) | `kidsdraw_listen.png` |
| Kids Draw | Memory Mission (L6) | `Kidsdraw_memory.png` |
| Kids Draw | Surprise Mission | `kidsdraws_surprise.png` |
| Kids Draw | See Kids' Drawings | `Kiddraw_see.png` |
| Kids Draw | Submit My Drawing | `kidsdraw_submit.png` |
| Color & Create | Explore & Color | `ExploreColor.png` |
| Color & Create | Imagine & Create (Premium) | `ImagineCreate.png` |
| My ColorHugs | My Sticker Book | `colorhugs_mystickerbook.png` |
| My ColorHugs | My Progress | `colorhugs_progress.png` |
| My ColorHugs | Next Goal | `colorhugs_nextgoal.png` |
| My ColorHugs | My Trophy Shelf | `colorhug_trophy.png` |
| Community | Community Favorite | `communityfavorite.png` |

## Plan badges

`Free.png` → `stickers/plans/free.webp` · `Premium.png` → `stickers/plans/premium.webp`
`Faixa_Free.png` → `banners/free.webp` · `Faixa_premium.png` → `banners/premium.webp`

---

## Complete as of 2026-08-14

Every section, every banner and every activity now has its approved artwork.
No `MissingArtwork` placeholder appears anywhere in a build. The fallback stays
in the components on purpose, so any future gap is signposted honestly rather
than filled with an invented graphic.

Supplied and integrated on 2026-08-14: Community sticker and banner,
Parents & Safety banner, Brain Gym / Memory Challenge, My ColorHugs / My Progress.

## Still outstanding

1. **Brand typefaces.** The interface currently falls back to a rounded system
   stack. Fredoka and Nunito (both SIL Open Font License) are the closest
   matches to the lettering in the artwork; once chosen, they should be
   self-hosted in `/public/fonts` so a child's browser makes no third-party
   font request.

## Retired source file

`innerword_howdoifeel.png` — a near-duplicate on a white background. The
black-background `innerworld_howdoifeel.png` (1536×1024) is confirmed as the
approved master and is the one in the build.

---

## Derived assets (generated, not drawn)

| File | Derived from | How |
| --- | --- | --- |
| `branding/colorhugs-mark.png` | approved logo | crop of the smiley + circular mask |
| `public/favicon.ico` (16–64px) | mark | scale |
| `src/app/icon.png`, `src/app/apple-icon.png` | mark | scale on cream |
| `public/icons/icon-192/512/maskable-512.png` | mark | scale on cream, extra padding for maskable |
| `public/og.png` (1200×630) | `banners/home.webp` | centre crop |

The mark is used only where the full lockup does not fit: below roughly 48px
the lockup is unreadable. **This needs approval — see Q-007 in the decision
log.** A commissioned small-size mark would replace it cleanly, since every
icon is regenerated from a single source.
