import Section from '../components/Section';
import { profile } from '../data/profile';

export default function AboutSection() {
  return (
    <Section id="about" number="02" label="About" title="A little about me." tone="light">
      <div className="about-grid">
        <div className="prose" data-reveal>
          {profile.bio.map((paragraph) => (
            <p key={paragraph}>{paragraph}</p>
          ))}
          <p className="small muted">
            {profile.university} · {profile.programme}
          </p>
        </div>

        <figure className="code-figure" data-reveal>
          <div className="code-bar" aria-hidden="true">
            <span />
            <span />
            <span />
          </div>
          <pre className="code-block">
            <code>
              <span className="tok-k">const</span> engineer = {'{'}
              {'\n'}  name: <span className="tok-s">&quot;{profile.name}&quot;</span>,
              {'\n'}  study: <span className="tok-s">&quot;{profile.programme}&quot;</span>,
              {'\n'}  languages: [{profile.languages.map((item, index) => (
                <span key={item}>
                  {index > 0 && ', '}
                  <span className="tok-s">&quot;{item}&quot;</span>
                </span>
              ))}],
              {'\n'}  currently: <span className="tok-s">&quot;Building StitchLedger&quot;</span>,
              {'\n'}{'}'};
            </code>
          </pre>
          <figcaption className="visually-hidden">A code snippet summarising Caleb Bentum’s study and languages.</figcaption>
        </figure>
      </div>
    </Section>
  );
}
