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
        rx.container(
            rx.hstack(
                rx.box(
                    rx.image(
                        src=image,
                        width="auto",    
                        height=rx.breakpoints(
                            initial="25px",
                            sm="40px",
                            lg="40px"
                        ),
                        alt=title,
                    ),
                    padding=Size.DEFAULT.value,
                    display="flex",
                    align="center", 
                    justify="center",
                    min_width="40px",  # Ancho mínimo fijo
                    flex_shrink="0",   # Evita que la imagen se encoja
                ),
                rx.vstack(
                    rx.text(
                        title,
                        size=rx.breakpoints(
                            initial="3",
                            sm="4", 
                            lg="5"
                        ),
                        style=styles.button_title_style,
                        text_align="center",
                        width="100%"
                    ),
                    rx.text(
                        body,
                        size=Spacing.SMALL.value,
                        style=styles.button_body_style,
                        text_align="center",
                        width="100%"
                    ),
                    width="auto",      # Ancho automático
                    flex_grow="1",     # Permite crecer para llenar espacio
                    spacing=Spacing.VERY_SMALL.value,
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value,
                    align_items="stretch",
                ),
                width="100%",
                spacing="4",
                align="center",
                flex_wrap="nowrap",    # Evita el wrapping dentro del hstack
            ),
            padding=Size.SMALL.value,
            border_radius=Size.DEFAULT.value,
            color=TextColor.HEADER.value,
            background_color=Color.CONTENT.value,
            white_space="normal",
            cursor="pointer",
            border=f"{'2px' if highlight_color != None else '0px'} solid {highlight_color}",
            class_name=animation_class,
            _hover={
                "background_color": Color.SECONDARY.value
            },
            width="100%",
            display="flex",           # Asegura comportamiento flex
            flex_direction="row",     # Dirección horizontal
        ),
        href=url,
        is_external=is_external,
        width=rx.breakpoints(
            initial="100%",
            sm="100%",
            lg="48%"
        ),
        text_decoration="none",
        display="flex",              # Asegura comportamiento flex
    )