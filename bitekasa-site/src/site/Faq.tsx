import { FAQS } from '../data/catalogue';
import Reveal from './Reveal';

export default function Faq() {
  return (
    <section id="questions" className="bg-cream px-4 py-14 sm:px-7 sm:py-20 lg:px-12 lg:py-24">
      <div className="mx-auto max-w-3xl">
        <Reveal className="mb-6">
          <p className="eyebrow">QUESTIONS</p>
          <h2 className="section-title">What people ask first.</h2>
        </Reveal>

        <div className="faq">
          {FAQS.map((item, index) => (
            <Reveal key={item.question} delay={index * 0.03}>
              <details className="faq-item" open={index === 0}>
                <summary className="faq-question">{item.question}</summary>
                <p className="faq-answer">{item.answer}</p>
              </details>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
