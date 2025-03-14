import reflex as rx
from Creyente.prueba_componentes.muestra_mueble.informacion_mueble import informacion_mueble

class ImageViewerState(rx.State):
    selected_image: str = "/trabajos_web/cafetera_horizontal_1080_web.JPG"  # Imagen por defecto
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
            # Usando vstack en lugar de box para mejor control del espaciado
            rx.vstack(
                rx.image(
                    src=ImageViewerState.selected_image,
                    width="100%",
                    height=rx.breakpoints(
                        initial="300px",
                        sm="400px",
                        lg="500px"
                    ),
                    object_fit="contain"
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
                                on_click=lambda: ImageViewerState.select_image(img)
                            )
                        ),
                        spacing="1",
                    ),
                    type="always",
                    scrollbars="horizontal",
                    width="100%",
                ),
                width="50%",
                spacing="0",  # Elimina el espacio entre elementos
                padding="0",  # Elimina el padding interno
            ),
            rx.box(
                informacion_mueble(),
                width="50%",
            ),
            width="100%",
            spacing="1",
        ),
        max_width="1200px",
        padding="1",
    )