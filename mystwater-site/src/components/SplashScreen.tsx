import { useCallback, useEffect, useRef, useState } from 'react';
import { asset } from '../lib/asset';
import { LiquidGlassLogo } from './liquid-glass-logo';

/**
 * SplashScreen — full-screen, MYST-coloured intro shown when the app opens.
 * No button is required: the logo animation plays on load, and tapping or
 * clicking anywhere (or pressing Escape/Enter/Space) reveals the site.
 * The site itself renders beneath it, so there is nothing to wait for.
 */
export default function SplashScreen({ onDone }: { onDone: () => void }) {
  const [closing, setClosing] = useState(false);
  const closingRef = useRef(false);

  const requestDone = useCallback(() => {
    if (closingRef.current) return; // tap anywhere, animation finish — once only
    closingRef.current = true;
    setClosing(true);
    window.setTimeout(onDone, 280); // match the fade-out, then unmount
  }, [onDone]);

  // Lock scroll while the intro is up; restore on unmount.
  useEffect(() => {
    const { body } = document;
    const previous = body.style.overflow;
    body.style.overflow = 'hidden';
    return () => {
      body.style.overflow = previous;
    };
  }, []);

  // Keyboard access for the tap-anywhere behaviour.
  useEffect(() => {
    const onKey = (event: KeyboardEvent) => {
      if (event.key === 'Escape' || event.key === 'Enter' || event.key === ' ') requestDone();
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [requestDone]);

  return (
    <div
      className={`splash${closing ? ' is-closing' : ''}`}
      role="button"
      tabIndex={0}
      aria-label="Continue to the Myst Water website"
      onPointerDown={requestDone}
      onKeyDown={(event) => {
        if (event.key === 'Escape' || event.key === 'Enter' || event.key === ' ') requestDone();
      }}
    >
      <div className="splash-glow splash-glow--top" aria-hidden="true" />
      <div className="splash-glow splash-glow--bottom" aria-hidden="true" />
      <div className="splash-inner">
        <LiquidGlassLogo
          logo={asset('assets/myst-logo.jpg')}
          ending="logo"
          theme="dark"
          depth={2.9}
          style={{ height: 480 }}
          onFinish={requestDone}
        />
        <p className="splash-hint">Tap anywhere to continue</p>
      </div>
    </div>
  );
}
