import reflex as rx
from reflex.components.component import NoSSRComponent

# Definición de los componentes
class Swiper(NoSSRComponent):
    """Swiper component."""
    library = "swiper@10.3.1"  # Especificamos una versión estable
    tag = "Swiper"
    is_default = True
    
    # Modificamos las dependencias
    lib_dependencies: list[str] = ["swiper@10.3.1"]
    
    slides_per_view: rx.Var[int]
    space_between: rx.Var[int]
    navigation: rx.Var[bool]
    pagination: rx.Var[dict]

    def add_imports(self):
        return {
            "": ["swiper/css", "swiper/css/navigation", "swiper/css/pagination"]
        }

class SwiperSlide(NoSSRComponent):
    """SwiperSlide component."""
    library = "swiper"
    tag = "SwiperSlide"
    is_default = True

# Funciones de componentes
def create_carousel(images: list[str]) -> rx.Component:
    return rx.box(
        Swiper.create(
            *[SwiperSlide.create(rx.image(src=img, width="100%")) for img in images],
            slides_per_view=3,
            space_between=20,
            navigation=True,
            pagination={"clickable": True}
        )
    )

def carrusel():
    """Página principal"""
    image_sets = [
        ["/CREYENTE_circular.png"] * 3,
        ["/CREYENTE_circular.png"] * 3,
        ["/CREYENTE_circular.png"] * 3,
        ["/CREYENTE_circular.png"] * 3,
        ["/CREYENTE_circular.png"] * 3,
    ]
    
    return rx.vstack(
        *[create_carousel(images) for images in image_sets],
        spacing="4"
    )

# Configuración de la app
