import reflex as rx
import Creyente.style.style as styles


def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        style=styles.title_style,
        color=styles.Color.CONTENT.value
    )