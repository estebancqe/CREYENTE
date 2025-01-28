import reflex as rx
import Creyente.estilo.estilo as styles
from Creyente.routes import Route
from Creyente.estilo.estilo import Size
from Creyente.estilo.colors import Color


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                rx.text("Crey", as_="span", color=Color.PRIMARY.value),
                rx.text("ente", as_="span", color=Color.SECONDARY.value),
                style=styles.navbar_title_style
            ),
            href=Route.INDEX.value
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )