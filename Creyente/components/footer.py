import reflex as rx
import datetime
import Creyente.constants as const
from Creyente.estilo.estilo import Size, Spacing
from Creyente.estilo.colors import Color
from Creyente.routes import Route
from Creyente.components.link_icon import link_icon
from Creyente.components.title import title

def footer() -> rx.Component:
    return rx.box(
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
                            spacing=Spacing.ZERO.value,  # Ajustado
                        ),
                        padding_top=Size.SMALL.value,  # Ajustado
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
                        initial=Spacing.LARGE.value,  # Ajustado
                        sm=Spacing.LARGE.value
                    ),
                    padding_top=Size.ZERO.value,  # Ajustado
                    display=rx.breakpoints(
                        initial="flex",
                        sm="flex"
                    ),
                ),
                flex_direction=["column", "row"],
                spacing=Spacing.LARGE.value,  # Ajustado
                spacing_y=Spacing.DEFAULT.value,  # Ajustado
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
            justify="between",
            align_items="center",
            padding=rx.breakpoints(
                initial="1em",
            ),
            padding_y=Size.MEDIUM_BIG.value,
            bg=Color.CONTENT.value,
            gap=rx.breakpoints(
                initial="2em",
                sm="0"
            ),
        ),
        width="100%",
        margin="0 auto",
    )