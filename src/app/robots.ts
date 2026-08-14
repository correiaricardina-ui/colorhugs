import type { MetadataRoute } from "next";
import { siteUrl } from "@/lib/site";

/**
 * Public informational pages may be indexed. Anything that will later sit
 * behind a child profile must be disallowed here as it is built.
 */
export default function robots(): MetadataRoute.Robots {
  return {
    rules: {
      userAgent: "*",
      allow: "/",
      // Reserved for authenticated surfaces added in later phases.
      disallow: ["/api/", "/account/", "/profile/"],
    },
    sitemap: `${siteUrl()}/sitemap.xml`,
  };
}
