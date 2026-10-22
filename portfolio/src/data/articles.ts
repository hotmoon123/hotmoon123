import type { Article } from './types';

// Drafts are kept out of the public list until published is true.
// Publish an article only when you can explain every claim in it.
export const articles: Article[] = [
  {
    slug: 'prepared-statements-in-php',
    title: '[Draft] Why prepared statements matter in PHP',
    summary: '[One-sentence summary of the article.]',
    date: '[YYYY-MM-DD]',
    topic: 'PHP',
    readMinutes: 6,
    published: false,
  },
  {
    slug: 'first-stack-in-cpp',
    title: '[Draft] Building a stack in C++ with clear ownership',
    summary: '[One-sentence summary of the article.]',
    date: '[YYYY-MM-DD]',
    topic: 'C++',
    readMinutes: 8,
    published: false,
  },
];

export const publishedArticles = (): Article[] => articles.filter((article) => article.published);
