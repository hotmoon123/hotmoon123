import { useEffect, useRef } from 'react';
import {
  WebGLRenderer,
  Scene,
  PerspectiveCamera,
  Group,
  IcosahedronGeometry,
  MeshBasicMaterial,
  Mesh,
  OctahedronGeometry,
  BufferGeometry,
  BufferAttribute,
  PointsMaterial,
  Points,
} from 'three';
import type { WebGLRenderer as WebGLRendererType } from 'three';
import { prefersReducedMotion } from '../animations/motion';

/**
 * A lightweight, decorative Three.js scene for the home hero.
 * - Pauses when the hero is off-screen or the tab is hidden.
 * - Renders a single still frame for reduced-motion visitors.
 * - Renders nothing (the hero text still works) if WebGL is unavailable.
 * - Disposes all GPU resources on unmount.
 */
export default function HeroScene() {
  const hostRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const host = hostRef.current;
    if (!host) return;

    let renderer: WebGLRendererType;
    try {
      renderer = new WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'low-power' });
    } catch {
      host.dataset.webgl = 'unavailable';
      return;
    }

    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5));
    renderer.setClearColor(0x000000, 0);
    host.appendChild(renderer.domElement);

    const scene = new Scene();
    const camera = new PerspectiveCamera(45, 1, 0.1, 100);
    camera.position.z = 6;

    const group = new Group();
    scene.add(group);

    const outerGeometry = new IcosahedronGeometry(1.7, 1);
    const outerMaterial = new MeshBasicMaterial({ color: 0x7dd3fc, wireframe: true, transparent: true, opacity: 0.75 });
    const outer = new Mesh(outerGeometry, outerMaterial);

    const innerGeometry = new OctahedronGeometry(0.85, 0);
    const innerMaterial = new MeshBasicMaterial({ color: 0x3b82f6, wireframe: true, transparent: true, opacity: 0.9 });
    const inner = new Mesh(innerGeometry, innerMaterial);

    group.add(outer, inner);

    // A sparse field of points gives depth without a heavy texture.
    const count = 260;
    const positions = new Float32Array(count * 3);
    for (let i = 0; i < positions.length; i += 3) {
      positions[i] = (Math.random() - 0.5) * 14;
      positions[i + 1] = (Math.random() - 0.5) * 9;
      positions[i + 2] = (Math.random() - 0.5) * 6;
    }
    const pointGeometry = new BufferGeometry();
    pointGeometry.setAttribute('position', new BufferAttribute(positions, 3));
    const pointMaterial = new PointsMaterial({ color: 0x93c5fd, size: 0.035, transparent: true, opacity: 0.7 });
    const points = new Points(pointGeometry, pointMaterial);
    scene.add(points);

    const reduced = prefersReducedMotion();
    const pointer = { x: 0, y: 0, tx: 0, ty: 0 };

    const resize = () => {
      const width = Math.max(host.clientWidth, 1);
      const height = Math.max(host.clientHeight, 1);
      renderer.setSize(width, height, false);
      camera.aspect = width / height;
      camera.updateProjectionMatrix();
    };
    resize();

    const resizeObserver = new ResizeObserver(resize);
    resizeObserver.observe(host);

    const onPointerMove = (event: PointerEvent) => {
      pointer.tx = (event.clientX / window.innerWidth - 0.5) * 0.6;
      pointer.ty = (event.clientY / window.innerHeight - 0.5) * 0.4;
    };
    if (!reduced) window.addEventListener('pointermove', onPointerMove, { passive: true });

    let frame = 0;
    let running = false;
    let visible = true;

    const renderOnce = () => {
      group.rotation.x = pointer.y;
      group.rotation.y = pointer.x;
      renderer.render(scene, camera);
    };

    const tick = (time: number) => {
      if (!running) return;
      pointer.x += (pointer.tx - pointer.x) * 0.05;
      pointer.y += (pointer.ty - pointer.y) * 0.05;
      outer.rotation.x = time * 0.00012;
      outer.rotation.y = time * 0.00018;
      inner.rotation.x = -time * 0.0002;
      inner.rotation.y = time * 0.00026;
      points.rotation.y = time * 0.00005;
      renderOnce();
      frame = requestAnimationFrame(tick);
    };

    const updateRunning = () => {
      const shouldRun = !reduced && visible && document.visibilityState === 'visible';
      if (shouldRun && !running) {
        running = true;
        frame = requestAnimationFrame(tick);
      } else if (!shouldRun && running) {
        running = false;
        cancelAnimationFrame(frame);
      }
    };

    const intersection = new IntersectionObserver(([entry]) => {
      visible = entry.isIntersecting;
      updateRunning();
    });
    intersection.observe(host);
    document.addEventListener('visibilitychange', updateRunning);

    if (reduced) {
      renderOnce();
    } else {
      updateRunning();
    }

    return () => {
      running = false;
      cancelAnimationFrame(frame);
      intersection.disconnect();
      resizeObserver.disconnect();
      document.removeEventListener('visibilitychange', updateRunning);
      window.removeEventListener('pointermove', onPointerMove);
      outerGeometry.dispose();
      outerMaterial.dispose();
      innerGeometry.dispose();
      innerMaterial.dispose();
      pointGeometry.dispose();
      pointMaterial.dispose();
      renderer.dispose();
      renderer.domElement.remove();
    };
  }, []);

  return <div ref={hostRef} className="hero-scene" aria-hidden="true" />;
}
