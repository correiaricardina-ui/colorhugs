import Image from "next/image";
import Link from "next/link";
import Footer from "@/components/layout/Footer";
import { BRAND } from "@/data/sections";
import { asset } from "@/lib/site";

/**
 * Frame for adult-facing pages.
 *
 * Visually distinct from the child environment on purpose: calmer palette,
 * denser type, no sticker chrome. A parent should never be unsure which side
 * of the product they are on — and neither should a child.
 */
export default function AdultShell({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="theme-parents flex min-h-dvh flex-col bg-[#F7F9FC]">
      <header className="border-b border-ch-ink/10 bg-white">
        <nav
          aria-label="Parents area"
          className="mx-auto flex w-full max-w-4xl items-center justify-between gap-4 px-4 py-3"
        >
          <Link href="/" className="flex items-center gap-2" aria-label="ColorHugs home">
            <Image src={asset(BRAND.logo.src)} alt="" width={96} height={96} className="h-9 w-auto" />
            <span className="font-display text-base font-600 text-ch-ink">
              Parents &amp; Safety
            </span>
          </Link>
          <Link
            href="/"
            className="tap-target inline-flex items-center rounded-lg border border-ch-ink/15 px-4 py-2 text-sm font-600 text-ch-ink transition hover:bg-ch-ink/5"
          >
            Back to ColorHugs
          </Link>
        </nav>
      </header>

      <main id="main" className="flex-1">
        {children}
      </main>
      <Footer />
    </div>
  );
}
