/* Klyara control panel — the tracker.
   Ticks every task, subtask and checklist item in the ninety-day plan and keeps
   the counts live. Vanilla, dependency-free, reduced-motion safe, file:// safe.

   WHERE THE STATE LIVES: window.localStorage, in this browser, under one
   versioned key. It is not on a server. It is not shared between people, it is
   not on your phone, and clearing site data clears it. The export button is the
   only way to move it. This is said out loud in the UI, not just here. */
(function () {
"use strict";

var KEY = 'klyara.ticks.v1';          /* versioned: a plan data update must not wipe ticks */
var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
var $ = function (s, r) { return (r || document).querySelector(s); };
var $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };
function esc(s) {
  return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) {
    return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; });
}
var MONL = ['January','February','March','April','May','June','July','August',
            'September','October','November','December'];
var WDL = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
function d(iso) { var p = String(iso).split('-'); return new Date(+p[0], +p[1] - 1, +p[2]); }
function today() { var n = new Date(); return new Date(n.getFullYear(), n.getMonth(), n.getDate()); }
function diff(a, b) { return Math.round((b - a) / 864e5); }
function fmtLong(dt) {
  return WDL[dt.getDay()] + ' ' + dt.getDate() + ' ' + MONL[dt.getMonth()] + ' ' + dt.getFullYear();
}
function plural(n, s) { return n + ' ' + s + (n === 1 ? '' : 's'); }
function hm(mins) {
  if (!mins) return '—';
  var h = Math.floor(mins / 60), m = mins % 60;
  return (h ? h + 'h' : '') + (h && m ? ' ' : '') + (m ? m + 'm' : '');
}

/* ══ the store ═════════════════════════════════════════════════════════════
   { v, planVersion, updated, ticks: { id: iso-timestamp } }
   Ticks are keyed by the stable task id from plan90.json. Ids the current data
   no longer contains are KEPT, never pruned — a data edit must not destroy a
   record of work that was actually done. */
var mem = null;                        /* in-memory mirror, always authoritative */
var storageOK = true;

function blank() {
  return { v: 1, planVersion: null, updated: null, ticks: {} };
}
function read() {
  if (mem) return mem;
  mem = blank();
  try {
    var raw = localStorage.getItem(KEY);
    if (raw) {
      var j = JSON.parse(raw);
      if (j && j.ticks && typeof j.ticks === 'object') mem = {
        v: 1, planVersion: j.planVersion || null, updated: j.updated || null, ticks: j.ticks };
    }
  } catch (e) { storageOK = false; }
  return mem;
}
function write() {
  mem.updated = new Date().toISOString();
  try { localStorage.setItem(KEY, JSON.stringify(mem)); }
  catch (e) { storageOK = false; flagStorage(); }
}
function isOn(id) { return !!read().ticks[id]; }
function setTick(id, on) {
  var s = read();
  if (on) s.ticks[id] = new Date().toISOString();
  else delete s.ticks[id];
  write();
}
function tickCount() { var n = 0, t = read().ticks; for (var k in t) if (t.hasOwnProperty(k)) n++; return n; }
function flagStorage() {
  $$('.tk-storewarn').forEach(function (el) { el.hidden = false; });
}

/* ══ the index ═════════════════════════════════════════════════════════════
   Every tickable id in the panel, grouped into sections and weeks, built once
   from plan90.json plus the two hand-written checklists on other tabs. */
var IX = null;

/* The two hand-written checklists that live on other tabs. Their ids are
   registered UP FRONT, not when the tab is first opened, so the overall total
   never moves depending on where you have clicked. `n` is the row count in
   admin.html (.step5) and in admin.js CLAIMS. bindChecklists() reconciles
   against the real DOM and warns loudly if either ever drifts. */
var EXTRA_SECTIONS = [
  { key: 'lc', name: 'This week’s five', sub: 'Launch control · 01', n: 5, id: 'lc-step-',
    note: 'The five things with a waiting period on them.' },
  { key: 'claims', name: 'Site claims', sub: 'Compliance', n: 7, id: 'claim-',
    note: 'Every claim on klyara.com that has to be true today, future-tensed, or taken down.' }
];

function buildIndex(P) {
  var sections = [], weeks = [], byId = {}, all = [];
  P.phases.forEach(function (ph) {
    sections.push({ key: ph.key, name: ph.name, sub: ph.sub, note: ph.note, ids: [] });
  });
  var sMap = {};
  sections.forEach(function (s) { sMap[s.key] = s; });

  var wMap = {};
  P.weeks.forEach(function (w) {
    var o = { key: w.key, name: w.name, range: w.range, phase: w.phase,
              from: w.from, to: w.to, ids: [], days: [] };
    weeks.push(o); wMap[w.key] = o;
  });

  P.days.forEach(function (day) {
    var ids = [];
    day.tasks.forEach(function (t) {
      ids.push(t.id); byId[t.id] = { kind: 'task', day: day, task: t };
      t.subtasks.forEach(function (s) {
        ids.push(s.id); byId[s.id] = { kind: 'sub', day: day, task: t, sub: s };
      });
    });
    day._ids = ids;
    all = all.concat(ids);
    if (sMap[day.phase]) sMap[day.phase].ids = sMap[day.phase].ids.concat(ids);
    if (wMap[day.week]) { wMap[day.week].ids = wMap[day.week].ids.concat(ids); wMap[day.week].days.push(day); }
  });

  EXTRA_SECTIONS.forEach(function (s) {
    var o = { key: s.key, name: s.name, sub: s.sub, note: s.note, ids: [], extra: true };
    for (var i = 1; i <= s.n; i++) { o.ids.push(s.id + i); all.push(s.id + i); }
    sections.push(o); sMap[s.key] = o;
  });

  IX = { plan: P, sections: sections, sMap: sMap, weeks: weeks, wMap: wMap,
         byId: byId, all: all };
  return IX;
}

function registerExtra(sectionKey, ids) {
  if (!IX) return;
  var s = IX.sMap[sectionKey];
  if (!s) return;
  /* A view that has not been built yet has no rows. That is not drift, so say
     nothing; the ids are already registered from EXTRA_SECTIONS. */
  if (!ids.length) return;
  if (s.ids.length !== ids.length) {
    console.warn('track.js: ' + sectionKey + ' declares ' + s.ids.length + ' rows but the page has ' +
      ids.length + '. Update EXTRA_SECTIONS in track.js.');
  }
  ids.forEach(function (id) {
    if (s.ids.indexOf(id) < 0) { s.ids.push(id); IX.all.push(id); }
  });
}

function doneIn(ids) {
  var n = 0;
  for (var i = 0; i < ids.length; i++) if (isOn(ids[i])) n++;
  return n;
}
function pct(a, b) { return b ? Math.round(a / b * 100) : 0; }

/* ══ you are here ══════════════════════════════════════════════════════════ */
function whereAreWe() {
  var P = IX.plan, t = today();
  var s0 = d(P.anchors.setupStart), s1 = d(P.anchors.setupEnd),
      l = d(P.anchors.launch), e = d(P.anchors.day90);
  if (t < s0) return { state: 'before', days: diff(t, s0), toLaunch: diff(t, l), day: null };
  if (t <= s1) return { state: 'setup', setupDay: diff(s0, t) + 1, toLaunch: diff(t, l), day: null };
  if (t <= e) return { state: 'run', day: diff(l, t) + 1 };
  return { state: 'after', day: 90 };
}
function todayDay() {
  var iso = (function (t) {
    var m = t.getMonth() + 1, dd = t.getDate();
    return t.getFullYear() + '-' + (m < 10 ? '0' : '') + m + '-' + (dd < 10 ? '0' : '') + dd;
  })(today());
  for (var i = 0; i < IX.plan.days.length; i++) if (IX.plan.days[i].date === iso) return IX.plan.days[i];
  return null;
}
function currentWeek() {
  var td = todayDay();
  if (td) return IX.wMap[td.week];
  var t = today();
  for (var i = 0; i < IX.weeks.length; i++) {
    if (t < d(IX.weeks[i].from)) return IX.weeks[i];
  }
  return IX.weeks[IX.weeks.length - 1];
}

