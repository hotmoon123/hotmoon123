import { Clock, Mail, MapPin, Phone } from 'lucide-react';
import { FaFacebookF, FaInstagram, FaLinkedinIn, FaXTwitter } from 'react-icons/fa6';
import { telLink } from '../lib/whatsapp';
import { SITE } from '../content';

export default function Contact() {
  return (
    <section className="section contact" id="contact" aria-labelledby="contact-title">
      <div className="wrap">
        <span className="kicker kicker--on-dark">Contact</span>
        <h2 className="section-title" id="contact-title" style={{ marginTop: '1rem', color: '#fff' }}>
          Come say <span className="accent" style={{ color: 'var(--cyan)' }}>hello.</span>
        </h2>

        <div className="contact-grid" style={{ marginTop: '2.5rem' }}>
          <div className="contact-block">
            <div className="contact-line">
              <span className="contact-label"><MapPin size={12} aria-hidden="true" style={{ display: 'inline', verticalAlign: '-1px' }} /> Visit</span>
              <a className="contact-value tel" href={SITE.mapsUrl} target="_blank" rel="noopener noreferrer">
                {SITE.addressDisplay}
                <small>Plus code {SITE.plusCode} · Open in Google Maps</small>
              </a>
            </div>

            <div className="contact-line">
              <span className="contact-label"><Phone size={12} aria-hidden="true" style={{ display: 'inline', verticalAlign: '-1px' }} /> Call / WhatsApp</span>
              <a className="contact-value tel" href={telLink(SITE.phoneMapsDisplay)}>
                {SITE.phoneMapsDisplay}
                <small>As listed on Google Maps · tap to call</small>
              </a>
              <a className="contact-value tel" href={telLink(SITE.phoneFbDisplay)} style={{ marginTop: '0.6rem' }}>
                {SITE.phoneFbDisplay}
                <small>As listed on Facebook · tap to call</small>
              </a>
            </div>

            <div className="contact-line">
              <span className="contact-label"><Mail size={12} aria-hidden="true" style={{ display: 'inline', verticalAlign: '-1px' }} /> Email</span>
              <a className="contact-value tel" href={`mailto:${SITE.email}`}>{SITE.email}</a>
            </div>

            <div className="contact-line" style={{ borderBottom: 0 }}>
              <span className="contact-label"><Clock size={12} aria-hidden="true" style={{ display: 'inline', verticalAlign: '-1px' }} /> Hours</span>
              <span className="contact-value" style={{ fontWeight: 400, color: 'var(--on-dark-soft)' }}>
                {SITE.hoursNote}
              </span>
            </div>

            <div className="socials" aria-label="Myst Water on social media">
              <a className="social" href={SITE.socials.instagram} target="_blank" rel="noopener noreferrer" aria-label="Myst Water on Instagram">
                <FaInstagram aria-hidden="true" size={20} />
              </a>
              <a className="social" href={SITE.socials.facebook} target="_blank" rel="noopener noreferrer" aria-label="Myst Water on Facebook">
                <FaFacebookF aria-hidden="true" size={18} />
              </a>
              <a className="social" href={SITE.socials.x} target="_blank" rel="noopener noreferrer" aria-label="Myst Water on X">
                <FaXTwitter aria-hidden="true" size={18} />
              </a>
              <a className="social" href={SITE.socials.linkedin} target="_blank" rel="noopener noreferrer" aria-label="PNF Industries Limited on LinkedIn">
                <FaLinkedinIn aria-hidden="true" size={18} />
              </a>
            </div>
          </div>

          <div className="map-frame">
            <iframe
              title="Myst Water on Google Maps"
              src={SITE.mapsEmbed}
              loading="lazy"
              referrerPolicy="no-referrer-when-downgrade"
              allowFullScreen
            />
          </div>
        </div>
      </div>
    </section>
  );
}
