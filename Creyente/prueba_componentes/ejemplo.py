import reflex as rx
import Creyente.style.style as styles

class CarouselState(rx.State):
    carousel_states: dict[str, int] = {}
    
    def init_carousel(self, carousel_id: str):
        if carousel_id not in self.carousel_states:
            self.carousel_states[carousel_id] = 0
    
    def toggle_slide(self, carousel_id: str, index: int):
        self.carousel_states[carousel_id] = index
    
    def next_slide(self, carousel_id: str, total_slides: int):
        self.carousel_states[carousel_id] = (self.carousel_states[carousel_id] + 1) % total_slides
    
    def prev_slide(self, carousel_id: str, total_slides: int):
        self.carousel_states[carousel_id] = (self.carousel_states[carousel_id] - 1) % total_slides

def carrusel_tailwind(carousel_id: str, images: list[str], titulo: str):
    return rx.box(
        rx.box(
            rx.heading(
                titulo,
                style=styles.title_style,
                color="gray"
            ),
            margin_bottom="2em",
        ),
        rx.box(
            rx.box(
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
                rx.box(
                    rx.foreach(
                        range(len(images)),
                        lambda i: rx.button(
                            type_="button",
                            width=rx.breakpoints(
                                initial="8px",
                                sm="10px",
                                lg="12px"
                            ),
                            height=rx.breakpoints(
                                initial="8px",
                                sm="10px",
                                lg="12px"
                            ),
                            border_radius="50%",
                            bg=rx.cond(
                                CarouselState.carousel_states[carousel_id] == i,
                                "white",
                                "rgba(255,255,255,0.3)"
                            ),
                            margin_x=rx.breakpoints(
                                initial="2px",
                                sm="3px",
                                lg="4px"
                            ),
                            on_click=lambda: CarouselState.toggle_slide(carousel_id, i),
                            _hover={"bg": "rgba(255,255,255,0.8)"}
                        )
                    ),
                    position="absolute",
                    z_index="30",
                    bottom=rx.breakpoints(
                        initial="10px",
                        sm="15px",
                        lg="20px"
                    ),
                    left="50%",
                    transform="translateX(-50%)",
                    display="flex",
                ),
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

def carrusel_tailwind_despliegue():
    images0 = [
        "/trabajos_web/cafetera_horizontal_1080_web.JPG",
        "/trabajos_web/cogador_horizontal_1080_web.JPG", 
        "/trabajos_web/escritorio_cerrado_1080_web.JPG",
        "/trabajos_web/mueble_sala_horizontal_1080_web.JPG",
        "/trabajos_web/estudio_con_homenaje_1080_web.JPG",
    ]
    images = [
        "/trabajos_web/cafetera_horizontal_1080_web.JPG",
        "/trabajos_web/cafetera_vertical_cerrado_1080_web.JPG",
        "/trabajos_web/cafetera_vertical_abierto_1080_web_.JPG"
    ]
    images2 = [
        "/trabajos_web/cogador_horizontal_1080_web.JPG",
        "/trabajos_web/colgador_vertical_cerrado_1080_web.JPG",
        "/trabajos_web/colgador_vertical_abierto_1080_web.JPG",
    ]
    images3 = [
        "/trabajos_web/escritorio_cerrado_1080_web.JPG",
        "/trabajos_web/escritorio_abierto_1080_web.JPG",
    ]
    images4 = [
        "/trabajos_web/mueble_sala_horizontal_1080_web.JPG",
        "/trabajos_web/mueble_sala_vertical_1080_web.JPG",
    ]
    images5 = [
        "/trabajos_web/mueble_cocina_electrodomesticos_1080_web.JPG",
        "/trabajos_web/mueble_cocina_alacena_1080_web.JPG",
        "/trabajos_web/mueble_cocina_horno_alacena_1080_web.JPG",
    ]
    
    return rx.vstack(
        rx.box(
            carrusel_tailwind("carrusel1", images0, "EJEMPLO"),
            id="ejemplo"
        ),
        rx.box(
            carrusel_tailwind("carrusel2", images, "Cafetera"),
            id="cafetera"
        ),
        rx.box(
            carrusel_tailwind("carrusel3", images2, "Colgador"),
            id="colgador"
        ),
        rx.box(
            carrusel_tailwind("carrusel4", images3, "Escritorio"),
            id="escritorio"
        ),
        rx.box(
            carrusel_tailwind("carrusel5", images4, "Mueble Sala"),
            id="mueble-sala"
        ),
        rx.box(
            carrusel_tailwind("carrusel6", images5, "Estudio"),
            id="estudio"
        ),
        width="100%",
        spacing="8",
        align_items="stretch",
    )