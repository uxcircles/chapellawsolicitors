document.documentElement.classList.add('js');

// Mobile navigation
const toggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('.nav');
if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && nav.classList.contains('open')) {
      nav.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
      toggle.focus();
    }
  });
}

// Header shadow once the page scrolls
const header = document.querySelector('.site-header');
if (header) {
  const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 8);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });
}

// Open / closed now, on London time (Mon–Fri 9:30–18:30)
document.querySelectorAll('.open-status').forEach((el) => {
  try {
    const parts = new Intl.DateTimeFormat('en-GB', {
      timeZone: 'Europe/London', weekday: 'short', hour: '2-digit', minute: '2-digit', hourCycle: 'h23',
    }).formatToParts(new Date());
    const get = (t) => parts.find((p) => p.type === t).value;
    const mins = Number(get('hour')) * 60 + Number(get('minute'));
    const open = !['Sat', 'Sun'].includes(get('weekday')) && mins >= 570 && mins < 1110;
    el.textContent = open ? el.dataset.open : el.dataset.closed;
    el.classList.toggle('is-open', open);
  } catch (e) { el.remove(); }
});

// Copy WeChat ID
document.querySelectorAll('[data-copy]').forEach((btn) => {
  const small = btn.querySelector('small');
  const label = small ? small.textContent : '';
  btn.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(btn.dataset.copy);
      btn.classList.add('done');
      if (small) small.textContent = btn.dataset.done;
      setTimeout(() => { btn.classList.remove('done'); if (small) small.textContent = label; }, 2200);
    } catch (e) { /* clipboard blocked: the ID is visible to copy by hand */ }
  });
});

// Scroll-spy for a list of in-page links
function spy(links, onActive) {
  const map = new Map();
  links.forEach((a) => {
    const t = document.getElementById(a.getAttribute('href').slice(1));
    if (t) map.set(t, a);
  });
  if (!map.size || !('IntersectionObserver' in window)) return;
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      links.forEach((l) => l.classList.remove('active'));
      const a = map.get(e.target);
      a.classList.add('active');
      if (onActive) onActive(a);
    });
  }, { rootMargin: '-35% 0px -60% 0px' });
  map.forEach((_, t) => io.observe(t));
}
const keepInView = (a) => {
  const row = a.parentElement;
  if (row.scrollWidth > row.clientWidth) row.scrollTo({ left: a.offsetLeft - 24, behavior: 'smooth' });
};
spy([...document.querySelectorAll('.rail a')], keepInView);
spy([...document.querySelectorAll('.chips a')], keepInView);

// Fee search
const search = document.getElementById('fee-search');
if (search) {
  const groups = [...document.querySelectorAll('[data-fee-group]')];
  const empty = document.getElementById('fee-empty');
  const chips = document.querySelector('.chips');
  groups.forEach((g) => g.querySelectorAll('tbody th').forEach((th) => { th.dataset.text = th.textContent; }));
  const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  search.addEventListener('input', () => {
    const q = search.value.trim().toLowerCase();
    let any = false;
    groups.forEach((g) => {
      const title = g.querySelector('h2').textContent.toLowerCase();
      const groupHit = q && title.includes(q);
      let shown = 0;
      g.querySelectorAll('tbody tr').forEach((tr) => {
        const th = tr.querySelector('th');
        const text = th.dataset.text;
        const i = text.toLowerCase().indexOf(q);
        const hit = !q || groupHit || i > -1;
        tr.hidden = !hit;
        th.innerHTML = q && i > -1
          ? esc(text.slice(0, i)) + '<mark>' + esc(text.slice(i, i + q.length)) + '</mark>' + esc(text.slice(i + q.length))
          : esc(text);
        if (hit) shown++;
      });
      g.hidden = shown === 0;
      if (shown) any = true;
    });
    empty.hidden = any;
    if (chips) chips.hidden = !!q;
  });
}

// Enquiry form: opens a pre-filled email (no backend needed)
const form = document.getElementById('enquiry-form');
if (form) {
  const params = new URLSearchParams(location.search);
  if (params.get('area')) form.elements.area.value = params.get('area');
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const f = form.elements;
    const required = [f.name, f.email, f.message];
    let ok = true;
    required.forEach((el) => {
      const bad = !el.value.trim() || (el.type === 'email' && !el.checkValidity());
      el.setAttribute('aria-invalid', String(bad));
      if (bad) ok = false;
    });
    form.querySelector('.form-error').hidden = ok;
    if (!ok) { required.find((el) => el.getAttribute('aria-invalid') === 'true').focus(); return; }
    const area = f.area.selectedIndex > 0 ? f.area.options[f.area.selectedIndex].text : '';
    const lines = [
      `Name / 姓名: ${f.name.value.trim()}`,
      `Phone / 电话: ${f.phone.value.trim()}`,
      `Email / 电邮: ${f.email.value.trim()}`,
      `Area / 事项: ${area}`,
      `Language / 语言: ${f.lang.value}`,
      '',
      f.message.value.trim(),
    ];
    const subject = `${form.dataset.subject}${area ? ' – ' + area : ''}`;
    location.href = `mailto:${form.dataset.to}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(lines.join('\n'))}`;
  });
}

// Reveal on scroll
const els = document.querySelectorAll('.reveal');
if ('IntersectionObserver' in window) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.08 });
  els.forEach((el) => io.observe(el));
} else {
  els.forEach((el) => el.classList.add('in'));
}

const y = document.getElementById('year');
if (y) y.textContent = new Date().getFullYear();
