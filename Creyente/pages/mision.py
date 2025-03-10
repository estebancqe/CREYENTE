# mision.py
import reflex as rx
from typing import Dict, Any
from Creyente.components.swiper import swiper_component
from Creyente.components.carrusel_tailwaind import carrusel_tailwind
from Creyente.components.navbar import navbar
from Creyente.components.footer import footer
from Creyente.views.sponsors import sponsors
from Creyente.style.style import Size, Spacing
from Creyente.routes import Route
import Creyente.utils as utils
import Creyente.style.style as styles

# mision.py
class SwiperState(rx.State):
    @rx.event
    def init_swiper(self):
        return rx.call_script(
            """
            new Swiper('.swiper-container', {
                slidesPerView: 1,
                spaceBetween: 30,
                loop: true,
                autoplay: {
                    delay: 3000,
                    disableOnInteraction: false,
                },
                effect: 'fade',
                fadeEffect: {
                    crossFade: true
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
                        slidesPerView: 2,
                        spaceBetween: 20,
                    },
                    768: {
                        slidesPerView: 2,
                        spaceBetween: 30,
                    },
                    1024: {
                        slidesPerView: 2,
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
            """
        ) 

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
            on_ready=SwiperState.init_swiper,
        ),
        navbar(),
        rx.center(
            rx.container(
                rx.vstack(
                    rx.heading("MISION", size=Spacing.VERY_BIG.value, color="silver"),
                    carrusel_tailwind(),
                    # rx.box(
                    #     swiper_component(),
                    #     width="100%",
                    #     margin_y="4"
                    # ),
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