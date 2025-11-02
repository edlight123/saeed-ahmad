// Theme toggle
const themeBtn = document.querySelector('.theme-toggle');
if (themeBtn) {
  themeBtn.addEventListener('click', () => {
    const cur = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
    document.documentElement.dataset.theme = cur;
    localStorage.setItem('theme', cur);
  });
}

// Mobile nav
const navToggle = document.querySelector('.nav-toggle');
const navList = document.querySelector('.nav-list');
if (navToggle && navList) {
  navToggle.addEventListener('click', () => {
    const open = navList.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', String(open));
  });
  navList.addEventListener('click', (e) => {
    if (e.target.closest('a')) navList.classList.remove('open');
  });
}

// Scroll spy
const sections = [...document.querySelectorAll('main .section[id]')];
const links = [...document.querySelectorAll('.nav-list a[href^="#"]')];
const spy = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    const id = entry.target.getAttribute('id');
    const link = links.find((a) => a.getAttribute('href') === `#${id}`);
    if (!link) return;
    if (entry.isIntersecting) {
      links.forEach((a) => a.classList.remove('active'));
      link.classList.add('active');
    }
  });
}, { rootMargin: '-50% 0px -45% 0px', threshold: [0, 0.2, 0.6, 1] });
sections.forEach((sec) => spy.observe(sec));

// Reveal animations
const reveals = document.querySelectorAll('.section .container > *');
const revObs = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('in');
      revObs.unobserve(entry.target);
    }
  });
});
reveals.forEach((el) => {
  el.classList.add('reveal');
  revObs.observe(el);
});

// Year footer
const yearEl = document.getElementById('year');
if (yearEl) yearEl.textContent = String(new Date().getFullYear());

