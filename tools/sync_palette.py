"""Copy a color-picker palette file into _data/palette.json for the guide.

Usage: python tools/sync_palette.py ../color-picker/ren.json

Adds a text colour ("ink") to every swatch so labels stay readable, and keys
the fixed swatch groups by a slug of their title (e.g. "contrasting-order").
"""
import json
import pathlib
import re
import sys

DARK_INK = "#191919"
LIGHT_INK = "#FFFFFF"


def luminance(hex_colour):
    def channel(c):
        c = int(c, 16) / 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    h = hex_colour.lstrip("#")
    r, g, b = (channel(h[i:i + 2]) for i in (0, 2, 4))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    hi, lo = sorted((luminance(a), luminance(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def ink(hex_colour):
    dark, light = contrast(hex_colour, DARK_INK), contrast(hex_colour, LIGHT_INK)
    return DARK_INK if dark >= light else LIGHT_INK


def swatch(name, value):
    return {"name": name, "hex": value.upper(), "ink": ink(value)}


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def main(src):
    palette = json.loads(pathlib.Path(src).read_text(encoding="utf-8"))
    colours = palette["colours"]
    ramps = palette["ramps"]

    out = {"groups": {}, "ramps": {}, "centre": None}
    for section in palette["sections"]:
        for group in section.get("groups", []):
            out["groups"][slug(group["title"])] = [swatch(n, colours[n]) for n in group["colours"]]
        if section.get("type") == "diverging":
            centre = section["centre"][0]
            out["centre"] = swatch(centre["name"], centre["value"])

    for name, steps in ramps["colours"].items():
        out["ramps"][name] = [
            dict(swatch(f"{name} {step}", value), step=step)
            for step, value in zip(ramps["steps"], steps)
        ]

    dest = pathlib.Path(__file__).resolve().parent.parent / "_data" / "palette.json"
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {dest}")


if __name__ == "__main__":
    main(sys.argv[1])
