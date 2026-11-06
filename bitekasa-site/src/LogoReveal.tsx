import { lazy, Suspense, useEffect, useRef, useState } from 'react';
import logoMark from '../assets/bitekasa-logo-mark.png';

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
            <img
              className="logo-reveal-still"
              src={logoMark}
              alt="BiteKasa crown, samosa and spring roll mark"
              width={220}
              height={220}
            />
          }
        >
          {inView ? (
            <LiquidGlassLogo
              logo={logoMark}
              ending="logo"
              theme="dark"
              background="#000000"
              logoColor="original"
              logoRelief={0}
              finalLogoScale={1}
              logoScale={0.72}
              speed={1}
              loop={false}
              maxDpr={1.75}
              style={{ height: 480 }}
              aria-label="BiteKasa — samosas and spring rolls"
            />
          ) : (
            <img
              className="logo-reveal-still"
              src={logoMark}
              alt="BiteKasa crown, samosa and spring roll mark"
              width={220}
              height={220}
            />
          )}
        </Suspense>
      </div>
    </section>
  );
}
