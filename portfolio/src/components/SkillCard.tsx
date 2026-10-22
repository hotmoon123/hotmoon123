import type { Skill } from '../data/types';
import { projects } from '../data/projects';

/** One skill with its real evidence: the projects where it was used. */
export default function SkillCard({ skill }: { skill: Skill }) {
  const linked = projects.filter((project) => skill.projectIds.includes(project.id));

  return (
    <article className="card skill-card">
      <p className="eyebrow">{skill.kind}</p>
      <h3>{skill.name}</h3>
      <p>{skill.description}</p>
      <p className="small evidence">
        {linked.length > 0 ? (
          <>
            Used in:{' '}
            {linked.map((project, index) => (
              <span key={project.id}>
                {index > 0 && ', '}
                <a href={`#project-${project.id}`}>{project.title}</a>
              </span>
            ))}
          </>
        ) : (
          'No project yet.'
        )}
      </p>
    </article>
  );
}
