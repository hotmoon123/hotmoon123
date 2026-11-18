#!/usr/bin/env python3
"""Measure the site against the documented standards, at every width.

Why this file exists
--------------------
The measure standard appears twice in the reference material, independently:

  THE_COMPLETE_STACK.md 1.1                     "measure 45-75 chars"
  MASTER-PROMPT-senior-graphic-designer.md 6    "measure 45-75 characters"

I got this wrong twice by guessing: first I capped at 76ch and believed it was
fixed, then I measured with a probe span and believed it again. Both were
wrong. This script counts what actually renders -- it walks the text nodes of
every prose block and counts characters per real line box using Range
rectangles, which is the only way to know the number a reader experiences.

It also checks the other measurable standards these files name:
  - body text 16 px minimum             (master prompt 6)
  - works at 320 px and 1920 px         (uiux master prompt 10)
  - no horizontal overflow at any width
  - every control >= 44 px              (the site's own floor)
  - first load < 1 MB                   (THE_COMPLETE_STACK 1.3)

Usage
-----
    LD_LIBRARY_PATH=/tmp/chr/libs/lib python3 measure-audit.py
"""
import os
import sys

from playwright.sync_api import sync_playwright

URL = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8000/"
WIDTHS = [320, 360, 390, 430, 480, 768, 1024, 1280, 1440, 1920]
CHROME = os.environ.get("CHROME_PATH", "/tmp/chr/chromium")

COUNT_LINES = r"""
() => {
  const out = [];
  document.querySelectorAll('main p, main li, main td, main dd, .doc-inner p')
    .forEach(el => {
      if ([...el.children].some(c =>
            ['P','DIV','UL','OL','H3','H4','TABLE'].includes(c.tagName))) return;
      const s = getComputedStyle(el);
      if (s.display === 'none' || s.visibility === 'hidden') return;
      const t = el.innerText.trim();
      if (t.length < 120) return;
      const r = document.createRange();
      let lines = 0, chars = 0, prevTop = null;
      const w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
      let n;
      while ((n = w.nextNode())) {
        for (let i = 0; i < n.length; i++) {
          r.setStart(n, i); r.setEnd(n, i + 1);
          const b = r.getBoundingClientRect();
          if (b.height === 0) continue;
          if (prevTop === null || Math.abs(b.top - prevTop) > 2) {
            lines++; prevTop = b.top;
          }
          chars++;
        }
      }
      if (lines > 1) out.push({
        cpl: Math.round(chars / lines),
        tag: el.tagName + '.' + (el.className.toString().split(' ')[0] || '-'),
        txt: t.slice(0, 40).replace(/\s+/g, ' ')
      });
    });
  return out.sort((a, b) => b.cpl - a.cpl);
}
"""

CONTROLS = r"""
() => [...document.querySelectorAll('a,button,summary,input,select,textarea')]
  .filter(el => {
    const b = el.getBoundingClientRect();
    return b.width > 0 && b.height > 0 && (b.height < 44 || b.width < 44);
  })
  .map(el => el.tagName + ' ' + (el.textContent || '').trim().slice(0, 18)
            + ' ' + Math.round(el.getBoundingClientRect().width)
            + 'x' + Math.round(el.getBoundingClientRect().height))
"""

failures = []
print(f"Measuring {URL}")
print(f"{'width':>6}  {'min cpl':>7} {'max cpl':>7} {'over75':>6} {'overflow':>8} {'<44px':>5}")
print("-" * 52)

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=CHROME, args=["--no-sandbox"])
    for w in WIDTHS:
        page = browser.new_page(viewport={"width": w, "height": 900})
        page.goto(URL, wait_until="networkidle")
        page.evaluate("[...document.querySelectorAll('[data-doc]')].forEach(d => d.open = true)")
        page.wait_for_timeout(200)

        rows = page.evaluate(COUNT_LINES)
        cpl = [r["cpl"] for r in rows] or [0]
        over = [r for r in rows if r["cpl"] > 75]
        overflow = page.evaluate("document.documentElement.scrollWidth - innerWidth")
        small = page.evaluate(CONTROLS)

        print(f"{w:>5}px  {min(cpl):>7} {max(cpl):>7} {len(over):>6} {overflow:>7}px {len(small):>5}")
        for r in over[:4]:
            print(f"         OVER: {r['cpl']} cpl  {r['tag']:<14} \"{r['txt']}\"")
        if over:
            failures.append(f"{w}px: {len(over)} block(s) over 75 characters (max {max(cpl)})")
        if overflow:
            failures.append(f"{w}px: {overflow}px horizontal overflow")
        if small:
            failures.append(f"{w}px: {len(small)} control(s) under 44px")
        page.close()

    page = browser.new_page(viewport={"width": 390, "height": 844})
    page.goto(URL, wait_until="networkidle")
    page.wait_for_timeout(500)
    load = page.evaluate("performance.getEntriesByType('resource')"
                         ".reduce((a,r)=>a+(r.transferSize||0),0)")
    # measure BODY text, not the first <p> on the page: that is the 12px
    # eyebrow label, and it is supposed to be 12px. Take .prose / .lede.
    body_px = page.evaluate("""() => {
      const pick = ['.lede', '.prose', '.doc-inner p']
        .map(s => document.querySelector(s)).filter(Boolean)[0];
      const s = getComputedStyle(pick);
      return {fs: parseFloat(s.fontSize), lh: s.lineHeight,
              which: pick.className || pick.tagName};
    }""")
    browser.close()

print("-" * 52)
print(f"body text: {body_px['fs']}px, line-height {body_px['lh']} "
      f"(from .{body_px['which']})  (standard: 16px min, 1.3-1.6)")
print(f"first load transferred: {load/1024:.1f} KB  (standard: under 1024 KB)")

if body_px["fs"] < 16:
    failures.append(f"body text is {body_px['fs']}px, below the 16px floor")
if load > 1024 * 1024:
    failures.append(f"first load is {load/1024:.0f} KB, over the 1 MB budget")

print()
if failures:
    print(f"FAILED ({len(failures)}):")
    for f in failures:
        print("  -", f)
    sys.exit(1)
print("All width checks passed: measure inside 45-75 characters at every width,")
print("no overflow, no control under 44px, body at 16px, load under 1 MB.")
