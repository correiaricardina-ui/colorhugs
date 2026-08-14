import cn from "clsx";
import type { ActivityStatus } from "@/data/types";

const LABELS: Record<ActivityStatus, string> = {
  live: "Ready to play",
  "in-progress": "Almost ready",
  planned: "Coming soon",
};

/** Sets expectations honestly while activities are still being built. */
export default function StatusChip({
  status,
  className,
}: {
  status: ActivityStatus;
  className?: string;
}) {
  return (
    <span
      className={cn(
        "chip",
        status === "live"
          ? "bg-ch-mint/25 text-emerald-900"
          : "bg-ch-ink/10 text-ch-ink/70",
        className,
      )}
    >
      <span aria-hidden>{status === "live" ? "★" : "◷"}</span>
      {LABELS[status]}
    </span>
  );
}
