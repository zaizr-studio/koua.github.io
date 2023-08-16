const html = document.querySelector('html');
const menuBtn = document.getElementById('menuBtn');
const menu = document.getElementById('menu');
const menuOverlay = document.getElementById('menuOverlay');
const s = document.getElementById('search');
menuBtn.onclick = function() {
    ShowMenu();
    menuOverlay.addEventListener('click', () => {
        HideMenu();
    });
}

function ShowMenu() {
    menuOverlay.style.opacity = '1';
    menuOverlay.style.pointerEvents = 'all';
    menu.style.left = '0';
    html.style.overflow = 'hidden';
}

function HideMenu() {
    menuOverlay.style.opacity = '0';
    menuOverlay.style.pointerEvents = 'none';
    menu.style.left = '-500px';
    html.style.overflow = 'auto';
}

const slideBtn = document.getElementById('slideBtn');
const slide = document.getElementById('slide');
let show = false;
slideBtn.onclick = () => {
    if (show) {
        slide.style.height = '0';
        show = false;
    } else {
        slide.style.height = 'calc('+slide.childElementCount+' * 40px)';
        show = true;
    }
};

const query = (new URL(window.location.href)).searchParams.get('q');
if (query) {
    s.value = query;
}
s.addEventListener('keypress', (e) => {
    if (s.value.length <= 0) return;
    if (e.keyCode === 13) {
        window.open(`${window.location.origin}/search?q=`+s.value);
    }
});