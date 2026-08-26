/* Klyara admin panel. Vanilla, dependency-free, reduced-motion safe, file:// safe.
   Reads assets/data/*.json over http(s); falls back to the window.KLY_* shims on file://. */
(function () {
"use strict";
var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
var $ = function (s, r) { return (r || document).querySelector(s); };
var $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };
var esc = function (s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) {
  return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };

var DATA = { plan: window.KLY_PLAN, library: window.KLY_LIBRARY, bplan: window.KLY_BPLAN };
var MON = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
var DAYMS = 864e5;

function d(iso) { var p = iso.split('-'); return new Date(+p[0], +p[1] - 1, +p[2]); }
function today() { var n = new Date(); return new Date(n.getFullYear(), n.getMonth(), n.getDate()); }
function diff(a, b) { return Math.round((b - a) / DAYMS); }
function shortDate(dt) { return dt.getDate() + ' ' + MON[dt.getMonth()]; }
function plural(n, s) { return n + ' ' + s + (n === 1 ? '' : 's'); }

/* ── data: prefer the real JSON when the protocol allows it ─────────────── */
function load(name, key, cb) {
  if (location.protocol === 'file:' || !window.fetch) { cb(); return; }
  fetch('assets/data/' + name + '.json', { cache: 'no-cache' })
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (j) { if (j) DATA[key] = j; cb(); })
    .catch(function () { cb(); });
}

/* ── count-up (own attribute so main.js does not double-bind) ──────────── */
function countUp(el) {
  if (el.dataset.done) return; el.dataset.done = '1';
  var end = parseFloat(el.dataset.acount) || 0, suf = el.dataset.suffix || '';
  if (reduce) { el.textContent = end + suf; return; }
  var t0 = null;
  requestAnimationFrame(function step(t) {
    if (!t0) t0 = t;
    var p = Math.min((t - t0) / 1100, 1); p = 1 - Math.pow(1 - p, 3);
    el.textContent = Math.round(end * p) + suf;
    if (p < 1) requestAnimationFrame(step);
  });
}
function armCounts(root) { $$('[data-acount]', root).forEach(countUp); }

/* ── router ────────────────────────────────────────────────────────────── */
var VIEWS = ['plan', 'bplan', 'library', 'compliance', 'links', 'launch'];
var built = {};
function show(view, push) {
  if (VIEWS.indexOf(view) < 0) view = 'plan';
  $$('.atab').forEach(function (t) { t.setAttribute('aria-selected', String(t.dataset.view === view)); });
  $$('.aview').forEach(function (v) { v.classList.toggle('on', v.id === 'v-' + view); });
  if (push && location.hash !== '#/' + view) history.replaceState(null, '', '#/' + view);
  var el = $('#v-' + view);
  if (BUILD[view] && !built[view]) { built[view] = 1; try { BUILD[view](el); } catch (e) { console.error('view ' + view, e); } }
  // main.js reveals on intersection; a view that was display:none may not have fired.
  setTimeout(function () {
    $$('[data-reveal],[data-stagger]', el).forEach(function (x) { x.classList.add('in'); });
    $$('.bars,.ptl,.rail-line', el).forEach(function (x) { x.classList.add('in'); });
    armCounts(el);
  }, 40);
  window.scrollTo(0, 0);
}

/* ══ (a) 90-day plan ═══════════════════════════════════════════════════ */
var PC = { setup: 'var(--a-setup)', m1: 'var(--a-m1)', m2: 'var(--a-m2)', m3: 'var(--a-m3)' };

