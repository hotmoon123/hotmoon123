import { Link } from 'react-router-dom';
import type { Project } from '../data/types';
import StatusBadge from './StatusBadge';

/** A project summary card. Uses a drawn placeholder when no screenshot has been added. */
export default function ProjectCard({ project }: { project: Project }) {
  return (
    <article className="card project-card" data-reveal>
      <Link to={`/projects/${project.slug}`} className="card-media" aria-label={`View ${project.title}`}>
        {project.image ? (
          <img src={project.image} alt={`Screenshot of ${project.title}`} loading="lazy" />
        ) : (
          <span className="media-placeholder" aria-hidden="true">
            <span className="media-glyph">{'</>'}</span>
          </span>
        )}
      </Link>
      <div className="card-body">
        <div className="card-meta">
          <StatusBadge status={project.status} />
          <span className="muted small">{project.year}</span>
        </div>
        <h3>
          <Link to={`/projects/${project.slug}`}>{project.title}</Link>
        </h3>
        <p>{project.summary}</p>
        <ul className="tags" aria-label="Technologies">
          {project.languages.map((language) => (
            <li key={language}>{language}</li>
          ))}
        </ul>
        <Link to={`/projects/${project.slug}`} className="text-link">
          View details <span aria-hidden="true">→</span>
        </Link>
      </div>
    </article>
  );
}
