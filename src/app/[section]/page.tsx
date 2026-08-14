import { notFound } from "next/navigation";
import type { Metadata } from "next";
import ChildShell from "@/components/layout/ChildShell";
import SectionBanner from "@/components/sections/SectionBanner";
import SectionGrid from "@/components/sections/SectionGrid";
import ActivityCard from "@/components/cards/ActivityCard";
import HomeButton from "@/components/navigation/HomeButton";
import { allSectionParams, getSection, groupedActivities } from "@/lib/sections";

/**
 * One template renders every section. Adding a section means adding data,
 * not building a page.
 */

type Params = { params: { section: string } };

export function generateStaticParams() {
  return allSectionParams();
}

export function generateMetadata({ params }: Params): Metadata {
  const section = getSection(params.section);
  return section
    ? { title: section.title, description: section.purpose }
    : { title: "Not found" };
}

export default function SectionPage({ params }: Params) {
  const section = getSection(params.section);
  if (!section || section.audience !== "child") notFound();

  const groups = groupedActivities(section);

  return (
    <ChildShell themeClassName={section.theme.className}>
      <SectionBanner
        artwork={section.banner}
        title={section.title}
        tagline={section.tagline}
        priority
      />

      <div className="mx-auto mt-8 w-full max-w-6xl space-y-12 px-4">
        {groups.map(({ group, activities }) => (
          <section
            key={group?.id ?? "all"}
            aria-labelledby={group ? `group-${group.id}` : undefined}
          >
            {group ? (
              <h2
                id={`group-${group.id}`}
                className="mb-5 text-center font-display font-700 text-ch-ink"
              >
                {group.title}
              </h2>
            ) : null}

            <SectionGrid
              columns={
                activities.every((a) => a.sticker.ratio === "wide")
                  ? "wide"
                  : "auto"
              }
            >
              {activities.map((activity) => (
                <ActivityCard
                  key={activity.slug}
                  activity={activity}
                  sectionSlug={section.slug}
                />
              ))}
            </SectionGrid>
          </section>
        ))}

        {section.activities.length === 0 ? (
          <p className="text-center text-lg text-ch-ink/60">
            Activities for this area are on the way.
          </p>
        ) : null}

        <div className="flex justify-center pt-2">
          <HomeButton />
        </div>
      </div>
    </ChildShell>
  );
}
