import reflex as rx

class AnimationState(rx.State):
    show: bool = False

    def on_mount(self):
        self.show = True
