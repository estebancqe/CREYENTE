import reflex as rx
import Creyente.constants as const
from Creyente.components.newsletter import newsletter 
# from Creyente.routes import Route
from Creyente.components.link_button import link_button
from Creyente.components.title import title
from Creyente.estilo.estilo import Spacing
# from Creyente.state.PageState import PageState


def index_links() -> rx.Component:
    return rx.vstack(
        title("SOCIAL MEDIA"),
        link_button(
            "Facebook",
            """Madera y Melamina: Donde la Creatividad Encuentra su Hogar.""",
            "/icons/facebook.svg",
            const.FACEBOOK
        ),
        link_button(
            "Instagram",
            """Diseño en Madera: Crea Tu Espacio Perfecto con Nosotros.""",
            "/icons/instagram.svg",
            const.INSTAGRAM
            ),
        link_button(
            "Youtube",
            """Estilo Personalizado, Calidad Artesanal: Nuestro Compromiso.""",
            "/icons/youtube.svg",
            const.YOUTUBE
            ),
        link_button(
            "Tik-Tok",
            """Tu Visión, Nuestra Creación: Experiencia en Madera y Melamina.""",
            "/icons/linkedin.svg",
            const.LINKEDLINK
            ),
        
        # title("Cátalogo De Materiales"),
        #  link_button(
        #     "Catalago de Materiales",
        #     "Consulta los diferentes colores que puedes elegir",
        #     "/icons/book-solid.svg",
        #     Route.COURSES.value,
        #     False,
        #     Color.PURPLE.value
        # ),
        # link_button(
        #     "Cotizacion",
        #     "cotizacion tu Productos",
        #     "/icons/book-solid.svg",
        #     Route.COTIZAR.value,
        #     False,
        #     Color.PRO.value
        # ),
        title("Cátalogo"),
        link_button(
            "Maderas Personalisadas",
            """Madera: Transformando Ideas en Realidad.""",
            "/icons/madera1.svg",
            const.MADERA_PERSONALIZADA
        ),
        link_button(
            "Tablas de Picar",
            """Tablas de Picar: Elegancia y Funcionalidad en Cada Corte.""",
            "/icons/madera2.svg",
            const.TABLA_PICAR
        ),
        link_button(
            "Muebles Personalizados",
            """Hecho para Ti: Muebles que Cuentan tu Historia.""",
            "/icons/madera3.svg",
            const.MUEBLES_PERSONLAZADOS
            ),
        link_button(
            "Amoblado de Áreas Específicas",
            """Amoblado a tu Medida, Espacios con Propósito.""",
            "/icons/madera4.svg",
            const.AMOBLADO_AREA
            ),
        
        title("Contacto"),
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
            
        # title("Newsletter"),
        # newsletter(),   
        width="100%",
        spacing=Spacing.DEFAULT.value,
        # on_mount=PageState.featured_links
    )   