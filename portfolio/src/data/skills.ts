import type { Skill } from './types';

// Each capability should be something you have actually done.
// projectSlugs must match slugs in projects.ts; the Skills page links to them.
export const skills: Skill[] = [
  {
    id: 'python',
    name: 'Python',
    group: 'Language',
    summary: 'Scripts, automation, and data processing.',
    capabilities: [
      'Write scripts and command-line tools that automate repetitive work',
      'Structure code into small functions that can be tested',
      'Read, clean, and transform structured data',
    ],
    projectSlugs: ['python-automation'],
  },
  {
    id: 'php',
    name: 'PHP',
    group: 'Language',
    summary: 'Server-side logic, forms, and database-backed web applications.',
    capabilities: [
      'Handle form input with server-side validation',
      'Query MySQL safely with prepared statements',
      'Structure a small application into routes, logic, and views',
    ],
    projectSlugs: ['examination-system'],
  },
  {
    id: 'mysql',
    name: 'MySQL',
    group: 'Database',
    summary: 'Relational design, querying, and data integrity.',
    capabilities: [
      'Model entities with primary and foreign keys',
      'Write joins, aggregates, and filtered queries',
      'Use constraints and transactions to keep data consistent',
    ],
    projectSlugs: ['examination-system'],
  },
  {
    id: 'cpp',
    name: 'C++',
    group: 'Language',
    summary: 'Algorithms, data structures, and object-oriented design.',
    capabilities: [
      'Implement core data structures such as stacks, queues, and trees',
      'Reason about the time and memory cost of an algorithm',
      'Write object-oriented code with clear ownership of resources',
    ],
    projectSlugs: ['cpp-algorithms'],
  },
  {
    id: 'practice',
    name: 'Engineering practice',
    group: 'Practice',
    summary: 'How I work on software day to day.',
    capabilities: [
      'Break requirements into small, testable changes',
      'Use Git for version history and reviewable commits',
      'Write tests for failure paths as well as success paths',
    ],
    projectSlugs: ['examination-system', 'python-automation', 'cpp-algorithms'],
  },
];

export const toolsUsed = ['Git', 'GitHub', 'Linux', '[Testing tool]', '[Editor]', '[Deployment platform]'] as const;
