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
                    "/renovacion_tia/armario_casa_lata_frontal.jpg",
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
                    border_radius="10px"
                ),
                rx.text(
                    "CREYENTE nació por necesidad. Después de malas experiencias con carpinteros, decidimos tomar las herramientas en nuestras propias manos. "
                    "Todo comenzó con un simple mueble para computadora, hecho con dedicación y cuidado. Lo que empezó como una solución a un problema personal "
                    "se convirtió en el inicio de algo mucho mayor.",
                    font_size=rx.breakpoints(
                        initial="14px",
                        sm="16px",
                        md="18px"
                    ),
                    padding=rx.breakpoints(
                        initial="1em",
                        md="2em"
                    ),
                    text_align="justify"
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
                    "Con cada proyecto, nuestra habilidad crecía. Pronto estábamos trabajando con melamina, construyendo los armarios de nuestra propia casa. "
                    "Familiares y amigos, al ver nuestro trabajo, comenzaron a pedirnos remodelaciones: mesas que renovar, muebles antiguos que restaurar. "
                    "Cada trabajo era un nuevo reto que aceptábamos con entusiasmo, perfeccionando nuestras técnicas.",
                    font_size=rx.breakpoints(
                        initial="14px",
                        sm="16px",
                        md="18px"
                    ),
                    padding=rx.breakpoints(
                        initial="1em",
                        md="2em"
                    ),
                    text_align="justify"
                ),
                rx.image(
                    "/renovacion_tia/comedor_tia_solo.jpg",
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
                    border_radius="10px"
                ),
                spacing="4",
                align="center",
                flex_direction=rx.breakpoints(
                    initial="column-reverse",
                    md="row"
                ),
                width="100%",
            ),
            rx.hstack(
                rx.image(
                    "/fotostecho/madera_interno_lateral.jpg",
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
                    border_radius="10px"
                ),
                rx.vstack(
                    rx.text(
                        "Lo que comenzó como una necesidad se transformó en pasión. Con cada proyecto, nos desafiamos a superarnos: diseños más complejos, "
                        "materiales de mejor calidad, acabados impecables. La reputación de CREYENTE creció orgánicamente, basada en el boca a boca de "
                        "clientes satisfechos que valoraban nuestra atención al detalle y compromiso con la excelencia.",
                        font_size=rx.breakpoints(
                            initial="14px",
                            sm="16px",
                            md="18px"
                        ),
                        padding=rx.breakpoints(
                            initial="1em",
                            md="2em"
                        ),
                        text_align="justify"
                    ),
                    rx.text(
                        "Hoy, CREYENTE representa más que muebles. Es la materialización de una filosofía: si algo vale la pena hacerse, vale la pena hacerse bien. "
                        "Cada pieza que creamos lleva no solo nuestra marca, sino nuestra historia de perseverancia y crecimiento.",
                        font_size=rx.breakpoints(
                            initial="14px",
                            sm="16px",
                            md="18px"
                        ),
                        padding=rx.breakpoints( 
                            initial="1em",
                            md="2em"
                        ),
                        text_align="justify"
                    ),
                    align_items="start"
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
        bg=Color.BACKGROUND.value
    )