function buildPlan(root) {
  var P = DATA.plan; if (!P) return;
  var t = today(), start = d(P.anchors.setupStart), launch = d(P.anchors.launch), end = d(P.anchors.day90);
  var span = diff(start, end);                       // 102
  var doneDays = Math.max(0, Math.min(90, diff(launch, t) + 1));
  var pct = Math.round(doneDays / 90 * 100);

  /* you-are-here */
  var kick, head, note, stats;
  if (t < start) {
    var togo = diff(t, start);
    kick = 'Not started';
    head = plural(togo, 'day') + ' to go';
    note = 'Nothing is scheduled for Key or Craig before Tuesday 1 September 2026. The setup phase opens that morning with the ICB practice licence application and the Google Business Profile claim — the two clocks everything else queues behind.';
    stats = [[togo, 'Days until setup'], [diff(t, launch), 'Days until Day 1'], [90, 'Days in the plan']];
  } else if (t <= d(P.anchors.setupEnd)) {
    var sn = diff(start, t) + 1;
    kick = 'Setup phase';
    head = 'Setup day ' + sn + ' of 13';
    note = 'The setup fortnight. Two items have waiting periods attached and both should already be running.';
    stats = [[sn, 'Setup days done'], [13 - sn, 'Setup days left'], [diff(t, launch), 'Days until Day 1']];
  } else if (t <= end) {
    kick = 'You are here';
    head = 'Day ' + doneDays + ' of 90';
    note = 'Today is ' + esc(fmtLong(t)) + '. Each day has one thing on it — if the day goes wrong and you only do one item, do that one.';
    stats = [[doneDays, 'Days done'], [90 - doneDays, 'Days remaining'], [pct + '%', 'Through the plan']];
  } else {
    kick = 'Complete';
    head = 'The ninety days are done';
    note = 'Day 90 was Saturday 12 December 2026. Full re-score against what actually happened, then re-plan.';
    stats = [[90, 'Days done'], [0, 'Days remaining'], ['100%', 'Through the plan']];
  }
  var C = 2 * Math.PI * 54;
  $('#p-now').innerHTML =
    '<div class="anow" data-reveal>' +
      '<div class="ring"><svg viewBox="0 0 132 132" aria-hidden="true">' +
        '<circle class="trk" cx="66" cy="66" r="54"></circle>' +
        '<circle class="bar" cx="66" cy="66" r="54" stroke-dasharray="' + C.toFixed(1) + '" stroke-dashoffset="' + C.toFixed(1) + '"></circle>' +
      '</svg><span class="lbl"><b>' + pct + '%</b><span>of 90 days</span></span></div>' +
      '<div><span class="kicker">' + esc(kick) + '</span><h2>' + esc(head) + '</h2><p>' + note + '</p>' +
        '<div class="anow-stats">' + stats.map(function (s) {
          return '<div><b>' + esc(s[0]) + '</b><span>' + esc(s[1]) + '</span></div>'; }).join('') +
      '</div></div>' +
    '</div>';
  var barEl = $('#p-now .bar');
  setTimeout(function () { barEl.setAttribute('stroke-dashoffset', (C * (1 - pct / 100)).toFixed(1)); }, reduce ? 0 : 260);

  /* date rail: phase bands, month ticks, numbered milestone pins, today needle */
  var counts = { setup: 13, m1: 30, m2: 30, m3: 30 };
  var short = { setup: 'Setup', m1: 'Month 1', m2: 'Month 2', m3: 'Month 3' };
  var youPct = Math.max(0, Math.min(100, diff(start, t) / span * 100));
  var ticks = [];
  for (var mo = 8; mo <= 11; mo++) {
    var md = new Date(2026, mo, 1);
    if (md < start) md = start;
    ticks.push('<span style="left:' + (diff(start, md) / span * 100).toFixed(2) + '%">' +
      MON[md.getMonth()] + '</span>');
  }
  var miles = P.milestones.slice().sort(function (a, b) { return a.date < b.date ? -1 : 1; });
  var pins = miles.map(function (m, i) {
    var p = Math.max(0, Math.min(100, diff(start, d(m.date)) / span * 100));
    var edge = p < 8 ? ' al' : p > 92 ? ' ae' : '';
    var pos = p < 8 ? 'left:0' : p > 92 ? 'right:0' : 'left:' + p.toFixed(2) + '%';
    return '<span class="rp ' + (i % 2 ? 'r2' : 'r1') + edge + '" style="' + pos + '" ' +
      'title="' + esc(m.title + ' — ' + m.note) + '"><b>' + (i + 1) + '</b><i>' +
      esc(shortDate(d(m.date))) + '</i></span>';
  }).join('');
  $('#p-rail').innerHTML =
    '<div class="rail" data-reveal>' +
      '<div class="rail-ticks">' + ticks.join('') + '</div>' +
      '<div class="rail-line">' + P.phases.map(function (ph) {
        return '<i style="flex:' + counts[ph.key] + ';background:' + PC[ph.key] + '">' +
          esc(short[ph.key]) + '</i>'; }).join('') + '</div>' +
      (t >= start && t <= end ? '<span class="rail-you" style="left:' + youPct.toFixed(2) + '%"><em>Today</em></span>' : '') +
      '<div class="rail-pins">' + pins + '</div>' +
    '</div>';

  /* legend */
  $('#p-legend').innerHTML = P.phases.map(function (ph) {
    return '<button type="button" data-ph="' + ph.key + '" aria-pressed="true">' +
      '<i style="background:' + PC[ph.key] + '"></i>' + esc(ph.name) + '</button>'; }).join('');
  $('#p-flegend').innerHTML = P.legend.map(function (l) {
    return '<span><b class="fchip ' + l.k + '">' + esc(l.sym) + '</b>' + esc(l.label) + '</span>'; }).join('');

  /* phases + tiles */
  $('#p-phases').innerHTML = P.phases.map(function (ph) {
    var days = P.days.filter(function (x) { return x.phase === ph.key; });
    var done = days.filter(function (x) { return d(x.date) < t; }).length;
    return '<section class="phase" data-ph="' + ph.key + '" style="--pc:' + PC[ph.key] + '">' +
      '<div class="phase-h"><h3>' + esc(ph.name) + '</h3><span class="mono">' + esc(ph.sub) + '</span>' +
        '<span class="pn">' + done + ' / ' + days.length + ' done</span></div>' +
      '<p class="phase-note">' + esc(ph.note) + '</p>' +
      '<div class="dgrid">' + days.map(function (x) {
        var dd = d(x.date), cls = 'dtile';
        if (dd < t) cls += ' done';
        if (+dd === +t) cls += ' today';
        if (/rest/i.test(x.hours)) cls += ' rest';
        var lab = x.n ? x.n : dd.getDate();
        return '<button type="button" class="' + cls + '" data-date="' + x.date + '" aria-expanded="false" ' +
          'title="' + esc(x.long) + '">' + lab +
          (x.flags.length ? '<i class="fdot"></i>' : '') + '</button>'; }).join('') +
      '</div><div class="ddetail" hidden></div></section>';
  }).join('');

  /* interactions */
  $('#p-legend').addEventListener('click', function (e) {
    var b = e.target.closest('button[data-ph]'); if (!b) return;
    var on = b.getAttribute('aria-pressed') !== 'true';
    b.setAttribute('aria-pressed', String(on));
    $('#p-phases').querySelector('.phase[data-ph="' + b.dataset.ph + '"]').style.display = on ? '' : 'none';
  });
  $('#p-phases').addEventListener('click', function (e) {
    var b = e.target.closest('.dtile'); if (!b) return;
    var sec = b.closest('.phase'), panel = $('.ddetail', sec);
    var open = b.getAttribute('aria-expanded') === 'true';
    $$('.dtile[aria-expanded="true"]').forEach(function (x) { x.setAttribute('aria-expanded', 'false'); });
    if (open) { panel.hidden = true; return; }
    b.setAttribute('aria-expanded', 'true');
    panel.innerHTML = dayCard(P.days.filter(function (x) { return x.date === b.dataset.date; })[0]);
    panel.hidden = false;
  });

  /* milestones + hard dates */
  $('#p-miles').innerHTML = miles.map(function (m, i) {
    var dt = d(m.date);
    return '<div class="mrow' + (dt < t ? ' past' : '') + '">' +
      '<span class="mL"><span class="mn">' + (i + 1) + '</span><span class="md">' + esc(shortDate(dt)) + '</span></span>' +
      '<span><b>' + esc(m.title) + '</b><span>' + esc(m.note) + '</span></span></div>'; }).join('');
  $('#p-hard').innerHTML =
    '<thead><tr><th>Date</th><th>Day</th><th>What</th></tr></thead><tbody>' +
    P.hardDates.map(function (h) {
      return '<tr><td class="k">' + h.when + '</td><td>' + esc(h.day) + '</td><td>' + h.what + '</td></tr>'; }).join('') +
    '</tbody>';
}

