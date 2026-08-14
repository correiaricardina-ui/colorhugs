import { SECTIONS } from "@/data/sections";
import type { Activity, Section } from "@/data/types";

export function getSection(slug: string): Section | undefined {
  return SECTIONS.find((s) => s.slug === slug);
}

export function getActivity(
  sectionSlug: string,
  activitySlug: string,
): { section: Section; activity: Activity } | undefined {
  const section = getSection(sectionSlug);
  const activity = section?.activities.find((a) => a.slug === activitySlug);
  return section && activity ? { section, activity } : undefined;
}

/** Groups activities for sections that declare groups; otherwise one flat group. */
export function groupedActivities(section: Section) {
  if (!section.groups?.length) {
    return [{ group: null, activities: section.activities }];
  }
  return section.groups.map((group) => ({
    group,
    activities: section.activities.filter((a) => a.group === group.id),
  }));
}

/** Every child-facing route, used for static generation and for sitemaps. */
export function allSectionParams() {
  return SECTIONS.filter((s) => s.audience === "child").map((s) => ({
    section: s.slug,
  }));
}

export function allActivityParams() {
  return SECTIONS.filter((s) => s.audience === "child").flatMap((s) =>
    s.activities.map((a) => ({ section: s.slug, activity: a.slug })),
  );
}
