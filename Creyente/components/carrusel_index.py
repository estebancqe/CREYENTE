import reflex as rx

# Define el estado para manejar la carga de imágenes y transiciones
class ImageState(rx.State):
    """State for handling image loading and transitions."""
    current_image: str = "/trabajos_web/cafetera_horizontal_1080_web.JPG"
    images: list[str] = [
        "/trabajos_web/cafetera_horizontal_1080_web.JPG",
        "/trabajos_web/cafetera_vertical_cerrado_1080_web.JPG",
        "/trabajos_web/cafetera_vertical_abierto_1080_web_.JPG"
    ]
    current_index: int = 0
    is_loaded: bool = False

    def next_image(self):
        """Change to next image."""
        self.current_index = (self.current_index + 1) % len(self.images)
        self.current_image = self.images[self.current_index]

    def set_loaded(self):
        """Mark image as loaded."""
        self.is_loaded = True

# Componente de imagen con carga diferida
def lazy_image() -> rx.Component:
    """Component for lazy-loaded image."""
    return rx.box(
        rx.image(
            src=ImageState.current_image,
            alt="Collection image",
            loading="lazy",
            width="auto", 
            height="600px",
            border_radius="15px 50px",
            box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
            opacity=1
        ),
        rx.button(
            "Siguiente imagen",
            on_click=ImageState.next_image,
            margin_top="1em"
        ),
        padding="1em",
        border="1px solid #eaeaea",
        border_radius="10px",
        margin="1em"
    )

# Script para manejar la carga de imágenes
def image_script() -> rx.Component:
    """Script component for image loading."""
    return rx.script(
        """
        document.addEventListener("DOMContentLoaded", function() {
            const images = document.querySelectorAll('img');
            images.forEach(img => {
                if (img.complete) {
                    img.classList.add('loaded');
                } else {
                    img.addEventListener('load', function() {
                        img.classList.add('loaded');
                    });
                }
            });
        });
        """
    )

# Componente principal que combina imagen y script
def producto() -> rx.Component:
    """Main product component."""
    return rx.vstack(
        rx.heading("Galería de Imágenes", size="4"),
        lazy_image(),
        image_script(),
        width="100%",
        spacing="4",
        align_items="center",
        padding="2em"
    )

# Configuración de la aplicación
app = rx.App(
    style={
        "background_color": "#f5f5f5",
        "min_height": "100vh",
    }
)

# Añade la página principal
app.add_page(
    producto,
    title="Galería de Imágenes",
    description="Una galería de imágenes con carga diferida"
)