#carrusel_tailwaind.py
import reflex as rx
import Creyente.style.style as styles

# Estado del carrusel para manejar las transiciones y slides
class CarouselState(rx.State):
    # Diccionario para mantener el estado de múltiples carruseles
    carousel_states: dict[str, int] = {}
    
    # Inicializa un nuevo carrusel con índice 0
    def init_carousel(self, carousel_id: str):
        if carousel_id not in self.carousel_states:
            self.carousel_states[carousel_id] = 0
    
    # Cambia directamente a un slide específico
    def toggle_slide(self, carousel_id: str, index: int):
        self.carousel_states[carousel_id] = index
    
    # Avanza al siguiente slide
    def next_slide(self, carousel_id: str, total_slides: int):
        self.carousel_states[carousel_id] = (self.carousel_states[carousel_id] + 1) % total_slides
    
    # Retrocede al slide anterior
    def prev_slide(self, carousel_id: str, total_slides: int):
        self.carousel_states[carousel_id] = (self.carousel_states[carousel_id] - 1) % total_slides

# Componente principal del carrusel
def carrusel_tailwind(carousel_id: str, images: list[str], titulo: str):
    return rx.box(
        # Contenedor del título
        rx.box(
            rx.heading(
                titulo,
                style=styles.title_style,
                color="gray"
            ),
            margin_bottom="2em",
        ),
        # Contenedor principal del carrusel
        rx.box(
            rx.box(
                # Contenedor de las imágenes
                rx.box(
                    rx.foreach(
                        images,
                        lambda src, i: rx.box(
                            rx.image(
                                src=src,
                                alt=f"Slide {i + 1}",
                                width="100%",
                                height="100%",
                                object_fit="contain",
                                object_position="center",
                            ),
                            display=rx.cond(
                                CarouselState.carousel_states[carousel_id] == i,
                                "block",
                                "none"
                            ),
                            opacity=rx.cond(
                                CarouselState.carousel_states[carousel_id] == i,
                                "1",
                                "0"
                            ),
                            transition="all 0.5s ease-in-out",
                            bg="rgb(240, 240, 240)",
                            height="100%",
                        )
                    ),
                    width="100%",
                    height=rx.breakpoints(
                        initial="300px",
                        sm="400px",
                        lg="500px"
                    ),
                    overflow="hidden",
                    border_radius="lg",
                ),
                # Indicadores de navegación (puntos)
                rx.box(
                    rx.foreach(
                        range(len(images)),
                        lambda i: rx.button(
                            type_="button",
                            width=rx.breakpoints(
                                initial="12px",  # Aumentado tamaño en móvil
                                sm="14px",
                                lg="16px"
                            ),
                            height=rx.breakpoints(
                                initial="12px",  # Aumentado tamaño en móvil
                                sm="14px",
                                lg="16px"
                            ),
                            border_radius="50%",
                            bg=rx.cond(
                                CarouselState.carousel_states[carousel_id] == i,
                                "white",  # Más oscuro cuando está activo
                                "rgba(255,255,255,0.3)"   # Más visible en inactivo
                            ),
                            margin_x=rx.breakpoints(
                                initial="4px",  # Más espacio entre puntos
                                sm="5px",
                                lg="6px"
                            ),
                            on_click=lambda: CarouselState.toggle_slide(carousel_id, i),
                            _hover={"bg": "rgba(255,255,255,0.8)"},
                            # border="2px solid white",  # Borde blanco para más contraste
                        )
                    ),
                    position="absolute",
                    z_index="30",
                    bottom=rx.breakpoints(
                        initial="20px",  # Subido más arriba en móvil
                        sm="25px",
                        lg="30px"
                    ),
                    left="50%",
                    transform="translateX(-50%)",
                    display="flex",
                    padding="8px",  # Padding para área de toque más grande
                    # bg="rgba(255,255,255,0.3)",  # Fondo semi-transparente
                    border_radius="full",  # Bordes redondeados
                ),
                # Botón anterior (flecha izquierda)
                rx.button(
                    rx.icon(
                        "chevron_left",
                        color="white",
                        font_size=rx.breakpoints(
                            initial="18px",
                            sm="20px",
                            lg="24px"
                        )
                    ),
                    position="absolute",
                    top="50%",
                    left=rx.breakpoints(
                        initial="10px",
                        sm="15px",
                        lg="20px"
                    ),
                    transform="translateY(-50%)",
                    z_index="30",
                    bg="rgba(0,0,0,0.5)",
                    border_radius="full",
                    padding=rx.breakpoints(
                        initial="4",
                        sm="5",
                        lg="6"
                    ),
                    height="fit-content",
                    min_height="40px",
                    width="40px",
                    on_click=lambda: CarouselState.prev_slide(carousel_id, len(images)),
                    _hover={"bg": "rgba(0,0,0,0.8)"}
                ),
                # Botón siguiente (flecha derecha)
                rx.button(
                    rx.icon(
                        "chevron_right",
                        color="white",
                        font_size=rx.breakpoints(
                            initial="18px",
                            sm="20px",
                            lg="24px"
                        )
                    ),
                    position="absolute",
                    top="50%",
                    right=rx.breakpoints(
                        initial="10px",
                        sm="15px",
                        lg="20px"
                    ),
                    transform="translateY(-50%)",
                    z_index="30",
                    bg="rgba(0,0,0,0.5)",
                    border_radius="full",
                    padding=rx.breakpoints(
                        initial="4",
                        sm="5",
                        lg="6"
                    ),
                    height="fit-content",
                    min_height="40px",
                    width="40px",
                    on_click=lambda: CarouselState.next_slide(carousel_id, len(images)),
                    _hover={"bg": "rgba(0,0,0,0.8)"}
                ),
                position="relative",
                width="100%",
            ),
            width="100%",
            padding=rx.breakpoints(
                initial="2",
                sm="3",
                lg="4"
            ),
            on_mount=lambda: CarouselState.init_carousel(carousel_id),
        ),
        margin_bottom="8",
    )

