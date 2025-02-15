import reflex as rx
from Creyente.estilo.colors import Color
from Creyente.estilo.estilo import Size

class bannerState(rx.ComponentState):
    contador: int
    imagenes: list[str] = [
        "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/cafetera_horizontal_trabajo.JPG",
        "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/cafetera_vertical_cerrado_trabajo.JPG", 
        "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/cafetera_vertical_abierto_trabajo.JPG"
    ]

    def avanzar(self):
        self.contador = (self.contador+1) % len(self.imagenes)

    def retroceder(self):
        self.contador = (self.contador-1) % len(self.imagenes)

    @rx.var
    def bannerstr(self) -> str:
        return self.imagenes[self.contador]

    @classmethod
    def get_component(cls, titulo: str = "", **props) -> rx.Component:
        return rx.vstack(
            rx.heading(
                titulo,
                color=Color.CONTENT.value
            ) 
        if titulo else None,
            rx.hstack(
                rx.image(
                    "/icons/angulo-izquierdo.png", 
                    on_click=cls.avanzar,
                    sizes=Size.DEFAULT.value,
                ),
                rx.image(
                    src=cls.bannerstr, 
                    width="auto", 
                    height="500px",
                    
                ),
                rx.image(
                    "/icons/angulo-derecho.png", 
                    on_click=cls.retroceder,
                    sizes=Size.DEFAULT.value,
                ),
                width="100%",
                align="center",      # Alineación vertical
                justify="center",    # Alineación horizontal
                spacing="4", 
            ),
            width="100%",
            justify="center",
            alinght="center",
            spacing="4"  
        )

img = bannerState.create

def carrusel() -> rx.Component:
    return rx.vstack(
        # First carousel
        img(titulo="Cafete"),
        rx.divider(),  # Adds a line between carousels
        # Second carousel
        img(
            titulo="Carrusel 2",
            imagenes=[
                "/CREYENTE_circular.png",
                "/CREYENTE.png", 
                "/logo_creyente_mami.jpeg"
            ]
        ),
        rx.divider(),
        # Third carousel
        img(
            titulo="Carrusel 3",
            imagenes=[
                "/CREYENTE_circular.png",
                "/CREYENTE.png", 
                "/logo_creyente_mami.jpeg"
            ]
        ),
        width="100%",
        spacing="4",  # Adds vertical spacing between all items in vstack
    )