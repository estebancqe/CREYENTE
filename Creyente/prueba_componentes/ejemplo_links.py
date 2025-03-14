import reflex as rx
from Creyente.components.title import title
from Creyente.components.link_button import link_button
import Creyente.constants as const
from Creyente.style.style import Color, Spacing
from Creyente.routes import Route
import Creyente.style.style as style



def ejemplo_links() -> rx.Component:
    return rx.vstack(
        title("SOCIAL MEDIA EXPERIMENTO"),
        rx.flex(
            link_button(
                "Facebook",
                "Clases de dibujo y mas.",
                "/icons/facebook.svg",
                const.FACEBOOK,
            ),
            link_button(
                "Instagram", 
                "Diseño y Arte",
                "/icons/instagram.svg",
                const.INSTAGRAM
            ),
            link_button(
                "Youtube",
                """Clases y tutoriales.""",
                "/icons/youtube.svg",
                const.YOUTUBE
            ),
            link_button(
                "Tik-Tok",
                """Videos cortos y divertidos.""",
                "/icons/linkedin.svg",
                const.LINKEDLINK 
            ),
            
            spacing="2",
            width="100%",
            flex_direction=["column", "row", "row"],
            align="center",
            justify="between",
        ),
        

        title("MODELOS"),
        rx.flex(
            rx.text(
                "CONOCE NUESTROS MODELOS",
                size=Spacing.MEDIUM_BIG.value,
                color=Color.SECOND_TITTLE.value,
                style=style.style_secod_tittle,
            ),
            rx.link(
                rx.image(
                src="https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/fotos%20trabajos%20web/colgador_de_ropa_mami.jpeg",
                width="100%",
                href=Route.PROYECTOS.value,
                ),
                href=Route.PROYECTOS.value,
                justify="end",
            ),
            spacing="4",
            width="100%",
            flex_direction=["column", "column", "row"],
            align="center",
            justify="between"
        ),




    )