import CopyEmail from '../components/CopyEmail';
import Section from '../components/Section';
import { profile } from '../data/profile';

export default function ContactSection() {
  return (
    <Section
      id="contact"
      number="07"
      label="Contact"
      title="Let's build something together."
      intro="For a project, a role or a question about my work, email me directly. This site has no contact form, so your message goes to your own email app."
      tone="dark"
    >
      <div className="contact-grid" data-reveal>
        <div>
          <p className="eyebrow">Email</p>
          <a className="contact-email" href={`mailto:${profile.email}`}>
            {profile.email}
          </a>
          <div className="actions">
            <a className="btn btn-primary" href={`mailto:${profile.email}?subject=Hello%20Caleb`}>
              Email me
            </a>
            <CopyEmail email={profile.email} />
          </div>
        </div>

        <div>
          <p className="eyebrow">Code</p>
          <p>
            <a className="text-link" href={profile.github} target="_blank" rel="noopener noreferrer">
              GitHub profile and repositories
              <span className="visually-hidden"> (opens in a new tab)</span> <span aria-hidden="true">↗</span>
            </a>
          </p>
        </div>
      </div>
    </Section>
  );
}
