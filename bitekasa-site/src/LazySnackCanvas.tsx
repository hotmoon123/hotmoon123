import { Suspense, lazy, useEffect, useRef, useState, type PointerEvent } from 'react';
import { useReducedMotion } from 'motion/react';

type PointerPosition = { x: number; y: number };
const ThreeAccent = lazy(() => import('./ThreeAccent'));

export default function LazySnackCanvas() {
  const container = useRef<HTMLDivElement>(null);
  const pointer = useRef<PointerPosition>({ x: 0, y: 0 });
  const [nearViewport, setNearViewport] = useState(false);
  const reduceMotion = useReducedMotion();

  useEffect(() => {
    const element = container.current;
    if (!element || !window.matchMedia('(min-width: 768px)').matches) return undefined;

    let timer = 0;
    const observer = new IntersectionObserver(([entry]) => {
      if (!entry.isIntersecting) return;
      observer.disconnect();
      // Let the image and primary CTAs render before requesting the optional 3D chunk.
      timer = window.setTimeout(() => setNearViewport(true), 900);
    }, { rootMargin: '0px' });
    observer.observe(element);

    return () => {
      observer.disconnect();
      window.clearTimeout(timer);
    };
  }, []);

  const handlePointerMove = (event: PointerEvent<HTMLDivElement>) => {
    const rect = event.currentTarget.getBoundingClientRect();
    pointer.current = {
      x: ((event.clientX - rect.left) / rect.width - 0.5) * 2,
      y: ((event.clientY - rect.top) / rect.height - 0.5) * 2,
    };
  };

  return (
    <div ref={container} className="absolute inset-0" onPointerMove={handlePointerMove} aria-hidden="true">
      {nearViewport && (
        <Suspense fallback={null}>
          <ThreeAccent reducedMotion={Boolean(reduceMotion)} pointer={pointer} />
        </Suspense>
      )}
    </div>
  );
}
