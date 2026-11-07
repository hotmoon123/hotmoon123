import { readFile, readdir, stat } from 'node:fs/promises';
import { gzipSync } from 'node:zlib';

/** Compressed-asset budget. Keep the concept lean — Ghana mobile networks are metered. */
const limits = [
  { match: /\.js$/, maxKB: 150, label: 'initial JS (gzip)' },
  { match: /\.css$/, maxKB: 40, label: 'CSS (gzip)' },
];

const assetsDir = new URL('../dist/assets/', import.meta.url);
let failed = false;

try {
  const files = await readdir(assetsDir);
  for (const file of files) {
    for (const { match, maxKB, label } of limits) {
      if (!match.test(file)) continue;
      const buffer = await readFile(new URL(file, assetsDir));
      const sizeKB = gzipSync(buffer).length / 1024;
      const status = sizeKB <= maxKB ? 'OK  ' : 'FAIL';
      console.log(`${status} ${file}: ${sizeKB.toFixed(1)} KB gzip (${label}, limit ${maxKB} KB)`);
      if (sizeKB > maxKB) failed = true;
    }
  }
  const total = await stat(assetsDir).then(() => files.length);
  console.log(`Assets in dist/assets: ${total} files.`);
} catch (error) {
  console.error(`Could not read dist/assets: ${error.message}`);
  failed = true;
}

if (failed) process.exit(1);
console.log('Bundle budget check passed.');
