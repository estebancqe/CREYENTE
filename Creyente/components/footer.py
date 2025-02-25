import reflex as rx
import datetime
import Creyente.constants as const
from Creyente.estilo.estilo import Size, Spacing
from Creyente.estilo.colors import Color
from Creyente.routes import Route
from Creyente.components.link_icon import link_icon
from Creyente.components.title import title

def footer() -> rx.Component:
    return rx.box(  # Contenedor exterior
        rx.container(
            rx.box(
                rx.flex(
                    # Logo + Slogan
                    rx.vstack(
                        rx.image(
                            src="/logocrebla.png",
                            width="auto",
                            height=rx.breakpoints(
                                initial="100px",    
                                sm="120px",         
                                lg="140px"          
                            ),
                            alt="logotipo de la marca",
                            object_fit="contain",
                        ),
                        rx.text(
                            "Tu estilo en madera.",
                            font_size=rx.breakpoints(
                                initial="1.2em",     
                                sm="1em"            
                            ),
                            margin_top=Size.ZERO.value,
                            color=Color.BACKGROUND.value,
                        ),
                        spacing="1",
                        align_items="start",
                        width="auto",
                    ),
                    
                    # Sección central con fecha e iconos
                    rx.vstack(
                        rx.hstack(
                            rx.text(
                                "Trabajando del",
                                as_="span", 
                                color=Color.BACKGROUND.value,
                                font_size=rx.breakpoints(
                                    initial="1.1em",    
                                    sm=Size.DEFAULT.value
                                ),
                            ),
                            rx.text(
                                f"2020 al -{datetime.date.today().year}",
                                color=Color.BACKGROUND.value,
                                font_size=rx.breakpoints(
                                    initial="1.1em",    
                                    sm=Size.DEFAULT.value
                                ),
                            ),
                            spacing="3",
                        ),
                        
                        rx.flex(
                            link_icon("/icons/instagram.svg", const.INSTAGRAM, "email@email.com"),
                            link_icon("/icons/facebook.svg", const.FACEBOOK, "facebook"),
                            link_icon("/icons/book-solid.svg", const.CATALOGO, "catalogo"),
                            link_icon("/icons/whatsapp.svg", const.WHATSAPP, "whatsapp"),
                            gap=rx.breakpoints(
                                initial="1.3em",    
                                sm="2em"
                            ),
                            padding_top=rx.breakpoints(
                                initial="0.5em",    
                                sm=Size.SMALL.value
                            ),
                            display="flex",
                            justify_content="center",
                            flex_wrap="wrap",
                        ),
                        align_items="center",
                        spacing="2",
                    ),
                    
                    # Location
                    rx.link(
                        rx.vstack(
                            rx.heading(
                                "Ubicacion",
                                font_size=rx.breakpoints(
                                    initial="1.3em",    
                                    sm=Size.MEDIUM_LARGE.value
                                ),
                                margin_top=Size.ZERO.value
                            ),
                            rx.text(
                                "Latacunga",
                                font_size=rx.breakpoints(
                                    initial="1.1em",    
                                    sm=Size.DEFAULT.value
                                ),
                                margin_top=Size.ZERO.value
                            ),
                            rx.text(
                                "Ibarra",
                                font_size=rx.breakpoints(
                                    initial="1.1em",    
                                    sm=Size.DEFAULT.value
                                ),
                                margin_top=Size.ZERO.value
                            ),
                            color=Color.BACKGROUND.value,
                            spacing="1",
                            align_items=rx.breakpoints(
                                initial="center",
                                sm="end"
                            ),
                        ),
                        href=Route.TRABAJOS.value,
                        is_external=True,
                    ),

                    width="100%",
                    flex_direction=rx.breakpoints(
                        initial="column",
                        sm="row"
                    ),
                    align_items="center",
                    justify_content=rx.breakpoints(
                        initial="center",
                        sm="space-between"
                    ),
                    padding=rx.breakpoints(
                        initial="0.8em",    
                        sm="2em"
                    ),
                    padding_y=rx.breakpoints(
                        initial="1em",      
                        sm=Size.DEFAULT.value
                    ),
                    gap=rx.breakpoints(
                        initial="1.5em",    
                        sm="1em"
                    ),
                ),
                max_width="1200px",
                margin="0 auto",
                width="100%",
            ),
            size="4",
        ),
        width="100%",
        bg=Color.CONTENT.value,  # Movido el background color aquí
    )