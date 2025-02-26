import reflex as rx
from Creyente.components.link_material import link_material
from Creyente.components.title import title
from Creyente.style.style import Spacing, Size


def color_melamina() -> rx.Component:
    return rx.vstack(
        title("Melamina en Diferentes Colores"),
        rx.grid(
            link_material(
            "Agave",
            "dimension 2.12 x 2.44 m",
            "/material/Agave.jpg"
        ),
        link_material(
            "Arupo",
            "dimension 2.12 x 2.44 m",
            "/material/Arupo.jpg"
        ),
        link_material(
            "Bardolino",
            "dimension 2.12 x 2.44 m",
            "/material/Bardolino.jpg"
        ),
        link_material(
            "Fumé",
            "dimension 2.12 x 2.44 m",
            "/material/Fumé.jpg"
        ),
        link_material(
            "Milán",
            "dimension 2.12 x 2.44 m",
            "/material/Milán.jpg"
        ),
        link_material(
            "Nazca",
            "dimension 2.12 x 2.44 m",
            "/material/Nazca.jpg"
        ),
        link_material(
            "Panela",
            "dimension 2.12 x 2.44 m",
            "/material/Panela.jpg"
        ),
        link_material(
            "Tivoli",
            "dimension 2.12 x 2.44 m",
            "/material/Tivoli.jpg"
        ),
        link_material(
            "Toquilla",
            "dimension 2.12 x 2.44 m",
            "/material/Toquilla.jpg"
        ),
        flex_direction=["column", "row"],
        columns=rx.breakpoints(
            initial="1",
            sm="3", 
            # lg="3"
        ),
        align="center",
        justify="center",
        width="auto",
        spacing=Spacing.LARGE.value,
        padding_top=Size.ZERO.value,
        class_name="animate__animated animate__bounce animate__delay-1s"
        ),
        width="100%",
        align="center",
        justify="center",
        spacing=Spacing.VERY_BIG.value,
    )