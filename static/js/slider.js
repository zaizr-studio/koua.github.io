let swiper = new Swiper(".ads", {
    loop: true,
    autoplay: {
        delay: 2000,
        disableOnInteraction: false
    },
});

var swiper2 = new Swiper(".cards", {
    spaceBetween: 20,
    pagination: {
        el: ".swiper-pagination",
        type: "progressbar",
    },
    breakpoints: {
        1360: {
            slidesPerView: 4
        },
        1000: {
			slidesPerView: 3
        },
        570: {
            slidesPerView: 2
        }
	}
});