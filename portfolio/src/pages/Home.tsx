import { Link } from 'react-router-dom';
import AnimatedWords from '../components/AnimatedWords';
import ProjectCard from '../components/ProjectCard';
import Section from '../components/Section';
import HeroScene from '../three/HeroScene';
import { experience } from '../data/experience';
import { projects } from '../data/projects';
import { site } from '../data/site';
import { skills } from '../data/skills';
import { prefersReducedMotion } from '../animations/motion';

const featured = projects.filter((project) => project.featured);
const stack = skills.filter((skill) => skill.group === 'Language' || skill.group === 'Database');
const highlights = experience.slice(0, 2);

const interests = [
  { title: 'Backend systems', text: 'Routes, validation, and database design that stay correct when inputs are messy.' },
  { title: 'Automation', text: 'Scripts that remove repetitive work and report what they did.' },
  { title: 'Algorithms', text: 'Implementations I can explain, test, and analyse for time and memory.' },
];

export default function Home() {
  return (
    <>
      <section className="hero" aria-labelledby="hero-title">
        <div className="container hero-grid">
          <div className="hero-copy">
            <p className="eyebrow">{site.role}</p>
            <h1 id="hero-title" className="hero-title">
              <AnimatedWords text={`Hi, I'm ${site.name}.`} />
            </h1>
            <p className="hero-lede">
              {site.tagline}
            </p>
            <div className="actions">
              <Link to="/projects" className="btn btn-primary">
                Explore projects
              </Link>
              <Link to="/contact" className="btn btn-ghost-light">
                Contact me
              </Link>
            </div>
          </div>
          <HeroScene />
        </div>
        {prefersReducedMotion() && <span className="visually-hidden">Animation is disabled by your system settings.</span>}
      </section>

      <Section id="stack" title="Technology stack" intro="The four languages I use most. Each one links to the skills page.">
        <ul className="stack-grid">
          {stack.map((skill) => (
            <li key={skill.id} className="card stack-card" data-reveal>
              <h3>
                <Link to={`/skills#${skill.id}`}>{skill.name}</Link>
              </h3>
              <p className="muted">{skill.summary}</p>
            </li>
          ))}
        </ul>
      </Section>

      <Section id="featured" title="Featured projects" intro="Three projects chosen for relevance. Each has a case study page.">
        <div className="card-grid">
          {featured.map((project) => (
            <ProjectCard key={project.slug} project={project} />
          ))}
        </div>
        <p className="section-foot">
          <Link to="/projects" className="text-link">
            All projects <span aria-hidden="true">→</span>
          </Link>
        </p>
      </Section>

      <Section id="interests" title="What I enjoy building" tone="alt">
        <ul className="interest-grid">
          {interests.map((item) => (
            <li key={item.title} className="interest" data-reveal>
              <h3>{item.title}</h3>
              <p className="muted">{item.text}</p>
            </li>
          ))}
        </ul>
      </Section>

      <Section id="experience" title="Experience highlights" intro="The most relevant entries. The full timeline is on the Experience page.">
        <ol className="timeline">
          {highlights.map((item) => (
            <li key={`${item.role}-${item.dates}`} className="timeline-item" data-reveal>
              <p className="small muted">
                {item.dates} · {item.type}
              </p>
              <h3>{item.role}</h3>
              <p className="muted">{item.organisation}</p>
            </li>
          ))}
        </ol>
        <p className="section-foot">
          <Link to="/experience" className="text-link">
            Full experience <span aria-hidden="true">→</span>
          </Link>
        </p>
      </Section>

      <section className="cta-band" aria-labelledby="cta-title">
        <div className="container cta-inner" data-reveal>
          <h2 id="cta-title">Have a project or role in mind?</h2>
          <p>Tell me what you are building and when you need it. I reply {site.responseTime}.</p>
          <div className="actions">
            <Link to="/contact" className="btn btn-primary">
              Start a conversation
            </Link>
            <a className="btn btn-ghost-light" href={`mailto:${site.email}`}>
              {site.email}
            </a>
          </div>
        </div>
      </section>
    </>
  );
}
