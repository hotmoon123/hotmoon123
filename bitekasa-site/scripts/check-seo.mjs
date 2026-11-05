import { readFile } from 'node:fs/promises';

const site = 'https://hotmoon123.github.io/hotmoon123/';
const pages = [
  { file: 'index.html', url: site },
  { file: 'services/fried/index.html', url: `${site}services/fried/` },
  { file: 'services/unfried/index.html', url: `${site}services/unfried/` },
  { file: 'services/frozen/index.html', url: `${site}services/frozen/` },
  { file: 'privacy.html', url: `${site}privacy.html` },
];
const titles = new Set();
let failed = false;

for (const page of pages) {
  const html = await readFile(new URL(`../dist/${page.file}`, import.meta.url), 'utf8');
  const title = html.match(/<title>(.*?)<\/title>/i)?.[1]?.trim();
  const description = html.match(/<meta\s+name="description"\s+content="([^"]+)"/i)?.[1];
  const canonical = html.match(/<link\s+rel="canonical"\s+href="([^"]+)"/i)?.[1];
  if (!title || !description || canonical !== page.url || titles.has(title)) {
    console.error(`SEO metadata check failed: ${page.file}`);
    failed = true;
  } else {
    console.log(`OK: ${page.file}: ${title}`);
  }
  if (title) titles.add(title);
}

const sitemap = await readFile(new URL('../dist/sitemap.xml', import.meta.url), 'utf8');
const robots = await readFile(new URL('../dist/robots.txt', import.meta.url), 'utf8');
for (const page of pages) {
  if (!sitemap.includes(`<loc>${page.url}</loc>`)) {
    console.error(`Sitemap is missing ${page.url}`);
    failed = true;
  }
}
if (!robots.includes(`Sitemap: ${site}sitemap.xml`)) {
  console.error('robots.txt does not reference the production sitemap.');
  failed = true;
}
if (failed) process.exit(1);
