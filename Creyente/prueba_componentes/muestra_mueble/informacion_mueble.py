import reflex as rx



class MuebleData(rx.Base):
    titulo: str
    modelo: str
    imagen_principal: str
    imagenes_galeria: list[str]
    colores: list[dict[str, str]]  # lista de diccionarios con nombre y url de imagen
    descripcion: str




def informacion_mueble():
    return rx.vstack(
        # Título
        rx.heading(
            "Escritorio",
            size=rx.breakpoints(
                initial="3",    # móvil
                sm="5",       # tablet
                lg="6"        # desktop
            ),
            color="black",
        ),
        
        # Subtítulo
        rx.text(
            "para estudiantes",
            font_size=rx.breakpoints(
                initial="md",    # móvil
                sm="lg",        # tablet
                lg="xl"         # desktop
            ),
            color="black",
        ),
        
        # Imágenes de materiales
        rx.hstack(
            rx.vstack(
                rx.image(
                    src="/material/Agave.jpg",
                    height=rx.breakpoints(
                        initial="40px",
                        sm="60px",
                        lg="80px"
                    ),
                    width="auto",
                ),
                rx.text(
                    "Agave",
                    font_size="sm",
                    color="black"
                ),
                align="center",
            ),
            rx.vstack(
                rx.image(
                    src="/material/Agave.jpg",
                    height=rx.breakpoints(
                        initial="40px",
                        sm="60px",
                        lg="80px"
                    ),
                    width="auto",
                ),
                rx.text(
                    "Color 2",
                    font_size="sm",
                    color="black"
                ),
                align="center",
            ),
            justify="center",
            width="100%",
            spacing_x="1",
        ),
        
        # Descripción
        rx.text(
            "Este escritorio para estudiante de melamina en tonos blanco y agave combina diseño moderno y funcionalidad. Con dimensiones compactas pero amplias, es ideal para espacios reducidos y perfecto para el uso de una persona adulta. Incluye un cajón en el escritorio para mantener tus útiles organizados y un asiento práctico con cajón adicional, maximizando el almacenamiento. Su estilo fresco y versátil se adapta a cualquier ambiente, ofreciendo comodidad y elegancia para estudiar o trabajar. ¡Optimiza tu espacio con este mueble que une practicidad y diseño!",
            text_align="start",
            color="black",
            padding_x="2",
            font_size=rx.breakpoints(
                initial="1",    # móvil
                sm="1",        # tablet
                lg="0.4"         # desktop
            ),
        ),
        
        spacing="3",
        width="100%",
        align="center",
    )