import { useMemo, useState } from 'react';
import PageHeader from '../components/PageHeader';
import ProjectCard from '../components/ProjectCard';
import Section from '../components/Section';
import { projects } from '../data/projects';
import type { Language } from '../data/types';

const filters: ('All' | Language)[] = ['All', 'Python', 'PHP', 'MySQL', 'C++'];

export default function Projects() {
  const [filter, setFilter] = useState<'All' | Language>('All');

  const visible = useMemo(
    () => (filter === 'All' ? projects : projects.filter((project) => project.languages.includes(filter))),
    [filter],
  );

  return (
    <>
      <PageHeader
        eyebrow="Projects"
        title="Selected work"
        lead="Each project states its status honestly. Open one to see the problem, the decisions, and the limits."
      />

      <Section id="all-projects" title="All projects">
        <div className="filter-bar" role="group" aria-label="Filter projects by language">
          {filters.map((item) => (
            <button
              key={item}
              type="button"
              className="filter-btn"
              aria-pressed={filter === item}
              onClick={() => setFilter(item)}
            >
              {item}
            </button>
          ))}
        </div>

        {visible.length > 0 ? (
          <div className="card-grid" aria-live="polite">
            {visible.map((project) => (
              <ProjectCard key={project.slug} project={project} />
            ))}
          </div>
        ) : (
          <div className="empty-state" role="status">
            <p>No project uses {filter} yet.</p>
            <button type="button" className="btn btn-ghost" onClick={() => setFilter('All')}>
              Show all projects
            </button>
          </div>
        )}
      </Section>
    </>
  );
}
