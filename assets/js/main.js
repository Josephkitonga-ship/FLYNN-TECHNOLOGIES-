/* Flynn Technologies — site behaviour (no dependencies) */
(function () {
  'use strict';
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------- Header: hide on scroll down, show on scroll up ---------- */
  var hdr = $('.hdr');
  var lastY = window.scrollY, ticking = false;
  function onScroll() {
    var y = window.scrollY;
    hdr.classList.toggle('is-scrolled', y > 24);
    if (!document.body.classList.contains('no-scroll')) {
      if (y > lastY && y > 220) hdr.classList.add('is-hidden');
      else hdr.classList.remove('is-hidden');
    }
    lastY = y;
    ticking = false;
  }
  if (hdr) {
    onScroll();
    window.addEventListener('scroll', function () {
      if (!ticking) { requestAnimationFrame(onScroll); ticking = true; }
    }, { passive: true });
  }

  /* ---------- Mobile menu ---------- */
  var burger = $('.burger'), menu = $('.menu');
  function setMenu(open) {
    if (!burger || !menu) return;
    burger.setAttribute('aria-expanded', String(open));
    burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    menu.classList.toggle('is-open', open);
    document.body.classList.toggle('no-scroll', open);
    if (open) hdr.classList.remove('is-hidden');
  }
  if (burger) {
    burger.addEventListener('click', function () {
      setMenu(burger.getAttribute('aria-expanded') !== 'true');
    });
    $$('a', menu).forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
    window.matchMedia('(min-width:861px)').addEventListener('change', function (e) { if (e.matches) setMenu(false); });
  }

  /* ---------- Hero: pointer glow + tap-to-open panels ---------- */
  var hero = $('.hero');
  if (hero && window.matchMedia('(pointer:fine)').matches) {
    hero.addEventListener('pointermove', function (e) {
      var r = hero.getBoundingClientRect();
      hero.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      hero.style.setProperty('--my', (e.clientY - r.top) + 'px');
    });
  }
  var panels = $$('.panel');
  panels.forEach(function (p) {
    p.addEventListener('click', function (e) {
      if (e.target.closest('a')) return;
      var wasOpen = p.classList.contains('is-open');
      panels.forEach(function (o) { o.classList.remove('is-open'); });
      if (!wasOpen) p.classList.add('is-open');
    });
  });

  /* ---------- Footer year ---------- */
  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- Gallery: filter + lightbox ---------- */
  var gal = $('.gal');
  if (gal) {
    var tiles = $$('.tile', gal);
    var chips = $$('.chip');
    var live = $('#gal-live');
    chips.forEach(function (c) {
      c.addEventListener('click', function () {
        var cat = c.dataset.filter;
        chips.forEach(function (o) { o.setAttribute('aria-pressed', String(o === c)); });
        var shown = 0;
        tiles.forEach(function (t) {
          var show = cat === 'All' || t.dataset.cat === cat;
          t.hidden = !show;
          if (show) shown++;
        });
        if (live) live.textContent = 'Showing ' + shown + ' ' + (cat === 'All' ? 'photos' : cat.toLowerCase() + ' photos');
      });
    });

    var lb = $('dialog.lb');
    var stage = $('.lb-stage-content', lb);
    var capEl = $('.lb-cap', lb);
    var idx = 0, list = [];

    function render() {
      var t = list[idx];
      stage.innerHTML = '';
      var art = document.createElement('div');
      art.className = 'ph-art';
      art.style.setProperty('--art', getComputedStyle(t).getPropertyValue('--art'));
      art.textContent = t.dataset.title;
      var src = t.dataset.full;
      if (src) {
        var img = new Image();
        img.alt = t.dataset.title;
        img.onload = function () { stage.innerHTML = ''; stage.appendChild(img); };
        img.src = src;
      }
      stage.appendChild(art);
      capEl.innerHTML = '<strong></strong><span></span>';
      capEl.firstChild.textContent = t.dataset.title;
      capEl.lastChild.textContent = t.dataset.cat + '  \u2022  ' + (idx + 1) + ' of ' + list.length;
    }
    function open(t) {
      list = tiles.filter(function (x) { return !x.hidden; });
      idx = list.indexOf(t);
      render();
      if (typeof lb.showModal === 'function') lb.showModal(); else lb.setAttribute('open', '');
    }
    function step(d) { idx = (idx + d + list.length) % list.length; render(); }
    tiles.forEach(function (t) { t.addEventListener('click', function () { open(t); }); });
    $('.lb-close', lb).addEventListener('click', function () { lb.close(); });
    $('.lb-nav.prev', lb).addEventListener('click', function () { step(-1); });
    $('.lb-nav.next', lb).addEventListener('click', function () { step(1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) lb.close(); });
    lb.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') step(-1);
      if (e.key === 'ArrowRight') step(1);
    });
    var sx = 0;
    lb.addEventListener('touchstart', function (e) { sx = e.changedTouches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', function (e) {
      var dx = e.changedTouches[0].clientX - sx;
      if (Math.abs(dx) > 50) step(dx > 0 ? -1 : 1);
    });
  }

  /* ---------- Contact form ---------- */
  var form = $('#contact-form');
  if (form) {
    var ok = $('.form-ok');
    function setErr(input, msg) {
      var e = input.parentNode.querySelector('.err');
      input.setAttribute('aria-invalid', msg ? 'true' : 'false');
      if (e) e.textContent = msg || '';
    }
    $$('input[required],textarea[required]', form).forEach(function (i) {
      i.addEventListener('input', function () { if (i.value.trim()) setErr(i, ''); });
    });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var bad = false, first = null;
      var name = form.elements.name, email = form.elements.email, msg = form.elements.message;
      setErr(name, ''); setErr(email, ''); setErr(msg, '');
      if (!name.value.trim()) { setErr(name, 'Enter your name.'); bad = true; first = first || name; }
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value.trim())) { setErr(email, 'Enter a valid email address, like name@company.com.'); bad = true; first = first || email; }
      if (msg.value.trim().length < 10) { setErr(msg, 'Tell us a little about the project (at least 10 characters).'); bad = true; first = first || msg; }
      if (bad) { first.focus(); return; }
      if (form.elements.company && form.elements.company.value) return; // honeypot

      var services = form.elements.service.value || 'Not sure yet';
      var payload = { name: name.value.trim(), company: form.elements.companyname.value.trim(), email: email.value.trim(), services: services, timeline: form.elements.timeline.value, budget: form.elements.budget.value, message: msg.value.trim() };
      var btn = $('button[type="submit"]', form);
      var action = form.getAttribute('action') || '';

      function done() {
        form.reset();
        ok.classList.add('show');
        ok.focus();
        btn.disabled = false; btn.textContent = 'Send message';
      }
      if (action.indexOf('YOUR_FORM_ID') !== -1 || !action) {
        // Fallback until a form endpoint is set: open the visitor's email app.
        var to = form.dataset.mailto;
        var body = 'Name: ' + payload.name + '\nCompany: ' + payload.company + '\nEmail: ' + payload.email + '\nInterested in: ' + payload.services + '\nTimeline: ' + payload.timeline + '\nBudget: ' + payload.budget + '\n\n' + payload.message;
        window.location.href = 'mailto:' + to + '?subject=' + encodeURIComponent('New project enquiry from ' + payload.name) + '&body=' + encodeURIComponent(body);
        done();
        return;
      }
      btn.disabled = true; btn.textContent = 'Sending\u2026';
      fetch(action, { method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify(payload) })
        .then(function (r) { if (!r.ok) throw new Error(); done(); })
        .catch(function () {
          btn.disabled = false; btn.textContent = 'Send message';
          setErr(msg, 'The message did not send. Check your connection and try again, or message us on WhatsApp.');
        });
    });
  }
  /* ---------- Home planner: chips build a WhatsApp message ---------- */
  var planner = $('[data-planner]');
  if (planner) {
    var send = $('[data-planner-send]', planner);
    var pchips = $$('.chip', planner);
    function updPlanner() {
      var picked = pchips.filter(function (c) { return c.getAttribute('aria-pressed') === 'true'; }).map(function (c) { return c.textContent.trim(); });
      var text = 'Hello Director Flynn, I would like to discuss a new project.' + (picked.length ? ' I need: ' + picked.join(', ') + '.' : '');
      send.href = 'https://wa.me/' + planner.dataset.wa + '?text=' + encodeURIComponent(text);
    }
    pchips.forEach(function (c) {
      c.addEventListener('click', function () {
        c.setAttribute('aria-pressed', String(c.getAttribute('aria-pressed') !== 'true'));
        updPlanner();
      });
    });
  }

  /* ---------- Contact: send the same details on WhatsApp ---------- */
  var waBtn = $('#wa-send');
  if (waBtn && form) {
    waBtn.addEventListener('click', function () {
      var f = form.elements;
      if (!f.name.value.trim() || f.message.value.trim().length < 10) {
        form.requestSubmit ? form.requestSubmit() : form.dispatchEvent(new Event('submit', { cancelable: true }));
        return;
      }
      var lines = ['Hello Director Flynn, I would like to discuss a new project.', 'Name: ' + f.name.value.trim()];
      if (f.companyname.value.trim()) lines.push('Company: ' + f.companyname.value.trim());
      lines.push('Interested in: ' + f.service.value);
      if (f.timeline.value) lines.push('Timeline: ' + f.timeline.value);
      if (f.budget.value) lines.push('Budget: ' + f.budget.value);
      lines.push('', f.message.value.trim());
      window.open('https://wa.me/' + form.dataset.wa + '?text=' + encodeURIComponent(lines.join('\n')), '_blank', 'noopener');
    });
  }
  /* ---------- Horizontal scrolling cards ---------- */
  $$('[data-hscroll]').forEach(function (w) {
    var track = $('.hscroll', w), prev = $('[data-hs="-1"]', w), next = $('[data-hs="1"]', w);
    var reduce = window.matchMedia('(prefers-reduced-motion:reduce)').matches;
    function upd() {
      prev.disabled = track.scrollLeft < 4;
      next.disabled = track.scrollLeft + track.clientWidth >= track.scrollWidth - 4;
    }
    function by(d) {
      var step = track.firstElementChild.offsetWidth + 18;
      track.scrollBy({ left: d * step, behavior: reduce ? 'auto' : 'smooth' });
    }
    prev.addEventListener('click', function () { by(-1); });
    next.addEventListener('click', function () { by(1); });
    track.addEventListener('scroll', upd, { passive: true });
    window.addEventListener('resize', upd);
    upd();
  });
  /* ---------- Scroll reveal: sections pop in as they enter the screen ---------- */
  (function () {
    var reduce = window.matchMedia('(prefers-reduced-motion:reduce)').matches;
    if (reduce || !('IntersectionObserver' in window)) return;
    var sel = '.sec-head,.strip li,.together article,.works .work,.work-cta,.gcard,.hs-ctrl,.svc-head,.row,.case,.facts>div,.cta-box,.values li,.faq details,.channels .channel,.form,.tile,.phone-wrap,.portrait,.about-grid>div,.ftr-grid>div,.next';
    var els = $$(sel).filter(function (el) { return el.getBoundingClientRect().top > window.innerHeight * 0.9; });
    var counts = new Map();
    els.forEach(function (el) {
      var p = el.parentNode, i = counts.get(p) || 0;
      counts.set(p, i + 1);
      el.style.setProperty('--d', Math.min(i, 5) * 90 + 'ms');
      el.setAttribute('data-reveal', '');
    });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
    els.forEach(function (el) { io.observe(el); });
  })();
  /* ---------- Dark / light theme switch ---------- */
  var tbtn = $('.theme-btn');
  if (tbtn) {
    var root = document.documentElement;
    var tmeta = $('meta[name="theme-color"]');
    function paintTheme() {
      var light = root.getAttribute('data-theme') === 'light';
      tbtn.setAttribute('aria-label', light ? 'Switch to dark theme' : 'Switch to light theme');
      if (tmeta) tmeta.setAttribute('content', light ? '#F4F7FF' : '#05070D');
    }
    paintTheme();
    tbtn.addEventListener('click', function () {
      var next = root.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('flynn-theme', next); } catch (e) {}
      paintTheme();
    });
  }
})();
