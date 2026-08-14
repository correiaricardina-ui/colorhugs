import Link from "next/link";

/**
 * Adult-facing footer. Kept quiet and text-only so it never competes with the
 * child interface above it.
 */
export default function Footer() {
  return (
    <footer className="mt-16 border-t border-ch-ink/10 bg-white/60">
      <div className="mx-auto flex w-full max-w-6xl flex-col gap-3 px-4 py-8 text-sm text-ch-ink/70 sm:flex-row sm:items-center sm:justify-between">
        <p>© {new Date().getFullYear()} ColorHugs — Create, Learn, Grow, Together.</p>
        <nav aria-label="Footer" className="flex flex-wrap gap-x-5 gap-y-2 font-600">
          <Link href="/parents" className="hover:underline">
            Parents &amp; Safety
          </Link>
          {/* MISSING CONTENT: legal pages are not yet written or approved. */}
          <span className="text-ch-ink/35">Privacy (pending)</span>
          <span className="text-ch-ink/35">Terms (pending)</span>
        </nav>
      </div>
    </footer>
  );
}
