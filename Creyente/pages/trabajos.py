import reflex as rx
import Creyente.utils as utils
import Creyente.style.style as styles
from Creyente.components.navbar import navbar
from Creyente.components.footer import footer
from Creyente.views.carrusel_imagenes import ejemplo_carrusel
from Creyente.style.style import Size, Spacing
from Creyente.routes import Route

@rx.page(
    route=Route.TRABAJOS.value,
    title=utils.trabajo_title,
    description=utils.trabajo_description,
    image=utils.preview,
    meta=utils.trabajo_meta
)

def trabajos() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                # header(),
                rx.text("Proyectos", size=Spacing.VERY_BIG.value,color="silver"),
                ejemplo_carrusel(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )