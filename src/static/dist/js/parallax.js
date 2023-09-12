document.addEventListener('DOMContentLoaded', function () {
    const parallaxImage = document.querySelector('.parallax-image');
    
    window.addEventListener('scroll', function () {
        const scrollY = window.scrollY;
        parallaxImage.style.transform = `translateY(${scrollY * 0.5}px)`; // Измените коэффициент, чтобы настроить скорость параллакса
    });
});