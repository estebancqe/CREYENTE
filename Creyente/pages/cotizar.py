import reflex as rx
import Creyente.utils as utils
import Creyente.estilo.estilo as styles
from Creyente.routes import Route
from Creyente.components.navbar import navbar
from Creyente.components.footer import footer
from Creyente.views.header import header
from Creyente.views.cotizar_links import cotizar_links
from Creyente.views.sponsors import sponsors
from Creyente.estilo.estilo import Size
from Creyente.state.PageState import PageState


@rx.page(
    route=Route.COTIZAR.value,
    title=utils.courses_title,
    description=utils.courses_description,
    image=utils.preview,
    meta=utils.courses_meta,
    on_load=[PageState.muebles_links,PageState.modelo_links]
)
def cotizar() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(False),
                cotizar_links(
                    PageState.mueble_info,
                    PageState.modelo_info,
                    
                ),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
    footer()
    )