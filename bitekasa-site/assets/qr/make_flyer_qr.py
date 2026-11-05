#!/usr/bin/env python3
"""Compose a corrected QR flyer: original artwork untouched, QR moved to a clean footer.

The earlier `../bitekasa-offer-flyer-website-qr.png` placed the QR over the Premium
card, hiding part of "70 PIECES + 1 LITRE COKE". This build keeps the original
`../bitekasa-offer-flyer.png` exactly as-is and appends a footer band, so nothing
on the artwork is covered.
"""

from pathlib import Path

import qrcode
from PIL import Image, ImageDraw, ImageFont

URL = "https://hotmoon123.github.io/hotmoon123/"
ASSETS = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent

RED = (167, 25, 32)
CREAM = (247, 238, 219)
INK = (26, 26, 26)
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def qr_image(side_with_padding=228, pad=16):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q, box_size=10, border=4)
    qr.add_data(URL)
    qr.make(fit=True)
    core = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    core = core.resize((side_with_padding - pad * 2, side_with_padding - pad * 2), resample=0)
    panel = Image.new("RGB", (side_with_padding, side_with_padding), "white")
    panel.paste(core, (pad, pad))
    return panel


def main():
    base = Image.open(ASSETS / "bitekasa-offer-flyer.png").convert("RGB")
    W, H = base.size
    band = 280
    canvas = Image.new("RGB", (W, H + band), CREAM)
    canvas.paste(base, (0, 0))

    draw = ImageDraw.Draw(canvas)
    draw.rectangle([0, H, W, H + 5], fill=RED)

    panel = qr_image()
    canvas.paste(panel, (52, H + 26))

    title = ImageFont.truetype(BOLD, 40)
    body = ImageFont.truetype(REG, 25)
    draw.text((52 + panel.width + 40, H + 56), "SCAN TO VIEW", font=title, fill=RED)
    draw.text(
        (52 + panel.width + 40, H + 112),
        "Packs, prices & product options",
        font=body,
        fill=INK,
    )
    draw.text(
        (52 + panel.width + 40, H + 148),
        "hotmoon123.github.io/hotmoon123",
        font=ImageFont.truetype(REG, 22),
        fill=(90, 74, 52),
    )

    out = OUT / "bitekasa-offer-flyer-qr-footer.png"
    canvas.save(out, optimize=True)
    print("wrote", out, canvas.size)


if __name__ == "__main__":
    main()
