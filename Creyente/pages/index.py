#index.py
import reflex as rx
import Creyente.utils as utils
import Creyente.style.style as styles
from Creyente.components.navbar import navbar
from Creyente.components.footer import footer
from Creyente.views.header import header
from Creyente.views.index_links import index_links
from Creyente.style.style import Size
from Creyente.swiper.swiper_state import SwiperState  # Importa el estado SwiperState
@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta, 
)
def index() -> rx.Component:
    return rx.box(
        # Solo un script CSS
        rx.script(
            src="https://unpkg.com/swiper/swiper-bundle.min.css",
            type="text/css"
        ),
        # Solo un script JS que inicializa ambos swipers
        rx.script(
            src="https://unpkg.com/swiper/swiper-bundle.min.js",
            on_ready=SwiperState.init_swiper,  # Solo usaremos un estado
        ),
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                rx.box(
                    index_links(),
                    padding=Size.BIG.value
                ),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
            )
        ),
        footer(),
        width="100%",
    )