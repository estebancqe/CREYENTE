import reflex as rx
import Creyente.estilo.estilo as styles
from Creyente.estilo.estilo import Size, Spacing, Color


def link_material(title: str,
                body: str,
                image: str,
                highlight_color=None,
                ) -> rx.Component:

    return rx.button(
        rx.hstack(
            rx.image(
                src=image,
                width=Size.SUPER_VERY_BIG.value,
                height=Size.SUPER_VERY_BIG.value,
                margin=Size.MEDIUM.value,
                alt=title
            ),
            rx.vstack(
                rx.text(
                    title,
                    size=Spacing.MEDIUM_BIG.value,
                    style=styles.button_title_material_style
                ),
                
                rx.text(
                    body,
                    size=Spacing.VERY_SMALL.value,
                    style=styles.button_title_material_style
                ),
                
                align_items="start",#posicion en el eje de las x del texto
                spacing=Spacing.VERY_SMALL.value,
                padding_y=Size.SMALL.value,
                padding_right=Size.SMALL.value,
            ),
            align="center",#posicion en el eje de las y del texto
            justify="center",#que este en el centro las imagenes
            width="100%"
        ),
        bg=Color.CONTENT.value,
        border=f"{'2px' if highlight_color != None else '0px'} solid {highlight_color}",
        class_name="animate__animated animate__bounce animate__delay-1s",
        
    )