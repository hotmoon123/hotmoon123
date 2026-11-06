# BiteKasa printable QR pack

**Encoded link (exactly):** `https://hotmoon123.github.io/hotmoon123/`
**Points to:** the live BiteKasa website, not to a picture of the flyer.

## Files

| File | Use it for | Size |
|---|---|---|
| `bitekasa-offer-flyer-qr-footer.png` | Print flyer, packs version. **Shows Golden 50 — superseded 5 Nov 2026 when the owner confirmed 55. Do not print.** Kept only as a layout reference. | 1024 × 1816 px |
| `bitekasa-premium-flyer-qr.png` | **Print this flyer.** “Upgrade to the Premium Pack” version, Golden 55, with `@bitekasa` bottom-right. The AI-composed QR in the supplied artwork was replaced with a real code in the same footprint. | 1664 × 2496 px |
| `bitekasa-qr-print-2400.png` | Standalone QR for layout/design work or a print shop. | 2400 × 2400 px, 600 dpi metadata |
| `bitekasa-qr-vector.svg` | Vector QR — scales to any size without blurring. Give this to a printer or designer. | vector |
| `bitekasa-qr-scan-card.png` | QR with a “Scan to view” caption, for a table card, poster or social post. | 2000 × 2380 px |

`make_qr.py` and `make_flyer_qr.py` regenerate the images; the URL is set once at the top of each file.

**Superseded:** `../bitekasa-offer-flyer-website-qr.png` places the QR over the Premium card and hides part of “70 PIECES + 1 LITRE COKE”. Use the footer version above for print.

**Replaced:** the QR drawn into the supplied “Upgrade to the Premium Pack” artwork did not decode in ZXing or OpenCV — it was an image-model approximation, not an encoded symbol. `bitekasa-premium-flyer-qr.png` keeps that layout and swaps in a real code (333 px footprint, 4-module quiet zone, error correction Q).

## Verification performed

- Decoded with ZXing (the engine used inside many phone camera apps): correct URL in every file.
- Flyer re-rendered at 1748 px (A5 at 300 dpi), 1200 px, 900 px, 700 px, 600 px and 480 px wide: decoded correctly at all sizes.
- Simulated photo conditions — Gaussian blur plus rotation of 5°, 10°, 15°, 25° and 40°: decoded correctly.
- Low-contrast and downscaled copies: decoded correctly.

This testing is a software simulation. It is not the same as scanning printed paper with a phone, which still needs to be done before a bulk print run.

## Print rules

1. **Minimum size:** 2 cm × 2 cm on the printed sheet. On this flyer the code prints about 2.9 cm wide at A5 and about 2.0 cm at A6. Do not shrink it further.
2. **Never stretch or squash it.** Scale proportionally, or use the SVG.
3. **Keep the white border (quiet zone) intact.** Do not crop it or put text over it.
4. **High contrast only.** Black modules on white. No gradients, no transparency, no colour tint on the code itself.
5. **Don't place it over a busy photo.** Plain background behind it.
6. **Test on paper.** Print one proof at final size and scan it with two different phones, outdoors and indoors, at arm's length. Only then order a bulk run.

## About using an AI image generator

**Do not ask an AI image generator to draw, redraw, restyle or "add" the QR code.** Image models repaint pixels. They produce a QR-like pattern that looks plausible but does not encode the URL, so printed copies will fail to scan. This is the most common way a working QR code gets destroyed.

Correct approach:

1. Generate or design the flyer artwork **without** a QR code.
2. Open that artwork in a layout tool — Canva, Figma, Photoshop, Illustrator, Affinity, PowerPoint or Word.
3. **Place** `bitekasa-qr-vector.svg` (preferred) or `bitekasa-qr-print-2400.png` as a separate layer. Do not trace, recolour or filter it.
4. Export at 300 dpi and print a proof.

If an AI editing tool is used at all, it must composite an existing image file as a layer (for example Canva's upload/place feature). Any prompt that says "add a QR code" to a diffusion model should be assumed to produce an unscannable code, and must be verified by scanning before print.

## If the web address changes

The QR encodes the current URL. If BiteKasa moves to a custom domain, regenerate with the new address:

```bash
python3 make_qr.py && python3 make_flyer_qr.py   # after editing URL at the top of each script
```

Requires `qrcode`, `pillow`, `opencv-python-headless`, `zxing-cpp`
(`python3 -m venv venv && venv/bin/pip install qrcode pillow opencv-python-headless zxing-cpp`).

Source artwork: `../premium-poster-source.webp` is the owner's supplied poster, stored unchanged. `make_premium_flyer.py` rebuilds the print file from it: it swaps the non-scannable QR for a real one and adds the Instagram handle.
