import reflex as rx
import Creyente.constants as const
import Creyente.style.style as styles
from Creyente.pages.index import index
from Creyente.pages.melamina import melamina
from Creyente.pages.cotizar import cotizar
from Creyente.pages.historia import historia
from Creyente.pages.mision import mision
from Creyente.pages.trabajos import trabajos
from Creyente.pages.prueba import prueba
from Creyente.api.api import repo,api_Muebles,api_Modelos

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(
            src=f"https://www.googletagmanager.com/gtag/js?id={const.G_TAG}"),
        rx.script(
            f"""
            window.dataLayer = window.dataLayer || [];
            function gtag(){{dataLayer.push(arguments);}}
            gtag('js', new Date());
            gtag('config', '{const.G_TAG}');
            """
        ),
    ],
)

app.api.add_api_route("/repo", repo)
app.api.add_api_route("/api_Muebles",api_Muebles)
app.api.add_api_route("/api_Modelos",api_Modelos)