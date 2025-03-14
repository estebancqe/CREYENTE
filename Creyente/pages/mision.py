# mision.py
import reflex as rx
from typing import Dict, Any
from Creyente.components.navbar import navbar
from Creyente.components.footer import footer
from Creyente.views.sponsors import sponsors
from Creyente.style.style import Size, Spacing
from Creyente.routes import Route
import Creyente.utils as utils 
from Creyente.prueba_componentes.muestra_mueble.mueble_explicacion import mueble_explicacion

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
        utils.lang(),
        navbar(),
        rx.center(
            rx.container(
                rx.vstack(
                    rx.heading("MISION", size=Spacing.VERY_BIG.value, color="silver"),
                    mueble_explicacion(),
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