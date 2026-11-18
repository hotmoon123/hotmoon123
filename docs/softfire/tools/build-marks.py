#!/usr/bin/env python3
"""Build the SoftFire marks as real outlines, not <text> in a font.

Why this file exists
--------------------
The marks used to be `<text font-family="Inter">SF</text>` inside an SVG that
the page loads through an <img>. An SVG in an <img> is a separate document:
it cannot fetch the page's web fonts, so the browser falls back to a system
sans. Measured in Chromium, three different S shapes appeared side by side --
Inter, Arial and the fallback the SVG actually got. The mark was therefore
not the locked mark: "ordinary S+F, Inter Bold 700, -0.03em, typed never
drawn" was being rendered in whatever font the device had.

The fix is to convert the type to outlines once, from the very Inter file the
site ships. The mark is still plainly an ordinary S and an ordinary F -- but
now it is those two letters at 700, in every browser, on every device, with
no font request and no fallback.

This script regenerates all five assets from assets/inter-latin-var.woff2.
Run it if the lock ever changes:

    python3 docs/softfire/tools/build-marks.py
"""
import pathlib

from fontTools.misc.transform import Transform
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

HERE = pathlib.Path(__file__).resolve().parent.parent
SRC = HERE / "assets" / "inter-latin-var.woff2"

WEIGHT = 700          # the locked weight
TRACKING = -0.03      # the locked tracking, in em

# palette (tokens.css is the source of truth; repeated here because the marks
# are standalone files that cannot read CSS custom properties)
CHARCOAL = "#16100D"
CREAM = "#F2E9E4"
GOLD = "#F4A300"
ORANGE = "#E85D04"
EMBER = "#B33A16"

font = instantiateVariableFont(TTFont(SRC), {"wght": WEIGHT}, inplace=False)
glyphs = font.getGlyphSet()
cmap = font.getBestCmap()
UPM = font["head"].unitsPerEm


def _round(path_d, places=2):
    """fontTools emits 14 decimal places. Two is invisible and a tenth the size."""
    import re
    def fix(m):
        return f"{float(m.group(0)):.{places}f}".rstrip("0").rstrip(".")
    return re.sub(r"-?\d+\.\d+", fix, path_d)


def outlines(text, size):
    """Return (list_of_path_d, total_ink_width) for `text` set at `size` px.

    Y is flipped so the baseline sits at y=0 and the letters rise to -cap,
    which is the convention the existing marks used (baseline at y=51.5 in an
    80px box with a 34px font).
    """
    scale = size / UPM
    track = TRACKING * size
    paths, x = [], 0.0
    for i, ch in enumerate(text):
        gname = cmap[ord(ch)]
        pen = SVGPathPen(glyphs)
        glyphs[gname].draw(TransformPen(pen, Transform(scale, 0, 0, -scale, x, 0)))
        paths.append(_round(pen.getCommands()))
        x += font["hmtx"][gname][0] * scale
        if i < len(text) - 1:
            x += track
    return paths, x - (track if text else 0)


def svg(view_box, body, title):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view_box}" '
        f'role="img" aria-label="SoftFire">\n'
        f"  <title>{title}</title>\n{body}</svg>\n"
    )


def tile_mark(box, radius, tile_fill, size, colours, title,
              font_size_ratio=0.425, draw_tile=True):
    """A rounded tile with SF centred in it."""
    px = size
    paths, width = outlines("SF", px)
    cap = font["OS/2"].sCapHeight * px / UPM
    # optically centre: centre the CAP height, not the em box
    baseline = box / 2 + cap / 2
    left = (box - width) / 2
    fill = colours if isinstance(colours, str) else colours
    rows = []
    for i, d in enumerate(paths):
        col = fill if isinstance(fill, str) else fill[i]
        rows.append(
            f'  <path transform="translate({left:.2f} {baseline:.2f})" '
            f'fill="{col}" d="{d}"/>'
        )
    body = ""
    if draw_tile and tile_fill != "none":
        body += f'  <rect width="{box}" height="{box}" rx="{radius}" fill="{tile_fill}"/>\n'
    body += "\n".join(rows) + "\n"
    return svg(f"0 0 {box} {box}", body, title)


def write(name, content):
    path = HERE / "assets" / name
    path.write_text(content, encoding="utf-8")
    print(f"  {name:<22} {len(content):>6} bytes")


print("Building marks from Inter at weight 700, tracking -0.03em")

# Tier A — gradient on charcoal. The only place a gradient is allowed in the
# mark. Worst stop against charcoal measures 3.17 (see the README); that is
# why Tier A is reserved for 64px cap and above, where 3:1 is the threshold.
# Tier A has no tile, so its box is sized to the ink plus exactly 0.5x cap
# clear space on every side — the clear-space rule the mark is specified with.
A_SIZE = 34
a_paths, a_w = outlines("SF", A_SIZE)
a_cap = font["OS/2"].sCapHeight * A_SIZE / UPM
CLEAR = a_cap * 0.5                      # 0.5x cap
A_W = a_w + CLEAR * 2
A_H = a_cap + CLEAR * 2
a_left = CLEAR
a_base = CLEAR + a_cap
body = (
    '  <defs>\n'
    f'    <linearGradient id="fireDark" gradientUnits="userSpaceOnUse" '
    f'x1="{a_left:.2f}" y1="0" x2="{a_left + a_w:.2f}" y2="0">\n'
    f'      <stop offset="0" stop-color="{EMBER}"/>\n'
    f'      <stop offset="0.55" stop-color="{ORANGE}"/>\n'
    f'      <stop offset="1" stop-color="{GOLD}"/>\n'
    '    </linearGradient>\n'
    '  </defs>\n'
    f'  <path transform="translate({a_left:.2f} {a_base:.2f})" fill="url(#fireDark)" d="{a_paths[0]}"/>\n'
    f'  <path transform="translate({a_left:.2f} {a_base:.2f})" fill="url(#fireDark)" d="{a_paths[1]}"/>\n'
)
write("logo-a-dark.svg", svg(f"0 0 {A_W:.2f} {A_H:.2f}", body,
      "SoftFire — Tier A: the gradient, on charcoal, 64px cap and above"))

# Tiers B, C, the crawler tile, and the favicon
write("logo-b.svg", tile_mark(80, 5, CHARCOAL, 34, [GOLD, ORANGE],
      "SoftFire — Tier B: two colour, for screen at 24px and above"))
write("logo-c.svg", tile_mark(80, 5, CHARCOAL, 34, CREAM,
      "SoftFire — Tier C: one colour, for print and every use under 24px"))
write("sf-mark.svg", tile_mark(64, 0, "none", 27, CREAM,
      "SoftFire mark, transparent — the tile that crawls behind the page",
      draw_tile=False))
write("favicon.svg", tile_mark(32, 5, CHARCOAL, 15, GOLD,
      "SoftFire"))

# a light-on-cream tile, for use on the cream field
write("logo-d-light.svg", tile_mark(80, 5, CREAM, 34, CHARCOAL,
      "SoftFire — Tier D: charcoal on cream, for light surfaces"))

print("Done. Every mark is now outlines: no font request, no fallback.")
