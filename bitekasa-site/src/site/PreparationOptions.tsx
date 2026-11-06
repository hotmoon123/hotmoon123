import { ArrowRight } from 'lucide-react';
import { PREPARATIONS, SITE_BASE } from '../data/catalogue';
import Reveal from './Reveal';

export default function PreparationOptions() {
  return (
    <section id="preparations" className="bg-paper px-4 py-14 sm:px-7 sm:py-20 lg:px-12 lg:py-24">
      <div className="mx-auto max-w-7xl">
        <Reveal className="mb-6">
          <p className="eyebrow">PREPARATION OPTIONS</p>
          <h2 className="section-title">Fried, unfried or frozen.</h2>
        </Reveal>

        <div className="grid gap-4 sm:grid-cols-3">
          {PREPARATIONS.map((option, index) => (
            <Reveal key={option.slug} delay={index * 0.05} className="option-card">
              <img src={option.image} alt={option.alt} className="option-image" loading="lazy" />
              <div className="option-copy">
                <p className="image-disclosure">Illustrative image</p>
                <h3 className="option-name">{option.label}</h3>
                <p className="option-state">{option.state}</p>
                <a className="option-detail-link" href={`${SITE_BASE}services/${option.slug}/`}>
                  Learn more about {option.slug} options <ArrowRight aria-hidden="true" size={15} />
                </a>
              </div>
            </Reveal>
          ))}
        </div>

        <p className="illustration-note">
          Generated examples, not verified photographs of BiteKasa products.
        </p>
      </div>
    </section>
  );
}
