// Strongly typed content model. All content lives in src/data/*.ts as plain objects.

export type Language = 'Python' | 'PHP' | 'MySQL' | 'C++';

export type ProjectStatus = 'Planned' | 'In progress' | 'Implemented' | 'Tested' | 'Deployed';

export interface CodeSample {
  title: string;
  language: string;
  code: string;
}

export interface Project {
  slug: string;
  title: string;
  summary: string;
  year: string;
  role: string;
  status: ProjectStatus;
  languages: Language[];
  tools: string[];
  featured: boolean;
  hasCaseStudy: boolean;
  problem: string;
  objectives: string[];
  features: string[];
  architecture: string[];
  database: string[];
  testing: string[];
  decisions: string[];
  results: string[];
  limitations: string[];
  futureWork: string[];
  codeSample?: CodeSample;
  image?: string;
  repoUrl?: string;
  demoUrl?: string;
}

export interface Skill {
  id: string;
  name: string;
  group: 'Language' | 'Database' | 'Practice';
  summary: string;
  capabilities: string[];
  projectSlugs: string[];
}

export type ExperienceType = 'Work' | 'Internship' | 'Freelance' | 'Academic' | 'Personal';

export interface ExperienceItem {
  role: string;
  organisation: string;
  dates: string;
  type: ExperienceType;
  context: string;
  actions: string[];
  outcomes: string[];
  tech: string[];
}

export interface EducationItem {
  qualification: string;
  institution: string;
  dates: string;
  status: 'Completed' | 'In progress';
  coursework: string[];
}

export interface Certification {
  title: string;
  issuer: string;
  date: string;
  verifyUrl?: string;
}

export interface Article {
  slug: string;
  title: string;
  summary: string;
  date: string;
  topic: string;
  readMinutes: number;
  published: boolean;
}

export interface Service {
  name: string;
  problem: string;
  deliverables: string[];
}
