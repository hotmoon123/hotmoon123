import { Component, Suspense, lazy, useEffect, useRef, useState, type ErrorInfo, type PointerEvent, type ReactNode } from 'react';
import { useReducedMotion } from 'motion/react';

type PointerPosition = { x: number; y: number };
const ThreeAccent = lazy(() => import('./ThreeAccent'));

class Optional3DErrorBoundary extends Component<{ children: ReactNode }, { failed: boolean }> {
  state = { failed: false };

  static getDerivedStateFromError() {
    return { failed: true };
  }

  componentDidCatch(error: Error, _info: ErrorInfo) {
    console.warn('Optional BiteKasa 3D accent unavailable; keeping the product image visible.', error);
  }

  render() {
    return this.state.failed ? null : this.props.children;
  }
}

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
        <Optional3DErrorBoundary>
          <Suspense fallback={null}>
            <ThreeAccent reducedMotion={Boolean(reduceMotion)} pointer={pointer} />
          </Suspense>
        </Optional3DErrorBoundary>
      )}
    </div>
  );
}
