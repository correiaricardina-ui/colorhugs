#!/usr/bin/env python3
"""
Generate the spoken version of every child-facing line.

**Why files and not the browser's own voice.** Web Speech is free and needs no
files, but on several systems the synthesis happens on a server — which means a
child's text leaving her device. D-009 says her browser talks to nobody. Files
built here are served from the same origin as everything else.

**Why this is not a comfort feature.** The fine emotion words and the literacy
line were written for a child who reads, and we ask nobody's age. Without
audio, the child who cannot read gets the smaller version of the activity —
and she is the one who needs it most.

## Naming

One file per string key, derived from its path in the language file:

    feelings.families.angry  →  public/assets/audio/pt-PT/feelings.families.angry.mp3

That is the whole mechanism, and it is what makes a recorded voice a drop-in
later: put a real recording at that path and it replaces the generated one with
**no code change**. Ricardina's own voice can arrive one line at a time.

## Generating with Piper

Piper runs locally, needs no account and no key, and nothing leaves the
machine — which keeps D-009 true even behind the scenes. Chosen over a cloud
service because the generated audio is a bridge until a recorded voice exists,
and a bridge does not justify a vendor, a key and an invoice. It also means
changing a word costs nothing, so nobody starts avoiding edits to the copy
while the content is still being written.

    pip install piper-tts
    python3 -m piper.download_voices <voice-name> --data-dir voices/

Then point the script at the model for each locale:

    export COLORHUGS_VOICE_PT_PT=voices/<pt-PT voice>.onnx
    export COLORHUGS_VOICE_EN=voices/<en voice>.onnx
    python3 scripts/prepare-audio.py

`python3 -m piper.download_voices --help` lists what is available. Pick a
pt_PT voice rather than pt_BR: the localisations are different (D-101), and it
is the one place where the accent is immediately obvious to a child.

Any other engine still works through COLORHUGS_TTS, using {text} and {out}.

Without either, the script reports what is missing and writes nothing. **A
robotic placeholder voice would be worse than silence**: it looks finished, so
nobody replaces it.

The manifest it writes lists only files that actually exist, so the Listen
button appears where there is something to play and is simply absent elsewhere
— never a button that fails.
"""

import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
I18N = os.path.join(ROOT, "src", "i18n")
AUDIO = os.path.join(ROOT, "public", "assets", "audio")
MANIFEST = os.path.join(I18N, "audio-manifest.json")

LOCALES = ["en", "pt-PT"]

# Piper writes WAV. Converted to MP3 when ffmpeg is present, kept as WAV
# otherwise — the manifest records the real extension either way, so a line
# recorded later in any format drops in without touching code.
VOICE_ENV = {"en": "COLORHUGS_VOICE_EN", "pt-PT": "COLORHUGS_VOICE_PT_PT"}
EXTENSIONS = (".mp3", ".m4a", ".ogg", ".wav")

# Keys that are never spoken: interface furniture a child does not need read
# aloud, and the label of the Listen button itself.
SKIP_PREFIXES = ("ui.languageLabel", "ui.listen")


def flatten(node, prefix=""):
    """Every leaf string in the language file, keyed by its dotted path."""
    out = {}
    for key, value in node.items():
        path = f"{prefix}{key}" if not prefix else f"{prefix}.{key}"
        if isinstance(value, dict):
            out.update(flatten(value, path))
        elif isinstance(value, str):
            out[path] = value
    return out


def speakable(strings):
    return {
        key: text
        for key, text in strings.items()
        # Activity keys carry a slug with a slash; keep them but make the path
        # filename-safe.
        if not key.startswith(SKIP_PREFIXES)
    }


def stem(key):
    return key.replace("/", "__")


def existing(out_dir, key):
    """A line already voiced, in whatever format it was recorded."""
    for ext in EXTENSIONS:
        path = os.path.join(out_dir, stem(key) + ext)
        if os.path.exists(path):
            return os.path.basename(path)
    return None


def have_ffmpeg():
    return (
        subprocess.run(
            ["which", "ffmpeg"], capture_output=True, text=True
        ).returncode
        == 0
    )


def synthesise(text, model, out_dir, key, to_mp3):
    """One line, through Piper. Returns the filename written."""
    wav = os.path.join(out_dir, stem(key) + ".wav")
    subprocess.run(
        ["piper", "--model", model, "--output-file", wav],
        input=text,
        text=True,
        check=True,
        capture_output=True,
    )
    if not to_mp3:
        return os.path.basename(wav)
    mp3 = os.path.join(out_dir, stem(key) + ".mp3")
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-i", wav, "-b:a", "64k", mp3],
        check=True,
    )
    os.remove(wav)
    return os.path.basename(mp3)


def main():
    command = os.environ.get("COLORHUGS_TTS")
    to_mp3 = have_ffmpeg()
    manifest = {}
    missing = []

    for locale in LOCALES:
        path = os.path.join(I18N, f"{locale}.json")
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as f:
            lines = speakable(flatten(json.load(f)))

        model = os.environ.get(VOICE_ENV[locale])
        out_dir = os.path.join(AUDIO, locale)
        os.makedirs(out_dir, exist_ok=True)
        present = {}

        for key, text in lines.items():
            already = existing(out_dir, key)
            if already:
                # Never overwrite. A line recorded in a real voice sitting here
                # is the whole point of the naming scheme.
                present[key] = already
                continue
            if model:
                present[key] = synthesise(text, model, out_dir, key, to_mp3)
            elif command:
                target = os.path.join(out_dir, stem(key) + ".mp3")
                subprocess.run(
                    command.format(text=text.replace('"', '\\"'), out=target),
                    shell=True,
                    check=True,
                )
                present[key] = os.path.basename(target)
            else:
                missing.append(f"{locale}/{key}")

        manifest[locale] = dict(sorted(present.items()))
        print(f"  {locale:6} {len(present)}/{len(lines)} lines available")

    with open(MANIFEST, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    if missing:
        print(f"\n  {len(missing)} lines have no audio.")
        print("  Set COLORHUGS_VOICE_PT_PT and COLORHUGS_VOICE_EN to a Piper model,")
        print("  or drop recordings into public/assets/audio/<locale>/.")
        print("  The Listen button stays hidden for these — never a button that fails.")
    if not to_mp3:
        print("\n  ffmpeg not found: audio kept as WAV. Larger files, works the same.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
