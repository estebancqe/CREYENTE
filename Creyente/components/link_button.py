import reflex as rx
import Creyente.style.style as styles
from Creyente.style.style import Size, Spacing, TextColor, Color

def link_button(title: str,
                body: str,
                image: str,
                url: str,
                is_external=True,
                highlight_color=None,
                animated=False) -> rx.Component:


    animation_class = styles.BOUNCEIN_ANIMATION if animated else ""
    return rx.link(
        rx.box(
            rx.hstack(
                rx.image(
                    src=image,
                    width=Size.LARGE.value,
                    height=Size.LARGE.value,
                    margin=Size.MEDIUM.value,
                    alt=title
                ),
                rx.vstack(
                    rx.text(
                        title,
                        size=Spacing.LARGE.value,
                        style=styles.button_title_style
                    ),
                    rx.text(
                        body,
                        size=Spacing.SMALL.value,
                        style=styles.button_body_style
                    ),
                    align_items="start",
                    spacing=Spacing.VERY_SMALL.value,
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value
                ),
                width=("100%"),
            ),
            # Estilos del botón
            height=["100%", "auto"],
            padding=Size.SMALL.value,
            border_radius=Size.DEFAULT.value,
            color=TextColor.HEADER.value,
            background_color=Color.CONTENT.value,
            white_space="normal",
            text_align="center",
            cursor="pointer",
            #borde adicional
            border=f"{'2px' if highlight_color != None else '0px'} solid {highlight_color}",
            #clase de animacion
            class_name=animation_class,
            # Hover effect
            _hover={
                "background_color": Color.SECONDARY.value
            }
        ),
        href=url,
        is_external=is_external,
        width=["100%", "100%", "48%"],
        text_decoration="none",
    )