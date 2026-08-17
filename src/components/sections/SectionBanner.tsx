import Image from "next/image";
import cn from "clsx";
import { asset } from "@/lib/site";
import MissingArtwork from "@/components/stickers/MissingArtwork";
import type { Artwork } from "@/data/types";
import BANNER_SIZES from "@/data/banner-sizes.json";

/**
 * Full-width approved banner artwork. The heading is real text sitting
 * beneath it, so the page still makes sense with images off, at any zoom
 * level, and to a screen reader.
 *
 * **The frame takes the artwork's shape, never the other way round** (D-204).
 * A fixed 1568x644 frame was cutting eighteen per cent off the top and bottom
 * of the three banners that are 1568x784 — which on My Inner World removed the
 * top of the heart. Cropping approved artwork to fit a frame is redrawing it by
 * another means (rule 6). Sizes are measured by
 * `scripts/measure-banners.py`, not typed.
 */

const SIZES = BANNER_SIZES as Record<string, { w: number; h: number }>;

/** The shape most banners are, used only when a file has not been measured. */
const FALLBACK_RATIO = 1568 / 644;
export default function SectionBanner({
  artwork,
  title,
  tagline,
  priority = false,
  className,
}: {
  artwork: Artwork;
  title: string;
  tagline?: string;
  priority?: boolean;
  className?: string;
}) {
  const measured = artwork.src ? SIZES[artwork.src] : undefined;
  const ratio = measured ? measured.w / measured.h : FALLBACK_RATIO;

  return (
    <header className={cn("mx-auto w-full max-w-6xl px-4 pt-4", className)}>
      <div className="relative overflow-hidden rounded-sticker shadow-[0_18px_40px_-24px_rgba(27,42,91,0.5)]">
        <div
          className="relative w-full bg-ch-cream"
          style={{ aspectRatio: `${ratio}` }}
        >
          {artwork.src ? (
            <Image
              src={asset(artwork.src)}
              alt={artwork.alt}
              fill
              sizes="(max-width: 1152px) 100vw, 1152px"
              className="object-cover object-center"
              priority={priority}
            />
          ) : (
            <MissingArtwork label={`${title} banner`} className="rounded-none" />
          )}
        </div>
      </div>

      <div className="mt-5 text-center">
        <h1 className="font-display font-700 leading-tight text-ch-ink">
          {title}
        </h1>
        {tagline ? (
          <p className="mt-1 text-base font-600 text-ch-ink/60 sm:text-lg">
            {tagline}
          </p>
        ) : null}
      </div>
    </header>
  );
}
