
styles = {
    "breakpoints": {
        "xs": "30em",
        "sm": "48em", 
        "md": "62em",
        "lg": "80em",
        "xl": "96em",
    },
}

# Creyente/pages/historia.py
import reflex as rx
from Creyente.style.style import Size
from Creyente.style.colors import Color

def historia_link() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.image(
                    "/militar_de_fe.jpeg",
                    width=rx.breakpoints(
                        initial="100%",
                        sm="300px", 
                        md="400px"
                    ),
                    height=rx.breakpoints(
                        initial="auto",
                        sm="300px",
                        md="400px"
                    ),
                    object_fit="cover",
                ),
                rx.text(
                    "'Creyente' no fue solo un alias militar, sino el reflejo de un hombre con fe inquebrantable. Mi padre, un hombre de principios sólidos, encontró en su vocación no solo disciplina, sino la pasión por crear, enseñar y construir un futuro para su familia.",
                    font_size=rx.breakpoints(
                        initial="14px",
                        sm="16px",
                        md="18px"
                    ),
                    padding=rx.breakpoints(
                        initial="1em",
                        md="2em"
                    ),
                ),
                spacing="4",
                align="center",
                flex_direction=rx.breakpoints(
                    initial="column",
                    md="row"
                ),
                width="100%",
            ),
            rx.hstack(
                rx.text(
                    "De su dedicación nació algo más que un simple oficio: una pasión por transformar materiales en piezas únicas. Nos enseñó que cada detalle cuenta, que la excelencia no es una opción, sino la única forma de trabajar.",
                    font_size=rx.breakpoints(
                        initial="14px",
                        sm="16px",
                        md="18px"
                    ),
                    padding=rx.breakpoints(
                        initial="1em",
                        md="2em"
                    ),
                ),
                rx.image(
                    "/artezano.jpg",
                    width=rx.breakpoints(
                        initial="100%",
                        sm="300px",
                        md="400px"
                    ),
                    height=rx.breakpoints(
                        initial="auto",
                        sm="300px",
                        md="400px"
                    ),
                    object_fit="cover",
                ),
                spacing="4",
                align="center",
                flex_direction=rx.breakpoints(
                    initial="column",
                    md="row"
                ),
                width="100%",
            ),
            rx.hstack(
                rx.text(
                    "Hoy, este negocio no es solo una empresa, es un legado. Como familia, seguimos el ejemplo de mi padre, combinando tradición con innovación, creando muebles que cuentan historias y acompañan hogares.",
                    font_size=rx.breakpoints(
                        initial="14px",
                        sm="16px",
                        md="18px"
                    ),
                    padding=rx.breakpoints(
                        initial="1em",
                        md="2em"
                    ),
                ),
                rx.image(
                    "/artezanos_familia.jpg",
                    width=rx.breakpoints(
                        initial="100%",
                        sm="300px",
                        md="400px"
                    ),
                    height=rx.breakpoints(
                        initial="auto",
                        sm="300px",
                        md="400px"
                    ),
                    object_fit="cover",
                ),
                rx.text(
                    "Para nosotros, cada cliente es parte de nuestra historia. No solo vendemos muebles, creamos espacios llenos de calidez y personalidad, con la misma dedicación con la que mi padre nos enseñó a trabajar.",
                    font_size=rx.breakpoints(
                        initial="14px",
                        sm="16px",
                        md="18px"
                    ),
                    padding=rx.breakpoints(
                        initial="1em",
                        md="2em"
                    ),
                ),
                spacing="4",
                align="center",
                flex_direction=rx.breakpoints(
                    initial="column",
                    md="row"
                ),
                width="100%",
            ),
            spacing="8",
            width="100%",
            padding=rx.breakpoints(
                initial="1em",
                md="2em"
            ),
        ),
        color=Color.BLACK.value,
        max_width="1200px",
        width="100%",
        margin="0 auto",
        padding_y="2em",
    )