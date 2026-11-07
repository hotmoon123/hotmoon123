import { readFile, readdir } from 'node:fs/promises';

/**
 * Concept-integrity gate for the MYST WATER proposal build.
 * Fails the build if any promise the proposal makes is broken:
 * - still marked noindex (we are NOT claiming this is the official site)
 * - both published phone numbers present
 * - brand email, concept credit, privacy notice present
 * Hero headline is split across JSX text nodes for styling, so the
 * headline check is matched on the "THE FEEL" fragment.
 * If the company adopts the site, update the expected values below together
 * with robots.txt / the meta tag (see README "Adoption checklist").
 */
const fileNeedles = [
  { file: 'index.html', needles: ['noindex', '<title>Myst Water | The Feel Good Water</title>'], why: 'concept meta/title missing' },
  { file: 'privacy.html', needles: ['Data Protection Act, 2012 (Act 843)'], why: 'Ghana DPA notice missing' },
];

const bundleNeedles = [
  'THE FEEL',            // hero headline (split across JSX nodes by design)
  'DODOWA',              // case-insensitive check below
  '020 410 2171',
  '+233 59 699 5220',
  'info@drinkmyst.com',
  'Caleb Bentum',
  'Website concept for MYST WATER COMPANY',
];

let failed = false;
const read = (file) => readFile(new URL(`../dist/${file}`, import.meta.url), 'utf8');

for (const { file, needles, why } of fileNeedles) {
  try {
    const html = (await read(file)).toLowerCase();
    for (const needle of needles) {
      if (html.includes(needle.toLowerCase())) {
        console.log(`OK: dist/${file} contains "${needle.slice(0, 60)}"`);
      } else {
        console.error(`MISSING in dist/${file}: ${needle} — ${why}`);
        failed = true;
      }
    }
  } catch (error) {
    console.error(`MISSING FILE dist/${file}: ${error.message}`);
    failed = true;
  }
}

const assetsDir = new URL('../dist/assets/', import.meta.url);
const jsFiles = (await readdir(assetsDir)).filter((name) => name.endsWith('.js'));
let haystack = '';
for (const name of jsFiles) haystack += (await readFile(new URL(name, assetsDir), 'utf8')).toLowerCase();

for (const needle of bundleNeedles) {
  if (haystack.includes(needle.toLowerCase())) {
    console.log(`OK: bundle contains "${needle}"`);
  } else {
    console.error(`MISSING in bundle: "${needle}"`);
    failed = true;
  }
}

if (failed) process.exit(1);
console.log('Content integrity check passed.');
