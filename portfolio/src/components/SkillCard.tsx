import { Link } from 'react-router-dom';
import type { Skill } from '../data/types';
import { projects } from '../data/projects';

/** A skill card with what you can do and links to the projects that show it. */
export default function SkillCard({ skill }: { skill: Skill }) {
  const evidence = projects.filter((project) => skill.projectSlugs.includes(project.slug));
  return (
    <article className="card skill-card" id={skill.id} data-reveal>
      <h3>{skill.name}</h3>
      <p className="muted">{skill.summary}</p>
      <ul className="check-list">
        {skill.capabilities.map((capability) => (
          <li key={capability}>{capability}</li>
        ))}
      </ul>
      {evidence.length > 0 && (
        <p className="evidence">
          Evidence:{' '}
          {evidence.map((project, index) => (
            <span key={project.slug}>
              <Link to={`/projects/${project.slug}`}>{project.title}</Link>
              {index < evidence.length - 1 ? ', ' : ''}
            </span>
          ))}
        </p>
      )}
    </article>
  );
}
