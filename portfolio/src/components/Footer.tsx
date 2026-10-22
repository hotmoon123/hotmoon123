import { profile } from '../data/profile';

export default function Footer() {
  const year = new Date().getFullYear();
  return (
    <footer className="site-footer theme-dark">
      <div className="container footer-inner">
        <p>
          © {year} {profile.copyrightHolder}. All rights reserved.
        </p>
        <ul className="footer-links" aria-label="Footer">
          <li>
            <a href={`mailto:${profile.email}`}>Email</a>
          </li>
          <li>
            <a href={profile.github} target="_blank" rel="noopener noreferrer">
              GitHub<span className="visually-hidden"> (opens in a new tab)</span>
            </a>
          </li>
          <li>
            <a href="#home">Back to top</a>
          </li>
        </ul>
      </div>
    </footer>
  );
}
