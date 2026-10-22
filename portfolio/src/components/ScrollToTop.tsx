import { useEffect } from 'react';
import { useLocation } from 'react-router-dom';

// Reset scroll on route change, unless the URL targets an in-page anchor.
export default function ScrollToTop() {
  const { pathname, hash } = useLocation();
  useEffect(() => {
    if (hash) {
      document.getElementById(hash.slice(1))?.scrollIntoView();
      return;
    }
    window.scrollTo(0, 0);
  }, [pathname, hash]);
  return null;
}
