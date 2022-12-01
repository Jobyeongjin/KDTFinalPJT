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