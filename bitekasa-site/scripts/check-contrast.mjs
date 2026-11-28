/**
 * Brand colour guard.
 *
 * The palette has three colours, and only one of the two golds may carry text.
 * Bright Royal Gold is 2.03:1 on cream — it is a mark, not type — while deep
 * gold is 4.61:1 and passes. That distinction lives in a comment today, and a
 * comment does not stop anyone. This does.
 *
 * Values are read from src/styles/tokens.css, so changing a hex re-tests it.
 */
import { readFileSync } from 'node:fs';

const css = readFileSync('src/styles/tokens.css', 'utf8');
const token = (name) => {
  const match = new RegExp(`--${name}:\\s*(#[0-9a-fA-F]{6})`).exec(css);
  if (!match) throw new Error(`token --${name} not found in tokens.css`);
  return match[1];
};

const luminance = (hex) => {
  const [r, g, b] = hex
    .replace('#', '')
    .match(/../g)
    .map((pair) => parseInt(pair, 16) / 255)
    .map((value) => (value <= 0.03928 ? value / 12.92 : ((value + 0.055) / 1.055) ** 2.4));
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
};

const contrast = (a, b) => {
  const [light, dark] = [luminance(a), luminance(b)].sort((x, y) => y - x);
  return (light + 0.05) / (dark + 0.05);
};

/** Every pair where the first colour is set as TEXT on the second. */
const textPairs = [
  ['ink', 'paper', 4.5, 'body text'],
  ['ink-soft', 'paper', 4.5, 'secondary text'],
  ['ink-muted', 'paper', 4.5, 'captions'],
  ['red', 'paper', 4.5, 'brand red as text'],
  ['red-deep', 'paper', 4.5, 'link and accent text'],
  ['gold-deep', 'paper', 4.5, 'prices, labels'],
  ['gold-deep', 'paper-raised', 4.5, 'prices on cards'],
  ['on-dark', 'red', 4.5, 'text on the red CTA'],
  ['gold', 'ink', 4.5, 'gold on dark'],
];

const failures = [];

console.log('WCAG 2.2 AA — text pairs\n');
for (const [fg, bg, minimum, purpose] of textPairs) {
  const front = token(fg);
  const behind = token(bg);
  const ratio = contrast(front, behind);
  const pass = ratio >= minimum;
  if (!pass) failures.push(`${fg} on ${bg} is ${ratio.toFixed(2)}:1, needs ${minimum}:1 (${purpose})`);
  console.log(
    `  ${pass ? 'PASS' : 'FAIL'}  ${ratio.toFixed(2).padStart(5)}:1  ${`--${fg}`.padEnd(12)} on --${bg.padEnd(12)} ${purpose}`,
  );
}

// Bright gold must stay BELOW the text threshold, or someone will use it for
// type and the palette will fail. This asserts the rule in the right direction.
const decorative = contrast(token('gold'), token('paper'));
if (decorative >= 3) {
  failures.push(`--gold is ${decorative.toFixed(2)}:1 on cream — high enough to look like text; revisit which gold carries type`);
}
console.log(
  `\n  NOTE  ${decorative.toFixed(2)}:1  --gold       on --paper     decorative only: marks, rules, glows, never small text`,
);

if (failures.length > 0) {
  console.error(`\nFAIL: ${failures.length} colour pair(s) do not meet the standard.`);
  for (const failure of failures) console.error(`  ${failure}`);
  process.exit(1);
}

console.log('\nOK: every text pair meets WCAG 2.2 AA; bright gold is confined to decoration.');
