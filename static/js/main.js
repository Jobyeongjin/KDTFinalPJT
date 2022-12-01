// Nav-search
const searchEl = document.querySelector('.nav__search');
const searchInputEl = searchEl.querySelector('input');

searchEl.addEventListener('click', function() {
    searchInputEl.focus();
});

searchInputEl.addEventListener('focus', function() {
    searchEl.classList.add('focused');
    searchInputEl.setAttribute('placeholder', '통합검색');
});

searchInputEl.addEventListener('blur', function() {
    searchEl.classList.remove('focused');
    searchInputEl.setAttribute('placeholder', '');
});


// Nav-toggle
const toggleBtn = document.querySelector('.nav-toogle-btn');
const menu = document.querySelector('.nav__list');
const userBtn = document.querySelector('.nav__user');

toggleBtn.addEventListener('click', () => {
    menu.classList.toggle('active');
    userBtn.classList.toggle('active');
});

// Main-swiper
let swiper = new Swiper(".mainSwiper", {
    centeredSlides: true,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
    },
    pagination: {
        el: ".swiper-pagination",
        type : 'progressbar',
    },
});