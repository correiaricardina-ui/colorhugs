import cn from "clsx";

/**
 * Honest placeholder for approved-but-not-yet-supplied artwork.
 *
 * ColorHugs never substitutes an invented graphic for a missing brand asset,
 * so this renders a neutral, clearly temporary tile instead. Every occurrence
 * is listed in docs/ASSET_MAP.md.
 */
export default function MissingArtwork({
  label,
  className,
}: {
  label: string;
  className?: string;
}) {
  return (
    <span
      className={cn(
        "absolute inset-0 flex flex-col items-center justify-center gap-2 rounded-[1.25rem] border-4 border-dashed border-ch-ink/15 bg-white/60 p-4 text-center",
        className,
      )}
    >
      <span aria-hidden className="text-3xl opacity-40">
        ✎
      </span>
      <span className="font-display text-base leading-tight text-ch-ink/60">
        {label}
      </span>
      <span className="text-[0.65rem] font-bold uppercase tracking-widest text-ch-ink/35">
        Artwork pending
      </span>
    </span>
  );
}
