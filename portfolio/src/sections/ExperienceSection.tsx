import Section from '../components/Section';
import { timeline } from '../data/skills';

export default function ExperienceSection() {
  return (
    <Section
      id="experience"
      number="06"
      label="Experience"
      title="Education & experience."
      intro="My studies, my group project and what I am building now. No dates or results are invented here."
      tone="light"
    >
      <ol className="timeline">
        {timeline.map((item) => (
          <li key={item.id} className="timeline-item" data-reveal>
            <p className="eyebrow">{item.label}</p>
            <h3>{item.title}</h3>
            <p className="timeline-org">{item.organisation}</p>
            <p>{item.description}</p>
          </li>
        ))}
      </ol>
    </Section>
  );
}
