import cn from "clsx";

/**
 * A collected reward. Earned badges are permanent — ColorHugs never removes
 * an achievement a child has already earned.
 */
export default function RewardBadge({
  title,
  earned = false,
  className,
}: {
  title: string;
  earned?: boolean;
  className?: string;
}) {
  return (
    <span
      className={cn(
        "inline-flex flex-col items-center gap-1.5 rounded-2xl px-3 py-3 text-center",
        earned ? "bg-white shadow-[0_6px_0_-2px_rgba(27,42,91,0.10)]" : "bg-white/50",
        className,
      )}
    >
      <span
        aria-hidden
        className={cn(
          "flex h-14 w-14 items-center justify-center rounded-full text-2xl",
          earned
            ? "bg-[var(--sec-accent)] text-white"
            : "border-4 border-dashed border-ch-ink/15 text-ch-ink/25",
        )}
      >
        ★
      </span>
      <span className="font-display text-sm font-600 text-ch-ink/80">
        {title}
      </span>
      <span className="sr-only">
        {earned ? "Earned" : "Not collected yet"}
      </span>
    </span>
  );
}
