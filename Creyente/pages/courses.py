import reflex as rx
import Creyente.utils as utils
import Creyente.estilo.estilo as styles
from Creyente.routes import Route
from Creyente.components.navbar import navbar
from Creyente.components.footer import footer
from Creyente.views.courses_links import courses_links
from Creyente.estilo.estilo import Size


@rx.page(
    route=Route.COURSES.value,
    title=utils.courses_title,
    description=utils.courses_description,
    image=utils.preview,
    meta=utils.courses_meta
)
def courses() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                courses_links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.ZERO.value,
                padding=Size.DEFAULT.value
            )
        ),
        footer()
    )

