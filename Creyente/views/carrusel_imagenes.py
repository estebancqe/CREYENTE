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
        # 1: [
        #     "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/1080_web/cafetera_horizontal_1080_web.JPG",
        #     "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/1080_web/cafetera_vertical_cerrado_1080_web.JPG",
        #     "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/1080_web/cafetera_vertical_abierto_1080_web_.JPG",
        # ],

        2: [
            "/trabajos_web/cogador_horizontal_1080_web.JPG",
            "/trabajos_web/colgador_vertical_cerrado_1080_web.JPG",
            "/trabajos_web/colgador_vertical_abierto_1080_web.JPG",
            # "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/1080_web/cogador_horizontal_1080_web.JPG",
            # "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/1080_web/colgador_vertical_cerrado_1080_web.JPG",
            # "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/1080_web/colgador_vertical_abierto_1080_web.JPG",
        ],
        3: [
            "/trabajos_web/escritorio_cerrado_1080_web.JPG",
            "/trabajos_web/escritorio_abierto_1080_web.JPG",
            # "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/1080_web/escritorio_cerrado_1080_web.JPG",
            # "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/1080_web/escritorio%20_abierto_1080_web.JPG",
        ],
        4: [
            "/trabajos_web/mueble_sala_horizontal_1080_web.JPG",
            "/trabajos_web/mueble_sala_vertical_1080_web.JPG",
            "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/1080_web/mueble_sala_horizontal_1080_web.JPG",
            "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/1080_web/mueble_sala_vertical_1080_web.JPG",
        ],
        5:[
            "/trabajos_web/mueble_cocina_electrodomesticos_1080_web.JPG",
            "/trabajos_web/mueble_cocina_alacena_1080_web.JPG",
            "/trabajos_web/mueble_cocina_horno_alacena_1080_web.JPG",
            # "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/1080_web/mueble_cocina_electrodomesticos_1080_web.JPG",
            # "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/1080_web/mueble_cocina_alacena_1080_web.JPG",
            # "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/1080_web/mueble_cocina_horno_alacena_1080_web.JPG",
        ],
        6:[
            "/trabajos_web/estudio_con_homenaje_1080_web.JPG",
            # "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/1080_web/estudio_con_homenaje_1080_web.JPG",
        ],
        7:[
            "/trabajos_web/mueble_armario_1080_web.JPG",
            # "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/1080_web/mueble_armario_1080_web.JPG",
        ],
    }

    @rx.event
    def cambiar_imagen(self, carrusel_id: int, direccion: int):
        self.contadores[carrusel_id] = (
            self.contadores[carrusel_id] + direccion
        ) % len(self.todas_imagenes[carrusel_id])

    def get_imagen_actual(self, carrusel_id: int) -> str:
        return self.todas_imagenes[carrusel_id][self.contadores[carrusel_id]]

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


def crear_carrusel(id: int, titulo: str) -> rx.Component:
    return rx.vstack(
        rx.heading(
            titulo,
            size="6", 
            color=Color.CONTENT.value,
            text_align="center"
        ),
        rx.hstack(
            rx.image(
                "/icons/angulo-izquierdo.png",
                sizes=Size.DEFAULT.value,
                on_click=lambda: CarruselState.cambiar_imagen(id, -1),
                width="auto",
                height="auto",
                max_width="100%"
            ),
            rx.image(
                src=getattr(CarruselState, f"imagen_actual{id}"),
                width="auto",
                height=["200px", "300px", "400px", "500px"],
                max_width="100%",
                object_fit="contain",
                class_name="animate__animated animate__fadeIn",
                key=f"imagen-{id}-{getattr(CarruselState, f'imagen_actual{id}')}"  # Clave única para forzar renderizado
            ),
            rx.image(
                "/icons/angulo-derecho.png", 
                sizes=Size.DEFAULT.value,
                on_click=lambda: CarruselState.cambiar_imagen(id, 1),
                width="auto", 
                height="auto",
                max_width="100%"
            ),
            width="100%",
            spacing="4",
            align="center",
            justify="center",
            padding="2"
        ),
        width="100%",
        align="center",
        margin="2"
    )

def ejemplo_carrusel():
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
