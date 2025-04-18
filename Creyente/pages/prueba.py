#prueba.py
import reflex as rx
import Creyente.utils as utils
import Creyente.style.style as styles
from Creyente.routes import Route
from Creyente.components.navbar import navbar
from Creyente.components.footer import footer
from Creyente.prueba_componentes.ejemplo_links import ejemplo_links
from Creyente.swiper.carousel_container import carousel_container
from Creyente.swiper.swipe_component import swiper_component
from Creyente.components.title import title
from Creyente.swiper.swiper_state import SwiperState
from Creyente.style.style import Size 
from Creyente.prueba_componentes.cond_imagenes import galeria
from Creyente.prueba_componentes.scrollbar import scrollbar
from Creyente.prueba_componentes.imagenes_muesetra_index import imagen_grid_muestra


@rx.page(
    route=Route.PRUEBA.value,
    title=utils.courses_title,
    description=utils.courses_description,
    image=utils.preview,
    meta=utils.courses_meta
)


def prueba() -> rx.Component:
    return rx.box(
        rx.script(
            src="https://unpkg.com/swiper/swiper-bundle.min.css",
            type="text/css"
        ),
        rx.script(
            src="https://unpkg.com/swiper/swiper-bundle.min.js",
            on_ready=SwiperState.init_swiper,  # Asegúrate de definir SwiperState si es necesario
        ),
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                rx.heading("Condicional por pantalla",color="black"),
                galeria(),
                rx.heading("Scrollbar con slide de Imágenes",color="black"),
                scrollbar(),
                rx.heading("Imágenes con otra configuracion de tamano",color="black"),
                imagen_grid_muestra(),
                rx.vstack(
                    rx.heading("Carrusel de Imágenes con container",color="black"),
                    carousel_container(),
                    title("GALERÍA"),
                        rx.grid(
                            swiper_component(), 
                            width="100%",
                            margin_y="4"
                        ),
                        ejemplo_links(),
                    align="center",
                    width="100%",
                    spacing="4",
                    padding="4",
                ),
                max_width="100%",
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )