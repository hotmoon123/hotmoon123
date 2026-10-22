import Section from '../components/Section';
import SkillCard from '../components/SkillCard';
import { portfolioStack, skills } from '../data/skills';

export default function SkillsSection() {
  return (
    <Section
      id="skills"
      number="03"
      label="Skills"
      title="The tools I work with."
      intro="Each skill shows the project where I used it. Skills without a project are listed as such."
      tone="dark"
    >
      <div className="skill-grid" data-reveal>
        {skills.map((skill) => (
          <SkillCard key={skill.id} skill={skill} />
        ))}
      </div>

      <div className="portfolio-stack" data-reveal>
        <h3>Built with</h3>
        <ul className="tags tags-large" aria-label="Technologies used to build this website">
          {portfolioStack.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
        <p className="small muted">These are the tools used to build this website. They are not a list of past work.</p>
      </div>
    </Section>
  );
}
