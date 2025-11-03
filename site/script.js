// Modern Portfolio JavaScript// Theme toggle

const themeBtn = document.querySelector('.theme-toggle');

// Initialize AOS (Animate On Scroll)if (themeBtn) {

AOS.init({  themeBtn.addEventListener('click', () => {

    duration: 800,    const cur = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';

    easing: 'ease-out',    document.documentElement.dataset.theme = cur;

    once: true,    localStorage.setItem('theme', cur);

    offset: 100  });

});}



// Navigation// Mobile nav

const navbar = document.getElementById('navbar');const navToggle = document.querySelector('.nav-toggle');

const navToggle = document.getElementById('navToggle');const navList = document.querySelector('.nav-list');

const navMenu = document.getElementById('navMenu');if (navToggle && navList) {

const navLinks = document.querySelectorAll('.nav-link');  navToggle.addEventListener('click', () => {

    const open = navList.classList.toggle('open');

// Mobile menu toggle    navToggle.setAttribute('aria-expanded', String(open));

navToggle.addEventListener('click', () => {  });

    navToggle.classList.toggle('active');  navList.addEventListener('click', (e) => {

    navMenu.classList.toggle('active');    if (e.target.closest('a')) navList.classList.remove('open');

});  });

}

// Close mobile menu when clicking on a link

navLinks.forEach(link => {// Scroll spy

    link.addEventListener('click', () => {const sections = [...document.querySelectorAll('main .section[id]')];

        navToggle.classList.remove('active');const links = [...document.querySelectorAll('.nav-list a[href^="#"]')];

        navMenu.classList.remove('active');const spy = new IntersectionObserver((entries) => {

    });  entries.forEach((entry) => {

});    const id = entry.target.getAttribute('id');

    const link = links.find((a) => a.getAttribute('href') === `#${id}`);

// Navbar scroll effect    if (!link) return;

let lastScroll = 0;    if (entry.isIntersecting) {

window.addEventListener('scroll', () => {      links.forEach((a) => a.classList.remove('active'));

    const currentScroll = window.pageYOffset;      link.classList.add('active');

    }

    if (currentScroll <= 0) {  });

        navbar.classList.remove('scroll-up');}, { rootMargin: '-50% 0px -45% 0px', threshold: [0, 0.2, 0.6, 1] });

    }sections.forEach((sec) => spy.observe(sec));



    if (currentScroll > lastScroll && currentScroll > 80) {// Reveal animations

        // Scrolling downconst reveals = document.querySelectorAll('.section .container > *');

        navbar.style.transform = 'translateY(-100%)';const revObs = new IntersectionObserver((entries) => {

    } else {  entries.forEach((entry) => {

        // Scrolling up    if (entry.isIntersecting) {

        navbar.style.transform = 'translateY(0)';      entry.target.classList.add('in');

    }      revObs.unobserve(entry.target);

    }

    lastScroll = currentScroll;  });

});});

