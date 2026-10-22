import { Link } from 'react-router-dom';
import PageHeader from '../components/PageHeader';
import Section from '../components/Section';
import { site } from '../data/site';

const principles = [
  { title: 'Correctness first', text: 'I write the failure paths before the happy path, and test both.' },
  { title: 'Security by default', text: 'Validate input on the server, use prepared statements, and never trust the client.' },
  { title: 'Maintainability', text: 'Small functions, clear names, and a short README beat clever code nobody else can change.' },
];

export default function About() {
  return (
    <>
      <PageHeader
        eyebrow="About"
        title="How I got here and how I work"
        lead="[One paragraph in your own voice: what you do now and what you want to build next.]"
      />

      <Section id="journey" title="My journey" intro="How I became interested in software engineering.">
        <div className="prose">
          <p>[How you became interested in programming. Be specific: a course, a problem, or a first project that worked.]</p>
          <p>[The turning point that shaped your focus on databases, back-end work, or systems.]</p>
        </div>
      </Section>

      <Section id="philosophy" title="Engineering philosophy" tone="alt">
        <ul className="principle-grid">
          {principles.map((item) => (
            <li key={item.title} className="card" data-reveal>
              <h3>{item.title}</h3>
              <p className="muted">{item.text}</p>
            </li>
          ))}
        </ul>
      </Section>

      <Section id="goals" title="Goals and learning" intro="Where I want to contribute, and what I am learning now.">
        <div className="two-col">
          <div className="prose">
            <h3>Career goals</h3>
            <p>[The kind of engineering role or project you are aiming for, and why.]</p>
          </div>
          <div className="prose">
            <h3>Currently learning</h3>
            <ul className="check-list">
              <li>[Topic and the project you are using to learn it]</li>
              <li>[Second topic]</li>
            </ul>
          </div>
        </div>
      </Section>

      <Section id="next" title="Where to go next">
        <p className="cta-line">
          <Link to="/projects" className="text-link">
            See the projects <span aria-hidden="true">→</span>
          </Link>{' '}
          <Link to="/experience" className="text-link">
            Experience <span aria-hidden="true">→</span>
          </Link>{' '}
          <a href={`mailto:${site.email}`} className="text-link">
            Email me <span aria-hidden="true">→</span>
          </a>
        </p>
      </Section>
    </>
  );
}
