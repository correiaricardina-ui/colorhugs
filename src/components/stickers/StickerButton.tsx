import Image from "next/image";
import Link from "next/link";
import cn from "clsx";
import { asset } from "@/lib/site";
import type { Artwork } from "@/data/types";
import MissingArtwork from "./MissingArtwork";

type Size = "sm" | "md" | "lg";

const SIZES: Record<Size, string> = {
  sm: "max-w-[190px]",
  md: "max-w-[280px]",
  lg: "max-w-[420px]",
};

export interface StickerButtonProps {
  href: string;
  /** Child-facing label. Always rendered as text, never only inside artwork. */
  label: string;
  /** Optional second line. Keep it to a handful of words. */
  caption?: string;
  artwork: Artwork;
  size?: Size;
  /** Small badge in the corner, e.g. the Premium marker. */
  badge?: React.ReactNode;
  /** Rendered under the label, e.g. "Coming soon". */
  footnote?: string;
  className?: string;
  priority?: boolean;
}

/**
 * The one control children use to move around ColorHugs.
 *
 * Design commitments:
 *  - the whole sticker is the target, and it never drops below 64px;
 *  - artwork and text always travel together, so meaning never depends on
 *    the picture alone (or on colour alone);
 *  - artwork keeps its own aspect ratio — `object-contain`, never stretched;
 *  - feedback is a lift and a press, not a continuous animation.
 */
export default function StickerButton({
  href,
  label,
  caption,
  artwork,
  size = "md",
  badge,
  footnote,
  className,
  priority = false,
}: StickerButtonProps) {
  const ratio = artwork.ratio === "square" ? "aspect-square" : "aspect-[3/2]";

  return (
    <Link
      href={href}
      className={cn(
        "sticker-surface tap-target group flex w-full flex-col items-center gap-2 text-center",
        SIZES[size],
        className,
      )}
    >
      {badge ? (
        <span className="absolute -right-2 -top-2 z-10">{badge}</span>
      ) : null}

      <span className={cn("relative w-full", ratio)}>
        {artwork.src ? (
          <Image
            src={asset(artwork.src)}
            alt="" /* decorative: the visible label already names the target */
            fill
            sizes="(max-width: 640px) 45vw, (max-width: 1024px) 30vw, 22vw"
            className="object-contain transition-transform duration-200 ease-out group-hover:scale-[1.03]"
            priority={priority}
          />
        ) : (
          <MissingArtwork label={label} />
        )}
      </span>

      <span className="flex flex-col gap-0.5 px-1 pb-1">
        <span className="font-display text-lg font-600 leading-tight text-ch-ink sm:text-xl">
          {label}
        </span>
        {caption ? (
          <span className="text-sm leading-snug text-ch-ink/70">{caption}</span>
        ) : null}
        {footnote ? (
          <span className="mt-1 text-xs font-bold uppercase tracking-wide text-ch-ink/45">
            {footnote}
          </span>
        ) : null}
      </span>
    </Link>
  );
}
