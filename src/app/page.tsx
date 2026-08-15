import Image from "next/image";
import ChildShell from "@/components/layout/ChildShell";
import SectionGrid from "@/components/sections/SectionGrid";
import StickerButton from "@/components/stickers/StickerButton";
import Link from "next/link";
import { BRAND, CHILD_SECTIONS, SECTIONS } from "@/data/sections";
import { asset } from "@/lib/site";


const parents = SECTIONS.find((s) => s.slug === "parents")!;

export default function HomePage() {
  return (
    <ChildShell>
      {/* Hero: the approved main banner does the talking. Minimal text. */}
      <section className="mx-auto w-full max-w-6xl px-4">
        <div className="overflow-hidden rounded-sticker shadow-[0_20px_44px_-26px_rgba(27,42,91,0.55)]">
          <div className="relative aspect-[1568/644] w-full bg-ch-cream">
            <Image
              src={asset(BRAND.homeBanner.src)}
              alt={BRAND.homeBanner.alt}
              fill
              sizes="(max-width: 1152px) 100vw, 1152px"
              className="object-cover"
              priority
            />
          </div>
        </div>

        <h1 className="sr-only">ColorHugs — Create, Learn, Grow, Together</h1>
        <p className="mt-6 text-center font-display text-xl font-600 text-ch-ink sm:text-2xl">
          Pick a place to start
        </p>
      </section>

      {/* The homepage grid IS the navigation. */}
      <section
        aria-label="ColorHugs areas"
        className="mx-auto mt-7 w-full max-w-6xl px-4"
      >
        <SectionGrid>
          {CHILD_SECTIONS.map((section, i) => (
            <StickerButton
              key={section.slug}
              href={`/${section.slug}`}
              label={section.title}
              caption={section.tagline}
              artwork={section.sticker}
              size="md"
              priority={i < 4}
            />
          ))}
        </SectionGrid>
      </section>

      {/* Adult entry point: same page, visibly different register. */}
      <section className="mx-auto mt-14 w-full max-w-6xl px-4">
        <div className="theme-parents flex flex-col items-center gap-5 rounded-sticker border-2 border-ch-ink/10 bg-white/70 p-6 text-center sm:flex-row sm:text-left">
          <div className="relative h-28 w-28 shrink-0">
            {parents.sticker.src ? (
              <Image
                src={asset(parents.sticker.src)}
                alt=""
                fill
                sizes="112px"
                className="object-contain"
              />
            ) : null}
          </div>
          <div className="flex-1">
            <h2 className="font-display font-700 text-ch-ink">
              For grown-ups
            </h2>
            <p className="mt-1 max-w-xl text-base text-ch-ink/70">
              Set up child profiles, manage consent and subscription, and see
              how ColorHugs protects your child&apos;s privacy.
            </p>
          </div>
          <Link
            href="/parents"
            className="tap-target inline-flex items-center gap-2 rounded-full bg-[var(--sec-accent)] px-6 py-3.5 font-display text-base font-600 text-white shadow-[0_6px_0_-2px_rgba(27,42,91,0.25)] transition hover:-translate-y-0.5 active:translate-y-0.5"
          >
            Parents &amp; Safety
          </Link>
        </div>
      </section>
    </ChildShell>
  );
}
