export type ProjectStatus = 'Planned' | 'In progress' | 'Implemented' | 'Tested' | 'Deployed';

export interface ProjectLink {
  label: string;
  url: string;
}

export interface Project {
  id: string;
  title: string;
  status: ProjectStatus;
  period: string;
  role: string;
  summary: string;
  stack: string[];
  problem: string;
  contribution: string;
  featuresLabel: string;
  features: string[];
  links: ProjectLink[];
  /** Short label for the placeholder artwork shown until a real screenshot is added. */
  mediaLabel: string;
  /** Optional screenshot in /public/images. Leave undefined until you have one. */
  image?: string;
  imageAlt?: string;
}

export type SkillKind = 'Language' | 'Database' | 'Web' | 'Framework';

export interface Skill {
  id: string;
  name: string;
  kind: SkillKind;
  description: string;
  /** Project ids where this skill was actually used. Empty means no project yet. */
  projectIds: string[];
}

export interface TimelineItem {
  id: string;
  label: string;
  title: string;
  organisation: string;
  description: string;
}

export interface ApproachStep {
  title: string;
  text: string;
}

export interface NavItem {
  id: string;
  label: string;
}
