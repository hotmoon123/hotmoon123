import type { Certification, EducationItem, ExperienceItem, Service } from './types';

// Keep only entries you can describe with a real context, an action, and an outcome.
export const experience: ExperienceItem[] = [
  {
    role: '[Role or project title]',
    organisation: '[Organisation or course]',
    dates: '[Start] – [End]',
    type: 'Academic',
    context: '[What the team or course needed.]',
    actions: ['[What you did, specifically]', '[Second action]'],
    outcomes: ['[What changed, measured or observed]'],
    tech: ['PHP', 'MySQL'],
  },
  {
    role: '[Role or project title]',
    organisation: '[Organisation]',
    dates: '[Start] – [End]',
    type: 'Personal',
    context: '[Why you built it.]',
    actions: ['[What you built]'],
    outcomes: ['[Observed result]'],
    tech: ['Python'],
  },
];

export const education: EducationItem[] = [
  {
    qualification: '[Degree or diploma]',
    institution: '[Institution]',
    dates: '[Start] – [End or expected year]',
    status: 'In progress',
    coursework: ['Data structures and algorithms', 'Database systems', '[Other relevant modules]'],
  },
];

// Completed items only. Anything still in progress belongs in education, marked as such.
export const certifications: Certification[] = [];

export const services: Service[] = [
  {
    name: 'Web applications with PHP and MySQL',
    problem: 'A process that lives in spreadsheets or paper and needs a secure, searchable database.',
    deliverables: ['Requirements summary', 'Working application with validated forms', 'Database schema and setup notes'],
  },
  {
    name: 'Python scripts and automation',
    problem: 'Repetitive data work that takes hours by hand and is prone to error.',
    deliverables: ['Tested script or command-line tool', 'Short usage guide', 'Handover session'],
  },
  {
    name: 'Algorithm and data-structure implementations',
    problem: 'Coursework or product logic that needs correct, well-explained C++ code.',
    deliverables: ['Implementation with tests', 'Complexity notes', 'Code walkthrough'],
  },
];
