import PageHeader from '../components/PageHeader';
import Section from '../components/Section';
import { experience } from '../data/experience';
import { site } from '../data/site';

export default function Experience() {
  return (
    <>
      <PageHeader
        eyebrow="Experience"
        title="Work and practical experience"
        lead="Paid roles, internships, academic work, and personal projects are labelled separately, so each is described accurately."
      >
        <p className="actions">
          <a className="btn btn-primary" href={site.cvUrl}>
            Download CV (PDF)
          </a>
        </p>
      </PageHeader>

      <Section id="timeline" title="Timeline" intro="Each entry gives the context, what I did, and the outcome.">
        <ol className="timeline timeline-wide">
          {experience.map((item) => (
            <li key={`${item.role}-${item.dates}`} className="timeline-item" data-reveal>
              <p className="small muted">
                {item.dates} · {item.type}
              </p>
              <h3>{item.role}</h3>
              <p className="muted">{item.organisation}</p>
              <p>
                <strong>Context.</strong> {item.context}
              </p>
              <p>
                <strong>What I did.</strong>
              </p>
              <ul className="check-list">
                {item.actions.map((action) => <li key={action}>{action}</li>)}
              </ul>
              <p>
                <strong>Outcome.</strong>
              </p>
              <ul className="check-list">
                {item.outcomes.map((outcome) => <li key={outcome}>{outcome}</li>)}
              </ul>
              <ul className="tags" aria-label="Technologies used">
                {item.tech.map((tech) => <li key={tech}>{tech}</li>)}
              </ul>
            </li>
          ))}
        </ol>
      </Section>
    </>
  );
}
