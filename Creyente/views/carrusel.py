import reflex as rx
from Creyente.estilo.colors import Color

class bannerState(rx.ComponentState):
    contador: int
    imagenes: list[str] = [
        "/CREYENTE_circular.png",
        "/CREYENTE.png", 
        "/logo_creyente_mami.jpeg"
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
                rx.icon_button(
                    "arrow_left", 
                    on_click=cls.avanzar
                ),
                rx.image(
                    src=cls.bannerstr, 
                    width="100px", 
                    height="100px"
                ),
                rx.icon_button(
                    "arrow-right", 
                    on_click=cls.retroceder
                ),
            )
        )

img = bannerState.create

def carrusel() -> rx.Component:
    return rx.vstack(
        # First carousel
        img(titulo="Carrusel 1"),
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
        spacing="4",  # Adds vertical spacing between all items in vstack
    )