function fmtLong(dt) {
  var W = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
  var M = ['January','February','March','April','May','June','July','August','September','October','November','December'];
  return W[dt.getDay()] + ' ' + dt.getDate() + ' ' + M[dt.getMonth()] + ' ' + dt.getFullYear();
}
var FLAGLABEL = { blocking: 'Blocking', deadline: 'Hard deadline', cost: 'Costs money', both: 'Both founders', wait: 'Waiting period' };
function dayCard(x) {
  if (!x) return '';
  return '<div class="dd-top"><b>' + esc(x.long) + '</b>' +
      (x.hours ? '<span class="mono small">' + esc(x.hours) + '</span>' : '') +
      (x.n ? '<span class="tag">Day ' + x.n + ' of 90</span>' : '<span class="tag">Setup</span>') +
      x.flags.map(function (f) { return '<span class="fchip ' + f + '">' + esc(FLAGLABEL[f]) + '</span>'; }).join('') +
      x.meta.map(function (m) { return '<span class="small">' + m + '</span>'; }).join('') +
    '</div>' +
    (x.one ? '<p class="dd-one"><em>One thing</em>' + x.one + '</p>' : '') +
    (x.tasks.length ? '<ol class="dtasks">' + x.tasks.map(function (tk) {
      return '<li><span>' + tk.t + tk.flags.map(function (f) {
        return '<span class="fchip ' + f + '">' + esc(FLAGLABEL[f]) + '</span>'; }).join('') + '</span></li>'; }).join('') + '</ol>' : '') +
    (x.notes.length ? '<div class="dnotes">' + x.notes.map(function (n) { return '<p>' + n + '</p>'; }).join('') + '</div>' : '');
}

