import { useEffect, useRef, type ReactNode } from 'react';
import { useLocation } from 'react-router-dom';
import { observeReveals, pageIn } from '../animations/motion';

/** Fades each route's content in and sets up scroll reveals. Reduced-motion visitors see the page immediately. */
export default function PageTransition({ children }: { children: ReactNode }) {
  const { pathname } = useLocation();
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!ref.current) return;
    pageIn(ref.current);
    return observeReveals(ref.current);
  }, [pathname]);

  return (
    <div ref={ref} className="page-transition">
      {children}
    </div>
  );
}
