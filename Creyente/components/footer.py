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
            rx.vstack(
                rx.image(
                    src="/logocrebla.png",
                    width=rx.breakpoints(
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
                spacing_y="0"
            ),
            
            rx.link(
                rx.hstack(
                    rx.vstack(
                        rx.text(
                            "Trabajando del ",
                            as_="span", 
                            color=Color.BACKGROUND.value,
                            size=rx.breakpoints(
                                initial=Spacing.SMALL.value,
                                sm=Spacing.DEFAULT.value
                            ),
                        ),
                        f"2020 al -{datetime.date.today().year} ",
                        justify="center",
                    ),
                    padding_top=Size.DEFAULT.value,
                    color=Color.BACKGROUND.value,
                ),
                href=const.CATALOGO,
                is_external=True,
                font_size=rx.breakpoints(
                    initial=Size.SMALL.value,
                    sm=Size.DEFAULT.value
                ),
                spacing=Spacing.BIG.value
            ),
            
            rx.flex(
                link_icon(
                    "/icons/instagram.svg",
                    const.INSTAGRAM,
                    "email@email.com"
                ),
                link_icon(
                    "/icons/facebook.svg", 
                    const.FACEBOOK,
                    "facebook"
                ),
                link_icon(
                    "/icons/book-solid.svg",
                    const.CATALOGO,
                    "catalogo"
                ),
                link_icon(
                    "/icons/whatsapp.svg",
                    const.WHATSAPP, 
                    "whatssap"
                ),
                spacing=rx.breakpoints(
                    initial=Spacing.DEFAULT.value,
                    sm=Spacing.LARGE.value
                ),
                padding_top=Size.SMALL.value,
                flex_direction=["column", "row", "row"],
            ),
            
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
                ),
                href=Route.TRABAJOS.value,
                is_external=True
            ),
            width="100%",
            flex_direction=["row", "row", "row"],
            align="center",
            justify="between",  # Cambiado de "space-between" a "between"
            gap=rx.breakpoints(
                initial="2",
                sm="4",
                lg="6"
            ),
            padding=rx.breakpoints(
                initial="1em",
                sm="2em",
                lg="3em"
            ),
            bg=Color.CONTENT.value,
        ),
        max_width="1200px",
        width="100%",
        margin="0 auto",
    )