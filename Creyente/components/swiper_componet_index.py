import reflex as rx

def swiper_component_index():
    return rx.container(
        rx.box(
            rx.box(
                rx.box(
                    rx.box(
                        class_name="swiper-container",
                        children=[
                            rx.box(
                                class_name="swiper-wrapper",
                                children=[
                                    rx.box(
                                        rx.image(
                                            src="/trabajos_web/cafetera_vertical_cerrado_1080_web.JPG",
                                            class_name="css-ducv57"
                                        ),
                                        rx.heading(
                                            "Cafetera Horizontal",
                                            size="6",
                                            class_name="css-4a056u"
                                        ),
                                        class_name="swiper-slide"
                                    ),
                                    rx.box(
                                        rx.image(
                                            src="/trabajos_web/cogador_horizontal_1080_web.JPG",
                                            class_name="css-ducv57"
                                        ),
                                        rx.heading(
                                            "Colgador Horizontal",
                                            size="6",
                                            class_name="css-1h6fk0o"
                                        ),
                                        class_name="swiper-slide"
                                    )
                                ]
                            ),
                            rx.box(
                                rx.text(
                                    "1/5",
                                    class_name="mobile-indicator"
                                )
                            ),
                            rx.box(class_name="swiper-pagination"),
                            rx.box(class_name="swiper-button-next"),
                            rx.box(class_name="swiper-button-prev")
                        ]
                    )
                )
            )
        ),
        size="3",
        class_name="css-p9nijr"
    )