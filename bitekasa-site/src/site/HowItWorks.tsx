import { Calculator, MessageCircle, PackageCheck } from 'lucide-react';
import Reveal from './Reveal';

const STEPS = [
  {
    icon: Calculator,
    title: 'Pick your packs',
    body: 'Choose Silver, Golden or Premium above. The total updates as you go — no forms, no account.',
  },
  {
    icon: MessageCircle,
    title: 'Send it on WhatsApp',
    body: 'One tap opens WhatsApp with your packs, quantities and total already written out.',
  },
  {
    icon: PackageCheck,
    title: 'BiteKasa confirms',
    body: 'Availability, timing, collection or delivery and payment are agreed in the chat before anything is paid.',
  },
];

export default function HowItWorks() {
  return (
    <section id="how-it-works" className="bg-cream px-4 py-14 sm:px-7 sm:py-20 lg:px-12 lg:py-24">
      <div className="mx-auto max-w-7xl">
        <Reveal className="mb-6">
          <p className="eyebrow">HOW IT WORKS</p>
          <h2 className="section-title">Three steps, no checkout.</h2>
        </Reveal>

        <ol className="steps">
          {STEPS.map((step, index) => (
            <li key={step.title} className="step">
              <span className="step-index" aria-hidden="true">
                0{index + 1}
              </span>
              <step.icon aria-hidden="true" size={20} className="step-icon" />
              <h3 className="step-title">{step.title}</h3>
              <p className="step-body">{step.body}</p>
            </li>
          ))}
        </ol>
      </div>
    </section>
  );
}
