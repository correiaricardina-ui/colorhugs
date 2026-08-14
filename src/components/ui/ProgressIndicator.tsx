import cn from "clsx";

/**
 * Effort-based progress.
 *
 * Deliberately shows steps completed and never a percentage of "how much you
 * are failing", never a streak that can be broken, and never a comparison
 * with other children.
 */
export default function ProgressIndicator({
  completed,
  total,
  label,
  className,
}: {
  completed: number;
  total: number;
  label: string;
  className?: string;
}) {
  const safeTotal = Math.max(total, 1);
  const pct = Math.min(100, Math.round((completed / safeTotal) * 100));

  return (
    <div className={cn("w-full", className)}>
      <div className="mb-1.5 flex items-baseline justify-between gap-3">
        <span className="font-display text-base font-600 text-ch-ink">
          {label}
        </span>
        <span className="text-sm font-700 text-ch-ink/60">
          {completed} of {total}
        </span>
      </div>
      <div
        role="progressbar"
        aria-valuenow={completed}
        aria-valuemin={0}
        aria-valuemax={total}
        aria-label={label}
        className="h-4 w-full overflow-hidden rounded-full bg-ch-ink/10"
      >
        <div
          className="h-full rounded-full bg-[var(--sec-accent)] transition-[width] duration-500 ease-out"
          style={{ width: `${pct}%` }}
        />
      </div>
    </div>
  );
}
