# Importaciones necesarias para el componente navbar
import reflex as rx
import Creyente.style.style as styles
from Creyente.components.link_navbar import link_navbar
from Creyente.routes import Route
from Creyente.style.style import Size, Color, TextColor

def navbar() -> rx.Component:
    """
    Componente de barra de navegación responsiva.
    Returns:
        rx.Component: Componente Flex que contiene la barra de navegación
    """
    return rx.flex(
        # Sección de navegación izquierda
        rx.hstack(
            # Primer grupo de enlaces
            rx.hstack(
                # Enlaces de Inicio e Historia
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
                
                spacing="2",  # Espaciado entre elementos
            ),
            # Segundo grupo de enlaces
            rx.hstack(
                # Enlaces de Misión, Proyectos y Prueba
                # link_navbar(
                #     "Misión",
                #     Route.MISION.value,
                #     "palabra mision",
                # ),
                link_navbar(
                    "Proyectos",
                    Route.PROYECTOS.value,
                    "palabra trabajos",
                ),
                link_navbar(
                    "Materiales",
                    Route.MELAMINA.value,
                    "tipos de materiales en melamina"
                ),
                # link_navbar(
                #     "Prueba",
                #     Route.PRUEBA.value,
                #     "palabra inicio",
                # ),
                spacing="2",  # Espaciado entre elementos
            ),
            # Estilos para el contenedor de navegación
            color=Color.BACKGROUND.value,
            style=styles.navbar_title_style,
            # Configuración responsiva de la dirección flex
            flex_direction=rx.breakpoints(
                initial="row",  # Móvil
                sm="row",       # Tablet
                lg="row"        # Desktop
            ),
            align_items="center",
            # Configuración responsiva del ancho
            width=rx.breakpoints(
                initial="100%", # Ancho completo en móvil
                sm="100%",      # Ancho completo en tablet
                lg="auto"       # Ancho automático en desktop
            ),
        ),
        # Sección del logo central
        rx.hstack(
            rx.link(
                # Imagen del logo con tamaños responsivos
                rx.image(
                    src="/CREYENTE.png",
                    height=rx.breakpoints(
                        initial="30px", # Altura en móvil
                        sm="40px",      # Altura en tablet
                        lg="50px"       # Altura en desktop
                    ),
                    width="auto",
                ),
                href=Route.INDEX.value 
            ),
            justify_content="center",
        ),
        # Estilos generales del contenedor principal
        spacing="4",
        # Configuración responsiva del ancho total
        width=rx.breakpoints(
            initial="100%",
            sm="100%",
            lg="100%"
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",         # Asegura que el navbar esté siempre visible
        top="0",              # Fija el navbar en la parte superior
        justify="between",     # Distribuye el espacio entre elementos
        align="center",        # Alinea elementos verticalmente
        # Configuración responsiva de la dirección flex
        flex_direction=rx.breakpoints(
            initial="row",
            sm="row", 
            lg="row"
        ),
    )