/* ══ (b) business plan ═════════════════════════════════════════════════ */
function buildBplan() {
  var B = DATA.bplan; if (!B) return;
  $('#bp-dl').innerHTML = B.downloads.map(function (f, i) {
    var name = f.path.split('/').pop().replace(/_/g, ' ').replace(/\.[a-z]+$/i, '');
    return '<a class="btn ' + (i === 0 ? 'btn-solid' : 'btn-line') + ' btn-sm" href="' + esc(f.path) + '" download>' +
      '<span>' + esc(name) + ' &middot; ' + f.ext + '</span><span class="ar">&darr;</span></a>'; }).join('');
  $('#bp-nav').innerHTML = B.sections.map(function (s) {
    return '<li><button type="button" data-s="' + s.n + '" aria-current="false"><i>' +
      String(s.n).padStart(2, '0') + '</i><span>' + esc(s.title) + '</span></button></li>'; }).join('');
  $('#bp-nav').addEventListener('click', function (e) {
    var b = e.target.closest('button[data-s]'); if (b) bpGo(+b.dataset.s);
  });
  $('#bp-body').addEventListener('click', function (e) {
    var b = e.target.closest('button[data-go]'); if (b) bpGo(+b.dataset.go);
  });
  bpGo(1);
}
function bpBlocks(bl) {
  if (bl.t === 'p') return '<p' + (bl.lead ? ' class="lead"' : '') + '>' + bl.x + '</p>';
  if (bl.t === 'h3') return '<h3>' + bl.x + '</h3>';
  if (bl.t === 'cap') return '<p class="bp-cap">' + bl.x + '</p>';
  if (bl.t === 'callout') return '<div class="bp-call"><b>' + bl.title + '</b>' +
    bl.body.map(function (x) { return '<p>' + x + '</p>'; }).join('') + '</div>';
  if (bl.t === 'list') return '<' + (bl.ord ? 'ol' : 'ul') + '>' + bl.items.map(function (i) {
    return '<li><span>' + i + '</span></li>'; }).join('') + '</' + (bl.ord ? 'ol' : 'ul') + '>';
  if (bl.t === 'figure') return '<figure class="bp-fig"><img loading="lazy" src="' + esc(bl.src) +
    '" alt="' + esc(bl.cap ? bl.cap.replace(/<[^>]+>/g, '') : 'Chart from the business plan') + '">' +
    (bl.cap ? '<figcaption>' + bl.cap + '</figcaption>' : '') + '</figure>';
  if (bl.t === 'table') return '<div class="bp-tbl"><div class="ascroll"><table class="atable">' +
    '<thead><tr>' + bl.head.map(function (h) { return '<th>' + esc(h) + '</th>'; }).join('') + '</tr></thead><tbody>' +
    bl.rows.map(function (r) { return '<tr>' + r.map(function (c, i) {
      return '<td' + (i === 0 ? ' class="k"' : '') + '>' + esc(c) + '</td>'; }).join('') + '</tr>'; }).join('') +
    '</tbody></table></div></div>';
  return '';
}
function bpGo(n) {
  var B = DATA.bplan, s = B.sections.filter(function (x) { return x.n === n; })[0];
  if (!s) return;
  $$('#bp-nav button').forEach(function (b) { b.setAttribute('aria-current', String(+b.dataset.s === n)); });
  var prev = B.sections.filter(function (x) { return x.n === n - 1; })[0];
  var next = B.sections.filter(function (x) { return x.n === n + 1; })[0];
  $('#bp-body').innerHTML = '<article class="bp-sec" data-reveal>' +
    '<span class="ord">Section ' + String(n).padStart(2, '0') + ' of ' + B.sections.length + '</span>' +
    '<h2>' + esc(s.title) + '</h2>' + s.blocks.map(bpBlocks).join('') +
    '<div class="bp-move">' +
      '<button type="button" ' + (prev ? 'data-go="' + prev.n + '"' : 'disabled') + '>&larr; ' + esc(prev ? prev.title : 'Start') + '</button>' +
      '<button type="button" ' + (next ? 'data-go="' + next.n + '"' : 'disabled') + '>' + esc(next ? next.title : 'End') + ' &rarr;</button>' +
    '</div></article>';
  setTimeout(function () { $$('#bp-body [data-reveal]').forEach(function (x) { x.classList.add('in'); }); }, 30);
}

