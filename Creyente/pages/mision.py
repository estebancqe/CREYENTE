# mision.py
import reflex as rx
from typing import Dict, Any
from Creyente.components.carrusel_tailwaind import carrusel_tailwind
from Creyente.components.navbar import navbar
from Creyente.components.footer import footer
from Creyente.views.sponsors import sponsors
from Creyente.swiper.carousel_container import carousel_container
from Creyente.style.style import Size, Spacing
from Creyente.routes import Route
import Creyente.utils as utils

# Estado para inicializar el Swiper
class SwiperState(rx.State):
    @rx.event
    def init_swiper(self):
        return rx.call_script(
            """
            const swiper = new Swiper('.swiper-container', {
                slidesPerView: 2,  // Muestra 2 slides en desktop
                spaceBetween: 30,
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
                        spaceBetween: 20,
                    },
                    768: {
                        slidesPerView: 2,  // 2 slides en tablet
                        spaceBetween: 30,
                    },
                    1024: {
                        slidesPerView: 2,  // 2 slides en desktop
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

# Página de Misión
@rx.page(
    route=Route.MISION.value,
    title=utils.courses_title,
    description=utils.courses_description,
    image=utils.preview,
    meta=utils.courses_meta
)
def mision() -> rx.Component: 
    return rx.box(
        rx.script(
            src="https://unpkg.com/swiper/swiper-bundle.min.css",
            type="text/css"
        ),
        rx.script(
            src="https://unpkg.com/swiper/swiper-bundle.min.js",
            on_ready=SwiperState.init_swiper,  # Asegúrate de definir SwiperState si es necesario
        ),
        utils.lang(),
        navbar(),
        rx.center(
            rx.container(
                rx.vstack(
                    rx.heading("MISION", size=Spacing.VERY_BIG.value, color="silver"),
                    carrusel_tailwind(),
                    sponsors(),
                    spacing=Spacing.BIG.value,
                    width="100%",
                    align="center"
                ),
                max_width="1200px", 
                width="100%",
                padding_x="4"
            )
        ),
        footer()
    )