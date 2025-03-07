# mision.py
import reflex as rx
import Creyente.utils as utils
import Creyente.style.style as styles
from Creyente.components.navbar import navbar
from Creyente.components.footer import footer
from Creyente.views.header import header
from Creyente.components.componente_web import review_carousel
from Creyente.components.carrusel_copia import carrusel
from Creyente.components.swiper_carrusel import swiper_carrusel
from Creyente.views.sponsors import sponsors
from Creyente.style.style import Size, Spacing
from Creyente.routes import Route
from Creyente.components.swipeable import swipeable_component

@rx.page(
    route=Route.MISION.value,
    title=utils.courses_title,
    description=utils.courses_description,
    image=utils.preview,
    meta=utils.courses_meta
)
def mision() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.text("MISION", size=Spacing.VERY_BIG.value, color="silver"),
                rx.container(
                    # swiper_carrusel(),
                    carrusel(),
                    max_width="1200px",
                    center_content=True,
                    padding_x="4"
                ),
                review_carousel(),
                sponsors(),
                spacing=Spacing.BIG.value,
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
                align="center",
            )
        ),
        # rx.box(
        #     swipeable_component(),
        #     width="100%",
        #     padding="2em"
        # ),
        footer()
    )