import type { ComponentType } from "react";
import dynamic from "next/dynamic";

/**
 * Built activities, keyed `section/activity`.
 *
 * Anything absent renders the honest `ComingSoon` placeholder instead (D-010).
 * Adding a built activity is one line here plus its component — the same
 * "content is data" discipline as D-002.
 */
export const ACTIVITIES: Record<string, ComponentType> = {
  "my-inner-world/how-do-i-feel": dynamic(
    () => import("@/components/activities/HowDoIFeel"),
  ),
};

export function activityComponent(section: string, activity: string) {
  return ACTIVITIES[`${section}/${activity}`] ?? null;
}
