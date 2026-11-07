import { useEffect, useState } from 'react';
import { Menu, Store, X } from 'lucide-react';
import { asset } from '../lib/asset';
import { NAV_ITEMS } from '../content';

export default function Header() {
  const [open, setOpen] = useState(false);
  const close = () => setOpen(false);

  useEffect(() => {
    const onKey = (event: KeyboardEvent) => {
      if (event.key === 'Escape') setOpen(false);
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, []);

  return (
    <header className="site-header">
      <div className="wrap header-inner">
        <a href="#top" onClick={close} aria-label="Myst Water — home" className="flex items-center">
          <img src={asset('assets/myst-logo.jpg')} alt="Myst Water logo" className="brand-logo" width={120} height={72} />
        </a>

        <nav className="hidden items-center gap-6 lg:flex" aria-label="Main navigation">
          {NAV_ITEMS.map((item) => (
            <a key={item.href} href={item.href} className="nav-link">
              {item.label}
            </a>
          ))}
        </nav>

        <a href="#wholesale" className="header-cta hidden lg:inline-flex">
          <Store aria-hidden="true" size={16} />
          Become a stockist
        </a>

        <button
          type="button"
          className="menu-toggle lg:hidden"
          aria-label={open ? 'Close menu' : 'Open menu'}
          aria-expanded={open}
          aria-controls="mobile-menu"
          onClick={() => setOpen((v) => !v)}
        >
          {open ? <X aria-hidden="true" size={20} /> : <Menu aria-hidden="true" size={20} />}
        </button>
      </div>

      {open && (
        <nav id="mobile-menu" className="mobile-menu lg:hidden" aria-label="Mobile navigation">
          {NAV_ITEMS.map((item) => (
            <a key={item.href} href={item.href} onClick={close} className="mobile-nav-link">
              {item.label}
            </a>
          ))}
          <a href="#wholesale" onClick={close} className="mobile-menu-cta">
            <Store aria-hidden="true" size={16} />
            Become a stockist
          </a>
        </nav>
      )}
    </header>
  );
}