reveals.forEach((el) => {

// Smooth scrolling for anchor links  el.classList.add('reveal');

document.querySelectorAll('a[href^="#"]').forEach(anchor => {  revObs.observe(el);

    anchor.addEventListener('click', function (e) {});

        const href = this.getAttribute('href');

        if (href !== '#' && href.length > 1) {// Year footer

            e.preventDefault();const yearEl = document.getElementById('year');

            const target = document.querySelector(href);if (yearEl) yearEl.textContent = String(new Date().getFullYear());

            if (target) {

                const offsetTop = target.offsetTop - 80;// Content loader (optional) — load site/content.json and render

                window.scrollTo({async function loadContent() {

                    top: offsetTop,  try {

                    behavior: 'smooth'    const res = await fetch('content.json', { cache: 'no-store' });

                });    if (!res.ok) return; // if missing, skip

            }    const c = await res.json();

        }

    });    // Hero

});    if (c.hero) {

      const nameEl = document.querySelector('#home .mega');

// Back to top button      const brandEl = document.querySelector('.brand .brand-name');

const backToTop = document.getElementById('backToTop');      const leadEl = document.querySelector('#home .lead');

      const metaItems = document.querySelectorAll('#home .meta li span');

window.addEventListener('scroll', () => {      if (nameEl && c.hero.name) nameEl.textContent = c.hero.name;

    if (window.pageYOffset > 300) {      if (brandEl && c.hero.name) brandEl.textContent = c.hero.name;

        backToTop.classList.add('visible');      if (leadEl && c.hero.tagline) leadEl.textContent = c.hero.tagline;

    } else {      if (metaItems[0] && 'location' in c.hero) metaItems[0].textContent = c.hero.location || '—';

        backToTop.classList.remove('visible');      if (metaItems[1] && 'currently' in c.hero) metaItems[1].textContent = c.hero.currently || '—';

    }    }

});

    // About

backToTop.addEventListener('click', () => {    if (c.about) {

    window.scrollTo({      const bioEl = document.querySelector('#about p.muted');

        top: 0,      if (bioEl && c.about.bio) bioEl.textContent = c.about.bio;

        behavior: 'smooth'      const aboutLists = document.querySelectorAll('#about .about-card ul');

    });      if (aboutLists[0] && Array.isArray(c.about.expertise)) {

});        aboutLists[0].innerHTML = c.about.expertise.map((x) => `<li>${escapeHtml(x)}</li>`).join('');

      }

// Add animation to cards on hover      if (aboutLists[1] && Array.isArray(c.about.highlights)) {

const cards = document.querySelectorAll('.quick-link-card');        aboutLists[1].innerHTML = c.about.highlights.map((x) => `<li>${escapeHtml(x)}</li>`).join('');

cards.forEach(card => {      }

    card.addEventListener('mouseenter', function() {    }

        this.style.transform = 'translateY(-8px) scale(1.02)';

    });    // Experience

    if (Array.isArray(c.experience)) {

    card.addEventListener('mouseleave', function() {      const timeline = document.querySelector('#experience .timeline');

        this.style.transform = 'translateY(0) scale(1)';      if (timeline) {

    });        timeline.innerHTML = c.experience.map(exp => `

});          <article class="item">

            <div class="item-head">

// Parallax effect for hero background              <h3>${escapeHtml(exp.role || '')} @ ${escapeHtml(exp.org || '')}</h3>

window.addEventListener('scroll', () => {              <span class="muted">${escapeHtml((exp.start || ''))} — ${escapeHtml((exp.end || ''))}</span>

    const scrolled = window.pageYOffset;            </div>

    const heroBackground = document.querySelector('.hero-background');            ${exp.summary ? `<p class="muted">${escapeHtml(exp.summary)}</p>` : ''}

    if (heroBackground && scrolled < window.innerHeight) {            ${Array.isArray(exp.bullets) && exp.bullets.length ? `<ul>${exp.bullets.map(b => `<li>${escapeHtml(b)}</li>`).join('')}</ul>` : ''}

        heroBackground.style.transform = `translateY(${scrolled * 0.5}px)`;          </article>

    }        `).join('');

});      }

    }

// Active nav link on scroll

window.addEventListener('scroll', () => {    // Skills

    const sections = document.querySelectorAll('section[id]');    if (Array.isArray(c.skills)) {

    const scrollY = window.pageYOffset;      const wrap = document.querySelector('#skills .skills-chips');

      if (wrap) wrap.innerHTML = c.skills.map(s => `<span class="chip">${escapeHtml(s)}</span>`).join('');

    sections.forEach(section => {    }

        const sectionHeight = section.offsetHeight;

        const sectionTop = section.offsetTop - 100;    // Projects

        const sectionId = section.getAttribute('id');    if (Array.isArray(c.projects)) {

        const navLink = document.querySelector(`.nav-link[href="#${sectionId}"]`);      const cards = document.querySelector('#projects .cards');

      if (cards) {

        if (navLink && scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {        cards.innerHTML = c.projects.map(p => `

            document.querySelectorAll('.nav-link').forEach(link => {          <article class="card project">

                link.classList.remove('active');            <div class="card-head">

            });              <h3>${escapeHtml(p.name || '')}</h3>

            navLink.classList.add('active');              <div class="tags">${(p.tags||[]).map(t => `<span class="chip">${escapeHtml(t)}</span>`).join('')}</div>

        }            </div>

    });            ${p.desc ? `<p class="muted">${escapeHtml(p.desc)}</p>` : ''}

});            <div class="card-actions">

              ${p.demo ? `<a class="btn small" href="${attr(p.demo)}" target="_blank" rel="noopener">Demo</a>` : ''}

// Add active class styling              ${p.code ? `<a class="btn small" href="${attr(p.code)}" target="_blank" rel="noopener">Code</a>` : ''}

const style = document.createElement('style');            </div>

style.textContent = `          </article>

    .nav-link.active {        `).join('');

        color: var(--primary);      }

        background: var(--bg-secondary);    }

    }

`;    // Gallery

document.head.appendChild(style);    if (Array.isArray(c.gallery)) {

      const grid = document.querySelector('#gallery .gallery-grid');

// Prevent dropdown from closing when clicking inside      if (grid) {

document.querySelectorAll('.dropdown-menu').forEach(menu => {        grid.innerHTML = c.gallery.map(g => `

    menu.addEventListener('click', (e) => {          <figure class="tile">

        e.stopPropagation();            <img src="${attr(g.src)}" alt="${attr(g.alt||'Gallery image')}" loading="lazy"/>

    });            ${g.caption ? `<figcaption class="muted" style="padding:8px 10px">${escapeHtml(g.caption)}</figcaption>` : ''}

});          </figure>

        `).join('');

// Close dropdown when clicking outside        initLightbox(grid);

document.addEventListener('click', (e) => {      }

    if (!e.target.closest('.dropdown')) {    }

        document.querySelectorAll('.dropdown-menu').forEach(menu => {

            menu.style.opacity = '0';    // Publications

            menu.style.visibility = 'hidden';    if (Array.isArray(c.publications)) {

        });      const list = document.querySelector('#publications .pub-list');

    }      if (list) {

});        list.innerHTML = c.publications.map(pub => `

          <li>

// Preloader (optional)            <span class="pub-title">${escapeHtml(pub.title || '')}</span>

window.addEventListener('load', () => {            <span class="pub-meta muted">${escapeHtml(pub.venue || '')}${pub.year ? `, ${escapeHtml(pub.year)}` : ''}</span>

    document.body.classList.add('loaded');            ${pub.pdf ? `<a class="link" href="${attr(pub.pdf)}" target="_blank" rel="noopener">PDF</a>` : ''}

});          </li>

        `).join('');

// Console message      }

console.log('%c Saeed Ahmad Portfolio ', 'background: #1a365d; color: #d4af37; font-size: 20px; padding: 10px;');    }

console.log('%c Built with modern web technologies ', 'color: #4a5568; font-size: 14px;');

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
