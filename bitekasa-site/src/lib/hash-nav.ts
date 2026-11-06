import { useEffect } from 'react';

/**
 * In-page navigation, made explicit.
 *
 * The site links to sections as `#packs`, `#order` and so on. Left to the
 * browser alone that works only if the target already exists at the moment the
 * hash changes — which is not guaranteed in a client-rendered app, and not
 * guaranteed at all when the link carries the site base path
 * (`/hotmoon123/#packs`) instead of a bare fragment.
 *
 * This hook takes over both cases:
 *  - a click on any same-document hash link scrolls the section into view,
 *    moves focus to it (so keyboard and screen-reader users follow along) and
 *    updates the address bar without a reload;
 *  - a visit that already carries a hash — a shared link, a service page's
 *    "see the packs" button, or the back button — is resolved after render.
 */

const HEADER_OFFSET = 88;

function prefersReducedMotion(): boolean {
  return typeof window !== 'undefined' && Boolean(window.matchMedia?.('(prefers-reduced-motion: reduce)').matches);
}

function scrollToTarget(id: string, moveFocus: boolean): boolean {
  const target = document.getElementById(id);
  if (!target) return false;

  const smooth = !prefersReducedMotion();
  const top = window.scrollY + target.getBoundingClientRect().top - HEADER_OFFSET;
  window.scrollTo({ top: Math.max(top, 0), behavior: smooth ? 'smooth' : 'auto' });

  if (moveFocus) {
    // Sections are not focusable by default; make it so temporarily so the
    // next Tab starts from the section the visitor chose.
    if (!target.hasAttribute('tabindex')) {
      target.setAttribute('tabindex', '-1');
      target.addEventListener('blur', () => target.removeAttribute('tabindex'), { once: true });
    }
    target.focus({ preventScroll: true });
  }

  return true;
}

function idFromHash(hash: string): string {
  try {
    return decodeURIComponent(hash.replace(/^#/, ''));
  } catch {
    return hash.replace(/^#/, '');
  }
}

export default function useHashNavigation(): void {
  useEffect(() => {
    const go = (hash: string, moveFocus: boolean) => {
      const id = idFromHash(hash);
      if (!id) return;
      // Wait one frame so a section rendered by this navigation exists first.
      window.requestAnimationFrame(() => scrollToTarget(id, moveFocus));
    };

    const onClick = (event: MouseEvent) => {
      if (event.defaultPrevented || event.button !== 0) return;
      if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;

      const anchor = (event.target as Element | null)?.closest?.('a[href]') as HTMLAnchorElement | null;
      if (!anchor || anchor.target === '_blank' || anchor.hasAttribute('download')) return;

      let url: URL;
      try {
        url = new URL(anchor.href, window.location.href);
      } catch {
        return;
      }

      if (url.origin !== window.location.origin) return;
      if (url.pathname !== window.location.pathname || !url.hash) return;

      event.preventDefault();
      window.history.pushState(null, '', `${url.pathname}${url.hash}`);
      go(url.hash, true);
    };

    const onHashChange = () => go(window.location.hash, true);

    document.addEventListener('click', onClick);
    window.addEventListener('hashchange', onHashChange);

    if (window.location.hash) go(window.location.hash, false);

    return () => {
      document.removeEventListener('click', onClick);
      window.removeEventListener('hashchange', onHashChange);
    };
  }, []);
}
