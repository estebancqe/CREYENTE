import reflex as rx
from Creyente.swiper.carousel_state import CarouselState1

def carousel_container():
    return rx.vstack(
        rx.image(
            src=CarouselState1.images[CarouselState1.current_image],
            width="100%",
            height="auto",
        ),
        rx.hstack(
            rx.button(
                "Anterior",
                on_click=CarouselState1.prev_image,
                color_scheme="gray",
            ),
            rx.button(
                "Siguiente",
                on_click=CarouselState1.next_image,
                color_scheme="gray", 
            ),
            spacing="3",
            justify="end",
        ),
        width="100%",
        spacing="4",
    )