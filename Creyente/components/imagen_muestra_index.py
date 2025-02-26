import reflex as rx

def imagen_muestra_index(image: str, url:str) -> rx.Component:
    return rx.link(
        rx.image(
            image,
            height="100%",
            object_fit="cover",
            width="auto",
        ),
        href=url,
        is_external=True
    )   
