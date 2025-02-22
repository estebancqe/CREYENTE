import reflex as rx
import Creyente.constants as const
from Creyente.estilo.estilo import Size,Spacing
from Creyente.components.title import title
from Creyente.components.link_sponsor import link_sponsor
from Creyente.components.link_button import link_button
from Creyente.estilo.colors import Color


def sponsors() -> rx.Component:
    return rx.vstack(

        rx.box(
            title("Donde nos puesdes encontrar ?"),
            class_name="animate__animated animate__fadeIn"
        ),
        rx.box(
            rx.heading(
                "Latacunga",
                color=Color.CONTENT.value
            ),
            class_name="animate__animated animate__fadeIn animate__delay-1s"
        ),
        title("Donde nos puesdes encontrar ?"),
        rx.heading(
            "Latacunga",
            color=Color.CONTENT.value,
            class_name="animate__animated animate__jello animate__duration-2s"
        ),
        rx.heading(
            "Ibarra",
            color=Color.CONTENT.value
        ),
        rx.vstack(
            rx.button(
                text=("Ibarra"),
                # text=("Av. beltran frente al campamento Panavial  San Antonio"),
                image=("/icons/location.svg"),
                src=const.UBI_IBARRA
            ),
                rx.button(
                text=("Ibarra"),
                # text=("Av. beltran frente al campamento Panavial  San Antonio"),
                image=("/icons/location.svg"),
                src=const.UBI_IBARRA
            ),
            width="100%",
            align="center",
            justify="center",
        ),
        width="100%",
        align_items="center",
        spacing=Spacing.DEFAULT.value
    )