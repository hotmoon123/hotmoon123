import type { Project } from './types';

// Status labels must be true. Allowed: Planned, In progress, Implemented, Tested, Deployed.
export const projects: Project[] = [
  {
    id: 'rent-lease',
    title: 'Rent & Lease Management System',
    status: 'Implemented',
    period: 'Group project · early 2026',
    role: 'Backend developer (group project)',
    summary:
      'A web application that helps landlords and tenants track properties, leases and rent, with an in-app chat so they can communicate directly.',
    stack: ['Python', 'Django', 'HTML', 'CSS', 'JavaScript'],
    problem:
      'Landlords and tenants need one place to track properties, leases and rent, and a direct way to communicate about them.',
    contribution: 'I developed the backend of the system as part of a group project completed in early 2026.',
    featuresLabel: 'Key features',
    features: [
      'Track properties and their details',
      'Record leases for each tenancy',
      'Track rent and payments',
      'Direct chat between landlords and tenants',
    ],
    links: [{ label: 'View the repository on GitHub', url: 'https://github.com/hotmoon123/hotmoon123' }],
    mediaLabel: 'R&L',
  },
  {
    id: 'stitch-ledger',
    title: 'StitchLedger',
    status: 'In progress',
    period: 'Personal project',
    role: 'Developer',
    summary:
      'A planned tool to help fashion designers track money and time, see completed and remaining work, and plan daily tasks.',
    stack: [],
    problem:
      'Fashion designers juggle money, time and production tasks, often across separate notes and tools.',
    contribution:
      'I am building this project now. The features below are planned unless they are marked as done.',
    featuresLabel: 'Planned features',
    features: [
      'Track money coming in and going out',
      'Track time spent on each piece',
      'Show completed and remaining work',
      'Schedule daily tasks',
    ],
    links: [],
    mediaLabel: 'SL',
  },
];

export const getProject = (id: string): Project | undefined => projects.find((project) => project.id === id);
