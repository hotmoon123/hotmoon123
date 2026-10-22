import PageHeader from '../components/PageHeader';
import Section from '../components/Section';
import { education } from '../data/experience';
import { projects } from '../data/projects';
import { site } from '../data/site';
import { skills } from '../data/skills';

export default function Resume() {
  return (
    <>
      <PageHeader eyebrow="Resume" title={site.role} lead={site.tagline}>
        <div className="actions">
          <a className="btn btn-primary" href={site.cvUrl} download>
            Download resume (PDF)
          </a>
          <a className="btn btn-ghost" href={`mailto:${site.email}`}>
            Contact me
          </a>
        </div>
      </PageHeader>

      <Section id="summary" title="Professional summary">
        <p className="prose-wide">
          [Three sentences: what you build, the languages you use with evidence, and what you are looking for next.]
        </p>
      </Section>

      <Section id="skills" title="Technical skills" tone="alt">
        <ul className="tags tags-large" aria-label="Skills">
          {skills.flatMap((skill) => (skill.group === 'Practice' ? [] : [skill.name])).map((name) => (
            <li key={name}>{name}</li>
          ))}
        </ul>
      </Section>

      <Section id="projects" title="Selected projects">
        <ul className="check-list">
          {projects.map((project) => (
            <li key={project.slug}>
              {project.title} · {project.status} · {project.languages.join(', ')}
            </li>
          ))}
        </ul>
      </Section>

      <Section id="education" title="Education" tone="alt">
        <ul className="check-list">
          {education.map((item) => (
            <li key={item.qualification}>
              {item.qualification}, {item.institution} ({item.dates}, {item.status.toLowerCase()})
            </li>
          ))}
        </ul>
      </Section>

      <Section id="pdf" title="Downloadable PDF">
        <p className="muted">
          The PDF is the document to send to employers. Keep it consistent with this page. Replace <code>public/resume.pdf</code> whenever
          you update it, and rebuild the site.
        </p>
      </Section>
    </>
  );
}
