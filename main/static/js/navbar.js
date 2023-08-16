const categories = document.querySelectorAll('#category');
const info = document.querySelector('.InfoContainer');
const all = document.getElementById('all');
let canLeave = false;
let isShown = false;
categories.forEach((category) => {
    category.onclick = () => {
        if (window.innerWidth >= 550) {
            info.style.display = 'block';
            isShown = true;
        }
    };

    all.onmouseleave = () => {
        if (isShown) {
            canLeave = true;
        }
    };
});

window.onclick = () => {
    if (canLeave) {
        info.style.display = 'none';
        canLeave = false;
        isShown = false;
    }
};