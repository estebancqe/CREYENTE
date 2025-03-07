import reflex as rx
import asyncio

class CarouselState(rx.State):
    show_slide: int = 0
    auto_play: bool = True
    
    @rx.event(background=True)
    async def auto_advance(self):
        while self.auto_play:
            await asyncio.sleep(3)
            async with self:
                self.show_slide = (self.show_slide + 1) % 5
    
    def toggle_slide(self, index: int):
        self.show_slide = index
        
    def next_slide(self):
        self.show_slide = (self.show_slide + 1) % 5
        
    def prev_slide(self):
        self.show_slide = (self.show_slide - 1) % 5

def carrusel():
    images = [
        "/trabajos_web/cafetera_horizontal_1080_web.JPG",
        "/trabajos_web/cogador_horizontal_1080_web.JPG", 
        "/trabajos_web/escritorio_cerrado_1080_web.JPG",
        "/trabajos_web/mueble_sala_horizontal_1080_web.JPG",
        "/trabajos_web/estudio_con_homenaje_1080_web.JPG",
    ]
    
    return rx.box(
        rx.box(
            rx.box(
                rx.foreach(
                    images,
                    lambda src, i: rx.box(
                        rx.image(
                            src=src,
                            alt=f"Slide {i+1}",
                            width="100%",
                            height=rx.breakpoints(
                                initial="300px",  # mobile
                                sm="400px",       # tablet
                                lg="500px"        # desktop
                            ),
                            object_fit="cover",
                        ),
                        display=rx.cond(
                            CarouselState.show_slide == i,
                            "block",
                            "none"
                        ),
                        opacity=rx.cond(
                            CarouselState.show_slide == i,
                            "1",
                            "0"
                        ),
                        transition="all 0.5s ease-in-out",
                    )
                ),
                width="100%",
                height=rx.breakpoints(
                    initial="300px",  # mobile
                    sm="400px",       # tablet  
                    lg="500px"        # desktop
                ),
                overflow="hidden",
                border_radius="lg",
            ),
            
            # Indicadores
            rx.box(
                rx.foreach(
                    range(5),
                    lambda i: rx.button(
                        type_="button",
                        width=rx.breakpoints(
                            initial="8px",    # mobile
                            sm="10px",        # tablet
                            lg="12px"         # desktop
                        ),
                        height=rx.breakpoints(
                            initial="8px",    # mobile
                            sm="10px",        # tablet
                            lg="12px"         # desktop
                        ),
                        border_radius="full",
                        bg=rx.cond(
                            CarouselState.show_slide == i,
                            "white",
                            "rgba(255,255,255,0.3)"
                        ),
                        margin_x=rx.breakpoints(
                            initial="2px",    # mobile
                            sm="3px",         # tablet
                            lg="4px"          # desktop
                        ),
                        on_click=lambda: CarouselState.toggle_slide(i),
                        _hover={"bg": "rgba(255,255,255,0.8)"}
                    )
                ),
                position="absolute",
                z_index="30",
                bottom=rx.breakpoints(
                    initial="10px",   # mobile
                    sm="15px",        # tablet
                    lg="20px"         # desktop
                ),
                left="50%",
                transform="translateX(-50%)",
                display="flex",
            ),
            
            # Botones de navegación con tamaño ajustado
            rx.button(
                rx.icon(
                    "chevron_left",
                    color="white",
                    font_size=rx.breakpoints(
                        initial="18px",   # mobile
                        sm="20px",        # tablet
                        lg="24px"         # desktop
                    )
                ),
                position="absolute",
                top="50%",
                left=rx.breakpoints(
                    initial="10px",   # mobile
                    sm="15px",        # tablet
                    lg="20px"         # desktop
                ),
                transform="translateY(-50%)",
                z_index="30",
                bg="rgba(0,0,0,0.5)",
                border_radius="full",
                padding=rx.breakpoints(
                    initial="4",      # mobile
                    sm="5",          # tablet
                    lg="6"           # desktop
                ),
                height="fit-content",  # Ajusta la altura al contenido
                min_height="40px",     # Altura mínima del botón
                width="40px",          # Ancho fijo del botón
                on_click=CarouselState.prev_slide,
                _hover={"bg": "rgba(0,0,0,0.8)"}
            ),
            rx.button(
                rx.icon(
                    "chevron_right",
                    color="white",
                    font_size=rx.breakpoints(
                        initial="18px",   # mobile
                        sm="20px",        # tablet
                        lg="24px"         # desktop
                    )
                ),
                position="absolute",
                top="50%",
                right=rx.breakpoints(
                    initial="10px",   # mobile
                    sm="15px",        # tablet
                    lg="20px"         # desktop
                ),
                transform="translateY(-50%)",
                z_index="30",
                bg="rgba(0,0,0,0.5)",
                border_radius="full",
                padding=rx.breakpoints(
                    initial="4",      # mobile
                    sm="5",          # tablet
                    lg="6"           # desktop
                ),
                height="fit-content",  # Ajusta la altura al contenido
                min_height="40px",     # Altura mínima del botón
                width="40px",          # Ancho fijo del botón
                on_click=CarouselState.next_slide,
                _hover={"bg": "rgba(0,0,0,0.8)"}
            ),
            position="relative",
            width="100%",
        ),
        width="100%",
        padding=rx.breakpoints(
            initial="2",    # mobile
            sm="3",         # tablet
            lg="4"          # desktop
        ),
    )