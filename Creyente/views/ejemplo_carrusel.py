import reflex as rx
from Creyente.estilo.estilo import Size
from Creyente.estilo.colors import Color

class CarruselState(rx.State):
    contadores: dict[int, int] = {1: 0, 2: 0, 3: 0, 4: 0,5: 0,6: 0,7: 0}
    
    todas_imagenes: dict[int, list[str]] = {
        1: [
            "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/cafetera_horizontal_trabajo.JPG",
            "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/cafetera_vertical_cerrado_trabajo.JPG", 
            "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/cafetera_vertical_abierto_trabajo.JPG"
        ],
        2: [
            "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/cogador_horizontal_trabajo.JPG", 
            "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/colgador_vertical_cerrado_trabajo.JPG",
            "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/colgador_vertical_abierto_trabajo.JPG", 
            
        ],
        3: [
            "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/escritorio_cerrado_trabajo.JPG", 
            "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/escritorio%20_abierto_trabajo.JPG", 
        ],
        4: [
            "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/mueble_sala_horizontal_trabajo.JPG", 
            "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/mueble_sala_vertical_trabajo.JPG", 
        ],
        5:[
            "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/mueble_cocina_electrodomesticos_trabajo.JPG",
            "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/mueble_cocina_alacena_trabajo.JPG",
            "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/mueble_cocina_horno_alacena_trabajo.JPG"
        ],
        6:[
            "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/estudio_con_homenaje_trbajo.JPG",
        ],
        7:[
            "https://sxdosvvnlmtjzebydzyy.supabase.co/storage/v1/object/public/imagenes%20para%20el%20proyecto/imagenes%20trabajos/mueble_armario_trabajo.JPG",
        ],
        


    }

    @rx.event
    def cambiar_imagen(self, carrusel_id: int, direccion: int):
        """
        carrusel_id: número del carrusel (1-9)
        direccion: 1 para avanzar, -1 para retroceder
        """
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
                object_fit="contain"
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
        crear_carrusel(1, "Mueble para tu Cafetera"),
        crear_carrusel(2, "Colgador para tu entrada de casa"),
        crear_carrusel(3, "Escritorio para toda ocacion"),
        crear_carrusel(4, "Muebles para tu cocina"),
        crear_carrusel(5, "Espacios para dar homenaje"),
        crear_carrusel(6, "Mueble para tu sala"),
        crear_carrusel(7, "Muebles para tu ropa"),
        width="100%",
        spacing="2",
        align="center",
    )
