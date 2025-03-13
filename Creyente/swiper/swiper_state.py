#swiper_state.py

import reflex as rx

class SwiperState(rx.State):
    @rx.event
    def init_swiper(self): 
        return rx.call_script(
            """
            const swiper = new Swiper('.swiper-container', { 
                slidesPerView: 1,  // Muestra 1 slide en móvil
                spaceBetween: 10,
                loop: true,
                autoplay: {
                    delay: 3000,
                    disableOnInteraction: true,  // Detiene la animación al interactuar
                },
                pagination: {
                    el: '.swiper-pagination',
                    clickable: true,
                },
                navigation: {
                    nextEl: '.swiper-button-next',
                    prevEl: '.swiper-button-prev',
                },
                breakpoints: {
                    640: {
                        slidesPerView: 1,  // 1 slide en móvil
                        spaceBetween: 10,
                    },
                    768: {
                        slidesPerView: 3,  // 3 slides en tablet
                        spaceBetween: 20,
                    },
                    1024: {
                        slidesPerView: 4,  // 4 slides en desktop
                        spaceBetween: 30,
                    },
                },
                on: {
                    slideChange: function () {
                        const indicator = document.querySelector('.mobile-indicator');
                        if (indicator) {
                            indicator.textContent = `${this.realIndex + 1}/${this.slides.length}`;
                        }
                    }
                }
            });

            // Detener la animación al interactuar manualmente
            swiper.on('touchStart', function () {
                swiper.autoplay.stop();
            });

            swiper.on('slideChange', function () {
                swiper.autoplay.stop();
            });
            """
        )