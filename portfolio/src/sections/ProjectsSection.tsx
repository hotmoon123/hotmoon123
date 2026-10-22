import ProjectCard from '../components/ProjectCard';
import Section from '../components/Section';
import { projects } from '../data/projects';

export default function ProjectsSection() {
  return (
    <Section
      id="projects"
      number="04"
      label="Projects"
      title="Projects that solve problems."
      intro="Each project shows its real status. Open a card to read the problem, my contribution and the features."
      tone="dark"
    >
      <div className="project-grid">
        {projects.map((project) => (
          <ProjectCard key={project.id} project={project} />
        ))}
      </div>
    </Section>
  );
}
