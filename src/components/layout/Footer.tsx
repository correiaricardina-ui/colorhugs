import Image from "next/image";
import Link from "next/link";
import LanguageSwitcher from "@/components/layout/LanguageSwitcher";
import { CREDIT } from "@/data/credits";

/**
 * Adult-facing footer. Kept quiet and text-only so it never competes with the
 * child interface above it — the authorship credit included: it belongs to
 * grown-ups, and a child has no use for it.
 */
export default function Footer() {
  return (
    <footer className="mt-16 border-t border-ch-ink/10 bg-white/60">
      <div className="mx-auto flex w-full max-w-6xl flex-col gap-3 px-4 py-8 text-sm text-ch-ink/70 sm:flex-row sm:items-center sm:justify-between">
        <div className="space-y-1">
          <p>© {new Date().getFullYear()} ColorHugs — Create, Learn, Grow, Together.</p>
          <p>
            {CREDIT.short.replace(` ${CREDIT.name}`, "")}{" "}
            <a
              href={CREDIT.url}
              target="_blank"
              rel="noopener noreferrer"
              className="font-600 underline decoration-ch-ink/25 underline-offset-2 hover:decoration-ch-ink/60"
            >
              {CREDIT.name}
            </a>
            <span className="text-ch-ink/45"> · {CREDIT.role}</span>
          </p>
        </div>
        <div className="flex flex-col gap-3 sm:items-end">
          <LanguageSwitcher />
        <nav aria-label="Footer" className="flex flex-wrap gap-x-5 gap-y-2 font-600">
          <Link href="/parents" className="hover:underline">
            Parents &amp; Safety
          </Link>
          {/* MISSING CONTENT: legal pages are not yet written or approved. */}
          <span className="text-ch-ink/35">Privacy (pending)</span>
          <span className="text-ch-ink/35">Terms (pending)</span>
        </nav>
        </div>
      </div>
    </footer>
  );
}
