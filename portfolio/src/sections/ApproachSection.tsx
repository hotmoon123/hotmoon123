import Section from '../components/Section';
import { approachSteps } from '../data/skills';

export default function ApproachSection() {
  return (
    <Section
      id="approach"
      number="05"
      label="Approach"
      title="From problem to working solution."
      intro="This is how I approach a project. It is a general process, not a claim that every project followed each step."
      tone="light"
    >
      <ol className="steps">
        {approachSteps.map((step, index) => (
          <li key={step.title} className="step" data-reveal>
            <span className="step-number" aria-hidden="true">
              {String(index + 1).padStart(2, '0')}
            </span>
            <h3>{step.title}</h3>
            <p>{step.text}</p>
          </li>
        ))}
      </ol>
    </Section>
  );
}
