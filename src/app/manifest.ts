import type { MetadataRoute } from "next";
import { withBasePath } from "@/lib/site";

/**
 * Web app manifest.
 *
 * `display: "standalone"` deliberately omitted for now: an installed,
 * chrome-less app removes the browser's own back button, and the child
 * navigation model has not been tested without it.
 */
export default function manifest(): MetadataRoute.Manifest {
  return {
    name: "ColorHugs — Create, Learn, Grow, Together",
    short_name: "ColorHugs",
    description:
      "A playful, psychology-informed place where children learn, create and grow — with families in control.",
    start_url: withBasePath("/"),
    display: "browser",
    background_color: "#FFFDF8",
    theme_color: "#FFFDF8",
    icons: [
      { src: withBasePath("/icons/icon-192.png"), sizes: "192x192", type: "image/png" },
      { src: withBasePath("/icons/icon-512.png"), sizes: "512x512", type: "image/png" },
      {
        src: withBasePath("/icons/icon-maskable-512.png"),
        sizes: "512x512",
        type: "image/png",
        purpose: "maskable",
      },
    ],
  };
}
