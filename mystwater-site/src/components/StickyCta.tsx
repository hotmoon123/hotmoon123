import { MessageCircle, Store } from 'lucide-react';
import { waLink } from '../lib/whatsapp';
import { SITE } from '../content';

export default function StickyCta() {
  return (
    <div className="sticky-cta" role="region" aria-label="Quick actions">
      <a className="sticky-primary" href="#wholesale">
        <Store aria-hidden="true" size={17} />
        Become a stockist
      </a>
      <a
        className="sticky-secondary"
        href={waLink(SITE.phoneFbIntl, 'Hello Myst Water! I would like to order Myst Water for delivery.')}
        target="_blank"
        rel="noopener noreferrer"
        aria-label="Order on WhatsApp"
      >
        <MessageCircle aria-hidden="true" size={17} />
        WhatsApp
      </a>
    </div>
  );
}
