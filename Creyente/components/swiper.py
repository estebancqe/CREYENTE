# swiper.py
import reflex as rx

def swiper_component():
    images = [
        "/trabajos_web/cafetera_horizontal_1080_web.JPG",
        "/trabajos_web/cogador_horizontal_1080_web.JPG", 
        "/trabajos_web/escritorio_cerrado_1080_web.JPG",
        "/trabajos_web/mueble_sala_horizontal_1080_web.JPG",
        "/trabajos_web/estudio_con_homenaje_1080_web.JPG",
    ]
    
    return rx.box(
        rx.box(
            rx.foreach(
                images,
                lambda image: rx.box(
                    rx.image(
                        src=image,
                        width="100%",
                        height="auto",
                        object_fit="cover"
                    ),
                    class_name="swiper-slide"
                )
            ),
            class_name="swiper-wrapper"
        ),
        rx.box(class_name="swiper-pagination"),
        rx.box(class_name="swiper-button-next"),
        rx.box(class_name="swiper-button-prev"),
        class_name="swiper-container",
        width="100%"
    )