import reflex as rx

class CarouselState(rx.State):
    """El estado del carrusel."""
    current_index: int = 0
    images: list[str] = [
        "/trabajos_web/cafetera_horizontal_1080_web.JPG",
        "/trabajos_web/cogador_horizontal_1080_web.JPG",
        "/trabajos_web/escritorio_cerrado_1080_web.JPG",
        "/trabajos_web/mueble_sala_horizontal_1080_web.JPG",
        "/trabajos_web/estudio_con_homenaje_1080_web.JPG",
    ]

    @rx.event
    def next_image(self):
        """Avanzar a la siguiente imagen."""
        if self.current_index < len(self.images) - 1:
            self.current_index += 1
        else:
            self.current_index = 0

    @rx.event
    def previous_image(self):
        """Retroceder a la imagen anterior."""
        if self.current_index > 0:
            self.current_index -= 1
        else:
            self.current_index = len(self.images) - 1

def swiper_carrusel():
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.button(
                    "←",
                    on_click=CarouselState.previous_image,
                    color_scheme="blue",
                ),
                rx.box(
                    rx.image(
                        src=CarouselState.images[CarouselState.current_index],
                        width="300px",
                        height="200px",
                    ),
                    padding="1",
                ),
                rx.button(
                    "→", 
                    on_click=CarouselState.next_image,
                    color_scheme="blue",
                ),
                spacing="1",
            ),
            rx.button(
                "Ver más",
                color_scheme="blue",
                margin_top="1em", 
            ),
            padding="1em",
            background="gray.50",
            border_radius="xl",
            box_shadow="lg",
        )
    )
