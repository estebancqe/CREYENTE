# swiper.py
import reflex as rx

def swiper_component():
    images = [
        {
            "src": "/trabajos_web/cafetera_vertical_cerrado_1080_web.JPG",
            "title": "Cafetera Horizontal"
        },
        {
            "src": "/trabajos_web/cogador_horizontal_1080_web.JPG",
            "title": "Colgador Horizontal"
        },
        {
            "src": "/trabajos_web/escritorio_cerrado_1080_web.JPG",
            "title": "Escritorio Cerrado"
        },
        {
            "src": "/trabajos_web/mueble_sala_horizontal_1080_web.JPG",
            "title": "Mueble Sala"
        },
        {
            "src": "/trabajos_web/estudio_con_homenaje_1080_web.JPG",
            "title": "Estudio con Homenaje" 
        }
    ]
    
    return rx.box(
        rx.box(
            rx.foreach(
                images,
                lambda image: rx.box(
                    rx.box(
                        rx.image(
                            src=image["src"],
                            width="100%",
                            height="100%",
                            object_fit="cover"
                        ),
                        rx.heading(
                            image["title"],
                            color="black",
                            font_size="1.2em",
                            background_color="rgba(255,255,255,0.9)",
                            padding="0.5em",
                            border_radius="0.25em",
                            position="absolute",
                            top="1em",
                            left="1em",
                            z_index="10",
                            box_shadow="0 2px 4px rgba(0,0,0,0.2)"
                        ),
                        position="relative",
                        width="100%",
                        height="100%"
                    ),
                    class_name="swiper-slide"
                )
            ),
            class_name="swiper-wrapper"
        ),
        rx.box(
            rx.text(
                "1/5",
                class_name="mobile-indicator",
                color="black",
                background_color="rgba(255,255,255,0.9)",
                padding="0.5em 1em",
                border_radius="2em",
                position="absolute",    
                bottom="1em",
                right="1em", 
                z_index="10",
                display=["block"]
            )
        ),
        rx.box(class_name="swiper-pagination"),
        rx.box(class_name="swiper-button-next"),
        rx.box(class_name="swiper-button-prev"),
        class_name="swiper-container",
        width="100%",
        position="relative"
    )