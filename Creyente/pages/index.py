import reflex as rx
import Creyente.utils as utils
import Creyente.estilo.estilo as styles
from Creyente.components.navbar import navbar
from Creyente.components.footer import footer
from Creyente.views.header import header
from Creyente.views.index_links import index_links
from Creyente.views.sponsors import sponsors
from Creyente.estilo.estilo import Size
from Creyente.state.PageState import PageState


@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta,
    
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                rx.box(
                    index_links(),
                    sponsors(),
                    padding=Size.BIG.value
                ),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
            )
        ),
        footer()
    )