/* ══ (c) library ═══════════════════════════════════════════════════════ */
var ICON = {
  eye: '<svg viewBox="0 0 24 24"><path d="M2 12s3.6-6.5 10-6.5S22 12 22 12s-3.6 6.5-10 6.5S2 12 2 12z"/><circle cx="12" cy="12" r="2.6"/></svg>',
  dl: '<svg viewBox="0 0 24 24"><path d="M12 3.5v11M7.5 10.5 12 15l4.5-4.5M4 19.5h16"/></svg>'
};
function kb(n) { return n >= 1048576 ? (n / 1048576).toFixed(1) + ' MB' : Math.max(1, Math.round(n / 1024)) + ' KB'; }
function buildLibrary() {
  var L = DATA.library; if (!L) return;
  $('#lib-lede').innerHTML = 'Everything in the delivery, in the same nine folders as the ZIP. <b>' +
    L.totals.documents + ' documents</b>, ' + L.totals.files + ' files, ' + L.totals.megabytes + ' MB. View it here or download the file.';
  $('#lib-f').innerHTML = '<button type="button" data-f="all" aria-pressed="true">All<span class="c">' + L.totals.documents + '</span></button>' +
    L.folders.map(function (f) {
      return '<button type="button" data-f="' + f.key + '" aria-pressed="false">' + esc(f.title) +
        '<span class="c">' + f.count + '</span></button>'; }).join('');
  var active = 'all', q = '';
  function draw() {
    var out = L.folders.map(function (f) {
      if (active !== 'all' && active !== f.key) return '';
      var items = L.items.filter(function (i) {
        return i.folder === f.key && (!q || i.search.indexOf(q) >= 0); });
      if (!items.length && (q || active === 'all') && !f.count) {
        if (q) return '';
        return '<section class="libgroup"><h3>' + esc(f.key.replace(/_/g, ' ')) + '</h3><p>' + esc(f.blurb) + '</p>' +
          '<p class="libempty">Nothing is staged in this folder yet. It appears here the moment a file lands in <code>v2/out/' + esc(f.key) + '/</code> and the build script is re-run.</p></section>';
      }
      if (!items.length) return '';
      return '<section class="libgroup"><h3>' + esc(f.key.replace(/_/g, ' ')) + '</h3><p>' + esc(f.blurb) +
        ' &middot; ' + plural(items.length, 'document') + '</p><div class="libgrid">' +
        items.map(card).join('') + '</div></section>';
    }).join('');
    $('#lib-out').innerHTML = out || '<p class="libempty">Nothing matches that search.</p>';
  }
  function card(i) {
    var thumb = i.preview
      ? '<img loading="lazy" src="' + esc(i.preview) + '" alt="">'
      : (i.kind === 'image' ? '<img loading="lazy" src="' + esc(i.view) + '" alt="">'
        : '<span class="noimg">' + esc(i.formats[0].ext) + '</span>');
    return '<article class="litem"><span class="lthumb">' + thumb + '</span><div>' +
      '<span class="t">' + esc(i.title) + '</span><span class="d">' + esc(i.desc) + '</span>' +
      '<span class="lfmts">' + i.formats.map(function (f) {
        return '<span class="lfmt ' + f.ext + '">' + f.ext + '</span>'; }).join('') + '</span>' +
      '<span class="lacts"><button type="button" class="prim" data-pv="' + esc(i.stem) + '" data-folder="' + esc(i.folder) + '">' +
        ICON.eye + 'Preview</button>' +
        i.formats.map(function (f) {
          return '<a href="' + esc(f.path) + '" download title="' + kb(f.bytes) + '">' + ICON.dl + f.ext + '</a>'; }).join('') +
      '</span></div></article>';
  }
  $('#lib-f').addEventListener('click', function (e) {
    var b = e.target.closest('button[data-f]'); if (!b) return;
    active = b.dataset.f;
    $$('#lib-f button').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
    draw();
  });
  $('#lib-q').addEventListener('input', function () { q = this.value.trim().toLowerCase(); draw(); });
  $('#lib-out').addEventListener('click', function (e) {
    var b = e.target.closest('button[data-pv]'); if (!b) return;
    var i = L.items.filter(function (x) { return x.stem === b.dataset.pv && x.folder === b.dataset.folder; })[0];
    if (i) preview(i);
  });
  draw();
}

