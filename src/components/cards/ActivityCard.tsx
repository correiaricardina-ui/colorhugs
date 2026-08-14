import StickerButton from "@/components/stickers/StickerButton";
import PlanBadge from "@/components/stickers/PlanBadge";
import type { Activity } from "@/data/types";

const STATUS_FOOTNOTE: Record<Activity["status"], string | undefined> = {
  live: undefined,
  "in-progress": "Almost ready",
  planned: "Coming soon",
};

/**
 * An activity presented as a sticker. Wide artwork gets a wider tile so the
 * original composition is never squeezed into a square.
 *
 * Only an activity that cannot be sampled at all carries a Premium badge.
 * Sampled activities look exactly like free ones, because to a child they
 * behave exactly like free ones: they open, and they play.
 */
export default function ActivityCard({
  activity,
  sectionSlug,
}: {
  activity: Activity;
  sectionSlug: string;
}) {
  return (
    <StickerButton
      href={`/${sectionSlug}/${activity.slug}`}
      label={activity.title}
      caption={activity.tagline}
      artwork={activity.sticker}
      size={activity.sticker.ratio === "wide" ? "lg" : "md"}
      badge={
        activity.access.kind === "premium" ? <PlanBadge plan="premium" /> : null
      }
      footnote={STATUS_FOOTNOTE[activity.status]}
    />
  );
}
