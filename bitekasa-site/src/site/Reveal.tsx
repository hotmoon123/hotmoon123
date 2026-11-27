import { useEffect, useRef, useState, type ReactNode } from 'react';

type RevealProps = {
  children: ReactNode;
  className?: string;
  delay?: number;
};

/**
 * One shared entrance, so every section behaves the same way.
 *
 * Plain CSS plus a single IntersectionObserver — no animation library. The
 * transition is authored in `styles.css` and disabled entirely under
 * `prefers-reduced-motion`, so the reduced-motion path is the browser's own
 * preference rather than JavaScript we have to remember to check.
 */
export default function Reveal({ children, className = '', delay = 0 }: RevealProps) {
  const ref = useRef<HTMLDivElement | null>(null);
  const [shown, setShown] = useState(false);

  useEffect(() => {
    const node = ref.current;
    if (!node) return undefined;

    // No observer (older browser, test environment) or the visitor asked for
    // less motion: show the content immediately instead of hiding it.
    const prefersLess =
      typeof window === 'undefined' ||
      typeof IntersectionObserver === 'undefined' ||
      Boolean(window.matchMedia?.('(prefers-reduced-motion: reduce)').matches);

    if (prefersLess) {
      setShown(true);
      return undefined;
    }

    const observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            setShown(true);
            observer.disconnect();
          }
        }
      },
      { threshold: 0.18, rootMargin: '0px 0px -8% 0px' },
    );

    observer.observe(node);
    return () => observer.disconnect();
  }, []);

  return (
    <div
      ref={ref}
      className={`reveal${shown ? ' is-shown' : ''}${className ? ` ${className}` : ''}`}
      style={delay > 0 ? { transitionDelay: `${delay}s` } : undefined}
    >
      {children}
    </div>
  );
}
