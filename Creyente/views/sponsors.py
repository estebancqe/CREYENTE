import reflex as rx
import Creyente.constants as const
from Creyente.estilo.estilo import Size,Spacing
from Creyente.components.title import title
from Creyente.components.link_sponsor import link_sponsor
from Creyente.components.link_button import link_button
from Creyente.estilo.colors import TextColor


def sponsors() -> rx.Component:
    return rx.vstack(
        title("Ubicación"),
      
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
          ),
      
        width="100%",
        align_items="start",
        spacing=Spacing.DEFAULT.value
    )
    
# def sponsors() -> rx.Component:
#     return rx.vstack(
#         title("Ubicacion"),
#           rx.flex(
#                link_sponsor(
#                     "/AvatarC.png",
#                     const.CARPINTERIA, 
#                     "Avatar"        
#                ),
#                link_sponsor(
#                     "/logocrebla.png",
#                     const.CARPINTERIA, 
#                     "simbolo de carpinteria"
#                ),
#                spacing=Spacing.BIG.value,
#                flex_direction=["column", "row"]

#           ),
#         width="100%",
#         align_items="start",
#         spacing=Spacing.DEFAULT.value
#     )