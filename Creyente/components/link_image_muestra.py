import reflex as rx

def link_image_muestra(image: str, url:str) -> rx.Component:
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
