import reflex as rx
import datetime
import Creyente.constants as const
from Creyente.style.style import Size,Spacing
from Creyente.style.colors import Color, TextColor
from Creyente.components.link_icon import link_icon
from Creyente.components.info_text import info_text
from Creyente.components.link_button import link_button
from Creyente.state.PageState import PageState


def header(details=True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            # rx.image(
            #     src="/CREYENTE.png",
            #     width="300px",
            #     aling="center",
            # ),
            rx.vstack(
                rx.heading(
                    "CREYENTE",
                    size=Spacing.VERY_BIG.value,
                    color=Color.CONTENT.value,
                ),
                rx.text(
                    "Diseño de muebles y mas",
                    margin_top=Size.ZERO.value,
                    color=Color.BLACK.value,
                    size=Spacing.BIG.value,
                ),
                padding=Size.SMALL.value
            ),

            flex_direction=["column", "row"],
            align="center",
            justify="center",
            spacing=Spacing.VERY_BIG.value,
            width="100%",
        ),
        rx.image(
            src="https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/1080_web/cogador_horizontal_1080_web.JPG",
            height="auto"
        ),
        
        spacing=Spacing.BIG.value,
        width=["100%","auto"],
    ),
    
def experience() -> int:
    return datetime.date.today().year - 2020
    