# Función para desplegar múltiples carruseles
def carrusel_tailwind_despliegue():
    # Lista de imágenes para el carrusel de ejemplo



    # Lista de imágenes para el carrusel de ejemplo
    images0 = [
        "/trabajos_web/cafetera_horizontal_1080_web.JPG",
        "/trabajos_web/cogador_horizontal_1080_web.JPG",
        "/trabajos_web/escritorio_cerrado_1080_web.JPG",
        "/trabajos_web/mueble_sala_horizontal_1080_web.JPG",
        "/trabajos_web/estudio_con_homenaje_1080_web.JPG",
    ]


    

    # Lista de imágenes para el carrusel de mueble sala
    images1 = [
        "/trabajos_web/mueble_sala_horizontal_1080_web.JPG",
        "/trabajos_web/mueble_sala_vertical_1080_web.JPG",
    ]

    # Lista de imágenes para el carrusel de perchero
    images2 = [
        "/trabajos_web/cogador_horizontal_1080_web.JPG",
        "/trabajos_web/colgador_vertical_cerrado_1080_web.JPG",
        "/trabajos_web/colgador_vertical_abierto_1080_web.JPG",
    ]
    # Lista de imágenes para el carrusel de estudio
    images3 = [
        "/trabajos_web/estudio_con_homenaje_1080_web.JPG",
    ]
    # Lista de imágenes para el carrusel de escritorio
    images4 = [
        "/trabajos_web/escritorio_cerrado_1080_web.JPG",
        "/trabajos_web/escritorio_abierto_1080_web.JPG",
    ]
    # Lista de imágenes para el carrusel de cafetera
    images5 = [
        "/trabajos_web/cafetera_horizontal_1080_web.JPG",
        "/trabajos_web/cafetera_vertical_cerrado_1080_web.JPG",
        "/trabajos_web/cafetera_vertical_abierto_1080_web_.JPG"
    ]
    # Lista de imágenes para el carrusel de cocina
    images6 = [
        "/trabajos_web/mueble_cocina_electrodomesticos_1080_web.JPG",
        "/trabajos_web/mueble_cocina_alacena_1080_web.JPG",
        "/trabajos_web/mueble_cocina_horno_alacena_1080_web.JPG",
    ]
    # Lista de imágenes para el carrusel de cuarto
    images7 = [
        "/trabajos_web/mueble_armario_1080_web.JPG",
    ]
    # Lista de imágenes para techo con tejas
    images8 = [
        "/fotostecho/inicio_techo.jpg",
        "/fotostecho/teja.jpg",
        "/fotostecho/madera_interno_lateral.jpg",
        "/fotostecho/madera_interno_puerta.jpg",
    ]
    
    # Retorna un stack vertical con todos los carruseles
    return rx.vstack(
        # Carrusel de ejemplo
        # rx.box(
        #     carrusel_tailwind("carrusel1", images1, "EJEMPLO"),
        #     id="ejemplo"
        # ),


        # Carrusel de mueble sala
        rx.box(
            carrusel_tailwind("carrusel5", images1, "Mueble Sala"),
            id="mueble-sala"
        ),
        # Carrusel de Perchero
        rx.box(
            carrusel_tailwind("carrusel3", images2, "Perchero"),
            id="perchero"
        ),
        # Carrusel de estudio
        rx.box(
            carrusel_tailwind("carrusel6", images3, "Estudio con Homenaje"),
            id="estudio"
        ),
        # Carrusel de escritorio
        rx.box(
            carrusel_tailwind("carrusel4", images4, "Escritorio"),
            id="escritorio"
        ),
        # Carrusel de cafetera
        rx.box(
            carrusel_tailwind("carrusel2", images5, "El Rincon del cafe"),
            id="cafetera"
        ),
        # Carrusel de Mueble Cocina
        rx.box(
            carrusel_tailwind("carrusel7", images6, "Mueble Cocina"),
            id="mueble-cocina"
        ),
        # Carrusel de Mueble Cuarto
        rx.box(
            carrusel_tailwind("carrusel7", images7, "Mueble Cuarto"),
            id="mueble-cuarto"
        ),
        # Carrusel de techo con tejas
        rx.box(
            carrusel_tailwind("carrusel8", images8, "Techo con Tejas"),
            id="techo_tejas"
        ),
        width="100%",
        spacing="8",
        align_items="stretch",
    )