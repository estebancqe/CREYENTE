#prueba.py
import reflex as rx
import Creyente.utils as utils
import Creyente.style.style as styles
from Creyente.routes import Route
from Creyente.components.navbar import navbar
from Creyente.components.footer import footer
from Creyente.swiper.carousel_container import carousel_container
from Creyente.swiper.swipe_component import swiper_component
from Creyente.swiper.swiper_state import SwiperState
from Creyente.swiper.carousel_state import CarouselState1
from Creyente.style.style import Size


@rx.page(
    route=Route.PRUEBA.value,
    title=utils.courses_title,
    description=utils.courses_description,
    image=utils.preview,
    meta=utils.courses_meta
)


def prueba() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                rx.vstack(
                    rx.heading("Carrusel de Imágenes",color="silver"),
                    carousel_container(),
                    rx.text("GALERÍA"),
                        rx.grid(
                            swiper_component(),
                            width="100%",
                            margin_y="4"
                        ),
                    align="center",
                    width="100%",
                    spacing="4",
                    padding="4",
                ),
                max_width="600px",
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )