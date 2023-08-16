const chars = document.querySelectorAll('.Char');

chars.forEach((char) => {
    let canReturn = true;

    char.onmouseenter = () => {
        if (!canReturn) return;

        char.style.color = 'transparent';
        char.style.webkitTextStroke = '1.6px var(--white)';
    };

    char.onclick = () => {
        if (canReturn) {
            canReturn = false;
        } else {
            char.style.color = 'transparent';
            char.style.webkitTextStroke = '1.6px var(--white)';
            canReturn = true;
        }
    }

    char.onmouseleave = () => {
        if (!canReturn) return;

        char.style.color = 'var(--white)';
        char.style.webkitTextStroke = '1.6px transparent';
    };
});