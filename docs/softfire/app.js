/* ============================================================
   SOFTFIRE — the islands

     1. crawler field     built once, 12 nodes, no runtime cost
     2. the rail          marks the section you are reading
     3. carousel           transform + opacity only
     4. the brief          four steps, ends in WhatsApp
     5. year

   Four rules this file exists to keep:
     · nothing animates two things for one change
     · decorative animation pauses when it is off screen
     · nothing is stored and nothing is sent until a person taps
     · reduced motion is honoured in JS, not only in CSS
   ============================================================ */

(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

  /* ============================================================
     1. CRAWLER FIELD
     One DOM node per column. Marks are built here rather than
     written 200 times in the HTML, then duplicated once so the
     -50% loop point is invisible.
     ============================================================ */

  (function crawlers() {
    var field = document.querySelector('[data-crawlers]');
    if (!field) return;

    var MARK = 'assets/sf-mark.svg';
    var PER_COLUMN = 9;

    field.querySelectorAll('[data-track]').forEach(function (track, colIndex) {
      // offset each column so they do not read as a marching band
      var offset = (colIndex * 37) % 100;
      track.style.animationDelay = '-' + ((offset / 100) * 46).toFixed(2) + 's';

      var frag = document.createDocumentFragment();
      var i;

      for (i = 0; i < PER_COLUMN; i++) frag.appendChild(mark());
      for (i = 0; i < PER_COLUMN; i++) frag.appendChild(mark());

      track.appendChild(frag);

      function mark() {
        var img = document.createElement('img');
        img.src = MARK;
        img.alt = '';
        img.setAttribute('aria-hidden', 'true');
        img.className = 'crawler-mark';
        img.width = 54;
        img.height = 54;
        img.decoding = 'async';
        img.loading = 'lazy';
        return img;
      }
    });

    // Pause the loop when nobody can see it. A phone in a pocket
    // should not be doing twelve compositor animations.
    document.addEventListener('visibilitychange', function () {
      field.querySelectorAll('.crawler-track').forEach(function (t) {
        t.style.animationPlayState = document.hidden ? 'paused' : '';
      });
    });

    if (reduceMotion.matches) {
      field.querySelectorAll('.crawler-track').forEach(function (t) {
        t.style.animation = 'none';
      });
    }
  })();

  /* ============================================================
     2. THE RAIL — a reading position, not a menu animation.
     One observer, one class. No scroll listener.
     ============================================================ */

  (function rail() {
    var links = Array.prototype.slice.call(document.querySelectorAll('.rail-list a'));
    if (!links.length || !('IntersectionObserver' in window)) return;

    var map = {};
    links.forEach(function (a) {
      var id = a.getAttribute('href').slice(1);
      var section = document.getElementById(id);
      if (section) map[id] = a;
    });

    function clear() {
      links.forEach(function (a) { a.removeAttribute('aria-current'); });
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        clear();
        var a = map[entry.target.id];
        if (a) a.setAttribute('aria-current', 'true');
      });
    }, { rootMargin: '-45% 0px -45% 0px', threshold: 0 });

    Object.keys(map).forEach(function (id) {
      var el = document.getElementById(id);
      if (el) io.observe(el);
    });
  })();

  /* ============================================================
     3. CAROUSEL
     order = [left, centre, right]; index 1 is the centre card.
     No auto-advance. Nothing moves unless a person moves it.
     ============================================================ */

  (function carousel() {
    var root = document.querySelector('[data-carousel]');
    if (!root) return;

    var slides = Array.prototype.slice.call(root.querySelectorAll('.slide'));
    var countEl = root.querySelector('[data-count]');
    var active = 1;

    function pad(n) { return n < 10 ? '0' + n : String(n); }

    function render() {
      var n = slides.length;
      slides.forEach(function (el, i) {
        var rel = (i - active + n) % n;
        var pos = rel === 0 ? 'centre' : (rel === 1 ? 'right' : 'left');
        el.dataset.pos = pos;

        if (pos === 'centre') {
          el.removeAttribute('role');
          el.removeAttribute('tabindex');
          el.removeAttribute('aria-label');
        } else {
          el.setAttribute('role', 'button');
          el.setAttribute('tabindex', '0');
          var h = el.querySelector('h3');
          el.setAttribute('aria-label', 'Bring this card forward: ' + (h ? h.textContent : ''));
        }
      });
      if (countEl) countEl.textContent = pad(active + 1) + ' / ' + pad(n);
    }

    function go(dir) {
      var n = slides.length;
      active = (active + dir + n) % n;
      render();
    }

    root.querySelectorAll('[data-dir]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        go(btn.dataset.dir === 'next' ? 1 : -1);
      });
    });

    slides.forEach(function (el) {
      function bring() {
        if (el.dataset.pos === 'centre') return;
        var i = slides.indexOf(el);
        if (i > -1) { active = i; render(); }
      }
      el.addEventListener('click', bring);
      el.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ' || e.key === 'Spacebar') {
          e.preventDefault();
          bring();
        }
      });
    });

    root.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { e.preventDefault(); go(1); }
      if (e.key === 'ArrowLeft')  { e.preventDefault(); go(-1); }
    });

    var startX = null;
    root.addEventListener('touchstart', function (e) {
      startX = e.touches[0].clientX;
    }, { passive: true });
    root.addEventListener('touchend', function (e) {
      if (startX === null) return;
      var dx = e.changedTouches[0].clientX - startX;
      if (Math.abs(dx) > 40) go(dx < 0 ? 1 : -1);
      startX = null;
    }, { passive: true });

    render();
  })();

  /* ============================================================
     4. THE FOUR-STEP BRIEF
     Answers live in this closure. No storage, no cookie, no
     network call. The WhatsApp link is a real href; only the
     composed words need JavaScript.
     ============================================================ */

  (function brief() {
    var root = document.querySelector('[data-brief]');
    if (!root) return;

    var steps   = Array.prototype.slice.call(root.querySelectorAll('.brief-step'));
    var bar     = root.querySelector('[data-bar]');
    var counter = root.querySelector('[data-stepnum]');
    var summary = root.querySelector('[data-summary]');
    var sendBtn = root.querySelector('[data-send]');
    var answers = { kind: '', problem: '', deadline: '', who: '', extra: '' };
    var at = 0;

    function show(i, moveFocus) {
      at = Math.max(0, Math.min(i, steps.length - 1));
      steps.forEach(function (s, idx) {
        s.setAttribute('data-active', idx === at ? 'true' : 'false');
      });
      var shown = Math.min(at + 1, 4);
      if (bar) bar.style.width = (shown / 4 * 100) + '%';
      if (counter) counter.textContent = shown + ' / 4';

      if (moveFocus) {
        var h = steps[at].querySelector('h3');
        if (h) {
          h.setAttribute('tabindex', '-1');
          h.focus({ preventScroll: true });
        }
      }
    }

    root.querySelectorAll('.choice').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var q = btn.dataset.q;
        root.querySelectorAll('.choice[data-q="' + q + '"]').forEach(function (sib) {
          sib.setAttribute('aria-pressed', sib === btn ? 'true' : 'false');
        });
        answers[q] = btn.dataset.a;
      });
    });

    root.querySelectorAll('input[data-q], textarea[data-q]').forEach(function (field) {
      field.addEventListener('input', function () {
        answers[field.dataset.q] = field.value.trim();
      });
    });

    root.querySelectorAll('[data-next]').forEach(function (b) {
      b.addEventListener('click', function () { show(at + 1, true); });
    });
    root.querySelectorAll('[data-back]').forEach(function (b) {
      b.addEventListener('click', function () { show(at - 1, true); });
    });

    function compose() {
      var lines = [];
      lines.push('Hello Caleb,');
      lines.push('');
      lines.push('I found SoftFire and would like to talk about a project.');
      lines.push('');
      if (answers.kind)     lines.push('What: ' + answers.kind);
      if (answers.problem)  lines.push('The main problem: ' + answers.problem);
      if (answers.deadline) lines.push('Timeline: ' + answers.deadline);
      if (answers.who)      lines.push('Me: ' + answers.who);
      if (answers.extra) {
        lines.push('');
        lines.push(answers.extra);
      }
      lines.push('');
      lines.push('Could you send me a written quote in 48 hours?');
      return lines.join('\n');
    }

    var finish = root.querySelector('[data-finish]');
    if (finish) {
      finish.addEventListener('click', function () {
        var text = compose();
        if (summary) summary.textContent = text;
        if (sendBtn) {
          sendBtn.href = 'https://wa.me/233570572221?text=' + encodeURIComponent(text);
        }
        show(4, true);
      });
    }

    var restart = root.querySelector('[data-restart]');
    if (restart) {
      restart.addEventListener('click', function () {
        answers = { kind: '', problem: '', deadline: '', who: '', extra: '' };
        root.querySelectorAll('.choice').forEach(function (b) {
          b.setAttribute('aria-pressed', 'false');
        });
        root.querySelectorAll('input[data-q], textarea[data-q]').forEach(function (f) {
          f.value = '';
        });
        // the composed message and the send link must reset too, or
        // "Start again" hands the next person the previous answers.
        if (summary) summary.textContent = '';
        if (sendBtn) sendBtn.href = 'https://wa.me/233570572221';
        show(0, true);
      });
    }
  })();


  /* ============================================================
     5. MOTION TOGGLE — WCAG 2.2.2
     The crawl runs longer than five seconds and cannot be stopped
     by hover, so the page offers its own control. The state lives
     in memory only: no storage, no cookie, nothing to clear.
     ============================================================ */

  (function motionToggle() {
    var btn = document.querySelector('[data-motion-toggle]');
    var field = document.querySelector('[data-crawlers]');
    if (!btn || !field) return;

    var label = btn.querySelector('[data-motion-label]');
    var paused = false;

    function apply() {
      field.querySelectorAll('.crawler-track').forEach(function (t) {
        t.style.animationPlayState = paused ? 'paused' : '';
      });
      document.documentElement.setAttribute('data-motion', paused ? 'off' : 'on');
      btn.setAttribute('aria-pressed', paused ? 'true' : 'false');
      if (label) label.textContent = paused ? 'Resume background motion' : 'Pause background motion';
      // remembered for this browser session only — no cookie, no storage
      try { sessionStorage.setItem('sf-motion', paused ? 'off' : 'on'); } catch (e) {}
    }

    btn.addEventListener('click', function () {
      paused = !paused;
      apply();
    });

    // a person who asked the OS for less motion, or who pressed Pause
    // last time in this session, starts paused
    paused = document.documentElement.getAttribute('data-motion') === 'off';
    apply();
    if (reduceMotion.matches) { paused = true; apply(); }
    if (reduceMotion.addEventListener) {
      reduceMotion.addEventListener('change', function (e) {
        paused = e.matches;
        apply();
      });
    }
  })();

  /* ============================================================
     6. YEAR
     ============================================================ */

  var yearEl = document.querySelector('[data-year]');
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

})();
