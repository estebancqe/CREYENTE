#Scrollbar
import reflex as rx
from Creyente.components.imagen_muestra_index import imagen_muestra_index
from Creyente.components.title import title
from Creyente.style.style import Color, Spacing



title("experimento de imagenes"),
def scrollbar () -> rx.components:
    return rx.flex(
            rx.scroll_area(
                rx.hstack(
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
                    spacing="4",
                    width="max-content",
                ),
                type="always",
                scrollbars="horizontal",
                style=rx.Style({
                    "width": ["65vw","95vw"],  # Ancho casi completo del viewport
                    "height": rx.breakpoints(
                        initial="300px",  # Móvil
                        sm="300px",      
                        md="500px",      # Tablet y desktop
                        lg="500px"       
                    ),
                    "background": "black",
                    "padding": "1em",
                    "border_radius": "8px",
                    "overflow": "hidden",
                    # Scrollbar negro
                    "&::-webkit-scrollbar": {
                        "width": "12px",
                        "height": "12px",
                        "background": "black"
                    },
                    "&::-webkit-scrollbar-thumb": {
                        "background": "black",
                        "border_radius": "2px"
                    },
                    "&::-webkit-scrollbar-thumb:hover": {
                        "background": "#333333"  # Un poco más claro al hover
                    }
                }),
            ),
            width="100%",
            justify="center",
            align="center",
            background_color=Color.BACKGROUND.value,
            padding=["1em","2em"],
        ),