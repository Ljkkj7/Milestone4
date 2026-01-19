// Responsive carousel functionality supporting multiple independent carousels
class Carousel {
    constructor(container) {
        this.container = container;
        this.carousel = container.querySelector('.listings-carousel');
        this.items = this.carousel ? Array.from(this.carousel.querySelectorAll('.carousel-item')) : [];
        this.dotsContainer = container.nextElementSibling && container.nextElementSibling.classList.contains('carousel-indicators') ? container.nextElementSibling : container.querySelector('.carousel-indicators');
        this.index = 0;

        this.init();
        this.onResize = this.onResize.bind(this);
        window.addEventListener('resize', this.debounce(this.onResize, 120));
    }

    getItemsPerSlide() {
        if (window.innerWidth < 1024) return 1;
        return 2;
    }

    init() {
        if (!this.carousel) return;
        this.carousel.style.transition = 'transform 0.45s ease';
        this.rebuildDots();
        this.show();
        this.attachButtons();
    }

    attachButtons() {
        const prev = this.container.querySelector('.carousel-prev');
        const next = this.container.querySelector('.carousel-next');
        if (prev) {
            prev.addEventListener('click', () => this.prev());
        }
        if (next) {
            next.addEventListener('click', () => this.next());
        } 
    }

    rebuildDots() {
        if (!this.dotsContainer) return;
        this.dotsContainer.innerHTML = '';
        const itemsPerSlide = this.getItemsPerSlide();
        const totalSlides = Math.max(1, Math.ceil(this.items.length / itemsPerSlide));
        for (let i = 0; i < totalSlides; i++) {
            const dot = document.createElement('button');
            dot.className = `carousel-dot ${i === 0 ? 'active' : ''}`;
            dot.setAttribute('aria-label', `Go to slide ${i + 1}`);
            dot.addEventListener('click', () => { this.goTo(i); });
            this.dotsContainer.appendChild(dot);
        }
        this.updateDots();
    }

    updateDots() {
        if (!this.dotsContainer) return;
        const dots = Array.from(this.dotsContainer.querySelectorAll('.carousel-dot'));
        dots.forEach((dot, idx) => dot.classList.toggle('active', idx === this.index));
    }

    show() {
        if (!this.carousel) return;
        const itemsPerSlide = this.getItemsPerSlide();
        const totalSlides = Math.max(1, Math.ceil(this.items.length / itemsPerSlide));
        if (this.index >= totalSlides) this.index = 0;
        if (this.index < 0) this.index = totalSlides - 1;

        // Calculate translate percentage based on slides (each slide = 100%)
        const offset = -this.index * 100;
        this.carousel.style.transform = `translateX(${offset}%)`;
        this.updateDots();
    }

    next() { this.index += 1; this.show(); }
    prev() { this.index -= 1; this.show(); }
    goTo(n) { this.index = n; this.show(); }

    onResize() {
        // rebuild items in case DOM changed
        this.items = this.carousel ? Array.from(this.carousel.querySelectorAll('.carousel-item')) : [];
        this.rebuildDots();
        this.show();
    }

    // Simple debounce utility
    debounce(fn, delay) {
        let t;
        return function(...args) { clearTimeout(t); t = setTimeout(() => fn.apply(this, args), delay); };
    }
}

// Keep a registry of carousels
const CAROUSELS = [];

document.addEventListener('DOMContentLoaded', () => {
    const containers = document.querySelectorAll('.listings-carousel-container');
    containers.forEach(container => {
        CAROUSELS.push(new Carousel(container));
    });
});

// Fallback: delegate clicks on carousel-prev/next to the matching carousel instance
document.addEventListener('click', function(e) {
    const prev = e.target.closest('.carousel-prev');
    const next = e.target.closest('.carousel-next');
    if (prev) {
        const container = prev.closest('.listings-carousel-container');
        const instance = CAROUSELS.find(c => c.container === container);
        if (instance) instance.prev();
    } else if (next) {
        const container = next.closest('.listings-carousel-container');
        const instance = CAROUSELS.find(c => c.container === container);
        if (instance) instance.next();
    }
});

// Backwards-compatible global functions that accept the clicked button element
function carouselNext(button) {
    // if called without args, move first carousel
    if (!button) return CAROUSELS[0] && CAROUSELS[0].next();
    const container = button.closest('.listings-carousel-container');
    const instance = CAROUSELS.find(c => c.container === container);
    if (instance) instance.next();
}

function carouselPrev(button) {
    if (!button) return CAROUSELS[0] && CAROUSELS[0].prev();
    const container = button.closest('.listings-carousel-container');
    const instance = CAROUSELS.find(c => c.container === container);
    if (instance) instance.prev();
}



