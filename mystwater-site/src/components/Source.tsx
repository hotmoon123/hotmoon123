import { CheckCircle2 } from 'lucide-react';
import { asset } from '../lib/asset';

const COMMITMENTS = [
  'Natural mineral water sourced from the Dodowa aquifer, Eastern Region — filtered and bottled at the origin.',
  'A PNF Industries Limited brand — Ghanaian-owned, produced and packaged.',
  'On-site services and facilities listed on Google: wheelchair-accessible parking, entrance, seating and toilet; assistive hearing loop; nursing room; changing table; gender-neutral toilets; free parking.',
  'Recycling accepted on-site: batteries, light bulbs and metal cans.',
] as const;

export default function Source() {
  return (
    <section className="section" id="source" aria-labelledby="source-title" style={{ background: '#fff' }}>
      <div className="wrap source-grid">
        <div>
          <span className="kicker">The source</span>
          <h2 className="section-title" id="source-title" style={{ marginTop: '1rem' }}>
            Purely sourced. <span className="accent">Bottled at the origin.</span>
          </h2>
          <p className="section-copy" style={{ marginTop: '1rem' }}>
            Myst Water begins as natural mineral water in the Dodowa aquifer. It is filtered and
            packaged there — nobody touches it in between. That is the whole idea behind the name:
            a mystery you can taste, answered by the source.
          </p>

          <ul className="commit-list">
            {COMMITMENTS.map((item) => (
              <li key={item} className="commit">
                <CheckCircle2 aria-hidden="true" size={18} />
                <span>{item}</span>
              </li>
            ))}
          </ul>

          <div className="source-lines" aria-label="Campaign lines from the brand">
            <span className="campaign-chip">The Feel Good Water</span>
            <span className="campaign-chip campaign-chip--alt">Drip too nice</span>
            <span className="campaign-chip campaign-chip--leaf">Sipping is believing</span>
          </div>

          <p className="products-foot" style={{ marginTop: '1.25rem' }}>
            Campaign lines and artwork are the property of the brand; used here with the supplied assets.
          </p>
        </div>

        <figure className="lifestyle-figure">
          <img
            src={asset('assets/myst-football.jpg')}
            alt="A Myst Water bottle resting on the grass beside football boots at a training ground"
            loading="lazy"
            decoding="async"
            width={399}
            height={501}
          />
        </figure>
      </div>
    </section>
  );
}
