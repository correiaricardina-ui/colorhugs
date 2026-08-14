import Image from "next/image";
import cn from "clsx";
import { asset } from "@/lib/site";
import MissingArtwork from "@/components/stickers/MissingArtwork";
import type { Artwork } from "@/data/types";

/**
 * Full-width approved banner artwork. The heading is real text sitting
 * beneath it, so the page still makes sense with images off, at any zoom
 * level, and to a screen reader.
 */
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
  return (
    <header className={cn("mx-auto w-full max-w-6xl px-4 pt-4", className)}>
      <div className="relative overflow-hidden rounded-sticker shadow-[0_18px_40px_-24px_rgba(27,42,91,0.5)]">
        <div className="relative aspect-[1568/644] w-full bg-ch-cream">
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
