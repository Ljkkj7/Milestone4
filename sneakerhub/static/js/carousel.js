// Carousel functionality for profile listings - 2 items per slide
let carouselIndex = 0;
const itemsPerSlide = 2;

function carouselNext() {
    showCarousel(carouselIndex += 1);
}

function carouselPrev() {
    showCarousel(carouselIndex -= 1);
}

function currentSlide(n) {
    showCarousel(carouselIndex = n);
}

function showCarousel(n) {
    const items = document.querySelectorAll('.carousel-item');
    const totalSlides = Math.ceil(items.length / itemsPerSlide);
    
    // Wrap around
    if (n >= totalSlides) {
        carouselIndex = 0;
    }
    if (n < 0) {
        carouselIndex = totalSlides - 1;
    }
    
    // Calculate translation
    const offset = -carouselIndex * 100;
    const carousel = document.querySelector('.listings-carousel');
    if (carousel) {
        carousel.style.transform = `translateX(${offset}%)`;
    }
    
    // Update active dot
    const dots = document.querySelectorAll('.carousel-dot');
    dots.forEach((dot, index) => {
        dot.classList.remove('active');
        if (index === carouselIndex) {
            dot.classList.add('active');
        }
    });
}

// Initialize carousel
document.addEventListener('DOMContentLoaded', function() {
    const items = document.querySelectorAll('.carousel-item');
    const dotsContainer = document.querySelector('.carousel-indicators');
    
    if (items.length > 0 && dotsContainer) {
        const totalSlides = Math.ceil(items.length / itemsPerSlide);
        
        // Clear existing dots and create new ones
        dotsContainer.innerHTML = '';
        
        for (let i = 0; i < totalSlides; i++) {
            const dot = document.createElement('span');
            dot.className = `carousel-dot ${i === 0 ? 'active' : ''}`;
            dot.onclick = () => currentSlide(i);
            dotsContainer.appendChild(dot);
        }
        
        showCarousel(carouselIndex);
    }
});


