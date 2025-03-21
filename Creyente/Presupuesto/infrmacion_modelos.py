import reflex as rx
import Creyente.style.style as styles
from Creyente.style.style import Size, Spacing, Color
from Creyente.model.MODELOS import MODELOS



def infrmacion_modelos(muestra_modelos: MODELOS) -> rx.Component:
    print(f"Mostrando modelo: {muestra_modelos}")  # Verifica qué datos están llegando

    return rx.link(
        # rx.text(
        #         muestra_modelos.id_muebles,
        #         " este es ",
        #         size=Spacing.VERY_SMALL.value,
        #         style=styles.button_body_style
        #     ),
        
        rx.vstack(
            rx.image(
                muestra_modelos.url_image,
                border_radius=Size.DEFAULT.value,
                background=Color.CONTENT.value,
                width=Size.VERY_BIG.value,
                height="100%",
                alt=f"Imagen destacada para: {muestra_modelos.modelo}"
            ),
            rx.text(
                muestra_modelos.descripcion,
                size=Spacing.VERY_SMALL.value,
                style=styles.button_body_style
            ),
            spacing=Spacing.SMALL.value,
            align_items="start",
            class_name=styles.FADEIN_ANIMATION
        ),
    )