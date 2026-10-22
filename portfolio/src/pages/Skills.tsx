import PageHeader from '../components/PageHeader';
import Section from '../components/Section';
import SkillCard from '../components/SkillCard';
import { skills, toolsUsed } from '../data/skills';

export default function Skills() {
  const languages = skills.filter((skill) => skill.group === 'Language');
  const database = skills.filter((skill) => skill.group === 'Database');
  const practice = skills.filter((skill) => skill.group === 'Practice');

  return (
    <>
      <PageHeader
        eyebrow="Skills"
        title="Python, PHP, MySQL, and C++"
        lead="Every skill links to the project where I used it. A skill without project evidence is not listed as a strength."
      />

      <Section id="languages" title="Core languages" intro="Each card lists what I can do and the project that shows it.">
        <div className="card-grid">
          {languages.map((skill) => (
            <SkillCard key={skill.id} skill={skill} />
          ))}
        </div>
      </Section>

      <Section id="database" title="Database" tone="alt">
        <div className="card-grid">
          {database.map((skill) => (
            <SkillCard key={skill.id} skill={skill} />
          ))}
        </div>
      </Section>

      <Section id="practice" title="Engineering practice and tools" intro="Only tools I have used on a real project.">
        <div className="card-grid">
          {practice.map((skill) => (
            <SkillCard key={skill.id} skill={skill} />
          ))}
        </div>
        <ul className="tags tags-large" aria-label="Tools">
          {toolsUsed.map((tool) => (
            <li key={tool}>{tool}</li>
          ))}
        </ul>
      </Section>
    </>
  );
}