/* ══ rendering ═════════════════════════════════════════════════════════════ */
var OWNER = { K: 'Kieran', C: 'Craig', B: 'Both' };
var FLAG = { blocking: 'Blocking', deadline: 'Hard deadline', cost: 'Costs money',
             both: 'Both founders', wait: 'Waiting period' };

function ring(p) {
  var C = 2 * Math.PI * 54;
  return '<div class="ring"><svg viewBox="0 0 132 132" aria-hidden="true">' +
    '<circle class="trk" cx="66" cy="66" r="54"></circle>' +
    '<circle class="bar" cx="66" cy="66" r="54" stroke-dasharray="' + C.toFixed(1) +
    '" stroke-dashoffset="' + (C * (1 - p / 100)).toFixed(1) + '"></circle>' +
    '</svg><span class="lbl"><b>' + p + '%</b><span>ticked</span></span></div>';
}

function box(id, cls) {
  var on = isOn(id);
  return '<button type="button" class="tkbox' + (cls ? ' ' + cls : '') + (on ? ' on' : '') +
    '" data-tick="' + esc(id) + '" role="checkbox" aria-checked="' + on + '">' +
    '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7"/></svg></button>';
}

function taskHTML(t) {
  var on = isOn(t.id);
  var deps = t.deps.map(function (id) {
    var r = IX.byId[id];
    if (!r) return null;
    return '<span class="tkdep' + (isOn(id) ? ' met' : '') + '">' +
      (isOn(id) ? '✓ ' : '↑ ') + esc(r.task.title) + '</span>';
  }).filter(Boolean).join('');
  var subs = t.subtasks.map(function (s) {
    return '<li class="tksub' + (isOn(s.id) ? ' on' : '') + '" data-row="' + esc(s.id) + '">' +
      box(s.id, 'sm') + '<span>' + esc(s.t) + '</span></li>';
  }).join('');
  return '<li class="tktask' + (on ? ' on' : '') + '" data-row="' + esc(t.id) + '">' +
    '<div class="tkt-h">' + box(t.id) +
      '<div class="tkt-b"><b>' + esc(t.title) + '</b>' +
        '<span class="tkt-meta">' +
          '<span class="tkown o' + t.owner + '">' + OWNER[t.owner] + '</span>' +
          '<span class="tkmin">' + hm(t.minutes) + '</span>' +
          t.flags.map(function (f) { return '<span class="fchip ' + f + '">' + esc(FLAG[f] || f) + '</span>'; }).join('') +
        '</span>' +
      '</div>' +
      '<button type="button" class="tkt-x" aria-expanded="false" aria-label="Why, tips and what goes wrong">' +
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg></button>' +
    '</div>' +
    (subs ? '<ul class="tksubs">' + subs + '</ul>' : '') +
    '<div class="tkt-more" hidden>' +
      (deps ? '<p class="tkl"><em>Waits on</em>' + deps + '</p>' : '') +
      '<p class="tkl"><em>Why it matters</em>' + esc(t.why) + '</p>' +
      (t.tips.length ? '<p class="tkl"><em>Tips</em></p><ul class="tktips">' +
        t.tips.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</ul>' : '') +
      '<p class="tkl bad"><em>What usually goes wrong</em>' + esc(t.wrong) + '</p>' +
      '<p class="tkl good"><em>The fix</em>' + esc(t.fix) + '</p>' +
    '</div>' +
  '</li>';
}

function dayHTML(day, isToday) {
  var done = doneIn(day._ids), tot = day._ids.length;
  var owners = {};
  day.tasks.forEach(function (t) { owners[t.owner] = 1; });
  return '<article class="tkday' + (isToday ? ' now' : '') + (done === tot && tot ? ' full' : '') +
      '" id="tkday-' + esc(day.id) + '" data-day="' + esc(day.id) + '">' +
    '<button type="button" class="tkd-h" aria-expanded="' + (isToday ? 'true' : 'false') + '">' +
      '<span class="tkd-n">' + (day.n ? '<b>' + day.n + '</b><i>of 90</i>' :
        '<b>S' + day.setupDay + '</b><i>setup</i>') + '</span>' +
      '<span class="tkd-t">' +
        '<span class="tkd-date">' + esc(day.label) + (isToday ? '<em class="tknow">Today</em>' : '') + '</span>' +
        '<b>' + esc(day.one || 'Rhythm only.') + '</b>' +
        (day.fixed.length ? '<span class="tkd-fixed">' + day.fixed.map(function (f) {
          return '⚠ ' + esc(f.what); }).join(' · ') + '</span>' : '') +
      '</span>' +
      '<span class="tkd-r">' +
        '<span class="tkd-c" data-count="' + esc(day.id) + '">' + done + ' / ' + tot + '</span>' +
        '<span class="tkd-m">' + hm(day.minutes) + '</span>' +
        '<span class="tkd-o">' + Object.keys(owners).map(function (o) {
          return '<i class="o' + o + '" title="' + OWNER[o] + '">' + o + '</i>'; }).join('') + '</span>' +
      '</span>' +
      '<span class="tkd-x" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></svg></span>' +
    '</button>' +
    '<div class="tkd-b"' + (isToday ? '' : ' hidden') + '>' +
      (isToday ? '' : '<!--lazy-->') +
      (isToday ? '<ul class="tktasks">' + day.tasks.map(taskHTML).join('') + '</ul>' : '') +
    '</div>' +
  '</article>';
}

function barRow(name, sub, done, tot, colour) {
  var p = pct(done, tot);
  return '<div class="tkbar' + (p === 100 ? ' full' : '') + '">' +
    '<span class="tkb-l"><b>' + esc(name) + '</b><i>' + esc(sub || '') + '</i></span>' +
    '<span class="tkb-t"><i style="--w:' + (p / 100).toFixed(4) + ';--bc:' + colour + '"></i></span>' +
    '<span class="tkb-v"><b>' + done + '</b>/' + tot + '<i>' + p + '%</i></span>' +
  '</div>';
}

var PC = { setup: 'var(--a-setup)', m1: 'var(--a-m1)', m2: 'var(--a-m2)', m3: 'var(--a-m3)',
           lc: 'var(--brass)', claims: 'var(--warn)' };

/* ══ live recount ══════════════════════════════════════════════════════════ */
/* The day rows are cached once when they are rendered. Re-querying all 103
   cards on every single tick made the panel feel sticky. */
var dayCells = [];
function cacheDayCells() {
  dayCells = [];
  $$('#tk-days .tkday').forEach(function (card) {
    var c = $('.tkd-c', card);
    if (!c) return;
    var id = card.dataset.day, day = null;
    for (var i = 0; i < IX.plan.days.length; i++) {
      if (IX.plan.days[i].id === id) { day = IX.plan.days[i]; break; }
    }
    if (day) dayCells.push({ card: card, c: c, ids: day._ids });
  });
}

function recount() {
  var done = doneIn(IX.all), tot = IX.all.length, p = pct(done, tot);

  var head = $('#tk-head');
  if (head) {
    var bar = $('.bar', head);
    if (bar) {
      var C = 2 * Math.PI * 54;
      bar.setAttribute('stroke-dashoffset', (C * (1 - p / 100)).toFixed(1));
    }
    var lbl = $('.ring .lbl b', head); if (lbl) lbl.textContent = p + '%';
    var dn = $('#tk-done'); if (dn) dn.textContent = done;
    var tn = $('#tk-total'); if (tn) tn.textContent = tot;
    var lft = $('#tk-left'); if (lft) lft.textContent = tot - done;
    var pb = $('#tk-pbar > i'); if (pb) pb.style.setProperty('--w', (p / 100).toFixed(4));
    var pv = $('#tk-pval'); if (pv) pv.textContent = p + '%';
  }

  var sec = $('#tk-sections');
  if (sec) sec.innerHTML = IX.sections.map(function (s) {
    return barRow(s.name, s.sub, doneIn(s.ids), s.ids.length, PC[s.key] || 'var(--em)');
  }).join('');

  var wk = $('#tk-weeks');
  if (wk) wk.innerHTML = IX.weeks.map(function (w) {
    return barRow(w.name, w.range, doneIn(w.ids), w.ids.length, PC[w.phase] || 'var(--em)');
  }).join('');

  for (var i = 0; i < dayCells.length; i++) {
    var cell = dayCells[i], dd = doneIn(cell.ids);
    cell.c.textContent = dd + ' / ' + cell.ids.length;
    cell.card.classList.toggle('full', cell.ids.length > 0 && dd === cell.ids.length);
  }

  var thisW = $('#tk-thisweek-c');
  if (thisW) {
    var w = currentWeek();
    thisW.textContent = doneIn(w.ids) + ' / ' + w.ids.length;
  }
  var io = $('#tk-iocount'); if (io) io.textContent = plural(tickCount(), 'tick');
}

/* ══ export / import ═══════════════════════════════════════════════════════ */
function exportObj() {
  var s = read();
  return {
    app: 'klyara-control', kind: 'ticks', v: 1,
    planVersion: IX ? IX.plan.version : null,
    exported: new Date().toISOString(),
    count: tickCount(),
    ticks: s.ticks
  };
}
function doExport() {
  var txt = JSON.stringify(exportObj(), null, 1);
  var stamp = new Date().toISOString().slice(0, 10);
  var name = 'klyara-ticks-' + stamp + '.json';
  try {
    var blob = new Blob([txt], { type: 'application/json' });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url; a.download = name;
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(function () { URL.revokeObjectURL(url); }, 4000);
    say('Saved ' + name + ' to your downloads.');
  } catch (e) {
    $('#tk-paste').value = txt;
    say('This browser blocked the download. The JSON is in the box below — copy it out.');
  }
}
function doCopy() {
  var txt = JSON.stringify(exportObj(), null, 1);
  var el = $('#tk-paste');
  el.value = txt;
  el.select();
  var ok = false;
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(txt).then(function () {
      say('Copied. Paste it to Craig, or into the box on his panel.');
    }, function () { say('Select the text in the box and copy it by hand.'); });
    return;
  }
  try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
  say(ok ? 'Copied. Paste it to Craig, or into the box on his panel.'
         : 'Select the text in the box and copy it by hand.');
}
function applyImport(txt, mode) {
  var j;
  try { j = JSON.parse(txt); }
  catch (e) { say('That is not valid JSON. Nothing was changed.', true); return; }
  if (!j || j.kind !== 'ticks' || !j.ticks || typeof j.ticks !== 'object') {
    say('That file is not a Klyara tick export. Nothing was changed.', true); return;
  }
  var s = read();
  var before = tickCount();
  if (mode === 'replace') s.ticks = {};
  var added = 0;
  for (var k in j.ticks) {
    if (!j.ticks.hasOwnProperty(k)) continue;
    if (!s.ticks[k]) added++;
    s.ticks[k] = j.ticks[k];
  }
  s.planVersion = j.planVersion || s.planVersion;
  write();
  refreshBoxes();
  recount();
  say(mode === 'replace'
    ? 'Replaced. ' + plural(tickCount(), 'tick') + ' loaded, ' + before + ' discarded.'
    : 'Merged. ' + plural(added, 'new tick') + ' added, ' + plural(tickCount(), 'tick') + ' in total.');
}
function say(msg, bad) {
  var el = $('#tk-iomsg');
  if (!el) return;
  el.textContent = msg;
  el.className = 'tk-iomsg' + (bad ? ' bad' : ' ok');
}
function refreshBoxes() {
  $$('[data-tick]').forEach(function (b) {
    var on = isOn(b.dataset.tick);
    b.classList.toggle('on', on);
    b.setAttribute('aria-checked', String(on));
    var row = b.closest('[data-row]');
    if (row) row.classList.toggle('on', on);
    var li = b.closest('li.step5, .row2');
    if (li) li.classList.toggle('ticked', on);
  });
}

