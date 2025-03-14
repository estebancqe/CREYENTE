import reflex as rx

def swiper_component():
    # Definimos la lista de imágenes con sus propiedades
    images = [
        {
            "src": "/trabajos_web/cafetera_horizontal_1080_web.JPG",  # Ruta de la imagen
            "title": "Cafetera Horizontal",                           # Título de la imagen
            "section_id": "cafetera"                                  # ID para navegación
        },
        {
            "src": "/trabajos_web/cogador_horizontal_1080_web.JPG",
            "title": "Colgador Horizontal",
            "section_id": "colgador"
        },
        {
            "src": "/trabajos_web/escritorio_cerrado_1080_web.JPG",
            "title": "Escritorio Cerrado",
            "section_id": "escritorio"
        },
        {
            "src": "/trabajos_web/mueble_sala_horizontal_1080_web.JPG",
            "title": "Mueble Sala",
            "section_id": "mueble-sala"
        },
        {
            "src": "/trabajos_web/estudio_con_homenaje_1080_web.JPG",
            "title": "Estudio con Homenaje",
            "section_id": "estudio"
        }
    ]
    
    # Retornamos el componente principal
    return rx.box(
        # Contenedor del carrusel
        rx.box(
            # Iteramos sobre las imágenes usando rx.foreach
            rx.foreach(
                images,  # Lista de imágenes a iterar
                lambda image: rx.box(  # Función que procesa cada imagen
                    rx.link(  # Componente de enlace
                        rx.box(
                            # Imagen del carrusel
                            rx.image(
                                src=image["src"],
                                width="100%",
                                height="100%",
                                object_fit="cover"  # Ajuste de la imagen
                            ),
                            # Título superpuesto
                            rx.heading(
                                image["title"],
                                color="black",
                                # Tamaños responsivos del texto
                                font_size=rx.breakpoints(
                                    initial="1rem",  # Tamaño móvil
                                    sm="1.2rem",     # Tamaño tablet
                                    lg="1.4rem"      # Tamaño desktop
                                ),
                                # Estilos del contenedor del título
                                background_color="rgba(255,255,255,0.9)",
                                padding="0.5em",
                                border_radius="0.25em",
                                position="absolute",
                                top="1em",
                                left="1em",
                                z_index="10",
                                box_shadow="0 2px 4px rgba(0,0,0,0.2)"
                            ),
                            # Estilos del contenedor de la imagen
                            position="relative",
                            width="100%",
                            height="100%",
                        ),
                        # URL de navegación
                        href=f"/proyectos#{image['section_id']}",
                        is_external=False
                    ),
                    class_name="swiper-slide"  # Clase para el slider
                )
            ),
            class_name="swiper-wrapper"  # Clase contenedora del slider
        ),
        
        # Indicador de posición móvil
        rx.box(
            rx.text(
                "1/5",  # Texto del indicador
                class_name="mobile-indicator-1",
                # Estilos del indicador
                color="black",
                background_color="rgba(255,255,255,0.9)",
                padding="0.5em 1em",
                border_radius="2em",
                position="absolute",    
                bottom="1em",
                right="1em",
                z_index="10",
                # Visibilidad responsiva
                display=rx.breakpoints(
                    initial="block",
                    sm="block",
                    lg="block"
                )
            )
        ),
        
        # Elementos de navegación del slider
        rx.box(class_name="swiper-pagination-1"),  # Paginación
        rx.box(class_name="swiper-button-next-1"), # Botón siguiente
        rx.box(class_name="swiper-button-prev-1"), # Botón anterior
        
        # Estilos del contenedor principal
        class_name="swiper-container-1",
        width="100%",
        # Altura responsiva
        height=rx.breakpoints(
            initial="300px",  # Altura móvil
            sm="400px",       # Altura tablet
            lg="500px"        # Altura desktop
        ),
        overflow="hidden",
        position="relative",
        # Márgenes responsivos
        margin_y=rx.breakpoints(
            initial="1em",    # Margen móvil
            sm="2em",         # Margen tablet
            lg="2em"          # Margen desktop
        )
    )