import type { MetadataRoute } from "next";
import { SECTIONS } from "@/data/sections";
import { siteUrl } from "@/lib/site";

export default function sitemap(): MetadataRoute.Sitemap {
  const base = siteUrl();
  const now = new Date();

  const pages = [
    "",
    ...SECTIONS.map((s) => `/${s.slug}`),
    ...SECTIONS.filter((s) => s.audience === "child").flatMap((s) =>
      s.activities.map((a) => `/${s.slug}/${a.slug}`),
    ),
  ];

  return pages.map((path) => ({
    url: `${base}${path}`,
    lastModified: now,
    changeFrequency: "monthly" as const,
    priority: path === "" ? 1 : path.split("/").length === 2 ? 0.8 : 0.6,
  }));
}
