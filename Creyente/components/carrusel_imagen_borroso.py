import reflex as rx
from Creyente.style.style import Size
from Creyente.style.colors import Color

class CarruselState(rx.State):
    contadores: dict[int, int] = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
    
    todas_imagenes: dict[int, list[str]] = {
        1: [
            "/trabajos_web/cafetera_horizontal_1080_web.JPG",
            "/trabajos_web/cafetera_vertical_cerrado_1080_web.JPG",
            "/trabajos_web/cafetera_vertical_abierto_1080_web_.JPG"
        ],
        2: [
            "/trabajos_web/cogador_horizontal_1080_web.JPG",
            "/trabajos_web/colgador_vertical_cerrado_1080_web.JPG",
            "/trabajos_web/colgador_vertical_abierto_1080_web.JPG",
        ],
        3: [
            "/trabajos_web/escritorio_cerrado_1080_web.JPG",
            "/trabajos_web/escritorio_abierto_1080_web.JPG",
        ],
        4: [
            "/trabajos_web/mueble_sala_horizontal_1080_web.JPG",
            "/trabajos_web/mueble_sala_vertical_1080_web.JPG",
        ],
        5:[
            "/trabajos_web/mueble_cocina_electrodomesticos_1080_web.JPG",
            "/trabajos_web/mueble_cocina_alacena_1080_web.JPG",
            "/trabajos_web/mueble_cocina_horno_alacena_1080_web.JPG",
        ],
        6:[
            "/trabajos_web/estudio_con_homenaje_1080_web.JPG",
        ],
        7:[
            "/trabajos_web/mueble_armario_1080_web.JPG",
        ],
    }

    @rx.event
    def cambiar_imagen(self, carrusel_id: int, direccion: int):
        self.contadores[carrusel_id] = (
            self.contadores[carrusel_id] + direccion
        ) % len(self.todas_imagenes[carrusel_id])

    def get_imagen_actual(self, carrusel_id: int) -> str:
        return self.todas_imagenes[carrusel_id][self.contadores[carrusel_id]]

    def get_imagen_anterior(self, carrusel_id: int) -> str:
        indice_actual = self.contadores[carrusel_id]
        indice_anterior = (indice_actual - 1) % len(self.todas_imagenes[carrusel_id])
        return self.todas_imagenes[carrusel_id][indice_anterior]

    def get_imagen_siguiente(self, carrusel_id: int) -> str:
        indice_actual = self.contadores[carrusel_id]
        indice_siguiente = (indice_actual + 1) % len(self.todas_imagenes[carrusel_id])
        return self.todas_imagenes[carrusel_id][indice_siguiente]

    # Variables computadas para imagen actual
    @rx.var
    def imagen_actual1(self) -> str:
        return self.get_imagen_actual(1)
    
    @rx.var
    def imagen_actual2(self) -> str:
        return self.get_imagen_actual(2)
    
    @rx.var
    def imagen_actual3(self) -> str:
        return self.get_imagen_actual(3)
    
    @rx.var
    def imagen_actual4(self) -> str:
        return self.get_imagen_actual(4)
    
    @rx.var
    def imagen_actual5(self) -> str:
        return self.get_imagen_actual(5)
    
    @rx.var
    def imagen_actual6(self) -> str:
        return self.get_imagen_actual(6)
    
    @rx.var
    def imagen_actual7(self) -> str:
        return self.get_imagen_actual(7)

    # Variables computadas para imagen anterior
    @rx.var
    def imagen_anterior1(self) -> str:
        return self.get_imagen_anterior(1)
    
    @rx.var
    def imagen_anterior2(self) -> str:
        return self.get_imagen_anterior(2)
    
    @rx.var
    def imagen_anterior3(self) -> str:
        return self.get_imagen_anterior(3)
    
    @rx.var
    def imagen_anterior4(self) -> str:
        return self.get_imagen_anterior(4)
    
    @rx.var
    def imagen_anterior5(self) -> str:
        return self.get_imagen_anterior(5)
    
    @rx.var
    def imagen_anterior6(self) -> str:
        return self.get_imagen_anterior(6)
    
    @rx.var
    def imagen_anterior7(self) -> str:
        return self.get_imagen_anterior(7)

    # Variables computadas para imagen siguiente
    @rx.var
    def imagen_siguiente1(self) -> str:
        return self.get_imagen_siguiente(1)
    
    @rx.var
    def imagen_siguiente2(self) -> str:
        return self.get_imagen_siguiente(2)
    
    @rx.var
    def imagen_siguiente3(self) -> str:
        return self.get_imagen_siguiente(3)
    
    @rx.var
    def imagen_siguiente4(self) -> str:
        return self.get_imagen_siguiente(4)
    
    @rx.var
    def imagen_siguiente5(self) -> str:
        return self.get_imagen_siguiente(5)
    
    @rx.var
    def imagen_siguiente6(self) -> str:
        return self.get_imagen_siguiente(6)
    
    @rx.var
    def imagen_siguiente7(self) -> str:
        return self.get_imagen_siguiente(7)

def crear_carrusel(id: int, titulo: str) -> rx.Component:
    return rx.vstack(
        rx.heading(
            titulo,
            size="6",
            color=Color.CONTENT.value,
            text_align="center"
        ),
        rx.box(
            rx.hstack(
                # Imagen izquierda (anterior)
                rx.image(
                    src=getattr(CarruselState, f"imagen_anterior{id}"),
                    width="auto",
                    height=["100px", "150px", "200px", "250px"],
                    max_width=["0", "0", "30%", "30%"],  # Oculta en móvil
                    opacity="0.5",
                    object_fit="contain",
                    display=["none", "none", "flex", "flex"],  # Oculta en móvil
                    on_click=lambda: CarruselState.cambiar_imagen(id, -1),
                ),
                # Imagen central (actual)
                rx.image(
                    src=getattr(CarruselState, f"imagen_actual{id}"),
                    width="auto",
                    height=["200px", "300px", "400px", "500px"],
                    max_width="100%",
                    object_fit="contain",
                    class_name="animate__animated animate__fadeIn",
                    key=f"imagen-{id}-{getattr(CarruselState, f'imagen_actual{id}')}",
                ),
                # Imagen derecha (siguiente)
                rx.image(
                    src=getattr(CarruselState, f"imagen_siguiente{id}"),
                    width="auto",
                    height=["100px", "150px", "200px", "250px"],
                    max_width=["0", "0", "30%", "30%"],  # Oculta en móvil
                    opacity="0.5",
                    object_fit="contain",
                    display=["none", "none", "flex", "flex"],  # Oculta en móvil
                    on_click=lambda: CarruselState.cambiar_imagen(id, 1),
                ),
                width="100%",
                spacing="4",
                align="center",
                justify="center",
                padding="2",
                overflow="hidden",  # Previene scroll horizontal
            ),
            width="100%",
            overflow="hidden",  # Previene scroll horizontal
        ),
        width="100%",
        align="center",
        margin="2"
    )


def carousel_imagenes_borrosa_lateral():
    return rx.vstack(
        crear_carrusel(1, "Mueble Cafetera"),
        crear_carrusel(2, "Perchero"),
        crear_carrusel(3, "Escritorios"),
        crear_carrusel(4, "Muebles Sala"),
        crear_carrusel(5, "Muebles Cocina"),
        crear_carrusel(6, "Estudio"),   
        crear_carrusel(7, "Mueble Dormitorio"),
        width="100%",
        spacing="2",
        align="center",
    )