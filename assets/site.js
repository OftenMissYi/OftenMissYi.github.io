const menu = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navigation');
if (menu && navigation) {
  const closeMenu = () => { navigation.classList.remove('open'); menu.setAttribute('aria-expanded', 'false'); };
  menu.addEventListener('click', () => {
    const expanded = navigation.classList.toggle('open');
    menu.setAttribute('aria-expanded', String(expanded));
  });
  navigation.addEventListener('click', (event) => { if (event.target.closest('a')) closeMenu(); });
  document.addEventListener('keydown', (event) => { if (event.key === 'Escape' && navigation.classList.contains('open')) { closeMenu(); menu.focus(); } });
}
const sections = document.querySelectorAll('.case-section');
if ('IntersectionObserver' in window && sections.length) {
  const observer = new IntersectionObserver((entries) => {
    for (const entry of entries) if (entry.isIntersecting) {
      document.querySelectorAll('.case-nav a').forEach((link) => {
        const active = link.hash === `#${entry.target.id}`;
        link.classList.toggle('active', active);
        if (active) link.setAttribute('aria-current', 'location'); else link.removeAttribute('aria-current');
      });
    }
  }, { rootMargin: '-10% 0px -65% 0px', threshold: 0 });
  sections.forEach((section) => observer.observe(section));
}

// Progressive enhancement: all project content is visible without JavaScript.
const projects = document.querySelector('.projects-grid');
if (projects) {
  const cards = [...projects.querySelectorAll('.project-card')];
  const activate = (selected) => {
    cards.forEach((card) => {
      const active = card === selected;
      card.classList.toggle('is-active', active);
      card.querySelector('.project-toggle').setAttribute('aria-expanded', String(active));
      card.querySelector('.project-toggle').setAttribute('aria-disabled', String(active));
      card.querySelector('.expand-mark').textContent = active ? '−' : '+';
      card.querySelector('.project-detail').hidden = !active;
    });
  };
  projects.classList.add('interactive');
  activate(cards[0]);
  cards.forEach((card, index) => {
    const toggle = card.querySelector('.project-toggle');
    toggle.addEventListener('click', () => activate(card));
    card.addEventListener('pointerenter', (event) => {
      if (event.pointerType === 'mouse' && !projects.querySelector('.project-detail:focus-within')) activate(card);
    });
    toggle.addEventListener('focus', () => activate(card));
    toggle.addEventListener('keydown', (event) => {
      if (!['ArrowRight', 'ArrowLeft', 'Home', 'End'].includes(event.key)) return;
      event.preventDefault();
      const next = event.key === 'Home' ? 0 : event.key === 'End' ? cards.length - 1 : (index + (event.key === 'ArrowRight' ? 1 : -1) + cards.length) % cards.length;
      cards[next].querySelector('.project-toggle').focus();
    });
  });
}

// A small, pointer-driven perspective response; no autoplay or scroll hijacking.
const art = document.querySelector('.hero-art');
const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
if (art) {
  art.addEventListener('pointermove', (event) => {
    if (motion.matches || event.pointerType !== 'mouse') return;
    const rect = art.getBoundingClientRect();
    const x = (event.clientX - rect.left) / rect.width - 0.5;
    const y = (event.clientY - rect.top) / rect.height - 0.5;
    art.style.setProperty('--tilt-x', `${-y * 7}deg`);
    art.style.setProperty('--tilt-y', `${x * 9}deg`);
  });
  const resetArt = () => { art.style.setProperty('--tilt-x', '0deg'); art.style.setProperty('--tilt-y', '0deg'); };
  art.addEventListener('pointerleave', resetArt);
  motion.addEventListener('change', resetArt);
}
