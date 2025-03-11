#carousel_state.py

import reflex as rx
from collections import Counter

class CarouselState1(rx.State):
    current_image: int = 0
    images: list[str] = [
        "/trabajos_web/cafetera_horizontal_1080_web.JPG",
        "/trabajos_web/cogador_horizontal_1080_web.JPG",
        "/trabajos_web/escritorio_cerrado_1080_web.JPG",
        "/trabajos_web/mueble_sala_horizontal_1080_web.JPG",
        "/trabajos_web/estudio_con_homenaje_1080_web.JPG",
    ]
    
    def next_image(self):
        if self.current_image < len(self.images) - 1:
            self.current_image += 1
        print(f"Next image: {self.current_image}")  # Depuración

    def prev_image(self):
        if self.current_image > 0:
            self.current_image -= 1
        print(f"Previous image: {self.current_image}")  # Depuración
            
    def on_swipe(self, event_data: dict):
        if event_data.get("dir") == "Left":
            self.next_image()
        elif event_data.get("dir") == "Right":
            self.prev_image()