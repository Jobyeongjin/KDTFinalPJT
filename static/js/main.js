// Nav-search
const searchEl = document.querySelector('.nav__search');
const searchInputEl = searchEl.querySelector('input');

searchEl.addEventListener('click', function() {
    searchInputEl.focus();
});

searchInputEl.addEventListener('focus', function() {
    searchInputEl.setAttribute('placeholder', '통합검색');
});

searchInputEl.addEventListener('blur', function() {
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
let mainSwiper = new Swiper(".mainSwiper", {
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


// Books-detail-visual-snow
function createSnow() {
    const visual = document.querySelector('.book-visual');
    const el = document.createElement("div");
    el.classList.add("snow");
    el.style.marginLeft = randomPostion() + "px";
    visual.appendChild(el);
}
function randomPostion() {
    return Math.floor(Math.random() * window.innerWidth);
}
for (let i = 0; i < 300; i++) {
    createSnow();
}


// Book-info-toggle
const infoToggleBtn = document.querySelector('.book-info-toggle');
const tableMenu = document.querySelector('.book-info-in-wrap');

infoToggleBtn.addEventListener('click', () => {
    tableMenu.classList.toggle('active');
    infoToggleBtn.classList.toggle('rotate');
});


// Book-info-swiper
let bookReviewSwiper = new Swiper(".bookReviewSwiper", {
    slidesPerView: 1,
    spaceBetween: 10,
    loop: false,
    centerSlide: 'true',
    fade: 'true',
    grabCursor: 'true',
    autoplay:{disableOnInteraction: false},
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    dynamicBullets: true,
    breakpoints: {
        576: {
        slidesPerView: 1,
        spaceBetween: 80,
        },
        768: {
        slidesPerView: 2,
        spaceBetween: 80,
        },
        992: {
        slidesPerView: 3,
        spaceBetween: 80,
        },  
        1200: {
        slidesPerView: 4,
        spaceBetween: 50,
        },  
        1400: {
        slidesPerView: 5,
        spaceBetween: 50,
        },  
    },
});