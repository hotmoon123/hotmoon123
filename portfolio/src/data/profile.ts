import type { NavItem } from './types';

// All site copy about the owner lives here. Edit this file, not the components.
export const profile = {
  name: 'Caleb Bentum',
  initials: 'CB',
  role: 'IT Student & Backend Developer',
  university: 'Regional Maritime University',
  programme: 'Information Technology',
  email: 'kojocbentum@gmail.com',
  github: 'https://github.com/hotmoon123/hotmoon123',
  headline: "Hi, I'm Caleb Bentum.",
  lead: 'I build practical software with Python, PHP, MySQL and C++, and I am growing my engineering skills through real projects.',
  languages: ['C++', 'Python', 'PHP', 'MySQL'],
  bio: [
    'I am an Information Technology student at Regional Maritime University. I am most interested in the backend of software: the logic, the data and the systems that make an application work reliably.',
    'My main project so far is the Rent & Lease Management System, a group project in which I developed the backend. I am now building StitchLedger, a tool for fashion designers, and I learn the most when I finish something end to end.',
  ],
  copyrightHolder: 'Caleb Bentum',
};

export const navItems: NavItem[] = [
  { id: 'home', label: 'Home' },
  { id: 'about', label: 'About' },
  { id: 'skills', label: 'Skills' },
  { id: 'projects', label: 'Projects' },
  { id: 'experience', label: 'Experience' },
  { id: 'contact', label: 'Contact' },
];
