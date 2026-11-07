import { MessageCircle, Star, Store } from 'lucide-react';
import { asset } from '../lib/asset';
import { waLink } from '../lib/whatsapp';
import { SITE } from '../content';

export default function Hero() {
  const orderMessage =
    'Hello Myst Water! I would like to order Myst Water for delivery. Please confirm availability, price and delivery to my address.';

  return (
    <section className="hero" id="top" aria-labelledby="hero-title">
      <div className="wrap hero-inner">
        <div>
          <span className="kicker kicker--on-dark hero-kicker">Natural mineral water · Ghana</span>
          <h1 className="hero-title" id="hero-title">
            THE FEEL <span className="feel">GOOD</span> WATER.
          </h1>
          <p className="hero-sub">
            Myst Water is natural mineral water sourced from the Dodowa aquifer — purely sourced,
            bottled at the origin, and proudly made in Ghana by PNF Industries Limited. Delivered
            to your doorstep, the same way our happiest customers buy it.
          </p>
          <div className="hero-actions">
            <a href="#wholesale" className="btn btn--solid">
              <Store aria-hidden="true" size={18} />
              Become a stockist
            </a>
            <a
              href={waLink(SITE.phoneMapsIntl, orderMessage)}
              target="_blank"
              rel="noopener noreferrer"
              className="btn btn--ghost"
            >
              <MessageCircle aria-hidden="true" size={18} />
              Order on WhatsApp
            </a>
          </div>
          <p className="hero-note">
            5.0 on Google Maps · Doorstep delivery · Mobile Money accepted · Wholesale enquiries welcome
          </p>
        </div>

        <figure className="hero-figure">
          <img
            src={asset('assets/myst-dark-ice.jpg')}
            alt="Myst Water blue 500 ml bottle covered in condensation, on crushed ice with fresh mint"
            width={503}
            height={609}
            fetchPriority="high"
          />
          <figcaption className="hero-badge">
            <Star aria-hidden="true" size={14} fill="#ffd54a" color="#ffd54a" />
            <span className="stars" aria-hidden="true">★★★★★</span>
            <span>5.0 · 6 Google reviews</span>
          </figcaption>
        </figure>
      </div>
    </section>
  );
}