/* preview overlay */
function preview(i) {
  var body = '', note = '';
  if (i.kind === 'pdf') {
    body = '<iframe src="' + esc(i.view) + '#view=FitH" title="' + esc(i.title) + '"></iframe>';
  } else if (i.kind === 'image') {
    body = '<img src="' + esc(i.view) + '" alt="' + esc(i.title) + '">';
  } else if (i.preview) {
    body = '<img src="' + esc(i.preview) + '" alt="First page of ' + esc(i.title) + '">';
    note = 'First page only. Download to open the editable file.';
  } else {
    body = '<p class="pvw-note"><b>Download to open</b>There is no page preview for this format. ' +
      'Download it and open it in the app it belongs to.</p>';
  }
  $('#pvw-t').textContent = i.title;
  $('#pvw-b').innerHTML = body;
  $('#pvw-f').innerHTML = (note ? '<span class="small" style="align-self:center;margin-right:auto">' + esc(note) + '</span>' : '') +
    i.formats.map(function (f, n) {
      return '<a class="btn btn-sm ' + (n === 0 ? 'btn-solid' : 'btn-line') + '" href="' + esc(f.path) + '" download>' +
        '<span>Download ' + f.ext + '</span></a>'; }).join('') +
    (i.kind === 'pdf' ? '<a class="btn btn-sm btn-line" href="' + esc(i.view) + '" target="_blank" rel="noopener"><span>Open in a new tab</span></a>' : '');
  $('#pvw').hidden = false;
  document.body.style.overflow = 'hidden';
  $('#pvw-x').focus();
}
function closePreview() {
  $('#pvw').hidden = true; $('#pvw-b').innerHTML = ''; document.body.style.overflow = '';
}

/* ══ (d) compliance ════════════════════════════════════════════════════ */
var STEPS = ['Not started', 'Applied', 'Waiting', 'Done'];
var COMPLIANCE = [
  { id: 'aml', title: 'AML / MLR supervision', who: 'ICB practice licence &middot; a statutory supervisor',
    state: 'todo', label: 'Not started', cur: 0,
    icon: '<path d="M12 3l7.5 3v5.5c0 4.4-3.1 8.3-7.5 9.5-4.4-1.2-7.5-5.1-7.5-9.5V6z"/><path d="m9 12 2 2 4-4.5"/>',
    started: 'Not started &mdash; to apply on Tuesday 1 September 2026',
    blocks: 'Every pound of revenue. Klyara cannot lawfully carry on bookkeeping by way of business until supervision is confirmed, so nothing that sells the service can go live before it.',
    next: 'Apply through ICB on day one of the setup phase: &pound;94 application, then &pound;373&ndash;&pound;406 a year (&pound;206 licence plus &pound;167&ndash;&pound;200 membership). Stated processing time is 28 days, so a 1 September application puts supervision around 29 September. Write the application date on a wall and chase weekly once it passes 28 days.',
    src: 'Risk register &sect;2 &middot; Market intelligence &sect;1' },
  { id: 'ico', title: 'ICO data protection fee', who: 'Information Commissioner&rsquo;s Office',
    state: 'todo', label: 'Not started', cur: 0,
    icon: '<rect x="4" y="10" width="16" height="10.5" rx="2.5"/><path d="M8 10V7.5a4 4 0 0 1 8 0V10"/>',
    started: 'Not started &mdash; to register during the setup phase',
    blocks: 'Holding client personal data lawfully, and the privacy notice in the pack being true on the day it is issued. It is also a question the practice licence application asks.',
    next: 'Register at ico.org.uk and pay the annual data protection fee. Confirm the fee tier at the point of registration and do not publish a figure until it is confirmed &mdash; no number in this pack has been verified for it.',
    src: 'Email programme &sect;1 &middot; Privacy notice' },
  { id: 'pii', title: 'Professional indemnity insurance', who: 'A condition of the ICB practice licence',
    state: 'todo', label: 'Not started', cur: 0,
    icon: '<path d="M12 3.5 4.5 6.5v6c0 4 3.1 7.6 7.5 8.7 4.4-1.1 7.5-4.7 7.5-8.7v-6z"/><path d="M12 9v5"/><circle cx="12" cy="16.6" r=".9" fill="currentColor" stroke="none"/>',
    started: 'Not started &mdash; quotes to be requested Tuesday 1 September 2026',
    blocks: 'The practice licence itself. ICB will not issue a licence without cover in place, so this sits in front of AML supervision, not beside it.',
    next: 'Get quotes on day one of the setup phase &mdash; ICB members have a discounted route. Chase on Thursday 3 September if nothing has come back. Decide the cover level in decision block 2 with Craig.',
    src: 'Day-by-day plan, Tue 1 Sep &middot; Market intelligence &sect;1' },
  { id: 'asa', title: 'ASA / CAP compliance of site claims', who: 'Advertising Standards Authority &middot; the CAP Code',
    state: 'todo', label: 'Not started', cur: 0,
    icon: '<path d="M12 4v16M12 4 5 7.5v6L12 10l7 3.5v-6z"/><path d="M4 20h16"/>',
    started: 'Not started &mdash; scheduled for Wednesday 2 September 2026',
    blocks: 'Driving any traffic at all to klyara.com. Five invented testimonials are live and several service claims describe things that are not running yet &mdash; a banned practice under the DMCC Act 2024 and a conduct problem in front of the licence application.',
    next: 'Remove the five homepage testimonials and replace them with the honest-new-firm block from the website audit. Then future-tense every claim that is not true today. The checklist is below, and the whole job takes an afternoon.',
    src: 'Website audit, critical section &middot; Risk register &sect;1' }
];
var CLAIMS = [
  ['&ldquo;Qualified, not just confident&rdquo;', 'Which qualifications are actually held right now?'],
  ['Xero / QuickBooks / FreeAgent certified', 'Certification is a week-1 task. Is it done?'],
  ['&ldquo;24/7 answering&rdquo;', 'Is the white-label service live and wired to the number?'],
  ['AI receptionist, chatbot, invoice chasing as live services', 'Month 1 sells core tiers, receptionist, website and phone only. The rest should read &ldquo;coming soon&rdquo;.'],
  ['Client portal', 'Is the build live at app.klyara.com?'],
  ['Review collection service', 'Selling a review service means being beyond reproach on your own site.'],
  ['Five named homepage testimonials', 'Klyara has no clients. They come down before any traffic is driven to the site.']
];
function buildCompliance() {
  $('#c-board').innerHTML = COMPLIANCE.map(function (c) {
    var stColor = { todo: 'var(--a-todo)', applied: 'var(--a-applied)', wait: 'var(--a-wait)', done: 'var(--a-done)' }[c.state];
    return '<article class="citem" data-reveal><div class="ctop">' +
      '<span class="cicn"><svg viewBox="0 0 24 24">' + c.icon + '</svg></span>' +
      '<span><h3>' + c.title + '</h3><span class="cwho">' + c.who + '</span></span>' +
      '<span class="cstate ' + c.state + '">' + c.label + '</span></div>' +
      '<div class="cstep" style="--st:' + stColor + '">' + STEPS.map(function (s, i) {
        return '<div class="' + (i <= c.cur ? 'on' : '') + (i === c.cur ? ' cur' : '') + '">' + s + '</div>'; }).join('') + '</div>' +
      '<div class="cmeta">' +
        '<div><span class="lbl">Started</span><span class="val">' + c.started + '</span></div>' +
        '<div><span class="lbl">Blocks</span><span class="val">' + c.blocks + '</span></div>' +
        '<div><span class="lbl">Next</span><span class="val">' + c.next + '</span></div>' +
        '<div><span class="lbl">Source</span><span class="val small">' + c.src + '</span></div>' +
      '</div></article>'; }).join('');
  $('#c-claims').innerHTML = CLAIMS.map(function (c) {
    return '<div class="row2"><span>' + c[0] + '<span class="small" style="display:block">' + c[1] + '</span></span>' +
      '<span class="cstate todo">To check</span></div>'; }).join('');
}