/* ══ the view ══════════════════════════════════════════════════════════════ */
var wired = false;

function build(root, P) {
  if (!P) {
    root.querySelector('#tk-head').innerHTML =
      '<p class="libempty">The plan data did not load. Check <code>assets/data/plan90.json</code>.</p>';
    return;
  }
  if (!IX) buildIndex(P);

  var w = whereAreWe();
  var done = doneIn(IX.all), tot = IX.all.length, p = pct(done, tot);
  var kick, head, note, stats;
  if (w.state === 'before') {
    kick = 'Not started';
    head = plural(w.days, 'day') + ' until setup opens';
    note = 'Nothing is scheduled for Kieran or Craig before Tuesday 1 September 2026. The setup ' +
      'phase opens that morning with the ICB practice licence and the Google Business Profile ' +
      'claim — the two clocks everything else queues behind.';
    stats = [[w.days, 'Days until setup'], [w.toLaunch, 'Days until Day 1'], [tot, 'Things to tick']];
  } else if (w.state === 'setup') {
    kick = 'Setup phase';
    head = 'Setup day ' + w.setupDay + ' of 13';
    note = 'Today is ' + fmtLong(today()) + '. Two items have waiting periods attached and both ' +
      'should already be running.';
    stats = [[w.setupDay, 'Setup days in'], [13 - w.setupDay, 'Setup days left'],
             [w.toLaunch, 'Days until Day 1']];
  } else if (w.state === 'run') {
    kick = 'You are here';
    head = 'Day ' + w.day + ' of 90';
    note = 'Today is ' + fmtLong(today()) + '. Each day has one thing on it — if the day goes ' +
      'wrong and you only do one item, do that one.';
    stats = [[w.day, 'Days in'], [90 - w.day, 'Days left'], [pct(w.day, 90) + '%', 'Through the plan']];
  } else {
    kick = 'Complete';
    head = 'The ninety days are done';
    note = 'Day 90 was Saturday 12 December 2026. Score every line, including the zeros.';
    stats = [[90, 'Days done'], [0, 'Days left'], ['100%', 'Through the plan']];
  }

  $('#tk-head').innerHTML =
    '<div class="anow tknow-card" id="tk-head-in" data-reveal>' + ring(p) +
      '<div><span class="kicker">' + esc(kick) + '</span><h2>' + esc(head) + '</h2>' +
        '<p>' + esc(note) + '</p>' +
        '<div class="anow-stats">' + stats.map(function (s) {
          return '<div><b>' + esc(s[0]) + '</b><span>' + esc(s[1]) + '</span></div>'; }).join('') +
        '</div>' +
        '<div class="tk-prog"><span class="tkp-t" id="tk-pbar"><i style="--w:' + (p / 100).toFixed(4) + '"></i></span>' +
          '<span class="tkp-v"><b id="tk-done">' + done + '</b> of <b id="tk-total">' + tot +
          '</b> ticked · <b id="tk-left">' + (tot - done) + '</b> left · <b id="tk-pval">' + p + '%</b></span></div>' +
        '<p class="tk-honest"><b>These ticks live in this browser only.</b> Not on a server, not ' +
          'shared with the other founder, not on your phone. Clearing site data clears them. ' +
          'Export the JSON below to move them or to send them to Craig.</p>' +
        '<p class="tk-storewarn" hidden><b>This browser will not save.</b> Private browsing or ' +
          'blocked site data. Ticks will work until you reload and then they are gone.</p>' +
      '</div></div>';
  if (!storageOK) flagStorage();

  /* this week */
  var cw = currentWeek();
  $('#tk-week').innerHTML =
    '<div class="acard tkweek"><div class="tkw-h"><div>' +
      '<span class="kicker">' + esc(cw.name) + '</span>' +
      '<h3 class="h3">' + esc(cw.range) + '</h3></div>' +
      '<span class="tkw-c"><b id="tk-thisweek-c">' + doneIn(cw.ids) + ' / ' + cw.ids.length + '</b>' +
      '<i>ticked this week</i></span>' +
      '<button type="button" class="btn btn-line btn-sm" id="tk-jump"><span>Jump to today</span></button>' +
    '</div><div class="tkw-days">' + cw.days.map(function (day) {
      var dd = doneIn(day._ids), td = todayDay();
      return '<a class="tkw-d' + (td && td.id === day.id ? ' now' : '') +
        (day._ids.length && dd === day._ids.length ? ' full' : '') +
        '" href="#tkday-' + esc(day.id) + '"><b>' + esc(day.weekday) + '</b>' +
        '<i>' + esc(day.label.replace(/^\w+ /, '')) + '</i>' +
        '<span>' + dd + '/' + day._ids.length + '</span></a>'; }).join('') +
    '</div></div>';

  /* days */
  var td = todayDay();
  $('#tk-days').innerHTML = IX.plan.days.map(function (day) {
    return dayHTML(day, !!(td && td.id === day.id));
  }).join('');
  cacheDayCells();

  /* fixed dates */
  $('#tk-fixed').innerHTML =
    '<thead><tr><th>Date</th><th>Day</th><th>What</th><th>Note</th></tr></thead><tbody>' +
    IX.plan.fixedDates.map(function (f) {
      return '<tr class="k' + f.kind + '"><td class="k">' + esc(f.label) + '</td>' +
        '<td>' + (f.day == null ? '—' : f.day) + '</td>' +
        '<td>' + esc(f.what) + '</td><td class="small">' + esc(f.note) + '</td></tr>'; }).join('') +
    '</tbody>';

  /* corrections */
  $('#tk-corr').innerHTML = IX.plan.corrections.map(function (c) {
    return '<div class="tkcorr"><b>' + esc(c.where) + '</b>' +
      '<span class="was"><em>Was</em>' + esc(c.was) + '</span>' +
      '<span class="now"><em>Now</em>' + esc(c.now) + '</span></div>'; }).join('');

  /* io */
  $('#tk-iocount').textContent = plural(tickCount(), 'tick');

  if (!wired) wire(root);
  recount();
  setTimeout(function () {
    $$('[data-reveal]', root).forEach(function (x) { x.classList.add('in'); });
  }, 40);
}

