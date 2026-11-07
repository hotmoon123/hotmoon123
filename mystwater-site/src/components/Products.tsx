import { asset } from '../lib/asset';
import { DESIGNS, SIZES } from '../content';

export default function Products() {
  return (
    <section className="section" id="range" aria-labelledby="range-title">
      <div className="wrap">
        <div className="section-head">
          <span className="kicker">The range</span>
          <h2 className="section-title" id="range-title">
            One water. <span className="accent">Three ways to feel good.</span>
          </h2>
          <p className="section-copy">
            Natural mineral water in 500 ml, 750 ml and 1 Litre, in three designs. Every bottle is
            the same honest water from Dodowa — pick the look that fits the moment.
          </p>
        </div>

        <div className="products-layout">
          <ul className="size-strip" aria-label="Bottle sizes">
            {SIZES.map((size) => (
              <li key={`${size.value}-${size.unit}`} className="size-chip">
                <span className="size-num">{size.value}</span>
                <span className="size-unit">{size.unit}</span>
                <span className="sr-only">— {size.note}</span>
              </li>
            ))}
          </ul>

          <div className="designs-grid">
            {DESIGNS.map((design) => (
              <article key={design.name} className="design-card">
                <div className="design-media">
                  <img
                    src={asset(`assets/${design.image}`)}
                    alt={design.alt}
                    loading="lazy"
                    decoding="async"
                    width={640}
                    height={480}
                  />
                </div>
                <div className="design-body">
                  <span className={`tag ${design.tagTone === 'leaf' ? 'tag--leaf' : 'tag--cyan'}`}>
                    {design.tag}
                  </span>
                  <h3 className="design-name">{design.name} design</h3>
                  <p className="design-note">{design.note}</p>
                </div>
              </article>
            ))}
          </div>
        </div>

        <p className="products-foot">
          Sizes, designs and stock rotate — for trade packs, mixed designs and the current price list,
          enquire on WhatsApp or via the <a href="#wholesale" className="underline underline-offset-2 font-semibold text-[var(--navy-deep)]">stockist form</a>.
          1 Litre design imagery supplied by the brand will be added on adoption.
        </p>
      </div>
    </section>
  );
}