/* ══ (f) launch control ════════════════════════════════════════════════ */
var DECIDE = [
  ['1 · Identity', 4, false], ['2 · Regulatory', 5, true], ['3 · Service', 4, false], ['4 · Capacity', 4, true],
  ['5 · Money', 4, false], ['6 · Content', 3, false], ['7 · Pricing', 6, false]
];
var DEFECTS = [
  ['Four pages scrolled sideways on a phone', 'A 390px viewport check. Earlier audits only tested desktop.', 'Fixed'],
  ['Six links to a page that never existed', 'Link-graph audit across every page', 'Page built'],
  ['Every carousel slide with a two-line headline was clipping', 'Looking at the rendered images rather than trusting the generator', '60 slides rebuilt'],
  ['Five factual claims wrong or overstated', 'Checking thirty figures against gov.uk, one by one', 'Sources recorded'],
  ['Four generators would fail on a fresh copy', 'Rebuilding the whole asset set into an empty directory', 'Fixed'],
  ['&ldquo;Nobody local publishes prices&rdquo; was not quite true', 'Actually running the searches instead of assuming', 'Reworded'],
  ['&ldquo;No good free CIS calculator online&rdquo; was wrong', 'Same search. There are at least eight and several are good.', 'Claim removed'],
  ['Two dates fell on the wrong weekday', 'Automated weekday check across every dated claim', '60 days verify'],
  ['Twelve breadcrumbs pointed at a URL that did not exist', 'Reading the structured data rather than trusting it', 'Index built'],
  ['Five pages referenced social cards nobody had generated', 'Checking whether every referenced file was actually there', '20 cards built'],
  ['Six documents carried no AML hold marker', 'An independent adversarial review', 'Hold box on all six'],
  ['The penalty estimator overstated the bill by about half', 'Same review, reasoning through the JavaScript by hand', '17 assertions test it'],
  ['The reverse charge tool was wrong for zero-rated new build', 'Same review, against HMRC&rsquo;s own guidance', 'Two questions added']
];
function bars(el, rows, colour) {
  var max = Math.max.apply(null, rows.map(function (r) { return r[1]; })) || 1;
  el.innerHTML = rows.map(function (r) {
    return '<div class="bar"><span class="lbl">' + r[0] + '</span>' +
      '<span class="trk"><i style="--w:' + (r[1] / max).toFixed(3) + ';--bc:' + (r[2] || colour) + '"></i></span>' +
      '<span class="v">' + r[1] + '</span></div>'; }).join('');
}
function buildLaunch() {
  bars($('#lc-decide'), DECIDE.map(function (r) {
    return [r[0] + (r[2] ? ' <span class="fchip both" style="margin:0">Craig</span>' : ''), r[1],
      r[2] ? 'var(--brass)' : 'var(--em)']; }));
  var L = DATA.library;
  if (L) bars($('#lc-pack'), L.folders.filter(function (f) { return f.count; }).map(function (f, i) {
    return [esc(f.title), f.count, ['var(--em)', 'var(--pine)', 'var(--brass)', 'var(--warn)'][i % 4]]; }));
  var P = DATA.plan;
  if (P) {
    var st = d(P.anchors.setupStart), en = d(P.anchors.day90), sp = diff(st, en);
    var sn = { setup: 'Setup', m1: 'Month 1 — Launch', m2: 'Month 2 — Build', m3: 'Month 3 — Convert' };
    var rows = P.phases.map(function (ph) {
      var days = P.days.filter(function (x) { return x.phase === ph.key; });
      var a = d(days[0].date), b = d(days[days.length - 1].date);
      var l = diff(st, a) / sp * 100, w = (diff(a, b) + 1) / sp * 100;
      var range = shortDate(a) + ' &ndash; ' + shortDate(b);
      var wide = w >= 22;
      return '<div class="ptl-row" style="--pc:' + PC[ph.key] + '">' +
        '<span class="w">' + esc(sn[ph.key]) + '<em>' + esc(ph.sub) + '</em></span>' +
        '<span class="ptl-track"><span class="ptl-bar" style="left:' + l.toFixed(2) + '%;width:' + w.toFixed(2) + '%" ' +
          'title="' + range + '">' + (wide ? range : '') + '</span>' +
          (wide ? '' : '<span class="ptl-out" style="left:' + (l + w).toFixed(2) + '%">' + range + '</span>') +
        '</span></div>'; }).join('');
    var ax = [];
    for (var mo = 8; mo <= 11; mo++) {
      var md = new Date(2026, mo, 1); if (md < st) md = st;
      ax.push('<span style="left:' + (diff(st, md) / sp * 100).toFixed(2) + '%">' + MON[md.getMonth()] + '</span>');
    }
    $('#lc-phases').innerHTML = rows +
      '<div class="ptl-axis"><span></span><span class="sc">' + ax.join('') + '</span></div>';
  }
  $('#lc-defects').innerHTML = DEFECTS.map(function (x) {
    return '<div class="def"><span class="tick"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7"/></svg></span>' +
      '<span><b>' + x[0] + '</b><span>' + x[1] + '</span></span><span class="st">' + x[2] + '</span></div>'; }).join('');
}

