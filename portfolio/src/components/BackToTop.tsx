import { useEffect, useState } from 'react';

/** Appears after the visitor scrolls far enough. Hidden (and not focusable) before that. */
export default function BackToTop() {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const onScroll = () => setVisible(window.scrollY > 800);
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  return (
    <a href="#home" className={`back-to-top${visible ? ' is-visible' : ''}`} aria-label="Back to top">
      <span aria-hidden="true">↑</span>
    </a>
  );
}
