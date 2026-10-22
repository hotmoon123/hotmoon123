import { Link, useParams } from 'react-router-dom';
import Section from '../components/Section';
import StatusBadge from '../components/StatusBadge';
import { getProject, projects } from '../data/projects';
import NotFound from './NotFound';

export default function ProjectDetails() {
  const { slug = '' } = useParams();
  const project = getProject(slug);
  if (!project) return <NotFound />;

  const index = projects.findIndex((item) => item.slug === project.slug);
  const previous = projects[(index - 1 + projects.length) % projects.length];
  const next = projects[(index + 1) % projects.length];

  return (
    <article>
      <header className="page-header">
        <div className="container">
          <p className="eyebrow">
            <Link to="/projects">Projects</Link> / {project.title}
          </p>
          <h1 className="page-title">{project.title}</h1>
          <p className="lead">{project.summary}</p>
          <div className="meta-row">
            <StatusBadge status={project.status} />
            <span className="muted">
              {project.year} · {project.role}
            </span>
          </div>
          <ul className="tags tags-large" aria-label="Technologies">
            {[...project.languages, ...project.tools].map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
          <div className="actions">
            {project.demoUrl && (
              <a className="btn btn-primary" href={project.demoUrl} rel="noopener noreferrer" target="_blank">
                Live demo
              </a>
            )}
            {project.repoUrl && (
              <a className="btn btn-ghost" href={project.repoUrl} rel="noopener noreferrer" target="_blank">
                Source code
              </a>
            )}
          </div>
        </div>
      </header>

      <Section id="overview" title="Problem and users">
        <p className="prose-wide">{project.problem}</p>
      </Section>

      <Section id="objectives" title="Objectives and features" tone="alt">
        <div className="two-col">
          <div>
            <h3>Objectives</h3>
            <ul className="check-list">
              {project.objectives.map((item) => <li key={item}>{item}</li>)}
            </ul>
          </div>
          <div>
            <h3>Features</h3>
            <ul className="check-list">
              {project.features.map((item) => <li key={item}>{item}</li>)}
            </ul>
          </div>
        </div>
      </Section>

      <Section id="architecture" title="Architecture and database">
        <div className="two-col">
          <div>
            <h3>Architecture</h3>
            <ol className="steps-list">
              {project.architecture.map((item) => <li key={item}>{item}</li>)}
            </ol>
          </div>
          <div>
            <h3>Database design</h3>
            {project.database.length > 0 ? (
              <ul className="check-list">
                {project.database.map((item) => <li key={item}>{item}</li>)}
              </ul>
            ) : (
              <p className="muted">This project does not use a database.</p>
            )}
          </div>
        </div>
      </Section>

      {project.codeSample && (
        <Section id="code" title="Code sample" intro={project.codeSample.title} tone="alt">
          <pre className="code-block" tabIndex={0} aria-label={`Code sample: ${project.codeSample.title}`}>
            <code className={`language-${project.codeSample.language}`}>{project.codeSample.code}</code>
          </pre>
        </Section>
      )}

      <Section id="decisions" title="Engineering decisions">
        <ul className="check-list">
          {project.decisions.map((item) => <li key={item}>{item}</li>)}
        </ul>
      </Section>

      <Section id="testing" title="Testing and security" tone="alt">
        <ul className="check-list">
          {project.testing.map((item) => <li key={item}>{item}</li>)}
        </ul>
      </Section>

      <Section id="results" title="Results and limitations">
        <div className="two-col">
          <div>
            <h3>Results</h3>
            <ul className="check-list">
              {project.results.map((item) => <li key={item}>{item}</li>)}
            </ul>
          </div>
          <div>
            <h3>Limitations</h3>
            <ul className="check-list">
              {project.limitations.map((item) => <li key={item}>{item}</li>)}
            </ul>
          </div>
        </div>
      </Section>

      <Section id="future" title="Future work" tone="alt">
        <ul className="check-list">
          {project.futureWork.map((item) => <li key={item}>{item}</li>)}
        </ul>
      </Section>

      <nav className="pager container" aria-label="Project navigation">
        <Link to={`/projects/${previous.slug}`} className="text-link">
          <span aria-hidden="true">←</span> {previous.title}
        </Link>
        <Link to={`/projects/${next.slug}`} className="text-link">
          {next.title} <span aria-hidden="true">→</span>
        </Link>
      </nav>
    </article>
  );
}
