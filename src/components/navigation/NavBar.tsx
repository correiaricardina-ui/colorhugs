import Image from "next/image";
import Link from "next/link";
import { BRAND } from "@/data/sections";
import { asset } from "@/lib/site";

/**
 * Deliberately minimal: the logo, and nothing else.
 *
 * No hamburger, no dropdown, no hidden gesture — the homepage grid is the
 * navigation. The adult entry point deliberately does not live up here: a
 * button in the child's top bar invites taps that lead somewhere a child has
 * no use for. Parents reach their area from the strip at the foot of the
 * homepage, and from the footer link on every page.
 */
export default function NavBar() {
  return (
    <nav
      aria-label="Main"
      className="mx-auto flex w-full max-w-6xl items-center px-4 py-3"
    >
      <Link
        href="/"
        className="flex items-center gap-2 rounded-2xl px-1 py-1"
        aria-label="ColorHugs home"
      >
        <Image
          src={asset(BRAND.logo.src)}
          alt=""
          width={132}
          height={132}
          className="h-11 w-auto sm:h-14"
          priority
        />
        <span className="sr-only">ColorHugs</span>
      </Link>
    </nav>
  );
}
