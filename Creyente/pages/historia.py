import reflex as rx
import Creyente.utils as utils
import Creyente.estilo.estilo as styles
from Creyente.components.navbar import navbar
from Creyente.components.footer import footer
from Creyente.views.header import header
from Creyente.views.index_links import index_links
from Creyente.views.sponsors import sponsors
from Creyente.estilo.estilo import Size, Spacing
from Creyente.routes import Route

@rx.page(
    route=Route.HISTORIA.value,
    title=utils.courses_title,
    description=utils.courses_description,
    image=utils.preview,
    meta=utils.courses_meta
)

def historia() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                # header(),
                rx.text("HISTORIA", size=Spacing.VERY_BIG.value,color="silver"),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )