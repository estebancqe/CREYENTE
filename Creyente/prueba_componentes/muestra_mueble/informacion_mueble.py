import reflex as rx

class MuebleData(rx.Base):
    titulo: str
    modelo: str
    imagen_principal: str
    imagenes_galeria: list[str]
    colores: list[dict[str, str]]
    descripcion: str

def informacion_mueble():
    return rx.container(
        rx.vstack(
            # Título y subtítulo
            rx.flex(
                rx.vstack(
                    rx.heading(
                        "Escritorio",
                        size=rx.breakpoints(
                            initial="3",
                            sm="4",
                            lg="6"
                        ),
                        color="black",
                    ),
                    rx.text(
                        "para estudiantes",
                        font_size=rx.breakpoints(
                            initial="sm",
                            sm="md",
                            lg="lg"
                        ),
                        color="black",
                    ),
                    align="center",
                    spacing="4",  # Valor fijo en lugar de breakpoints
                ),
                width="100%",
                justify="center",
                padding=rx.breakpoints(
                    initial="2",
                    sm="4",
                    lg="6"
                ),
            ),

            # Imágenes de materiales
            rx.box(
                rx.hstack(
                    rx.card(
                        rx.vstack(
                            rx.image(
                                src="/material/Agave.jpg",
                                height=rx.breakpoints(
                                    initial="30px",
                                    sm="50px",
                                    lg="70px"
                                ),
                                width="auto",
                            ),
                            rx.text(
                                "Agave",
                                font_size=rx.breakpoints(
                                    initial="xs",
                                    sm="sm",
                                    lg="md"
                                ),
                                color="black"
                            ),
                            align="center",
                            padding=rx.breakpoints(
                                initial="1",
                                sm="2",
                                lg="3"
                            ),
                        ),
                        width=rx.breakpoints(
                            initial="120px",
                            sm="150px",
                            lg="180px"
                        ),
                    ),
                    rx.card(
                        rx.vstack(
                            rx.image(
                                src="/material/Agave.jpg",
                                height=rx.breakpoints(
                                    initial="30px",
                                    sm="50px",
                                    lg="70px"
                                ),
                                width="auto",
                            ),
                            rx.text(
                                "Bardolino",
                                font_size=rx.breakpoints(
                                    initial="xs",
                                    sm="sm",
                                    lg="md"
                                ),
                                color="black"
                            ),
                            align="center",
                            padding=rx.breakpoints(
                                initial="1",
                                sm="2",
                                lg="3"
                            ),
                        ),
                        width=rx.breakpoints(
                            initial="150px",
                            sm="180px",
                            lg="200px"
                        ),
                    ),
                    justify="center",
                    width="100%",
                    spacing="4",  # Valor fijo en lugar de breakpoints
                ),
                padding_y=rx.breakpoints(
                    initial="2",
                    sm="4",
                    lg="6"
                ),
            ),

            # Descripción
            rx.box(
                rx.text(
                    "Este escritorio para estudiante de melamina en tonos blanco y agave combina diseño moderno y funcionalidad. Con dimensiones compactas pero amplias, es ideal para espacios reducidos y perfecto para el uso de una persona adulta. Incluye un cajón en el escritorio para mantener tus útiles organizados y un asiento práctico con cajón adicional, maximizando el almacenamiento. Su estilo fresco y versátil se adapta a cualquier ambiente, ofreciendo comodidad y elegancia para estudiar o trabajar. ¡Optimiza tu espacio con este mueble que une practicidad y diseño!",
                    text_align="start",
                    color="black",
                    white_space="pre-wrap",
                    font_size=rx.breakpoints(
                        initial="0.75em",
                        sm="0.875em",
                        lg="1em"
                    ),
                    padding=rx.breakpoints(
                        initial="2",
                        sm="3",
                        lg="4"
                    ),
                ),
                height=rx.breakpoints(
                    initial="150px",
                    sm="200px",
                    lg="250px"
                ),
                width=rx.breakpoints(
                    initial="95%",
                    sm="90%",
                    lg="85%"
                ),
                overflow_y="auto",
                border="1px solid #E2E8F0",
                border_radius=rx.breakpoints(
                    initial="sm",
                    sm="md",
                    lg="lg"
                ),
                background="white",
                margin="auto",
            ),
            spacing="4",  # Valor fijo en lugar de breakpoints
            width="100%",
            align="stretch",
        ),
        padding_x=rx.breakpoints(
            initial="2",
            sm="4",
            lg="6"
        ),
        padding_y=rx.breakpoints(
            initial="3",
            sm="5",
            lg="7"
        ),
        size=rx.breakpoints( 
            initial="2",
            sm="3",
            lg="4"
        ),
    )