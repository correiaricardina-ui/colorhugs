#!/usr/bin/env bash
# Assembles the pre-launch site layout.
#
#   /            -> holding page (what visitors see)
#   /preview/    -> the real site, unlinked and not indexed
#
# One build, one deployment, one source of truth. Clearing the SITE_MODE
# variable and re-running the workflow puts the real site back at the root.
set -euo pipefail

SRC="${1:-out}"
DEST="${2:-site}"

rm -rf "$DEST"
mkdir -p "$DEST/preview"

# The real site, moved under /preview. It was built with BASE_PATH=/preview,
# so every internal link and image already points there.
cp -r "$SRC"/. "$DEST/preview/"

# The holding page and its assets at the root.
cp holding/index.html "$DEST/index.html"
cp holding/robots.txt "$DEST/robots.txt"
# No banner. The holding page shows the word in plain text, so the brand
# artwork is not published on the domain before the mark is registered
# (D-166). Restore this line when it is.
cp public/favicon.ico "$DEST/favicon.ico"

# GitHub Pages serves this for unknown paths.
cp holding/index.html "$DEST/404.html"

echo "Assembled:"
find "$DEST" -maxdepth 1 -mindepth 1 | sort
