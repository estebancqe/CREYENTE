import reflex as rx
import Creyente.estilo.estilo as styles
from Creyente.estilo.estilo import Size, Spacing, Color
from Creyente.model.Featured import Featured



def featured_link(pepito: Featured) -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.image(
                src=pepito.image,
                border_radius=Size.DEFAULT.value,
                background=Color.CONTENT.value,
                width="100%",
                height="auto",
                alt=f"Imagen destacada para: {pepito.title}"
            ),
            rx.text(
                pepito.title,
                size=Spacing.VERY_SMALL.value,
                style=styles.button_body_style
            ),
            spacing=Spacing.SMALL.value,
            align_items="start",
            class_name=styles.FADEIN_ANIMATION
        ),
        href=pepito.url,
        is_external=True
    )