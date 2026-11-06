import { ArrowRight, MessageCircle, Phone } from 'lucide-react';
import { SiInstagram } from 'react-icons/si';
import { INSTAGRAM_HANDLE, INSTAGRAM_URL, PHONES } from '../data/catalogue';
import { whatsappHref } from '../lib/order';
import Reveal from './Reveal';

export default function ContactCta() {
  return (
    <section id="contact" className="cta-section px-4 py-16 sm:px-7 sm:py-20 lg:px-12 lg:py-24">
      <div className="mx-auto grid max-w-7xl gap-6 md:grid-cols-[1fr_0.9fr] md:items-center">
        <Reveal>
          <p className="eyebrow eyebrow-light">CONTACT BITEKASA</p>
          <h2 className="cta-title">
            Let’s talk
            <br />
            snack time.
          </h2>
          <p className="cta-copy">Ask about the packs, current availability and how you would like to receive them.</p>
        </Reveal>

        <Reveal delay={0.05} className="cta-actions">
          <a
            className="whatsapp-button cta-whatsapp"
            href={whatsappHref('Hello BiteKasa! I would like to ask about your packs and current availability.')}
            target="_blank"
            rel="noopener noreferrer"
          >
            <MessageCircle aria-hidden="true" size={17} />
            Order on WhatsApp <ArrowRight aria-hidden="true" size={17} />
          </a>

          {PHONES.map((phone) => (
            <a className="phone-link" key={phone.label} href={phone.href}>
              <Phone aria-hidden="true" size={16} />
              <strong>{phone.label}</strong>
              <ArrowRight aria-hidden="true" size={16} />
            </a>
          ))}

          <a className="instagram-link" href={INSTAGRAM_URL} target="_blank" rel="noopener noreferrer">
            <SiInstagram aria-hidden="true" size={16} />
            Instagram · {INSTAGRAM_HANDLE} <ArrowRight aria-hidden="true" size={16} />
          </a>
        </Reveal>
      </div>
    </section>
  );
}