function jumpToToday() {
  var td = todayDay();
  var el = td ? $('#tkday-' + td.id) : null;
  if (!el) { say('Today is outside the plan window.'); return; }
  var h = $('.tkd-h', el);
  if (h.getAttribute('aria-expanded') !== 'true') h.click();
  el.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'center' });
  el.classList.add('flash');
  setTimeout(function () { el.classList.remove('flash'); }, 1400);
}

function wire(root) {
  wired = true;

  /* one delegated handler for every checkbox in the whole panel */
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-tick]');
    if (!b) return;
    e.preventDefault(); e.stopPropagation();
    var id = b.dataset.tick, on = !isOn(id);
    setTick(id, on);
    $$('[data-tick="' + id.replace(/"/g, '') + '"]').forEach(function (x) {
      x.classList.toggle('on', on);
      x.setAttribute('aria-checked', String(on));
      var row = x.closest('[data-row]');
      if (row) row.classList.toggle('on', on);
      var li = x.closest('li.step5, .row2');
      if (li) li.classList.toggle('ticked', on);
    });
    recount();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key !== ' ' && e.key !== 'Enter') return;
    var b = e.target.closest && e.target.closest('[data-tick]');
    if (b) { e.preventDefault(); b.click(); }
  });

  /* day open/close, with the task list built on first open */
  $('#tk-days').addEventListener('click', function (e) {
    var x = e.target.closest('.tkt-x');
    if (x) {
      var more = x.closest('.tktask').querySelector('.tkt-more');
      var open = x.getAttribute('aria-expanded') === 'true';
      x.setAttribute('aria-expanded', String(!open));
      more.hidden = open;
      return;
    }
    var h = e.target.closest('.tkd-h');
    if (!h) return;
    var card = h.closest('.tkday'), body = $('.tkd-b', card);
    var open = h.getAttribute('aria-expanded') === 'true';
    if (!open && !body.querySelector('.tktasks')) {
      var day = null;
      for (var i = 0; i < IX.plan.days.length; i++) {
        if (IX.plan.days[i].id === card.dataset.day) { day = IX.plan.days[i]; break; }
      }
      if (day) body.innerHTML = '<ul class="tktasks">' + day.tasks.map(taskHTML).join('') + '</ul>';
    }
    h.setAttribute('aria-expanded', String(!open));
    body.hidden = open;
  });

  $('#tk-jump').addEventListener('click', jumpToToday);

  $('#tk-filters').addEventListener('click', function (e) {
    var b = e.target.closest('button[data-f]');
    if (!b) return;
    $$('#tk-filters button').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
    applyFilter(b.dataset.f);
  });

  $('#tk-io').addEventListener('click', function (e) {
    var b = e.target.closest('button[data-io]');
    if (!b) return;
    var a = b.dataset.io;
    if (a === 'export') doExport();
    else if (a === 'copy') doCopy();
    else if (a === 'merge') applyImport($('#tk-paste').value, 'merge');
    else if (a === 'replace') {
      if (confirm('Replace every tick in this browser with the ones in the box?\n\nThis cannot be undone. Export first if you are not sure.'))
        applyImport($('#tk-paste').value, 'replace');
    } else if (a === 'clear') {
      if (confirm('Clear every tick in this browser?\n\nThis cannot be undone. Export first if you are not sure.')) {
        mem = blank(); write(); refreshBoxes(); recount();
        say('Cleared. Every tick in this browser has gone.');
      }
    }
  });
  $('#tk-file').addEventListener('change', function () {
    var f = this.files && this.files[0];
    if (!f) return;
    var r = new FileReader();
    r.onload = function () { $('#tk-paste').value = String(r.result); applyImport(String(r.result), 'merge'); };
    r.onerror = function () { say('Could not read that file.', true); };
    r.readAsText(f);
    this.value = '';
  });
}

