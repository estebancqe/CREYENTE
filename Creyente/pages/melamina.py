import reflex as rx
import Creyente.utils as utils
import Creyente.style.style as styles
from Creyente.routes import Route
from Creyente.components.navbar import navbar
from Creyente.components.footer import footer
from Creyente.views.melamina_links import color_melamina
from Creyente.style.style import Size


@rx.page(
    route=Route.MELAMINA.value,
    title=utils.melamina_title,
    description=utils.melamina_description,
    image=utils.preview,
    meta=utils.melamina_meta
)
def melamina() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                color_melamina(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.ZERO.value,
                padding=Size.DEFAULT.value
            )
        ),
        footer()
    )

