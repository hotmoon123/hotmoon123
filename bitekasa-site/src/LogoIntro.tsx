import { lazy, Suspense, useCallback, useEffect, useRef, useState } from 'react';
import logoFull from '../assets/bitekasa-logo-full.png';

/**
 * ReactDrops "Liquid Glass Logo" as the site's opening splash.
 * Registry item: https://reactdrops.dev/r/liquid-glass-logo.json
 *
 * Rules this follows:
 * - Once per browser session, so a return visit is never delayed twice.
 * - The reveal plays in full and then the splash leaves on its own.
 * - It ends on its own after the reveal, or early with Escape. There is no
 *   button on it: a stray tap or scroll must not swallow the animation, and the
 *   page underneath is what the visitor came for.
 * - `prefers-reduced-motion: reduce` gets the still artwork for a shorter beat instead
 *   of the droplet animation.
 * - No WebGL, no slow network, or a failed module load all fall back to the same still.
 * - The page renders underneath the whole time, so nothing is blocked from loading.
 */
const LiquidGlassLogo = lazy(() =>
  import('./components/liquid-glass-logo').then((module) => ({ default: module.LiquidGlassLogo })),
);

const STORAGE_KEY = 'bitekasa-intro-seen';
const HOLD_MS = 2400;
const REDUCED_HOLD_MS = 1200;

function prefersReducedMotion() {
  return typeof window !== 'undefined' && Boolean(window.matchMedia?.('(prefers-reduced-motion: reduce)').matches);
}

function introAlreadySeen() {
  const params = new URLSearchParams(window.location.search);
  // ?intro=1 replays the splash on demand; ?intro=0 suppresses it.
  if (params.get('intro') === '1') return false;
  if (params.get('intro') === '0') return true;
  try {
    return Boolean(window.sessionStorage.getItem(STORAGE_KEY));
  } catch {
    return false;
  }
}

export default function LogoIntro() {
  const reduced = prefersReducedMotion();
  const [visible, setVisible] = useState(() => !introAlreadySeen());
  const [leaving, setLeaving] = useState(false);
  const previouslyFocused = useRef<Element | null>(null);

  const dismiss = useCallback(() => {
    setLeaving(true);
    try {
      window.sessionStorage.setItem(STORAGE_KEY, '1');
    } catch {
      /* private mode — the splash simply shows again next load */
    }
    window.setTimeout(() => setVisible(false), 260);
  }, []);

  useEffect(() => {
    if (!visible) return undefined;
    previouslyFocused.current = document.activeElement;
    const { body } = document;
    const previousOverflow = body.style.overflow;
    body.style.overflow = 'hidden';

    const timer = window.setTimeout(dismiss, reduced ? REDUCED_HOLD_MS : HOLD_MS);
    const onKey = (event: KeyboardEvent) => {
      if (event.key === 'Escape') dismiss();
    };
    window.addEventListener('keydown', onKey);

    return () => {
      window.clearTimeout(timer);
      window.removeEventListener('keydown', onKey);
      body.style.overflow = previousOverflow;
      const target = previouslyFocused.current;
      if (target instanceof HTMLElement) target.focus();
    };
  }, [visible, dismiss, reduced]);

  if (!visible) return null;

  const still = (
    <img className="logo-intro-still" src={logoFull} alt="" width={240} height={279} aria-hidden="true" />
  );

  return (
    <div
      className={`logo-intro${leaving ? ' is-leaving' : ''}`}
      role="dialog"
      aria-modal="true"
      aria-label="BiteKasa is opening"
    >
      <div className="logo-intro-stage">
        {reduced ? (
          still
        ) : (
          <Suspense fallback={still}>
            <LiquidGlassLogo
              logo={logoFull}
              ending="logo"
              theme="light"
              depth={2.9}
              background="#000000"
              logoColor="original"
              logoRelief={0}
              finalLogoScale={1}
              logoSize={384}
              logoScale={0.9}
              speed={1}
              loop={false}
              maxDpr={1.75}
              style={{ height: '100%' }}
              aria-label="BiteKasa — samosas and spring rolls, hot, crispy, fresh"
            />
          </Suspense>
        )}
      </div>
    </div>
  );
}
