import { readdir, readFile } from 'node:fs/promises';
import { gzipSync } from 'node:zlib';

const assetDirectory = new URL('../dist/assets/', import.meta.url);
const files = await readdir(assetDirectory);
const budgets = [
  { pattern: /^main-.*\.js$/, label: 'JavaScript (gzip)', limit: 150 * 1024 },
  { pattern: /^main-.*\.css$/, label: 'CSS (gzip)', limit: 20 * 1024 },
];
let failed = false;

for (const budget of budgets) {
  const file = files.find((name) => budget.pattern.test(name));
  if (!file) {
    console.error(`Missing built asset for ${budget.label}.`);
    failed = true;
    continue;
  }
  const content = await readFile(new URL(file, assetDirectory));
  const actual = gzipSync(content).byteLength;
  const status = actual <= budget.limit ? 'OK' : 'OVER BUDGET';
  console.log(`${status}: ${budget.label}: ${(actual / 1024).toFixed(1)} KiB / ${(budget.limit / 1024).toFixed(0)} KiB`);
  if (actual > budget.limit) failed = true;
}

if (failed) process.exit(1);
