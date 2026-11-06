import { lazy, Suspense, useEffect, useRef, useState } from 'react';
import logoFull from '../assets/bitekasa-logo-full.png';

/**
 * ReactDrops "Liquid Glass Logo" — installed from
 * https://reactdrops.dev/r/liquid-glass-logo.json
 *
 * The component (canvas, shaders, renderer) is ~90 KB of source and must not land
 * in the main bundle: the project's CI fails any main chunk above 150 KiB gzip.
 * It is therefore loaded on demand, and only once the section is actually on
 * screen — otherwise the reveal would play to an empty viewport and the visitor
 * would scroll down to a finished still.
 */
const LiquidGlassLogo = lazy(() =>
  import('./components/liquid-glass-logo').then((module) => ({ default: module.LiquidGlassLogo })),
);

const supportsIntersectionObserver = typeof IntersectionObserver !== 'undefined';
const LOGO_ALT = 'BiteKasa logo — samosas, spring rolls, hot, crispy, fresh';

export default function LogoReveal() {
  const section = useRef<HTMLDivElement>(null);
  const [inView, setInView] = useState(!supportsIntersectionObserver);

  useEffect(() => {
    if (!supportsIntersectionObserver || !section.current) return;
    const observer = new IntersectionObserver(
      (entries) => {
        if (entries.some((entry) => entry.isIntersecting)) {
          setInView(true);
          observer.disconnect();
        }
      },
      { threshold: 0.35 },
    );
    observer.observe(section.current);
    return () => observer.disconnect();
  }, []);

  return (
    <section className="logo-reveal" aria-labelledby="logo-reveal-heading">
      <h2 id="logo-reveal-heading" className="logo-reveal-heading">
        BiteKasa
      </h2>
      <div ref={section} className="logo-reveal-stage">
        <Suspense
          fallback={
            <img className="logo-reveal-still" src={logoFull} alt={LOGO_ALT} width={220} height={255} />
          }
        >
          {inView ? (
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
              style={{ height: 480 }}
              aria-label="BiteKasa — samosas and spring rolls, hot, crispy, fresh"
            />
          ) : (
            <img className="logo-reveal-still" src={logoFull} alt={LOGO_ALT} width={220} height={255} />
          )}
        </Suspense>
      </div>
    </section>
  );
}
