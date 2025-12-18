// Mobile hamburger menu toggle
document.addEventListener('DOMContentLoaded', function () {
    const toggle = document.querySelector('.menu-toggle');
    if (!toggle) return;

    // Build mobile nav from existing desktop nav links
    const desktopNav = document.querySelector('.nav');
    const mobileNav = document.createElement('div');
    mobileNav.id = 'mobile-nav';
    mobileNav.className = 'mobile-nav';
    mobileNav.setAttribute('aria-hidden', 'true');

    // Clone nav links into mobile nav
    const cloned = desktopNav.cloneNode(true);
    cloned.classList.add('mobile-nav-links');
    mobileNav.appendChild(cloned);

    document.body.appendChild(mobileNav);

    function openMenu() {
        toggle.setAttribute('aria-expanded', 'true');
        mobileNav.classList.add('mobile-nav--open');
        mobileNav.setAttribute('aria-hidden', 'false');
        document.body.classList.add('no-scroll');
    }

    function closeMenu() {
        toggle.setAttribute('aria-expanded', 'false');
        mobileNav.classList.remove('mobile-nav--open');
        mobileNav.setAttribute('aria-hidden', 'true');
        document.body.classList.remove('no-scroll');
    }

    toggle.addEventListener('click', function (e) {
        const expanded = toggle.getAttribute('aria-expanded') === 'true';
        if (expanded) closeMenu(); else openMenu();
    });

    // close when clicking outside
    mobileNav.addEventListener('click', function (e) {
        if (e.target === mobileNav) closeMenu();
    });

    // close on escape
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') closeMenu();
    });
});
