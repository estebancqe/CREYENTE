import reflex as rx
class SwiperState1(rx.State):
    current_slide: int = 1
    total_slides: int = 5

    @rx.event
    def init_swiper (self):
        return rx.call_script(
            """
            new Swiper('.swiper-container', {
                slidesPerView: 1,
                spaceBetween: 20,
                loop: true,
                pagination: {
                    el: '.swiper-pagination',
                    clickable: true
                },
                navigation: {
                    nextEl: '.swiper-button-next',
                    prevEl: '.swiper-button-prev'
                },
                on: {
                    slideChange: function () {
                        document.querySelector('.mobile-indicator').textContent = 
                        `${this.realIndex + 1}/${this.slides.length}`;
                    }
                },
                breakpoints: {
                    640: {
                        slidesPerView: 2
                    },
                    1024: {
                        slidesPerView: 2
                    }
                }
            });
            """
        )