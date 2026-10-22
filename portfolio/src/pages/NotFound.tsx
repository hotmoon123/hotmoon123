import { Link } from 'react-router-dom';

/** Custom 404 with a small inline illustration. Also used for unknown project slugs. */
export default function NotFound() {
  return (
    <section className="not-found">
      <div className="container not-found-inner">
        <svg className="not-found-art" viewBox="0 0 160 120" aria-hidden="true" focusable="false">
          <rect x="22" y="18" width="116" height="84" rx="8" fill="none" stroke="currentColor" strokeWidth="3" />
          <path d="M22 36 H138" stroke="currentColor" strokeWidth="3" />
          <path d="M64 58 L96 90 M96 58 L64 90" stroke="#1d4ed8" strokeWidth="5" strokeLinecap="round" />
        </svg>
        <p className="eyebrow">Error 404</p>
        <h1 className="page-title">This page does not exist.</h1>
        <p className="lead">The link may be old, or the address may contain a typo.</p>
        <div className="actions">
          <Link to="/" className="btn btn-primary">
            Go home
          </Link>
          <Link to="/projects" className="btn btn-ghost">
            See projects
          </Link>
          <Link to="/contact" className="btn btn-ghost">
            Contact me
          </Link>
        </div>
      </div>
    </section>
  );
}
