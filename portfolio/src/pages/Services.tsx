import { Link } from 'react-router-dom';
import PageHeader from '../components/PageHeader';
import Section from '../components/Section';
import { services } from '../data/experience';
import { site } from '../data/site';

const process = ['Requirements', 'Proposal', 'Development', 'Testing', 'Handover'];

export default function Services() {
  return (
    <>
      <PageHeader
        eyebrow="Services"
        title="What I can deliver"
        lead="Only work I can deliver reliably. If something is outside these areas, I will tell you."
      />

      <Section id="offers" title="Services">
        <ul className="card-grid service-grid">
          {services.map((service) => (
            <li key={service.name} className="card" data-reveal>
              <h3>{service.name}</h3>
              <p className="muted">{service.problem}</p>
              <p>
                <strong>Deliverables</strong>
              </p>
              <ul className="check-list">
                {service.deliverables.map((item) => <li key={item}>{item}</li>)}
              </ul>
            </li>
          ))}
        </ul>
      </Section>

      <Section id="process" title="How an engagement works" tone="alt">
        <ol className="process">
          {process.map((step) => (
            <li key={step} data-reveal>
              <span className="process-step">{step}</span>
            </li>
          ))}
        </ol>
        <p className="section-foot">
          Availability: {site.availability}
        </p>
      </Section>

      <Section id="quote" title="Ask for a quote">
        <p>
          Send a short brief to{' '}
          <a href={`mailto:${site.email}?subject=Project%20enquiry`}>{site.email}</a> with the goal, the users, and your timeline.
          Or <Link to="/contact">use the contact page</Link>.
        </p>
      </Section>
    </>
  );
}
