import reflex as rx
#import pytz
# from datetime import datetime, timedelta

# Función para establecer el idioma del documento
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

# URL de la imagen de vista previa
preview = "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto//logo_creyente_mami%20(1).jpeg"

# Metadatos comunes para la web
_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@Creyente"}
]

# Metadatos para la página de inicio
index_title = "Creyente | Te enseño los mejores modelos de madera y melamina"
index_description = "Hola, me llamo Creyente y tengo lo mejor de madera y melamina a medida y totalmente personalizado."

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)

# Metadatos para la página de cursos
courses_title = "Ejemplo | Cursos"
courses_description = "descripcion de la pagina"

courses_meta = [
    {"name": "og:title", "content": courses_title},
    {"name": "og:description", "content": courses_description},
]
courses_meta.extend(_meta)

# Metadatos para la página de melamina
melamina_title = "Melamina | Colores y Texturas"
melamina_description = "Colores y texturas disponibles para tus pedidos"

melamina_meta = [
    {"name": "og:title", "content": melamina_title},
    {"name": "og:description", "content": melamina_description},
]
melamina_meta.extend(_meta)



# Metadatos para la página de trabajos
proyectos_title = "Proyectos | nuestros diseños"
proyectos_description = "algunos de los proyectos que hemos hecho"

proyectos_meta = [
    {"name": "og:title", "content": proyectos_title},
    {"name": "og:description", "content": proyectos_description},
]
proyectos_meta.extend(_meta)



# Metadatos para la página de cotizar
cotizar_title = "Cotizar | Precios referenciales"
cotizar_description = "Los modelos con sus precios referenciales"

cotizar_meta = [
    {"name": "og:title", "content": cotizar_title},
    {"name": "og:description", "content": cotizar_description},
]
cotizar_meta.extend(_meta)