import { ArrowRight, Check } from 'lucide-react';
import { PACKS, SITE_BASE, cedi, packContents, packUnitPrice } from '../data/catalogue';
import { whatsappHref } from '../lib/order';
import Reveal from './Reveal';

export default function Packs() {
  return (
    <section id="packs" className="bg-paper px-4 py-14 sm:px-7 sm:py-20 lg:px-12 lg:py-24">
      <div className="mx-auto max-w-7xl">
        <Reveal className="section-heading-row">
          <div>
            <p className="eyebrow">THE PACKS</p>
            <h2 className="section-title">Three sizes. No surprises.</h2>
          </div>
          <p className="section-intro">
            Every price below is what BiteKasa charges. Ask about fried, unfried and frozen options when you order.
          </p>
        </Reveal>

        <div className="grid gap-3 sm:grid-cols-3 sm:gap-4">
          {PACKS.map((pack, index) => (
            <Reveal key={pack.id} delay={index * 0.06} className={`product-pack ${pack.className}`}>
              <h3 className="pack-name">{pack.name}</h3>
              <p className="pack-price">{cedi(pack.price)}</p>
              <p className="pack-description">{packContents(pack)}</p>
              <p className="pack-unit">{cedi(Math.round(packUnitPrice(pack) * 100) / 100)} per piece</p>
              <ul className="pack-points">
                <li>
                  <Check aria-hidden="true" size={14} /> Fried, unfried or frozen — ask what is available
                </li>
                <li>
                  <Check aria-hidden="true" size={14} /> Collection or delivery agreed on WhatsApp
                </li>
              </ul>
              <a
                href={whatsappHref(
                  `Hello BiteKasa! I am interested in the ${pack.name} pack: ${cedi(pack.price)}, ${packContents(pack)}. Please confirm current availability and product condition.`,
                )}
                target="_blank"
                rel="noopener noreferrer"
                className="pack-link"
                aria-label={`Ask about the ${pack.name} pack on WhatsApp`}
              >
                Ask about this pack <ArrowRight aria-hidden="true" size={16} />
              </a>
            </Reveal>
          ))}
        </div>

        <Reveal className="packs-cta-row">
          <a className="whatsapp-button" href={`${SITE_BASE}#order`}>
            Build your order <ArrowRight aria-hidden="true" size={17} />
          </a>
          <p className="product-state-note">
            Prices are fixed. Quantities and product condition are confirmed before you pay.
          </p>
        </Reveal>
      </div>
    </section>
  );
}
