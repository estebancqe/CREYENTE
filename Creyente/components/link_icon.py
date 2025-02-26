import reflex as rx
from Creyente.style.style import Size

def link_icon(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width="auto",
            height=[Size.DEFAULT.value,Size.MEDIUM_BIG.value],
            alt=alt
        ),
        href=url,
        is_external=True
    )