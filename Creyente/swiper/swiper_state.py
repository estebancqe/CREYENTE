import reflex as rx

class SwiperState(rx.State):
    @rx.event
    def init_swiper(self):
        return [
            rx.call_script("""
                // Configuración común para ambos swipers
                const swiperConfig = {
                    slidesPerView: 2, // Cambiado a 2 para móvil
                    spaceBetween: 10,
                    loop: true,
                    autoplay: {
                        delay: 3000,
                        disableOnInteraction: true,
                    },
                    pagination: {
                        clickable: true,
                    },
                    navigation: {
                        nextEl: '',
                        prevEl: '',
                    },
                    breakpoints: {
                        640: {
                            slidesPerView: 1,
                            spaceBetween: 10,
                        },
                        768: {
                            slidesPerView: 3,
                            spaceBetween: 20,
                        },
                        1024: {
                            slidesPerView: 4,
                            spaceBetween: 30,
                        },
                    }
                };

                // Primer swiper
                const swiper1 = new Swiper('.swiper-container-1', { 
                    ...swiperConfig,
                    pagination: {
                        el: '.swiper-pagination-1',
                        clickable: true,
                    },
                    navigation: {
                        nextEl: '.swiper-button-next-1',
                        prevEl: '.swiper-button-prev-1',
                    },
                    on: {
                        slideChange: function () {
                            const indicator = document.querySelector('.mobile-indicator-1');
                            if (indicator) {
                                indicator.textContent = `${this.realIndex + 1}/${this.slides.length}`;
                            }
                        }
                    }
                });

                // Segundo swiper con la misma configuración
                const swiper2 = new Swiper('.swiper-container-2', {
                    ...swiperConfig,
                    pagination: {
                        el: '.swiper-pagination-2',
                        clickable: true,
                    },
                    navigation: {
                        nextEl: '.swiper-button-next-2',
                        prevEl: '.swiper-button-prev-2',
                    },
                    on: {
                        slideChange: function () {
                            const indicator = document.querySelector('.mobile-indicator-2');
                            if (indicator) {
                                indicator.textContent = `${this.realIndex + 1}/${this.slides.length}`;
                            }
                        }
                    }
                });

                // Eventos comunes para ambos swipers
                [swiper1, swiper2].forEach(swiper => {
                    swiper.on('touchStart', () => swiper.autoplay.stop());
                    swiper.on('slideChange', () => swiper.autoplay.stop());
                });
            """)
        ]