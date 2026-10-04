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


// Move one underline between hover, keyboard focus and the section in view.
if (navigation) {
  const links = [...navigation.querySelectorAll('a')];
  const localSections = links.map(link => document.getElementById(link.hash.slice(1)));
  const onHome = localSections.some(Boolean);
  let current = onHome ? null : links[0];
  let hovered = null;
  const drawMarker = () => {
    const focused = links.includes(document.activeElement) ? document.activeElement : null;
    const target = hovered || focused || current;
    navigation.style.setProperty('--marker-opacity', target ? '1' : '0');
    if (target) {
      const navRect = navigation.getBoundingClientRect();
      const rect = target.getBoundingClientRect();
      navigation.style.setProperty('--marker-left', `${rect.left - navRect.left}px`);
      navigation.style.setProperty('--marker-width', `${rect.width}px`);
    }
  };
  const updateCurrent = () => {
    if (onHome) {
      current = null;
      localSections.forEach((section, index) => {
        if (section && section.getBoundingClientRect().top <= 155) current = links[index];
      });
      if (window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 5) current = links.at(-1);
    }
    links.forEach(link => {
      if (link === current) link.setAttribute('aria-current', onHome ? 'location' : 'page');
      else link.removeAttribute('aria-current');
    });
    drawMarker();
  };
  links.forEach(link => {
    link.addEventListener('pointerenter', event => { if (event.pointerType === 'mouse') { hovered = link; drawMarker(); } });
    link.addEventListener('focus', drawMarker);
  });
  navigation.addEventListener('pointerleave', () => { hovered = null; drawMarker(); });
  navigation.addEventListener('focusout', () => requestAnimationFrame(drawMarker));
  let scheduled = false;
  window.addEventListener('scroll', () => {
    if (scheduled) return;
    scheduled = true;
    requestAnimationFrame(() => { scheduled = false; updateCurrent(); });
  }, { passive: true });
  window.addEventListener('resize', drawMarker);
  document.fonts.ready.then(drawMarker);
  navigation.classList.add('marker-ready');
  updateCurrent();
}

const workMap = document.querySelector('.work-map');
if (workMap) {
  const nodes = [...workMap.querySelectorAll('.map-node')];
  const selectNode = (node) => {
    nodes.forEach(item => item.setAttribute('aria-pressed', String(item === node)));
    workMap.querySelector('.map-keywords').textContent = node.dataset.keywords;
    workMap.querySelector('.map-details h3').textContent = node.dataset.title;
    workMap.querySelector('.map-description').textContent = node.dataset.description;
    const link = workMap.querySelector('.map-link');
    link.href = node.dataset.href;
    link.setAttribute('aria-label', `Read case study: ${node.dataset.title}`);
  };
  nodes.forEach((node, index) => {
    node.addEventListener('pointerenter', event => { if (event.pointerType === 'mouse') selectNode(node); });
    node.addEventListener('focus', () => selectNode(node));
    node.addEventListener('click', () => selectNode(node));
    node.addEventListener('keydown', event => {
      if (!['ArrowRight', 'ArrowLeft', 'ArrowDown', 'ArrowUp'].includes(event.key)) return;
      event.preventDefault();
      const direction = ['ArrowRight', 'ArrowDown'].includes(event.key) ? 1 : -1;
      nodes[(index + direction + nodes.length) % nodes.length].focus();
    });
  });
}
