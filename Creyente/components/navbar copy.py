import reflex as rx
import Creyente.style.style as styles
from Creyente.components.link_navbar import link_navbar
from Creyente.routes import Route
from Creyente.style.style import Size, Color, TextColor

def navbar_proyectos() -> rx.Component:
    return rx.flex(
        # Navegación izquierda
        rx.hstack(
            rx.hstack(
                link_navbar(
                    "Inicio",
                    Route.INDEX.value,
                    "palabra inicio",
                ),
                link_navbar(
                    "Historia",
                    Route.HISTORIA.value,
                    "palabra historia"
                ),
                spacing="4",  # Valor fijo para spacing
            ),
            rx.hstack(
                link_navbar(
                    "Misión",
                    Route.MISION.value,
                    "palabra mision",
                ),
                link_navbar(
                    "Proyectos",
                    Route.PROYECTOS.value,
                    "palabra trabajos",
                ),
                link_navbar(
                    "Prueba",
                    Route.PRUEBA.value,
                    "palabra inicio",
                ),
                
                
                spacing="4",  # Valor fijo para spacing
            ),
            color=Color.BACKGROUND.value,
            style=styles.navbar_title_style,
            flex_direction=rx.breakpoints(
                initial="row",
                sm="row",
                lg="row"
            ),
            align_items="center",
            width=rx.breakpoints(
                initial="100%",
                sm="100%",
                lg="auto"
            ),
        ),
        # Logo/Título centrado
        rx.hstack(
            rx.link(
                rx.image(
                    src="/CREYENTE.png",
                    height=rx.breakpoints(
                        initial="30px",
                        sm="40px",
                        lg="50px"
                    ),
                    width="auto",
                ),
                href=Route.INDEX.value 
            ),
            justify_content="center",
        ),
        spacing="4",  # Valor fijo para spacing
        width=rx.breakpoints(
            initial="100%",
            sm="100%",
            lg="100%"
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        justify="between",
        align="center",
        flex_direction=rx.breakpoints(
            initial="row",
            sm="row", 
            lg="row"
        ),
    )