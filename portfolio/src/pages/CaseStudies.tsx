import { Link } from 'react-router-dom';
import PageHeader from '../components/PageHeader';
import Section from '../components/Section';
import { projects } from '../data/projects';

// A case study is a deeper read of a project: the reasoning, not only the result.
export default function CaseStudies() {
  const studies = projects.filter((project) => project.hasCaseStudy);

  return (
    <>
      <PageHeader
        eyebrow="Case studies"
        title="How I approached the hard parts"
        lead="Each case study explains the constraints, the alternatives I considered, the decision I made, and what I would change."
      />

      <Section id="studies" title="Case studies">
        {studies.length > 0 ? (
          <div className="stack-list">
            {studies.map((project) => (
              <article key={project.slug} className="card study-card" data-reveal>
                <h3>
                  <Link to={`/projects/${project.slug}`}>{project.title}</Link>
                </h3>
                <p className="muted">{project.problem}</p>
                <h4>Decisions</h4>
                <ul className="check-list">
                  {project.decisions.map((item) => <li key={item}>{item}</li>)}
                </ul>
                <h4>Outcome</h4>
                <ul className="check-list">
                  {project.results.map((item) => <li key={item}>{item}</li>)}
                </ul>
              </article>
            ))}
          </div>
        ) : (
          <p className="muted">No case studies yet.</p>
        )}
      </Section>
    </>
  );
}