function applyFilter(f) {
  var td = todayDay(), cw = currentWeek();
  $$('#tk-days .tkday').forEach(function (card) {
    var id = card.dataset.day, day = null;
    for (var i = 0; i < IX.plan.days.length; i++) if (IX.plan.days[i].id === id) { day = IX.plan.days[i]; break; }
    if (!day) return;
    var show = true;
    if (f === 'today') show = !!(td && td.id === id);
    else if (f === 'week') show = day.week === cw.key;
    else if (f === 'open') show = doneIn(day._ids) < day._ids.length;
    else if (f === 'deadline') show = day.fixed.length > 0 ||
      day.tasks.some(function (t) { return t.flags.indexOf('deadline') >= 0; });
    else if (f === 'K' || f === 'C' || f === 'B')
      show = day.tasks.some(function (t) { return t.owner === f; });
    card.hidden = !show;
  });
}

/* ══ the two hand-written checklists on the other tabs ═════════════════════ */
function bindChecklists() {
  var ids;
  ids = [];
  $$('#v-launch .step5').forEach(function (li, i) {
    var id = 'lc-step-' + (i + 1);
    ids.push(id);
    if (!$('[data-tick]', li)) li.insertBefore(mk(box(id, 'step')), li.firstChild);
    li.classList.toggle('ticked', isOn(id));
  });
  registerExtra('lc', ids);

  ids = [];
  $$('#v-compliance #c-claims .row2').forEach(function (row, i) {
    var id = 'claim-' + (i + 1);
    ids.push(id);
    if (!$('[data-tick]', row)) row.insertBefore(mk(box(id, 'sm')), row.firstChild);
    row.classList.toggle('ticked', isOn(id));
  });
  registerExtra('claims', ids);
  recount();
}
function mk(html) {
  var t = document.createElement('template');
  t.innerHTML = html.trim();
  return t.content.firstChild;
}

window.KLYTRACK = {
  /* One number, computed once: every tickable thing in the panel. The rail
     badge and the overall counter must never disagree. */
  total: function (P) { if (!IX && P) buildIndex(P); return IX ? IX.all.length : 0; },
  build: build,
  bindChecklists: bindChecklists,
  index: function () { return IX; },
  recount: recount
};
})();
