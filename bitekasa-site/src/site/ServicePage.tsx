import { ArrowRight, MessageCircle } from 'lucide-react';
import { SiInstagram } from 'react-icons/si';
import {
  INSTAGRAM_HANDLE,
  INSTAGRAM_URL,
  PREPARATIONS,
  SITE_BASE,
  type PreparationSlug,
} from '../data/catalogue';
import { whatsappHref } from '../lib/order';
import Header from './Header';
import Footer from './Footer';
import Reveal from './Reveal';

export default function ServicePage({ slug }: { slug: PreparationSlug }) {
  const page = PREPARATIONS.find((item) => item.slug === slug) ?? PREPARATIONS[0];
  const others = PREPARATIONS.filter((item) => item.slug !== slug);
  const message = `Hello BiteKasa! I would like to ask about ${page.slug} samosas and spring rolls. Please confirm current availability, pack options and product mix.`;

  return (
    <>
      <Header />
      <main id="main">
        <section className="bg-cream px-4 py-10 sm:px-7 sm:py-16 lg:px-12">
          <div className="mx-auto grid max-w-7xl items-center gap-8 md:grid-cols-2 md:gap-12">
            <Reveal>
              <a href={`${SITE_BASE}#home`} className="service-back-link">
                BiteKasa home <ArrowRight aria-hidden="true" size={14} />
              </a>
              <p className="eyebrow mt-5">PRODUCT PREPARATION OPTION</p>
              <h1 className="section-title mt-2">{page.title}.</h1>
              <p className="hero-description mt-4">{page.description}</p>
              <p className="image-disclosure mt-4">
                Illustrative image; not a verified BiteKasa product photograph.
              </p>
              <div className="hero-actions">
                <a className="whatsapp-button" href={whatsappHref(message)} target="_blank" rel="noopener noreferrer">
                  <MessageCircle aria-hidden="true" size={17} />
                  Ask about availability <ArrowRight aria-hidden="true" size={17} />
                </a>
                <a className="call-button" href={`${SITE_BASE}#packs`}>
                  View packs
                </a>
              </div>
            </Reveal>
            <Reveal>
              <img src={page.image} alt={page.alt} className="hero-image" />
              <p className="image-disclosure">Illustrative example</p>
            </Reveal>
          </div>
        </section>

        <section className="bg-paper px-4 py-10 sm:px-7 sm:py-14 lg:px-12">
          <div className="mx-auto max-w-7xl">
            <Reveal>
              <p className="eyebrow">EXPLORE PREPARATION OPTIONS</p>
              <h2 className="section-title mt-2">Other options to ask about.</h2>
              <p className="section-intro mt-3">
                Current stock, quantities, pack mix and collection or delivery details are confirmed directly with
                BiteKasa.
              </p>
            </Reveal>
            <div className="service-cross-links mt-7">
              {others.map((other) => (
                <a key={other.slug} href={`${SITE_BASE}services/${other.slug}/`}>
                  <span>{other.label} options</span>
                  <ArrowRight aria-hidden="true" size={16} />
                </a>
              ))}
              <a href={`${SITE_BASE}#packs`}>
                <span>View BiteKasa packs</span>
                <ArrowRight aria-hidden="true" size={16} />
              </a>
            </div>
          </div>
        </section>

        <section className="cta-section px-4 py-10 sm:px-7 sm:py-14 lg:px-12">
          <div className="mx-auto max-w-7xl">
            <p className="eyebrow eyebrow-light">CONFIRM BEFORE ORDERING</p>
            <h2 className="cta-title">
              Ask BiteKasa
              <br />
              about this option.
            </h2>
            <div className="hero-actions">
              <a className="whatsapp-button" href={whatsappHref(message)} target="_blank" rel="noopener noreferrer">
                <MessageCircle aria-hidden="true" size={17} />
                WhatsApp BiteKasa <ArrowRight aria-hidden="true" size={17} />
              </a>
              <a className="instagram-link" href={INSTAGRAM_URL} target="_blank" rel="noopener noreferrer">
                <SiInstagram aria-hidden="true" size={16} />
                Instagram · {INSTAGRAM_HANDLE}
              </a>
            </div>
          </div>
        </section>
      </main>
      <Footer />
    </>
  );
}
