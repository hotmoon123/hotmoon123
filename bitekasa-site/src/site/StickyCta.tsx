import { Calculator, MessageCircle } from 'lucide-react';
import { SITE_BASE } from '../data/catalogue';
import { whatsappHref } from '../lib/order';

/**
 * Mobile-only action bar. Two choices that matter on a small screen:
 * build an order, or go straight to WhatsApp.
 */
export default function StickyCta() {
  return (
    <div className="sticky-cta" role="region" aria-label="Quick order actions">
      <a className="sticky-cta-primary" href={`${SITE_BASE}#order`}>
        <Calculator aria-hidden="true" size={17} />
        Build order
      </a>
      <a
        className="sticky-cta-secondary"
        href={whatsappHref('Hello BiteKasa! I would like to ask about your packs and current availability.')}
        target="_blank"
        rel="noopener noreferrer"
      >
        <MessageCircle aria-hidden="true" size={17} />
        WhatsApp
      </a>
    </div>
  );
}
