(() => {
  const countryCodeNumber = '233595638696';
  const orderLinks = document.querySelectorAll('[data-order]');

  orderLinks.forEach((link) => {
    const message = link.dataset.order || 'Hello BiteKasa! I would like to place an order.';
    link.href = `https://wa.me/${countryCodeNumber}?text=${encodeURIComponent(message)}`;
  });

  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#primary-nav');
  if (toggle && nav) {
    const closeMenu = () => {
      nav.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    };

    toggle.addEventListener('click', () => {
      const isOpen = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!isOpen));
      nav.classList.toggle('open', !isOpen);
    });

    nav.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', closeMenu);
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') closeMenu();
    });
  }

  const year = document.querySelector('#year');
  if (year) year.textContent = new Date().getFullYear();
})();