// Content loader (optional) — load site/content.json and render
async function loadContent() {
  try {
    const res = await fetch('content.json', { cache: 'no-store' });
    if (!res.ok) return; // if missing, skip
    const c = await res.json();

    // Hero
    if (c.hero) {
      const nameEl = document.querySelector('#home .mega');
      const brandEl = document.querySelector('.brand .brand-name');
      const leadEl = document.querySelector('#home .lead');
      const metaItems = document.querySelectorAll('#home .meta li span');
      if (nameEl && c.hero.name) nameEl.textContent = c.hero.name;
      if (brandEl && c.hero.name) brandEl.textContent = c.hero.name;
      if (leadEl && c.hero.tagline) leadEl.textContent = c.hero.tagline;
      if (metaItems[0] && 'location' in c.hero) metaItems[0].textContent = c.hero.location || '—';
      if (metaItems[1] && 'currently' in c.hero) metaItems[1].textContent = c.hero.currently || '—';
    }

    // About
    if (c.about) {
      const bioEl = document.querySelector('#about p.muted');
      if (bioEl && c.about.bio) bioEl.textContent = c.about.bio;
      const aboutLists = document.querySelectorAll('#about .about-card ul');
      if (aboutLists[0] && Array.isArray(c.about.expertise)) {
        aboutLists[0].innerHTML = c.about.expertise.map((x) => `<li>${escapeHtml(x)}</li>`).join('');
      }
      if (aboutLists[1] && Array.isArray(c.about.highlights)) {
        aboutLists[1].innerHTML = c.about.highlights.map((x) => `<li>${escapeHtml(x)}</li>`).join('');
      }
    }

    // Experience
    if (Array.isArray(c.experience)) {
      const timeline = document.querySelector('#experience .timeline');
      if (timeline) {
        timeline.innerHTML = c.experience.map(exp => `
          <article class="item">
            <div class="item-head">
              <h3>${escapeHtml(exp.role || '')} @ ${escapeHtml(exp.org || '')}</h3>
              <span class="muted">${escapeHtml((exp.start || ''))} — ${escapeHtml((exp.end || ''))}</span>
            </div>
            ${exp.summary ? `<p class="muted">${escapeHtml(exp.summary)}</p>` : ''}
            ${Array.isArray(exp.bullets) && exp.bullets.length ? `<ul>${exp.bullets.map(b => `<li>${escapeHtml(b)}</li>`).join('')}</ul>` : ''}
          </article>
        `).join('');
      }
    }

    // Skills
    if (Array.isArray(c.skills)) {
      const wrap = document.querySelector('#skills .skills-chips');
      if (wrap) wrap.innerHTML = c.skills.map(s => `<span class="chip">${escapeHtml(s)}</span>`).join('');
    }

    // Projects
    if (Array.isArray(c.projects)) {
      const cards = document.querySelector('#projects .cards');
      if (cards) {
        cards.innerHTML = c.projects.map(p => `
          <article class="card project">
            <div class="card-head">
              <h3>${escapeHtml(p.name || '')}</h3>
              <div class="tags">${(p.tags||[]).map(t => `<span class="chip">${escapeHtml(t)}</span>`).join('')}</div>
            </div>
            ${p.desc ? `<p class="muted">${escapeHtml(p.desc)}</p>` : ''}
            <div class="card-actions">
              ${p.demo ? `<a class="btn small" href="${attr(p.demo)}" target="_blank" rel="noopener">Demo</a>` : ''}
              ${p.code ? `<a class="btn small" href="${attr(p.code)}" target="_blank" rel="noopener">Code</a>` : ''}
            </div>
          </article>
        `).join('');
      }
    }

    // Gallery
    if (Array.isArray(c.gallery)) {
      const grid = document.querySelector('#gallery .gallery-grid');
      if (grid) {
        grid.innerHTML = c.gallery.map(g => `
          <figure class="tile">
            <img src="${attr(g.src)}" alt="${attr(g.alt||'Gallery image')}" loading="lazy"/>
            ${g.caption ? `<figcaption class="muted" style="padding:8px 10px">${escapeHtml(g.caption)}</figcaption>` : ''}
          </figure>
        `).join('');
        initLightbox(grid);
      }
    }

    // Publications
    if (Array.isArray(c.publications)) {
      const list = document.querySelector('#publications .pub-list');
      if (list) {
        list.innerHTML = c.publications.map(pub => `
          <li>
            <span class="pub-title">${escapeHtml(pub.title || '')}</span>
            <span class="pub-meta muted">${escapeHtml(pub.venue || '')}${pub.year ? `, ${escapeHtml(pub.year)}` : ''}</span>
            ${pub.pdf ? `<a class="link" href="${attr(pub.pdf)}" target="_blank" rel="noopener">PDF</a>` : ''}
          </li>
        `).join('');
      }
    }

    // Contact
    if (c.contact) {
      const actions = document.querySelector('#contact .contact-actions');
      if (actions) {
        const emailBtn = c.contact.email ? `<a class="btn primary" href="mailto:${attr(c.contact.email)}">Email</a>` : '';
        const links = Array.isArray(c.contact.links) ? c.contact.links.map(l => `<a class="btn" href="${attr(l.url)}" target="_blank" rel="noopener">${escapeHtml(l.label||'Link')}</a>`).join('') : '';
        const cv = c.contact.cv ? `<a class="btn" href="${attr(c.contact.cv)}" target="_blank" rel="noopener">CV</a>` : '';
        actions.innerHTML = emailBtn + links + cv;
      }
    }

    // JSON-LD enrich
    try {
      const ld = document.querySelector('script[type="application/ld+json"]');
      if (ld) {
        const data = JSON.parse(ld.textContent);
        if (c.hero?.name) data.name = c.hero.name;
        if (c.contact?.links?.length) data.sameAs = c.contact.links.map(l => l.url);
        ld.textContent = JSON.stringify(data);
      }
    } catch {}
  } catch (e) {
    // fail silent: content.json is optional
    // console.warn('Content load skipped:', e);
  }
}

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, (c) => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;','\'':'&#39;'}[c]));
}
function attr(s) {
  return String(s).replace(/["']/g, (c) => ({'"':'&quot;','\'':'&#39;'}[c]));
}

loadContent();

// Simple lightbox
function initLightbox(container){
  const overlay = document.getElementById('lightbox') || createLightbox();
  container.addEventListener('click', (e) => {
    const img = e.target.closest('img');
    if (!img) return;
    overlay.querySelector('img').src = img.src;
    overlay.classList.add('open');
  });
}
function createLightbox(){
  const o = document.createElement('div');
  o.id = 'lightbox';
  o.className = 'lightbox';
  o.innerHTML = `<button class="close" aria-label="Close">✕</button><img alt="Expanded image"/>`;
  o.addEventListener('click', (e) => {
    if (e.target.classList.contains('close') || e.target === o) o.classList.remove('open');
  });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') o.classList.remove('open'); });
  document.body.appendChild(o);
  return o;
}
