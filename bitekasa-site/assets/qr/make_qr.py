#!/usr/bin/env python3
"""Generate print-ready BiteKasa QR assets for the live website URL.

Outputs (this folder):
  bitekasa-qr-print-2400.png  2400px, 8-module quiet zone, error correction Q
  bitekasa-qr-vector.svg      vector, scales to any print size
  bitekasa-qr-scan-card.png   QR + caption card for flyer / social placement

Verify with:
  /tmp/qrenv/bin/python verify_qr.py
"""

from pathlib import Path

import qrcode
from qrcode.image.svg import SvgPathImage

URL = "https://hotmoon123.github.io/hotmoon123/"
OUT = Path(__file__).resolve().parent

RED = "#A71920"
CREAM = "#F7EEDB"
INK = "#111111"


def build_qr(border=8):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=border,
    )
    qr.add_data(URL)
    qr.make(fit=True)
    return qr


def main():
    qr = build_qr(border=8)

    # 1. Print PNG: crisp integer modules, exact 2400x2400 canvas.
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    img = img.resize((2400, 2400), resample=0)  # nearest-neighbour keeps edges hard
    img.save(OUT / "bitekasa-qr-print-2400.png", dpi=(600, 600))

    # 2. Vector SVG for designers / print shops.
    svg_qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=8,
        image_factory=SvgPathImage,
    )
    svg_qr.add_data(URL)
    svg_qr.make(fit=True)
    svg_qr.make_image().save(OUT / "bitekasa-qr-vector.svg")

    # 3. Scan card: white QR panel on brand cream, red caption underneath.
    from PIL import Image, ImageDraw, ImageFont

    W, H = 2000, 2380
    card = Image.new("RGB", (W, H), CREAM)
    draw = ImageDraw.Draw(card)

    # thin red frame
    draw.rectangle([40, 40, W - 40, H - 40], outline=RED, width=10)

    qr_core = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    qr_side = 1560
    qr_core = qr_core.resize((qr_side, qr_side), resample=0)

    panel_pad = 40
    panel = Image.new("RGB", (qr_side + panel_pad * 2, qr_side + panel_pad * 2), "white")
    panel.paste(qr_core, (panel_pad, panel_pad))
    card.paste(panel, ((W - panel.width) // 2, 130))

    font_path = None
    for candidate in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ):
        if Path(candidate).exists():
            font_path = candidate
            break

    def font(size):
        if font_path:
            return ImageFont.truetype(font_path, size)
        return ImageFont.load_default()

    def centred(text, y, fnt, fill):
        box = draw.textbbox((0, 0), text, font=fnt)
        draw.text(((W - (box[2] - box[0])) // 2, y), text, font=fnt, fill=fill)

    centred("SCAN TO VIEW", 1900, font(96), RED)
    centred("BiteKasa packs, prices & options", 2030, font(60), INK)

    # Keep the caption clear of the caption area inside the frame.
    card.save(OUT / "bitekasa-qr-scan-card.png", optimize=True)

    print("URL encoded:", URL)
    print("Wrote:", *(p.name for p in sorted(OUT.glob("bitekasa-qr-*"))), sep="\n  - ")


if __name__ == "__main__":
    main()
