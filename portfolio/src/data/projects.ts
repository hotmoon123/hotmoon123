import type { Project } from './types';

// Status labels must be true. Allowed: Planned, In progress, Implemented, Tested, Deployed.
export const projects: Project[] = [
  {
    id: 'rent-lease',
    title: 'Rent & Lease Management System',
    status: 'Implemented',
    period: 'Group project',
    role: 'Backend developer (group project)',
    summary:
      'A web application that helps landlords and tenants track properties, leases and rent, with an in-app chat so they can communicate directly.',
    stack: ['Python', 'Django', 'HTML', 'CSS', 'JavaScript'],
    problem:
      'Landlords and tenants need one place to track properties, leases and rent, and a direct way to communicate about them.',
    contribution:
      'I developed the backend of the system as part of a group project. My work covered user authentication, account verification and the WebSocket connection that powers the chat.',
    featuresLabel: 'Key features',
    features: [
      'Track properties and their details',
      'Record leases for each tenancy',
      'Track rent and payments',
      'User authentication and account verification',
      'Real-time chat between landlords and tenants over WebSocket',
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
    stack: ['React Native', 'Python', 'Django', 'FastAPI', 'OpenRouter'],
    problem:
      'Fashion designers juggle money, time and production tasks, often across separate notes and tools.',
    contribution:
      'I am building this project now, across a React Native app and a Python back end using Django and FastAPI. Features are listed as planned until they are finished.',
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
