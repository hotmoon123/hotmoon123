import type { ApproachStep, Skill, TimelineItem } from './types';

// Each skill links to the project where it was used. Empty projectIds means no project yet.
export const skills: Skill[] = [
  {
    id: 'cpp',
    name: 'C++',
    kind: 'Language',
    description: 'A programming language I use for algorithms and problem-solving.',
    projectIds: [],
  },
  {
    id: 'python',
    name: 'Python',
    kind: 'Language',
    description: 'The main language of my backend work on the Rent & Lease Management System.',
    projectIds: ['rent-lease'],
  },
  {
    id: 'php',
    name: 'PHP',
    kind: 'Language',
    description: 'A server-side language for building web applications.',
    projectIds: [],
  },
  {
    id: 'mysql',
    name: 'MySQL',
    kind: 'Database',
    description: 'A relational database for storing and querying structured data.',
    projectIds: [],
  },
  {
    id: 'web',
    name: 'HTML, CSS & JavaScript',
    kind: 'Web',
    description: 'The front end of the Rent & Lease Management System.',
    projectIds: ['rent-lease'],
  },
  {
    id: 'django',
    name: 'Django',
    kind: 'Framework',
    description: 'The Python web framework behind the Rent & Lease backend.',
    projectIds: ['rent-lease'],
  },
];

export const portfolioStack = ['React', 'TypeScript', 'Anime.js', 'Three.js'];

export const timeline: TimelineItem[] = [
  {
    id: 'study',
    label: 'Current',
    title: 'Information Technology',
    organisation: 'Regional Maritime University',
    description: 'Building skills in programming, databases and software systems.',
  },
  {
    id: 'rent-lease',
    label: 'Early 2026',
    title: 'Backend developer, group project',
    organisation: 'Rent & Lease Management System',
    description: 'Developed the backend of a web application for landlords and tenants to manage properties, leases and rent.',
  },
  {
    id: 'stitch-ledger',
    label: 'In progress',
    title: 'Developer',
    organisation: 'StitchLedger · personal project',
    description: 'Building a tool that helps fashion designers track money and time and plan daily tasks.',
  },
];

// A proposed development approach. It describes how I work, not a claim that every project followed each step.
export const approachSteps: ApproachStep[] = [
  { title: 'Understand', text: 'Identify the problem, the users and the constraints.' },
  { title: 'Plan', text: 'Break the work into manageable tasks and set priorities.' },
  { title: 'Design', text: 'Consider the data, the architecture and the user workflow.' },
  { title: 'Build', text: 'Implement the features and connect the parts that depend on each other.' },
  { title: 'Test', text: 'Check expected behaviour, error cases and usability.' },
  { title: 'Improve', text: 'Use feedback and testing to refine the solution.' },
];
