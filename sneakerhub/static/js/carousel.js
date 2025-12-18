// Responsive carousel functionality for profile listings
let carouselIndex = 0;

function getItemsPerSlide() {
    if (window.innerWidth < 900) return 1; // 1 item for mobile and tablet
    return 2; // default for larger screens
}

function carouselNext() {
    showCarousel(carouselIndex += 1);
}

function carouselPrev() {
    showCarousel(carouselIndex -= 1);
}

function currentSlide(n) {
    showCarousel(carouselIndex = n);
}

function rebuildDots(itemsPerSlide) {
    const items = document.querySelectorAll('.carousel-item');
    const dotsContainer = document.querySelector('.carousel-indicators');
    if (!dotsContainer) return;
    dotsContainer.innerHTML = '';
    const totalSlides = Math.max(1, Math.ceil(items.length / itemsPerSlide));
    for (let i = 0; i < totalSlides; i++) {
        const dot = document.createElement('span');
        dot.className = `carousel-dot ${i === 0 ? 'active' : ''}`;
        dot.onclick = () => currentSlide(i);
        dotsContainer.appendChild(dot);
    }
}

function showCarousel(n) {
    const items = document.querySelectorAll('.carousel-item');
    const carousel = document.querySelector('.listings-carousel');
    if (!carousel || items.length === 0) return;

    const itemsPerSlide = getItemsPerSlide();
    const totalSlides = Math.max(1, Math.ceil(items.length / itemsPerSlide));

    // Wrap around
    if (n >= totalSlides) {
        carouselIndex = 0;
    }
    if (n < 0) {
        carouselIndex = totalSlides - 1;
    }

    // Translate by full viewport width per slide-group
    const offset = -carouselIndex * 100;
    carousel.style.transform = `translateX(${offset}%)`;

    // Update active dot
    const dots = document.querySelectorAll('.carousel-dot');
    dots.forEach((dot, index) => {
        dot.classList.toggle('active', index === carouselIndex);
    });
}

// Initialize carousel and keep it responsive on resize
document.addEventListener('DOMContentLoaded', function() {
    const items = document.querySelectorAll('.carousel-item');
    const dotsContainer = document.querySelector('.carousel-indicators');
    if (items.length === 0 || !dotsContainer) return;

    // Create dots and set initial state
    rebuildDots(getItemsPerSlide());
    showCarousel(carouselIndex);

    // Rebuild on resize to adapt to new itemsPerSlide
    let resizeTimer;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(() => {
            rebuildDots(getItemsPerSlide());
            const totalSlides = Math.max(1, Math.ceil(items.length / getItemsPerSlide()));
            if (carouselIndex >= totalSlides) carouselIndex = totalSlides - 1;
            showCarousel(carouselIndex);
        }, 120);
    });
});


