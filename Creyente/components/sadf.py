import reflex as rx
from Creyente.state.animation_state import AnimationState
import Creyente.estilo.estilo as styles

def animated_link_button(
    title: str,
    body: str,
    image: str,
    url: str
) -> rx.Component:
    return rx.box(
        rx.cond(
            AnimationState.show,
            rx.box(
                link_button(
                    title=title,
                    body=body,
                    image=image,
                    url=url
                ),
                class_name=styles.BOUNCEIN_ANIMATION
            ),
        ),
        on_mount=AnimationState.on_mount
    )