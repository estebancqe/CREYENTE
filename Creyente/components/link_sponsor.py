import reflex as rx
from Creyente.style.style import Size

def link_sponsor(imagen: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=imagen,
            width=Size.LARGE.value,
            height=Size.LARGE.value,
        ),
        href=url,
        is_external=True
    )