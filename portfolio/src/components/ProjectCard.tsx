import { useId, useState } from 'react';
import type { Project } from '../data/types';
import StatusBadge from './StatusBadge';

/** A project summary with an accessible disclosure for its case-study details. */
export default function ProjectCard({ project }: { project: Project }) {
  const [open, setOpen] = useState(false);
  const panelId = useId();

  return (
    <article id={`project-${project.id}`} className="card project-card" data-reveal>
      <div className="project-media">
        {project.image ? (
          <img src={project.image} alt={project.imageAlt ?? ''} loading="lazy" width={640} height={360} />
        ) : (
          <span className="media-label" aria-hidden="true">
            {project.mediaLabel}
          </span>
        )}
      </div>

      <div className="project-body">
        <div className="project-meta">
          <StatusBadge status={project.status} />
          <span className="small muted">{project.period}</span>
        </div>
        <h3>{project.title}</h3>
        <p className="project-role">{project.role}</p>
        <p>{project.summary}</p>

        {project.stack.length > 0 ? (
          <ul className="tags" aria-label={`Technologies in ${project.title}`}>
            {project.stack.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        ) : (
          <p className="small muted">Technology to be confirmed.</p>
        )}

        <button
          type="button"
          className="text-button"
          aria-expanded={open}
          aria-controls={panelId}
          onClick={() => setOpen((value) => !value)}
        >
          {open ? 'Hide details' : 'Show details'} <span aria-hidden="true">{open ? '↑' : '↓'}</span>
        </button>

        <div id={panelId} className="project-details" hidden={!open}>
          <h4>The problem</h4>
          <p>{project.problem}</p>
          <h4>My contribution</h4>
          <p>{project.contribution}</p>
          <h4>{project.featuresLabel}</h4>
          <ul className="check-list">
            {project.features.map((feature) => (
              <li key={feature}>{feature}</li>
            ))}
          </ul>
          {project.links.map((link) => (
            <p key={link.url}>
              <a className="text-link" href={link.url} target="_blank" rel="noopener noreferrer">
                {link.label}
                <span className="visually-hidden"> (opens in a new tab)</span> <span aria-hidden="true">↗</span>
              </a>
            </p>
          ))}
        </div>
      </div>
    </article>
  );
}
