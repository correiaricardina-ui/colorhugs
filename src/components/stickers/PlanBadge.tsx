import Image from "next/image";
import { PLAN_BADGES } from "@/data/sections";
import { asset } from "@/lib/site";
import type { Plan } from "@/data/types";

/**
 * Uses the approved Free / Premium badge artwork. Text is included for
 * screen readers so the plan is never signalled by the image alone.
 */
export default function PlanBadge({
  plan,
  size = 56,
}: {
  plan: Plan;
  size?: number;
}) {
  const badge = PLAN_BADGES[plan];
  return (
    <span className="inline-flex items-center">
      <Image
        src={asset(badge.src)}
        alt={plan === "premium" ? "Premium activity" : "Free activity"}
        width={size}
        height={size}
        className="drop-shadow-[0_4px_6px_rgba(27,42,91,0.25)]"
      />
    </span>
  );
}
