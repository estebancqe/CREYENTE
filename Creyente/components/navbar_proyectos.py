import reflex as rx
import Creyente.style.style as styles
from Creyente.components.link_navbar import link_navbar
from Creyente.routes import Route
from Creyente.style.style import Size, Color, TextColor

def navbar_proyectos() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.scroll_area(
                rx.hstack(
                    # Enlaces a las secciones
                    link_navbar(
                        "Inicio",
                        Route.INDEX.value,
                        "palabra inicio",
                    ),
                    # link_navbar("Ejemplo", "#ejemplo", "Ejemplo"),
                    link_navbar("Mueble Sala", "#mueble-sala", "Mueble Sala"),
                    link_navbar("Perchero", "#perchero", "Perchero"),
                    link_navbar("Estudio con Homenaje", "#estudio", "Estudio"),
                    link_navbar("Escritorio", "#escritorio", "Escritorio"), 
                    link_navbar("El Rincón del café", "#cafetera", "EL Rincon del cafe"),
                    link_navbar("Mueble Cocina", "#mueble-cocina", "Mueble Cocina"),
                    link_navbar("Mueble Cuarto", "#mueble-cuarto", "Mueble Cuarto"),
                    link_navbar("Techo con teja"," #techo_tejas", "Techo con teja"),
                    spacing="6",  # Aumentado el espaciado
                    padding="16px",  # Aumentado el padding
                    padding_right="48px",
                    style={
                        "white-space": "nowrap",  # Mantiene el texto en una línea
                        "margin-bottom": "0.5em"  # Espacio adicional debajo
                    }
                ),
                type="always",
                scrollbars="horizontal",
                style={
                    "height": "auto", 
                    "width": "100%",
                    "padding-bottom": "0.5em"  # Espacio adicional para el scrollbar
                },
            ),
            rx.desktop_only(
                rx.hstack(
                    rx.link(
                        rx.image(
                            src="/CREYENTE.png",
                            height="50px",
                            width="auto",
                        ),
                        href="/"
                    ),
                    justify_content="center",
                ),
            ),
            width="100%",
            justify="between",
            align="center",
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
    )