var BUILD = { plan: buildPlan, bplan: buildBplan, library: buildLibrary, compliance: buildCompliance, launch: buildLaunch };

/* ══ boot ══════════════════════════════════════════════════════════════ */
function boot() {
  var P = DATA.plan, L = DATA.library, B = DATA.bplan;
  if (P) $('#n-plan').textContent = '90';
  if (B) $('#n-bplan').textContent = B.sections.length;
  if (L) $('#n-library').textContent = L.totals.documents;
  $('#a-gen').textContent = L ? 'Built from the pack on ' + L.generated : '';
  var t = today();
  $('#a-clock').textContent = fmtLong(t);

  $('.atabs').addEventListener('click', function (e) {
    var b = e.target.closest('.atab'); if (b) show(b.dataset.view, true);
  });
  addEventListener('hashchange', function () { show((location.hash || '').replace('#/', ''), false); });
  $('#pvw-x').addEventListener('click', closePreview);
  $('#pvw').addEventListener('click', function (e) { if (e.target === this) closePreview(); });
  addEventListener('keydown', function (e) { if (e.key === 'Escape' && !$('#pvw').hidden) closePreview(); });
  $('#q-onedrive').addEventListener('click', function (e) {
    e.preventDefault();
    alert('The OneDrive folder URL has not been set yet.\n\nPaste it into admin.html, on the link with id "q-onedrive".');
  });

  show((location.hash || '').replace('#/', '') || 'plan', true);
}

var pending = 3;
function ready() { if (--pending === 0) boot(); }
load('plan', 'plan', ready);
load('library', 'library', ready);
load('bplan', 'bplan', ready);
})();
