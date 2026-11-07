import { FAQS } from '../content';

export default function Faq() {
  return (
    <section className="section" id="faq" aria-labelledby="faq-title" style={{ background: '#fff' }}>
      <div className="wrap">
        <div className="section-head">
          <span className="kicker">Questions</span>
          <h2 className="section-title" id="faq-title">
            Everything you’d ask <span className="accent">before your first pack.</span>
          </h2>
        </div>
        <div className="faq">
          {FAQS.map((item) => (
            <details key={item.q} className="faq-item">
              <summary className="faq-q">{item.q}</summary>
              <p className="faq-a">{item.a}</p>
            </details>
          ))}
        </div>
      </div>
    </section>
  );
}
