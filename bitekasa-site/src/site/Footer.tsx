import { SITE_BASE } from '../data/catalogue';

export default function Footer() {
  return (
    <footer className="site-footer px-4 py-5 sm:px-7 lg:px-12">
      <div className="mx-auto flex max-w-7xl flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
        <a href={`${SITE_BASE}#home`} className="footer-brand">
          BiteKasa
        </a>
        <p className="footer-note">
          Pack details, quantities and product condition are confirmed when you order. Food photographs are
          illustrative.
        </p>
        <small className="footer-copyright">© 2026 BiteKasa.</small>
      </div>
    </footer>
  );
}
