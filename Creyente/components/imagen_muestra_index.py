import reflex as rx

def imagen_muestra_index(image: str, url:str) -> rx.Component:
    return rx.link(
        rx.image(
            image,
            height=["300px","500px"],
            object_fit="cover",
            width="auto",
        ),
        href=url,
        is_external=True,
        aling="center",
        justify="center",
        width="100%",
    )   
