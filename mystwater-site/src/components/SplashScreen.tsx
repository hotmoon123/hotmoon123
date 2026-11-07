import { useCallback, useEffect, useRef, useState } from 'react';
import { asset } from '../lib/asset';
import { LiquidGlassLogo } from './liquid-glass-logo';

const CHIME_SRC = 'assets/audio/myst-splash.wav';

/**
 * SplashScreen — full-screen, MYST-coloured intro shown when the app opens.
 * No button is required: the logo animation plays on load, and tapping or
 * clicking anywhere (or pressing Escape/Enter/Space) reveals the site.
 * The site itself renders beneath it, so there is nothing to wait for.
 *
 * Sound: a short, self-contained water chime (synthesized in-repo) plays with
 * the intro. Browser autoplay rules may block it before the first user
 * gesture — if so, it is silently retried on the first tap/click. Pressing M
 * mutes it (no extra button, by design). If audio APIs are unavailable or the
 * file fails to load, the intro simply runs silently.
 */
export default function SplashScreen({ onDone }: { onDone: () => void }) {
  const [closing, setClosing] = useState(false);
  const closingRef = useRef(false);
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const mutedRef = useRef(false);

  const playChime = useCallback(() => {
    if (mutedRef.current) return;
    if (typeof window === 'undefined' || typeof window.Audio !== 'function') return;
    try {
      const player = audioRef.current ?? new Audio(asset(CHIME_SRC));
      audioRef.current = player;
      player.volume = 0.6;
      const started = player.play() as unknown;
      if (started && typeof (started as Promise<void>).catch === 'function') {
        (started as Promise<void>).catch(() => {
          // Autoplay blocked before a user gesture — will retry on first tap.
        });
      }
    } catch {
      // Audio unavailable (e.g. restricted embeds) — intro runs silently.
    }
  }, []);

  const toggleMute = useCallback(() => {
    mutedRef.current = !mutedRef.current;
    try {
      audioRef.current?.pause();
      if (audioRef.current) audioRef.current.currentTime = 0;
    } catch {
      /* media element not supported — nothing to mute */
    }
  }, []);

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

  // Play the chime with the animation (may be blocked until first gesture).
  useEffect(() => {
    playChime();
  }, [playChime]);

  // Keyboard access for the tap-anywhere behaviour; M mutes the chime.
  useEffect(() => {
    const onKey = (event: KeyboardEvent) => {
      if (event.key === 'Escape' || event.key === 'Enter' || event.key === ' ') requestDone();
      if (event.key === 'm' || event.key === 'M') toggleMute();
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [requestDone, toggleMute]);

  return (
    <div
      className={`splash${closing ? ' is-closing' : ''}`}
      role="button"
      tabIndex={0}
      aria-label="Continue to the Myst Water website"
      onPointerDown={() => {
        playChime(); // user gesture: unlock/retry the blocked chime
        requestDone();
      }}
      onKeyDown={(event) => {
        if (event.key === 'Escape' || event.key === 'Enter' || event.key === ' ') requestDone();
        if (event.key === 'm' || event.key === 'M') toggleMute();
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
