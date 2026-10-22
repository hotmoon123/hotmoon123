import { Link } from 'react-router-dom';
import { primaryNav, secondaryNav, site } from '../data/site';

export default function Footer() {
  const year = new Date().getFullYear();
  return (
    <footer className="site-footer">
      <div className="container footer-grid">
        <div>
          <p className="footer-name">{site.name}</p>
          <p className="muted">{site.tagline}</p>
        </div>

        <nav aria-label="Footer">
          <ul className="footer-links">
            {[...primaryNav, ...secondaryNav].map((item) => (
              <li key={item.to}>
                <Link to={item.to}>{item.label}</Link>
              </li>
            ))}
          </ul>
        </nav>

        <div>
          <ul className="footer-links">
            <li>
              <a href={`mailto:${site.email}`}>{site.email}</a>
            </li>
            <li>
              <a href={site.links.github} rel="noopener noreferrer" target="_blank">
                GitHub
              </a>
            </li>
            <li>
              <a href={site.links.linkedin} rel="noopener noreferrer" target="_blank">
                LinkedIn
              </a>
            </li>
          </ul>
        </div>
      </div>
      <div className="container footer-base">
        <p>
          © {year} {site.name}. Built with React, TypeScript, Anime.js and Three.js.
        </p>
        <a href="#top">Back to top ↑</a>
      </div>
    </footer>
  );
}
