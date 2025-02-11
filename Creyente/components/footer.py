import reflex as rx
import datetime
import Creyente.constants as const
from Creyente.estilo.estilo import Size, Spacing
from Creyente.estilo.colors import Color

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/logocrebla.png",    #alto del logo
            width=Size.SUPER_VERY_BIG.value,   #ancho del logo
            alt="logotipo de la marca",  #esto es para personas ividentes
        ),
        rx.link(
            rx.box(
                f"2020-{datetime.date.today().year} ",
                rx.text(
                    "trabajo con excelencia",
                    as_="span",
                    color=Color.BACKGROUND.value,
                    size=Spacing.DEFAULT.value,
                ),
                " Creyente.",
                padding_top=Size.DEFAULT.value,
                color=Color.BACKGROUND.value,
                size=Spacing.DEFAULT.value,
            ),
            href=const.CATALOGO,
            is_external=True,
            font_size=Size.DEFAULT.value
        ),
        rx.link(
            rx.hstack(
                rx.text(
                    "Innovación en Madera: Inspirando Espacios, Creando Historias para ti.",
                    font_size=Size.DEFAULT.value,
                    margin_top=Size.ZERO.value
                ),
                color=Color.BACKGROUND.value,
            ),
            href=const.CATALOGO,
            is_external=True
        ),
        width="100%",
        align="center",
        margin_bottom=Size.DEFAULT.value,
        padding_bottom=Size.DEFAULT.value,
        padding_x=Size.BIG.value,
        spacing=Spacing.ZERO.value,
        bg=Color.CONTENT.value,
    )