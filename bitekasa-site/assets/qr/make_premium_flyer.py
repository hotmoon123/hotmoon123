#!/usr/bin/env python3
"""Build the print-ready “Premium Pack” flyer: real QR + Instagram handle.

Input artwork: `../premium-poster-source.webp` (the owner's supplied image, kept
unchanged). Two edits are applied to a copy:

1. The QR drawn into the supplied artwork is an image-model approximation and does
   not decode. It is replaced by a real code in the same footprint
   (333 px, 4-module quiet zone, error correction Q).
2. The Instagram handle `@bitekasa` is added bottom-right, clear of the
   “ORDER NOW” button and the yellow accents.

Output: `bitekasa-premium-flyer-qr.png` (1664 × 2496).

Usage:
    python3 make_premium_flyer.py
Verify:
    python3 -c "import cv2,zxingcpp; print(zxingcpp.read_barcodes(cv2.imread('bitekasa-premium-flyer-qr.png')))"
"""

from pathlib import Path

import qrcode
from PIL import Image, ImageDraw, ImageFont

URL = "https://hotmoon123.github.io/hotmoon123/"
HANDLE = "@bitekasa"
HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "premium-poster-source.webp"
OUT = HERE / "bitekasa-premium-flyer-qr.png"

# Footprint of the QR that exists in the supplied artwork (x0, y0, x1, y1).
QR_BOX = (77, 2147, 421, 2479)

RED = (167, 25, 32)
INK = (26, 26, 26)
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def real_qr(side: int) -> Image.Image:
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q, box_size=12, border=4)
    qr.add_data(URL)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    return img.resize((side, side), resample=0)


def main() -> None:
    img = Image.open(SOURCE).convert("RGB")
    draw = ImageDraw.Draw(img)

    # 1. Replace the fake QR.
    x0, y0, x1, y1 = QR_BOX
    draw.rectangle([x0, y0, x1, y1], fill=(255, 255, 255))
    side = min(x1 - x0, y1 - y0)
    img.paste(real_qr(side), (x0 + 4, y0))

    # 2. Instagram lockup, bottom-right, below the yellow accents.
    W, _ = img.size
    icon, gap = 62, 20
    font = ImageFont.truetype(BOLD, 58)
    box = draw.textbbox((0, 0), HANDLE, font=font)
    text_w, text_h = box[2] - box[0], box[3] - box[1]
    text_x = (W - 74) - text_w
    icon_x = text_x - gap - icon
    icon_y = 2378

    draw.rounded_rectangle([icon_x, icon_y, icon_x + icon, icon_y + icon], radius=18, outline=RED, width=6)
    cx, cy = icon_x + icon // 2, icon_y + icon // 2
    r = 14
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=RED, width=6)
    draw.ellipse([icon_x + icon - 19, icon_y + 11, icon_x + icon - 11, icon_y + 19], fill=RED)

    text_y = icon_y + (icon - text_h) // 2 - box[1]
    draw.text((text_x, text_y), HANDLE, font=font, fill=INK)

    img.save(OUT, optimize=True)
    print(f"wrote {OUT.name} {img.size} · QR {side}px · handle at x={icon_x} y={icon_y}")


if __name__ == "__main__":
    main()
