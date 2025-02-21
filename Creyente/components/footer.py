import reflex as rx
import datetime
import Creyente.constants as const
from Creyente.estilo.estilo import Size, Spacing
from Creyente.estilo.colors import Color
from Creyente.routes import Route
from Creyente.components.link_icon import link_icon
from Creyente.components.title import title

def footer() -> rx.Component:
    return rx.container(
        rx.hstack(
            # Logo + Slogan
            rx.vstack(
                rx.image(
                    src="/logocrebla.png",
                    width="auto",
                    height=rx.breakpoints(
                        initial=Size.BIG.value,
                        sm=Size.VERY_BIG.value,
                        lg=Size.SUPER_VERY_BIG.value
                    ),
                    alt="logotipo de la marca",
                ),
                rx.text(
                    "Tu estilo en madera.",
                    font_size=rx.breakpoints(
                        initial=Size.SMALL.value,
                        sm=Size.DEFAULT.value
                    ),
                    margin_top=Size.ZERO.value,
                    color=Color.BACKGROUND.value,
                ),
                spacing=Spacing.ZERO.value,
                align_items="start"
            ),
            
            # Texto de los años + Redes sociales
            rx.vstack(
                rx.link(
                    rx.hstack(
                        rx.vstack(
                            rx.text(
                                "Trabajando del ",
                                as_="span", 
                                color=Color.BACKGROUND.value,
                                font_size=rx.breakpoints(
                                    initial=Size.DEFAULT.value,
                                    sm=Size.DEFAULT.value
                                ),
                            ),
                            f"2020 al -{datetime.date.today().year} ",
                            justify="center",
                            align="center",
                            spacing=Spacing.ZERO.value,
                        ),
                        padding_top=Size.ZERO.value,
                        color=Color.BACKGROUND.value,
                    ),
                    href=const.CATALOGO,
                    is_external=True,
                    font_size=rx.breakpoints(
                        initial=Size.SMALL.value,
                        sm=Size.DEFAULT.value
                    ),
                ),
                
                # Social media icons section
                rx.flex(
                    link_icon("/icons/instagram.svg", const.INSTAGRAM, "email@email.com"),
                    link_icon("/icons/facebook.svg", const.FACEBOOK, "facebook"),
                    link_icon("/icons/book-solid.svg", const.CATALOGO, "catalogo"),
                    link_icon("/icons/whatsapp.svg", const.WHATSAPP, "whatsapp"),
                    spacing=rx.breakpoints(
                        initial=Spacing.DEFAULT.value,
                        sm=Spacing.LARGE.value
                    ),
                    padding_top=Size.SMALL.value,
                    display=rx.breakpoints(
                        initial="flex",
                        sm="flex"
                    ),
                    # flex_direction=rx.breakpoints(
                    #     initial="column",
                    #     sm="row"
                    # ),
                ),
                spacing=Spacing.VERY_SMALL.value,
                align_items="center"
            ),
            
            # Location
            rx.link(
                rx.vstack(
                    rx.heading(
                        "Ubicacion",
                        font_size=rx.breakpoints(
                            initial=Size.DEFAULT.value,
                            sm=Size.MEDIUM_LARGE.value
                        ),
                        margin_top=Size.ZERO.value
                    ),
                    rx.text(
                        "Latacunga",
                        font_size=rx.breakpoints(
                            initial=Size.SMALL.value,
                            sm=Size.DEFAULT.value
                        ),
                        margin_top=Size.ZERO.value
                    ),
                    rx.text(
                        "Ibarra",
                        font_size=rx.breakpoints(
                            initial=Size.SMALL.value,
                            sm=Size.DEFAULT.value
                        ),
                        margin_top=Size.ZERO.value
                    ),
                    color=Color.BACKGROUND.value,
                    spacing=Spacing.ZERO.value,
                    align_items="end"
                ),
                href=Route.TRABAJOS.value,
                is_external=True
            ),

            width="100%",
            justify="between",  # Changed from "space-between" to "between"
            align_items="center",
            padding=rx.breakpoints(
                initial="1em",
                sm="2em",
                lg="3em"
            ),
            bg=Color.CONTENT.value,
            # flex_direction=rx.breakpoints(
            #     # initial="column",
            #     sm="row"
            # ),
            gap=rx.breakpoints(
                initial="2em",
                sm="0"
            )
        ),
        max_width="100%",
        width="100%",
        margin="0 auto",
    )