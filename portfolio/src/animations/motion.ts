import { animate, stagger } from 'animejs';

// Anime.js helpers. Every helper returns early when the visitor prefers reduced motion,
// so content is shown immediately with no movement.

export const prefersReducedMotion = (): boolean =>
  typeof window !== 'undefined' && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/** Fade and rise a set of elements in sequence. */
export function staggerIn(targets: Element | Element[] | NodeListOf<Element>, delay = 0): void {
  if (prefersReducedMotion()) return;
  animate(targets, {
    opacity: [0, 1],
    translateY: [24, 0],
    duration: 700,
    delay: stagger(90, { start: delay }),
    ease: 'outExpo',
  });
}

/** Slide each word of a heading up from behind a mask. */
export function wordsIn(targets: Element | Element[] | NodeListOf<Element>): void {
  if (prefersReducedMotion()) return;
  animate(targets, {
    translateY: ['110%', '0%'],
    opacity: [0, 1],
    duration: 900,
    delay: stagger(70, { start: 120 }),
    ease: 'outExpo',
  });
}

/** Subtle fade for page transitions. */
export function pageIn(target: Element): void {
  if (prefersReducedMotion()) return;
  animate(target, {
    opacity: [0, 1],
    translateY: [12, 0],
    duration: 450,
    ease: 'outQuad',
  });
}

/**
 * Scroll reveal for elements marked with [data-reveal].
 * Watches for elements added later (for example, content from a lazy-loaded route),
 * so nothing stays hidden. The CSS hides items only when html.js-motion is set.
 * Returns a cleanup function for React effects.
 */
export function observeReveals(root: HTMLElement): () => void {
  if (prefersReducedMotion() || !('IntersectionObserver' in window)) return () => {};

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        animate(entry.target, {
          opacity: [0, 1],
          translateY: [28, 0],
          duration: 800,
          ease: 'outExpo',
        });
        observer.unobserve(entry.target);
      });
    },
    { rootMargin: '0px 0px -10% 0px', threshold: 0.12 },
  );

  const watch = (node: Element) => {
    if (node.matches('[data-reveal]')) observer.observe(node);
    node.querySelectorAll<HTMLElement>('[data-reveal]').forEach((el) => observer.observe(el));
  };

  watch(root);

  const mutations = new MutationObserver((records) => {
    records.forEach((record) => {
      record.addedNodes.forEach((node) => {
        if (node instanceof Element) watch(node);
      });
    });
  });
  mutations.observe(root, { childList: true, subtree: true });

  return () => {
    mutations.disconnect();
    observer.disconnect();
  };
}
