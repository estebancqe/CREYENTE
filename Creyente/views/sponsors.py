import reflex as rx
import Creyente.constants as const
from Creyente.style.style import Size,Spacing
from Creyente.components.title import title
from Creyente.components.link_sponsor import link_sponsor
from Creyente.components.link_button import link_button
from Creyente.style.colors import Color


def sponsors() -> rx.Component:
    return rx.vstack(

        rx.box(
            title("Donde nos puedes encontrar ?"),
            class_name="animate__animated animate__fadeIn"
        ),
        rx.box(
            rx.heading(
                "Latacunga",
                color=Color.CONTENT.value,
                class_name="animate__animated animate__fadeIn animate__delay-1s",
                
            ),     
        ),
        rx.box(
            rx.heading(
            "Ibarra",
            color=Color.CONTENT.value,
            class_name="animate__animated animate__fadeIn animate__delay-2s"
        ),
        ),
        
        
        width="100%",
        align_items="center",
        spacing=Spacing.DEFAULT.value
    )