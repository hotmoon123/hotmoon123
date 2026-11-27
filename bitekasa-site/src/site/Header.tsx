import { useEffect, useState } from 'react';
import { Menu, MessageCircle, X } from 'lucide-react';
import { SITE_BASE } from '../data/catalogue';
import { whatsappHref } from '../lib/order';
import ResponsiveImage from './ResponsiveImage';

const OPENING_MESSAGE = 'Hello BiteKasa! I would like to ask about your packs and current availability.';

export const NAV_ITEMS = [
  { label: 'Packs', href: `${SITE_BASE}#packs` },
  { label: 'Build an order', href: `${SITE_BASE}#order` },
  { label: 'Questions', href: `${SITE_BASE}#questions` },
  { label: 'Contact', href: `${SITE_BASE}#contact` },
];

export default function Header() {
  const [open, setOpen] = useState(false);
  const closeMenu = () => setOpen(false);

  useEffect(() => {
    const handleKey = (event: KeyboardEvent) => {
      if (event.key === 'Escape') setOpen(false);
    };
    window.addEventListener('keydown', handleKey);
    return () => window.removeEventListener('keydown', handleKey);
  }, []);

  return (
    <header className="site-header">
      <div className="header-inner mx-auto max-w-7xl px-4 sm:px-7 lg:px-12">
        <a href={`${SITE_BASE}#home`} onClick={closeMenu} aria-label="BiteKasa home" className="flex items-center">
          <ResponsiveImage
            name="bitekasa-logo"
            alt="BiteKasa BITES logo"
            className="brand-logo"
            sizes="48px"
            width={96}
            height={96}
            priority
          />
        </a>

        <nav className="hidden items-center gap-6 md:flex" aria-label="Main navigation">
          {NAV_ITEMS.map((item) => (
            <a key={item.href} href={item.href} className="nav-link">
              {item.label}
            </a>
          ))}
          <a
            href={whatsappHref(OPENING_MESSAGE)}
            target="_blank"
            rel="noopener noreferrer"
            className="header-cta"
          >
            <MessageCircle aria-hidden="true" size={16} />
            Order on WhatsApp
          </a>
        </nav>

        <button
          type="button"
          className="menu-toggle md:hidden"
          aria-label={open ? 'Close navigation' : 'Open navigation'}
          aria-expanded={open}
          aria-controls="mobile-menu"
          onClick={() => setOpen((current) => !current)}
        >
          {open ? <X aria-hidden="true" size={20} strokeWidth={1.8} /> : <Menu aria-hidden="true" size={20} strokeWidth={1.8} />}
        </button>
      </div>

      {open && (
        <nav
          id="mobile-menu"
          aria-label="Mobile navigation"
          className="mobile-nav-panel overflow-hidden border-t border-[color:var(--line)] px-4 md:hidden"
        >
          <div className="flex flex-col gap-1 py-2">
            {NAV_ITEMS.map((item) => (
              <a key={item.href} href={item.href} onClick={closeMenu} className="mobile-nav-link">
                {item.label}
              </a>
            ))}
            <a
              href={whatsappHref(OPENING_MESSAGE)}
              target="_blank"
              rel="noopener noreferrer"
              onClick={closeMenu}
              className="mobile-menu-cta"
            >
              <MessageCircle aria-hidden="true" size={16} />
              Order on WhatsApp
            </a>
          </div>
        </nav>
      )}
    </header>
  );
}
