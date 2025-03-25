# Importa la biblioteca Reflex y el módulo de colores personalizado
import reflex as rx
from Creyente.style.style import Color

# Define una clase base para almacenar datos de muebles
class MuebleData(rx.Base):
    # Define los atributos que tendrá cada mueble
    titulo: str                    # Título del mueble
    modelo: str                    # Modelo del mueble
    imagen_principal: str          # URL de la imagen principal
    imagenes_galeria: list[str]    # Lista de URLs de imágenes adicionales
    colores: list[dict[str, str]]  # Lista de diccionarios con información de colores
    descripcion: str               # Descripción detallada del mueble

def informacion_mueble():
    # Crea un contenedor principal con márgenes responsivos
    return rx.container(
        # Stack vertical que organiza todo el contenido verticalmente
        rx.vstack(
            # Contenedor flex para el título y subtítulo
            rx.flex(
                rx.vstack(
                    # Encabezado principal con tamaño responsivo
                    rx.heading(
                        "Escritorio",
                        # Tamaño del texto que cambia según el tamaño de pantalla
                        size=rx.breakpoints(
                            initial="3",  # Tamaño inicial para móviles
                            sm="4",       # Tamaño para tablets
                            lg="6"        # Tamaño para desktop
                        ),
                        color="black",
                    ),
                    # Texto del subtítulo con tamaño responsivo
                    rx.text(
                        "para estudiantes",
                        # Tamaño de fuente que cambia según el tamaño de pantalla
                        font_size=rx.breakpoints(
                            initial="sm",  # Tamaño inicial para móviles
                            sm="md",       # Tamaño para tablets
                            lg="lg"        # Tamaño para desktop
                        ),
                        color="black",
                    ),
                    align="center",      # Centra el contenido verticalmente
                    spacing="4",         # Espacio entre elementos
                ),
                width="100%",           # Ocupa todo el ancho disponible
                justify="center",        # Centra el contenido horizontalmente
                # Padding que cambia según el tamaño de pantalla
                padding=rx.breakpoints(
                    initial="2",
                    sm="4",
                    lg="6"
                ),
            ),

            # Contenedor para las tarjetas de materiales
            rx.box(
                # Stack horizontal para organizar las tarjetas
                rx.hstack(
                    # Primera tarjeta (Material Agave)
                    rx.card(
                        rx.vstack(
                            # Imagen del material
                            rx.image(
                                src="/material/Agave.jpg",
                                # Altura responsiva de la imagen
                                height=rx.breakpoints(
                                    initial="30px",
                                    sm="50px",
                                    lg="70px"
                                ),
                                width="auto",
                            ),
                            # Texto del nombre del material
                            rx.text(
                                "Agave",
                                # Tamaño de fuente responsivo
                                font_size=rx.breakpoints(
                                    initial="xs",
                                    sm="sm",
                                    lg="md"
                                ),
                                color="black"
                            ),
                            align="center",
                            # Padding interno responsivo
                            padding=rx.breakpoints(
                                initial="1",
                                sm="2",
                                lg="3"
                            ),
                        ),
                        # Ancho responsivo de la tarjeta
                        width=rx.breakpoints(
                            initial="120px",
                            sm="150px",
                            lg="180px"
                        ),
                    ),
                    # Segunda tarjeta (Material Bardolino)
                    rx.card(
                        rx.vstack(
                            # Imagen del material
                            rx.image(
                                src="/material/Agave.jpg",
                                # Altura responsiva de la imagen
                                height=rx.breakpoints(
                                    initial="30px",
                                    sm="50px",
                                    lg="70px"
                                ),
                                width="auto",
                            ),
                            # Texto del nombre del material
                            rx.text(
                                "Bardolino",
                                # Tamaño de fuente responsivo
                                font_size=rx.breakpoints(
                                    initial="xs",
                                    sm="sm",
                                    lg="md"
                                ),
                                color="black"
                            ),
                            align="center",
                            # Padding interno responsivo
                            padding=rx.breakpoints(
                                initial="1",
                                sm="2",
                                lg="3"
                            ),
                        ),
                        # Ancho responsivo de la tarjeta
                        width=rx.breakpoints(
                            initial="150px",
                            sm="180px",
                            lg="200px"
                        ),
                    ),
                    justify="center",    # Centra las tarjetas horizontalmente
                    width="100%",        # Ocupa todo el ancho disponible
                    spacing="4",         # Espacio entre tarjetas
                ),
                # Padding vertical responsivo
                padding_y=rx.breakpoints(
                    initial="2",
                    sm="4",
                    lg="6"
                ),
            ),

            # Contenedor para la descripción del mueble
            rx.box(
                # Texto de la descripción
                rx.text(
                    "Este escritorio para estudiante de melamina en tonos blanco y agave combina diseño moderno y funcionalidad. Con dimensiones compactas pero amplias, es ideal para espacios reducidos y perfecto para el uso de una persona adulta. Incluye un cajón en el escritorio para mantener tus útiles organizados y un asiento práctico con cajón adicional, maximizando el almacenamiento. Su estilo fresco y versátil se adapta a cualquier ambiente, ofreciendo comodidad y elegancia para estudiar o trabajar. ¡Optimiza tu espacio con este mueble que une practicidad y diseño!",
                    text_align="start",         # Alineación del texto a la izquierda
                    color="black",              # Color del texto
                    white_space="pre-wrap",     # Preserva espacios y saltos de línea
                    # Tamaño de fuente responsivo
                    font_size=rx.breakpoints(
                        initial="0.75em",
                        sm="0.875em",
                        lg="1em"
                    ),
                    # Padding interno responsivo
                    padding=rx.breakpoints(
                        initial="2",
                        sm="3",
                        lg="4"
                    ),
                ),
                # Altura responsiva del contenedor
                height=rx.breakpoints(
                    initial="180px",
                    sm="200px",
                    lg="350px"
                ),
                # Ancho responsivo del contenedor
                width=rx.breakpoints(
                    initial="98%",
                    sm="90%",
                    lg="98%"
                ),
                overflow_y="auto",           # Habilita scroll vertical
                border="1px solid #E2E8F0", # Borde del contenedor
                # Radio del borde responsivo
                border_radius=rx.breakpoints(
                    initial="sm",
                    sm="md",
                    lg="lg"
                ),
                background=Color.BACKGROUND.value,  # Color de fondo aplicado al contenedor
                margin="auto",              # Centra el contenedor
            ),
            spacing="4",                    # Espacio entre secciones principales
            width="100%",                   # Ocupa todo el ancho disponible
            align="stretch",                # Estira los elementos al ancho del contenedor
        ),
        # Padding horizontal responsivo del contenedor principal
        padding_x=rx.breakpoints(
            initial="2",
            sm="4",
            lg="6"
        ),
        # Padding vertical responsivo del contenedor principal
        padding_y=rx.breakpoints(
            initial="3",
            sm="5",
            lg="7"
        ),
        # Tamaño responsivo del contenedor principal
        size=rx.breakpoints(
            initial="2", 
            sm="3",
            lg="4"
        ),
    )