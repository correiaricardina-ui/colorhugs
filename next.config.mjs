/** @type {import('next').NextConfig} */

/**
 * Two deployment modes:
 *
 *  - default: a normal Next.js server build (Vercel, Netlify, a Node host).
 *  - `EXPORT=1 npm run build`: a fully static export in `out/`, suitable for
 *    GitHub Pages. Set `BASE_PATH=/repo-name` when the site is served from a
 *    project subpath rather than a custom domain.
 *
 * Static export is a build-time switch, not a rewrite, so the same code ships
 * either way and the choice stays reversible.
 */
const isExport = process.env.EXPORT === "1";
const basePath = process.env.BASE_PATH ?? "";

const nextConfig = {
  reactStrictMode: true,
  ...(isExport ? { output: "export", trailingSlash: true } : {}),
  ...(basePath ? { basePath, assetPrefix: basePath } : {}),
  images: {
    // Artwork is pre-optimised (WebP, sized, transparent) by
    // scripts/prepare-assets.py, so no image-optimisation server is needed.
    unoptimized: true,
  },
  // Conservative baseline headers. Review before launch alongside the privacy
  // and consent work — a child-facing product should ship a CSP too.
  async headers() {
    if (isExport) return [];
    return [
      {
        source: "/:path*",
        headers: [
          { key: "X-Content-Type-Options", value: "nosniff" },
          { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
          { key: "X-Frame-Options", value: "SAMEORIGIN" },
          {
            key: "Permissions-Policy",
            value: "camera=(), microphone=(), geolocation=(), interest-cohort=()",
          },
        ],
      },
    ];
  },
};

export default nextConfig;
