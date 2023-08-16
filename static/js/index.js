const cards = document.querySelectorAll('.card')
cards.forEach((card) => {
    const image = card.querySelector('img');
    const overlay = card.querySelector('.overlay');
    const text = overlay.querySelector('span');
    card.onmouseenter = () => {
        image.style.transform = 'scale(1.025)'
        text.style.top = '95%';
        overlay.style.opacity = '1';
    };
    card.onmouseleave = () => {
        image.style.transform = 'scale(1)'
        overlay.style.opacity = '0';
        text.style.top = '100%';
    };
});