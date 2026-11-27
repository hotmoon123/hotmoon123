/**
 * Every asset URL the built site asks for must exist on disk.
 *
 * This exists because a base-path bug cannot be caught locally: `npm run dev`
 * and `npm test` both run with base `/`, while the real deployment runs with
 * base `/hotmoon123/`. Code that handled the root case correctly still shipped
 * `/hotmoon123/hotmoon123/assets/...` to production, and nothing failed — the
 * page rendered, it just showed no photographs.
 *
 * So this checks the built output, not the source. Run it after a build:
 *
 *   npm run build -- --base=/hotmoon123/
 *   node scripts/check-asset-paths.mjs /hotmoon123/
 */
import { existsSync, readdirSync, readFileSync, statSync } from 'node:fs';
import { join, relative } from 'node:path';

const base = (process.argv[2] ?? '/').replace(/\/?$/, '/');
const dist = 'dist';

if (!existsSync(dist)) {
  console.error(`FAIL: no build found at ${dist}/. Run the build first.`);
  process.exit(1);
}

const walk = (dir) => {
  const out = [];
  for (const entry of readdirSync(dir)) {
    const full = join(dir, entry);
    if (statSync(full).isDirectory()) out.push(...walk(full));
    else out.push(full);
  }
  return out;
};

const files = walk(dist);
const bundleFiles = files.filter((file) => /\.(js|html)$/.test(file));

// Absolute URLs only; data: URIs and fragments are not files on disk.
const assetPattern = /\/[A-Za-z0-9._~/-]*assets\/[A-Za-z0-9._-]+\.(?:js|css|woff2|avif|webp|jpg|jpeg|png|svg|ico)/g;

const missing = new Map();
let checked = 0;

for (const file of bundleFiles) {
  const source = readFileSync(file, 'utf8');
  for (const match of source.match(assetPattern) ?? []) {
    // Skip the directory prefix itself (`/assets/`) and sourcemap comments.
    if (/\/assets\/$/.test(match) || match.endsWith('.map')) continue;

    checked += 1;

    const withoutBase = match.startsWith(base) ? match.slice(base.length) : match;
    const onDisk = join(dist, withoutBase);

    if (!existsSync(onDisk)) {
      const key = `${match}  (referenced by ${relative(dist, file)})`;
      if (!missing.has(match)) missing.set(match, key);
    }
  }
}

if (checked === 0) {
  console.error('FAIL: found no asset URLs to check. Is the build complete?');
  process.exit(1);
}

if (missing.size > 0) {
  console.error(`FAIL: ${missing.size} asset URL(s) point at files that do not exist (base ${base}):`);
  for (const detail of [...missing.values()].slice(0, 10)) console.error(`  ${detail}`);
  if (missing.size > 10) console.error(`  ... and ${missing.size - 10} more`);
  process.exit(1);
}

console.log(`OK: ${checked} asset URL(s) resolve to real files (base ${base})`);
