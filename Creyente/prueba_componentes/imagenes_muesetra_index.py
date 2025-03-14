#imagenes_muestra_index
import reflex as rx
from Creyente.components.imagen_simple_index import imagen_muestra_index
from Creyente.components.title import title
from Creyente.style.style import Color, Spacing



title("experimento de imagenes"),
def imagen_grid_muestra () -> rx.components:
    return rx.flex(
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