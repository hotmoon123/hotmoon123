import { asset } from '../lib/asset';

export default function Footer() {
  const year = new Date().getFullYear();

  return (
    <footer className="site-footer">
      <div className="wrap footer-inner">
        <a href="#top" aria-label="Myst Water — back to top">
          <img src={asset('assets/myst-logo.jpg')} alt="Myst Water logo" className="footer-logo" width={60} height={37} />
        </a>

        <p className="concept-chip">
          <strong>Website concept for MYST WATER COMPANY.</strong> Prepared by Caleb Bentum as a
          private proposal — not an official website, and not affiliated until the company adopts it.
          “MYST”, “The Feel Good Water” and all imagery are the property of MYST WATER COMPANY /
          PNF Industries Limited.{' '}
          <a href="./privacy.html" style={{ color: '#fff', textDecoration: 'underline', textUnderlineOffset: 3 }}>
            Privacy
          </a>
        </p>

        <div className="footer-links" aria-label="Footer navigation">
          <a href="#range">Range</a>
          <a href="#wholesale">Stockists</a>
          <a href="#delivery">Delivery</a>
          <a href="#faq">FAQ</a>
        </div>
      </div>
      <div className="wrap" style={{ marginTop: '0.75rem' }}>
        <small>© {year} Myst Water (concept). Ghana. All rights reserved by their respective owners.</small>
      </div>
    </footer>
  );
}
