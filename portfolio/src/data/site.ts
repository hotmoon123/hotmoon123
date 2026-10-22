// Site-wide facts. Replace the placeholders before publishing.
export const site = {
  name: 'Your Name',
  role: 'Software Engineer',
  tagline: 'I build practical, secure software with Python, PHP, MySQL, and C++.',
  location: 'Your City, Country',
  email: 'you@example.com',
  availability: '[State what you are open to: internship, freelance, or full-time roles]',
  responseTime: 'within two working days',
  cvUrl: '/resume.pdf',
  links: {
    github: 'https://github.com/your-handle',
    linkedin: 'https://www.linkedin.com/in/your-handle',
  },
} as const;

export const primaryNav = [
  { label: 'Home', to: '/' },
  { label: 'About', to: '/about' },
  { label: 'Skills', to: '/skills' },
  { label: 'Projects', to: '/projects' },
  { label: 'Experience', to: '/experience' },
  { label: 'Contact', to: '/contact' },
] as const;

export const secondaryNav = [
  { label: 'Education', to: '/education' },
  { label: 'Resume', to: '/resume' },
  { label: 'Case studies', to: '/case-studies' },
  { label: 'Articles', to: '/articles' },
  { label: 'Services', to: '/services' },
] as const;
