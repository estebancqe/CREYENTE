import reflex as rx

class AnimationState(rx.ComponentState):
    visible_components: dict[str, bool] = {}

    @rx.event
    def set_visible(self, component_id: str):
        self.visible_components = {
            **self.visible_components,
            component_id: True
        }

    @rx.event
    def is_visible(self, component_id: str) -> bool:
        return self.visible_components.get(component_id, False)

    @classmethod
    def get_component(cls, **props):
        return rx.box(
            rx.vstack(
                **props
            )
        )

animation_state = AnimationState.create