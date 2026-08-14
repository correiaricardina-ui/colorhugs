import type { Metadata, Viewport } from "next";
import { siteUrl } from "@/lib/site";
import "./globals.css";

export const metadata: Metadata = {
  metadataBase: new URL(siteUrl()),
  title: {
    default: "ColorHugs — Create, Learn, Grow, Together",
    template: "%s · ColorHugs",
  },
  description:
    "ColorHugs is a playful, psychology-informed platform where children learn, create and grow — with families in control.",
  // While the holding page is up, the preview build must not be indexed even
  // if someone links to it. robots.txt blocks crawling; this blocks listing.
  robots:
    process.env.NEXT_PUBLIC_SITE_MODE === "holding"
      ? { index: false, follow: false }
      : { index: true, follow: true },
  openGraph: {
    type: "website",
    siteName: "ColorHugs",
    title: "ColorHugs — Create, Learn, Grow, Together",
    description:
      "A playful, psychology-informed place where children learn, create and grow — with families in control.",
    images: [{ url: "/og.png", width: 1200, height: 630, alt: "ColorHugs" }],
  },
  twitter: { card: "summary_large_image" },
};

export const viewport: Viewport = {
  themeColor: "#FFFDF8",
  width: "device-width",
  initialScale: 1,
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    /**
     * `lang` is fixed to English for now and becomes the active locale when
     * internationalisation lands (EN, FR, ES, PT-PT, PT-BR, ZH, HI).
     *
     * Fonts are resolved from a rounded system stack and, when the licensed
     * brand faces are added, from self-hosted files declared in globals.css.
     * ColorHugs deliberately makes no third-party font requests: a child's
     * browser should not be talking to a font CDN.
     */
    <html lang="en">
      <body className="min-h-dvh">
        <a
          href="#main"
          className="sr-only rounded-full bg-ch-ink px-5 py-3 font-bold text-white focus:not-sr-only focus:absolute focus:left-4 focus:top-4 focus:z-50"
        >
          Skip to content
        </a>
        {children}
      </body>
    </html>
  );
}
