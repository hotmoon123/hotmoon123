import { useEffect, useLayoutEffect, useRef, useState } from 'react';
import type { CSSProperties } from 'react';

/**
 * LiquidGlassLogo — MYST WATER intro mark.
 *
 * Original implementation written for this project (2026-11-07). It was built
 * to the brief "sphere-to-tile glass entrance" after the ReactDrops registry
 * file (https://reactdrops.dev/r/liquid-glass-logo.json) could not be fetched
 * from the build sandbox (network is restricted to npm/GitHub hosts). It is
 * NOT the ReactDrops component; to swap in the real registry component, see
 * README § "Swap in the ReactDrops Liquid Glass Logo".
 *
 * Preserved/derived behaviours, all self-contained (no dependencies, no assets
 * beyond the supplied logo):
 *  1. Sphere-to-tile glass entrance — the mark scales in as a glossy orb,
 *     then morphs (border-radius + transform) into a rounded tile, settles at
 *     its normal size and finishes on the ORIGINAL logo alone. No text reveal.
 *  2. Wavelength-based bevel refraction — an animated conic bevel ring whose
 *     hue order (cyan → ice → campaign blue → leaf) mimics wavelength
 *     separation at a glass edge, masked to just the outer bevel band.
 *  3. Chromatic edge streaks — offset, softly tinted edge fringes (cyan /
 *     leaf / campaign blue) that bloom during the morph and decay to zero.
 *  4. Measured responsive fitting — the stage is sized by measuring its parent
 *     (ResizeObserver, with a clientWidth fallback), capped to the requested
 *     style height (default 480) and to the width available.
 *  5. Reduced-motion support — prefers-reduced-motion renders the settled
 *     original logo immediately (no animation), and onFinish fires quickly.
 *  6. Image fallback — if the logo fails to load, a CSS-only MYST wordmark
 *     tile is rendered instead (the site never shows a broken image).
 */

export interface LiquidGlassLogoProps {
  /** URL of the logo image. Use a base-aware path (see src/lib/asset.ts). */
  logo: string;
  /** Kept for API parity with the requested integration. Only the bare logo ending is supported. */
  ending?: 'logo';
  /** 'dark' suits the MYST splash gradient; 'light' suits an ice/mist background. */
  theme?: 'dark' | 'light';
  /** Bevel/refraction intensity, 0–5. 2.9 was the requested calibration. */
  depth?: number;
  style?: CSSProperties;
  /** Fired once the entrance has finished (or immediately-ish for reduced motion). */
  onFinish?: () => void;
}

const clamp = (value: number, min: number, max: number) => Math.min(max, Math.max(min, value));
const FINISH_MS = 2700;
const REDUCED_FINISH_MS = 350;

export function LiquidGlassLogo({
  logo,
  ending = 'logo',
  theme = 'dark',
  depth = 2.9,
  style,
  onFinish,
}: LiquidGlassLogoProps) {
  void ending; // single supported ending; prop retained for call-site parity

  const hostRef = useRef<HTMLDivElement>(null);
  const onFinishRef = useRef(onFinish);
  onFinishRef.current = onFinish;

  const requestedHeight = typeof style?.height === 'number' ? style.height : 480;
  const [fit, setFit] = useState<number>(requestedHeight);
  const [imageFailed, setImageFailed] = useState(false);

  const prefersReducedMotion =
    typeof window !== 'undefined' &&
    typeof window.matchMedia === 'function' &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Measured responsive fitting: measure the host parent, keep the mark square.
  useLayoutEffect(() => {
    const host = hostRef.current;
    if (!host) return undefined;

    const measure = () => {
      const parentWidth = host.parentElement?.clientWidth ?? host.clientWidth ?? requestedHeight;
      const viewportH = typeof window !== 'undefined' ? window.innerHeight : requestedHeight;
      setFit(Math.round(clamp(Math.min(requestedHeight, parentWidth, viewportH * 0.66), 96, 560)));
    };

    measure();
    if (typeof ResizeObserver === 'undefined') return undefined;
    const observer = new ResizeObserver(measure);
    if (host.parentElement) observer.observe(host.parentElement);
    observer.observe(host);
    return () => observer.disconnect();
  }, [requestedHeight]);

  // Auto-finish so callers can drop the overlay without a forced tap.
  useEffect(() => {
    const timer = window.setTimeout(
      () => onFinishRef.current?.(),
      prefersReducedMotion ? REDUCED_FINISH_MS : FINISH_MS,
    );
    return () => window.clearTimeout(timer);
  }, [prefersReducedMotion]);

  const bevel = clamp(depth / 5, 0, 1); // 2.9 ≈ 0.58 — vivid but not garish
  const stageStyle = {
    '--lg-size': `${fit}px`,
    '--lg-bevel': String(0.35 + bevel * 0.6),
    width: fit,
    height: fit,
  } as CSSProperties;

  return (
    <div
      ref={hostRef}
      className={`lg-logo lg-logo--${theme}${prefersReducedMotion ? ' lg-logo--reduced' : ''}`}
      style={{ ...style, height: fit }}
      data-testid="liquid-glass-logo"
    >
      <div className="lg-stage" style={stageStyle}>
        {imageFailed ? (
          // Image fallback — CSS-only wordmark tile, never a broken-image glyph.
          <div className="lg-wordmark" role="img" aria-label="MYST Water logo">
            <span>MYST</span>
            <small>W A T E R</small>
          </div>
        ) : (
          <>
            {/* Chromatic edge streaks (wavelength-separated fringes) */}
            <span className="lg-chroma lg-chroma--cyan" aria-hidden="true" />
            <span className="lg-chroma lg-chroma--blue" aria-hidden="true" />
            <span className="lg-chroma lg-chroma--leaf" aria-hidden="true" />

            {/* Bevel refraction ring — conic, wavelength-ordered, masked to the outer band */}
            <span className="lg-bevel" aria-hidden="true" />

            {/* The morphing glass tile carrying the supplied (unmodified) logo */}
            <span className="lg-tile">
              <img
                className="lg-img"
                src={logo}
                alt="MYST Water logo"
                width={fit}
                height={fit}
                draggable={false}
                decoding="async"
                onError={() => setImageFailed(true)}
              />
              <span className="lg-specular" aria-hidden="true" />
            </span>
          </>
        )}
      </div>
    </div>
  );
}

export default LiquidGlassLogo;
