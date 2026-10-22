import PageHeader from '../components/PageHeader';
import Section from '../components/Section';
import { certifications, education } from '../data/experience';
import { site } from '../data/site';

export default function Education() {
  return (
    <>
      <PageHeader
        eyebrow="Education"
        title="Academic background and training"
        lead="A qualification, a course, and a certificate are different things. Each is labelled with its real status."
      />

      <Section id="qualifications" title="Qualifications">
        <ol className="timeline timeline-wide">
          {education.map((item) => (
            <li key={item.qualification} className="timeline-item" data-reveal>
              <p className="small muted">
                {item.dates} · <span className={item.status === 'Completed' ? 'badge badge-deployed' : 'badge badge-in-progress'}>{item.status}</span>
              </p>
              <h3>{item.qualification}</h3>
              <p className="muted">{item.institution}</p>
              <p>
                <strong>Relevant coursework</strong>
              </p>
              <ul className="check-list">
                {item.coursework.map((course) => <li key={course}>{course}</li>)}
              </ul>
            </li>
          ))}
        </ol>
      </Section>

      <Section id="certifications" title="Certifications" intro="Completed certificates only." tone="alt">
        {certifications.length > 0 ? (
          <ul className="check-list">
            {certifications.map((cert) => (
              <li key={cert.title}>
                {cert.title}, {cert.issuer}, {cert.date}
                {cert.verifyUrl && (
                  <>
                    {' '}
                    <a href={cert.verifyUrl} rel="noopener noreferrer" target="_blank">
                      Verify
                    </a>
                  </>
                )}
              </li>
            ))}
          </ul>
        ) : (
          <p className="muted">No completed certificates listed yet. <a href={`mailto:${site.email}`}>Ask me</a> about current training.</p>
        )}
      </Section>
    </>
  );
}
