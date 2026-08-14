import Image from "next/image";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import ChildShell from "@/components/layout/ChildShell";
import BackButton from "@/components/navigation/BackButton";
import HomeButton from "@/components/navigation/HomeButton";
import ComingSoon from "@/components/ui/ComingSoon";
import PlanBadge from "@/components/stickers/PlanBadge";
import MissingArtwork from "@/components/stickers/MissingArtwork";
import { allActivityParams, getActivity } from "@/lib/sections";
import { asset } from "@/lib/site";

/**
 * Activity placeholder.
 *
 * Phase 1 establishes the route, the chrome and the way back. The activity
 * itself arrives in a later phase, per the agreed development strategy.
 */

type Params = { params: { section: string; activity: string } };

export function generateStaticParams() {
  return allActivityParams();
}

export function generateMetadata({ params }: Params): Metadata {
  const found = getActivity(params.section, params.activity);
  return found
    ? { title: `${found.activity.title} · ${found.section.title}` }
    : { title: "Not found" };
}

export default function ActivityPage({ params }: Params) {
  const found = getActivity(params.section, params.activity);
  if (!found) notFound();
  const { section, activity } = found;

  return (
    <ChildShell themeClassName={section.theme.className}>
      <div className="mx-auto w-full max-w-4xl px-4 pt-4">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <BackButton href={`/${section.slug}`} label={section.title} />
          <HomeButton compact />
        </div>

        <article className="mt-8 text-center">
          <div className="relative mx-auto aspect-[3/2] w-full max-w-lg">
            {activity.sticker.src ? (
              <Image
                src={asset(activity.sticker.src)}
                alt={activity.sticker.alt}
                fill
                sizes="(max-width: 640px) 90vw, 512px"
                className="object-contain"
                priority
              />
            ) : (
              <MissingArtwork label={activity.title} />
            )}
          </div>

          <h1 className="mt-5 font-display font-700 text-ch-ink">
            {activity.title}
          </h1>
          <p className="mt-1 text-lg text-ch-ink/70">{activity.tagline}</p>

          {/*
            The only plan message a child ever sees, and only where an activity
            genuinely cannot be opened. It points at a grown-up rather than at a
            price, and there is no purchase button on any child-facing screen.
          */}
          {activity.access.kind === "premium" ? (
            <p className="mt-4 inline-flex items-center gap-2">
              <PlanBadge plan="premium" size={44} />
              <span className="font-display font-600 text-ch-ink/70">
                Ask a grown-up to unlock this one
              </span>
            </p>
          ) : null}

          <div className="mt-8">
            <ComingSoon title={activity.title} />
          </div>
        </article>

        <div className="mt-10 flex flex-wrap justify-center gap-3">
          <BackButton href={`/${section.slug}`} label={section.title} />
          <HomeButton />
        </div>
      </div>
    </ChildShell>
  );
}
