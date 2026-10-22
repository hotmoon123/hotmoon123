import PageHeader from '../components/PageHeader';
import Section from '../components/Section';
import { site } from '../data/site';

// No form: this is a static site. A mailto link sends the message from the visitor's own email app.
export default function Contact() {
  return (
    <>
      <PageHeader
        eyebrow="Contact"
        title="Let's talk"
        lead="Tell me what you are building, who it is for, and your timeline. A short, specific message gets a faster reply."
      />

      <Section id="reach" title="Ways to reach me">
        <ul className="contact-list">
          <li>
            <span className="small muted">Email</span>
            <a href={`mailto:${site.email}`}>{site.email}</a>
          </li>
          <li>
            <span className="small muted">GitHub</span>
            <a href={site.links.github} rel="noopener noreferrer" target="_blank">
              {site.links.github}
            </a>
          </li>
          <li>
            <span className="small muted">LinkedIn</span>
            <a href={site.links.linkedin} rel="noopener noreferrer" target="_blank">
              {site.links.linkedin}
            </a>
          </li>
          <li>
            <span className="small muted">Location</span>
            <span>{site.location}</span>
          </li>
        </ul>
        <div className="actions">
          <a className="btn btn-primary" href={`mailto:${site.email}?subject=Project%20enquiry`}>
            Email me
          </a>
        </div>
      </Section>

      <Section id="expect" title="What to expect" tone="alt">
        <ul className="check-list">
          <li>Reply {site.responseTime}.</li>
          <li>Open to: {site.availability}</li>
          <li>If I cannot help, I will say so and point you to someone who can.</li>
        </ul>
      </Section>

      <Section id="privacy" title="Before you write">
        <p className="muted">
          This site has no contact form and stores nothing you type here. Your email app sends the message directly to me. I use your
          details only to reply.
        </p>
      </Section>
    </>
  );
}
