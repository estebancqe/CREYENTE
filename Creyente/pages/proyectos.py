import reflex as rx
import Creyente.utils as utils
import Creyente.style.style as styles
from Creyente.components.navbar_proyectos import navbar_proyectos
from Creyente.components.footer import footer
from Creyente.components.carrusel_tailwaind import carrusel_tailwind_despliegue
from Creyente.views.carrusel_imagenes import ejemplo_carrusel
from Creyente.style.style import Size, Spacing
from Creyente.routes import Route

@rx.page(
    route=Route.PROYECTOS.value,
    title=utils.proyectos_title,
    description=utils.proyectos_description,
    image=utils.preview,
    meta=utils.proyectos_meta
)

def proyectos() -> rx.Component:
    return rx.box(
        navbar_proyectos(),
        rx.center(
            rx.vstack(
                rx.text("Proyectos", size=Spacing.VERY_BIG.value,color="silver"),
                carrusel_tailwind_despliegue(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )