#index_links.py 
import reflex as rx
import Creyente.constants as const
import Creyente.style.style as style
from Creyente.components.imagen_simple_index import imagen_muestra_index
from Creyente.routes import Route
from Creyente.components.link_button import link_button
from Creyente.components.title import title
from Creyente.swiper.swipe_component import swiper_component
from Creyente.swiper.swiper_pedido import swiper_pedido
from Creyente.swiper.swiper_state import SwiperState 
from Creyente.style.style import Color, Spacing


def index_links() -> rx.Component:
    return rx.vstack(
        

        title("NUESTROS PRODUCTOS"),
        rx.grid(
            swiper_component (), 
            width="100%",
            margin_y="4"
        ),

        # title("POR QUE ELEGIRNOS"),
        # rx.grid(
        #     swiper_pedido(),
        #     width="100%",
        #     margin_y="4"
        # ),

        title("SOCIAL MEDIA"),
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
            
            spacing="2",
            width="100%",
            flex_direction=["column", "column", "row"],
            align="center",
            justify="between"
        ),

        rx.flex(
            link_button(
                "X",
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
            flex_direction=["column", "column", "row"],
            align="center",
            justify="between"
        ),
        
        # title("Cátalogo De Materiales"),
        # rx.flex(
        #     link_button(
        #         "Catalago de Materiales",
        #         "Consulta los diferentes colores que puedes elegir",
        #         "/icons/book-solid.svg",
        #         Route.MELAMINA.value,
        #         False,
        #         Color.GRIS.value
        #     ),
            # link_button(
            #     "Cotizacion",
            #     "cotizacion tu Productos",
            #     "/icons/book-solid.svg",
            #     Route.COTIZAR.value,
            #     False,
            #     Color.GRIS.value
            # ),
        #     spacing="2",    
        #     width="100%",
        #     flex_direction=["column", "column", "row"],
        #     align="center",
        #     justify="center"
        # ),
        
        title("Crea lo que Siempre has Soñado"),

        rx.flex(
            rx.grid(
                imagen_muestra_index(
                    "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/fotos%20trabajos%20web/mueble_cocina_electrodomesticos_copy.JPG",
                    "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/fotos%20trabajos%20web/imagenes%20completas%20full%20definicion/mueble_cocina_electrodomesticos.JPG",
                ),
                imagen_muestra_index(
                    "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/fotos%20trabajos%20web/mueble_armario%20copy.JPG",
                    "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/fotos%20trabajos%20web/imagenes%20completas%20full%20definicion/mueble_armario.JPG",
                ),
                imagen_muestra_index(
                    "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/fotos%20trabajos%20web/cafetera_vertical_cerrado%20copy.JPG",
                    "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/fotos%20trabajos%20web/imagenes%20completas%20full%20definicion/cafetera_vertical_cerrado.JPG",
                ),
                imagen_muestra_index(
                    "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/fotos%20trabajos%20web/mueble_sala_vertical%20copy.JPG",
                    "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/fotos%20trabajos%20web/imagenes%20completas%20full%20definicion/mueble_sala_vertical.JPG",
                ),
                gap="1rem",
                grid_template_columns=[
                    "1fr",  # móvil: 1 columna
                    "repeat(2, 1fr)",  # tablet/desktop: 2 columnas
                ],
                align="center",
                justify="center",   
            ),
            width="100%",
            spacing="2",
            justify="center",
            align="center",
        ),
        
        title("Contacto"),

        rx.vstack(
            link_button(
            "WhatsApp",
            "respuesta rápida y de preferencia",
            "/icons/whatsapp.svg",
            const.WHATSAPP
            ),
            link_button(
                "Email",
                const.EMAIL,
                "/icons/email.svg",
                f"mailto:{const.EMAIL}"
            ),
            width="100%",
            align="center",
            justify="center",
        ),
        width="100%",
        spacing=Spacing.DEFAULT.value,
    )   