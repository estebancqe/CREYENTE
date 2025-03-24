import reflex as rx
from Creyente.prueba_componentes.muestra_mueble.informacion_mueble import informacion_mueble

class ImageViewerState(rx.State):
    selected_image: str = "/trabajos_web/cafetera_horizontal_1080_web.JPG"
    image_list: list[str] = [
        "/trabajos_web/cafetera_horizontal_1080_web.JPG",
        "/trabajos_web/cogador_horizontal_1080_web.JPG",
        "/trabajos_web/escritorio_cerrado_1080_web.JPG",
        "/trabajos_web/mueble_sala_horizontal_1080_web.JPG",
        "/trabajos_web/estudio_con_homenaje_1080_web.JPG",
    ]
    
    def select_image(self, image: str):
        self.selected_image = image

def mueble_explicacion():
    return rx.container(
        rx.hstack(
            rx.vstack(
                rx.box(
                    rx.image(
                        src=ImageViewerState.selected_image,
                        width="100%",
                        height=rx.breakpoints(
                            initial="300px",
                            sm="400px",
                            lg="500px"
                        ),
                        object_fit="contain",
                        display="block",
                        margin="0",
                        padding="0"
                    ),
                    height="fit-content",
                    width="100%",
                    padding="0",
                    margin="0"
                ),
                rx.scroll_area(
                    rx.hstack(
                        rx.foreach(
                            ImageViewerState.image_list,
                            lambda img: rx.image(
                                src=img,
                                height=rx.breakpoints(
                                    initial="60px",
                                    sm="80px",
                                    lg="100px"
                                ),
                                width="auto",
                                object_fit="contain",
                                cursor="pointer",
                                on_click=lambda: ImageViewerState.select_image(img),
                                display="block",
                                margin="0",
                                padding="0"
                            )
                        ),
                        spacing="1",
                        align_items="center",
                        justify_content="flex-start",
                        width="100%",
                        padding="0",
                        margin="0"
                    ),
                    type="always",
                    scrollbars="horizontal",
                    width="100%",
                    padding="0",
                    margin="0"
                ),
                width="50%",
                spacing="0",
                padding="0",
                margin="0",
                align_items="stretch",
                justify_content="flex-start"
            ),
            rx.box(
                informacion_mueble(),
                width="50%",
                padding="0",
                margin="0"
            ),
            width="100%",
            spacing="1",
            align_items="flex-start",
            justify_content="space-between"
        ),
        max_width="1200px",
        padding="1",
        margin="0 auto"
    )