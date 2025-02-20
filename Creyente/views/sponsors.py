import reflex as rx
import Creyente.constants as const
from Creyente.estilo.estilo import Size,Spacing
from Creyente.components.title import title
from Creyente.components.link_sponsor import link_sponsor
from Creyente.components.link_button import link_button
from Creyente.estilo.colors import Color


def sponsors() -> rx.Component:
    return rx.vstack(
        title("Donde nos puesdes encontrar ?"),
        rx.heading(
            "Latacunga",
            color=Color.CONTENT.value
        ),
        rx.heading(
            "Ibarra",
            color=Color.CONTENT.value
        ),
          rx.vstack(
            link_button(
                "Ibarra",
                "Av. beltran frente al campamento Panavial  San Antonio",
                "/icons/location.svg",
                const.UBI_IBARRA
            ),
                link_button(
                "Latacunga",
                "Urb. Estrella de la Mañana",
                "/icons/location.svg",
                const.UBI_LATA
            ),
            width="100%",
            align="center",
            justify="center",
          ),
          width="100%",
          align_items="center",
          spacing=Spacing.DEFAULT.value
    )