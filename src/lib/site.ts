/**
 * Absolute site URL, used for sitemap, robots and social metadata.
 * Set NEXT_PUBLIC_SITE_URL per environment; never hard-code a domain.
 */
export function siteUrl(): string {
  return (
    process.env.NEXT_PUBLIC_SITE_URL?.replace(/\/$/, "") ??
    "http://localhost:3000"
  );
}

/**
 * Path prefix when the site is served from a subpath — a GitHub project page
 * at /colorhugs, for example.
 *
 * Next applies `basePath` to <Link> automatically, but **not** to <Image>
 * when `images.unoptimized` is on: the default loader returns the src
 * untouched, so every sticker and banner would 404 under a subpath. Artwork
 * paths therefore go through `asset()`, and plain strings such as manifest
 * icon paths through `withBasePath()`.
 */
export function basePath(): string {
  return process.env.NEXT_PUBLIC_BASE_PATH ?? "";
}

export function withBasePath(path: string): string {
  return `${basePath()}${path}`;
}

/** Prefixes an /assets path so <Image> resolves under any base path. */
export const asset = withBasePath;
