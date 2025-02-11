import reflex as rx
import Creyente.estilo.estilo as styles
from Creyente.estilo.estilo import Color

def link_navbar(title:str,url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.text(
            title,
            color=Color.BACKGROUND.value,
        ),
        width=["100%", "auto"],
        style=styles.navbar_title_style,
        href=url,
    )