import reflex as rx

class SwipeableComponent(rx.ComponentState):
    """Componente de estado para manejar eventos swipe."""
    mensaje: str = ""
    imagenes: list[str] = [
        "/trabajos_web/cafetera_horizontal_1080_web.JPG",
        "/trabajos_web/cogador_horizontal_1080_web.JPG",
        "/trabajos_web/escritorio_cerrado_1080_web.JPG",
        "/trabajos_web/mueble_sala_horizontal_1080_web.JPG",
        "/trabajos_web/estudio_con_homenaje_1080_web.JPG",




    ]
    indice_actual: int = 0
    total_imagenes: int = 5
    cargando: bool = False

    @rx.event
    def siguiente_imagen(self):
        self.indice_actual = (self.indice_actual + 1) % self.total_imagenes
        self.mensaje = ""

    @rx.event 
    def anterior_imagen(self):
        self.indice_actual = (self.indice_actual - 1) % self.total_imagenes
        self.mensaje = ""

    @rx.event
    def ir_a_imagen(self, indice: int):
        self.indice_actual = indice
        self.mensaje = ""

    @classmethod
    def get_component(cls, **props):
        return rx.vstack(
            rx.script("""
                // Usar window para variables globales
                window._swipeState = window._swipeState || {
                    startX: 0,
                    endX: 0,
                    isDragging: false
                };
                
                window.handleMouseEvent = function(event) {
                    const state = window._swipeState;
                    
                    if (event.type === 'mousedown') {
                        state.startX = event.clientX;
                        state.isDragging = true;
                    }
                    else if (event.type === 'mousemove' && state.isDragging) {
                        state.endX = event.clientX;
                    }
                    else if (event.type === 'mouseup' || event.type === 'mouseleave') {
                        if (!state.isDragging) return;
                        
                        state.isDragging = false;
                        const swipeThreshold = 50;
                        const swipeDistance = state.endX - state.startX;
                        
                        if (Math.abs(swipeDistance) > swipeThreshold) {
                            if (swipeDistance > 0) {
                                window.swipeEvent('right');
                            } else {
                                window.swipeEvent('left');
                            }
                        }
                        
                        state.startX = 0;
                        state.endX = 0;
                    }
                };
            """),
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.button(
                            rx.icon("chevron-left"),
                            on_click=cls.anterior_imagen,
                            bg="black",
                            color="blue.500",
                            border="1px solid",
                            border_color="blue.500",
                            border_radius="full",
                            _hover={"bg": "blue.50"},
                            size="3",
                            aria_label="Imagen anterior"
                        ),
                        rx.box(
                            rx.center(
                                rx.cond(
                                    cls.cargando,
                                    rx.spinner(size="3", color="blue.500"),
                                    rx.image(
                                        src=cls.imagenes[cls.indice_actual],
                                        width="500px",
                                        height="auto",
                                        object_fit="cover",
                                        border_radius="xl",
                                        box_shadow="xl",
                                        transition="all 0.3s ease-in-out",
                                        _hover={"transform": "scale(1.02)"}
                                    )
                                ),
                                width="30em",
                                height="30em",
                                padding="2em",
                                background="linear-gradient(to bottom right, #f7fafc, #edf2f7)",
                                border_radius="2xl",
                                box_shadow="lg",
                                overflow="hidden",
                            ),
                            on_mouse_down=rx.call_script("handleMouseEvent(event)"),
                            on_mouse_move=rx.call_script("handleMouseEvent(event)"),
                            on_mouse_up=rx.call_script("handleMouseEvent(event)"),
                            on_mouse_leave=rx.call_script("handleMouseEvent(event)"),
                            style={
                                "user-select": "none",
                                "cursor": "grab"
                            }
                        ),
                        rx.button(
                            rx.icon("chevron-right"),
                            on_click=cls.siguiente_imagen,
                            bg="black",
                            color="blue.500",
                            border="1px solid",
                            border_color="blue.500",
                            border_radius="full",
                            _hover={"bg": "blue.50"},
                            size="3",
                            aria_label="Siguiente imagen"
                        ),
                        spacing="4",
                        align="center",
                    ),
                    rx.hstack(
                        rx.box(
                            bg=rx.cond(
                                cls.indice_actual == 0,
                                "blue.500",
                                "gray.200"
                            ),
                            width="8px",
                            height="8px",
                            border_radius="full",
                            cursor="pointer",
                            on_click=lambda: cls.ir_a_imagen(0),
                            _hover={"bg": "blue.600"},
                            transition="all 0.2s"
                        ),
                        rx.box(
                            bg=rx.cond(
                                cls.indice_actual == 1,
                                "blue.500",
                                "gray.200"
                            ),
                            width="8px",
                            height="8px",
                            border_radius="full",
                            cursor="pointer",
                            on_click=lambda: cls.ir_a_imagen(1),
                            _hover={"bg": "blue.600"},
                            transition="all 0.2s"
                        ),
                        rx.box(
                            bg=rx.cond(
                                cls.indice_actual == 2,
                                "blue.500",
                                "gray.200"
                            ),
                            width="8px",
                            height="8px",
                            border_radius="full",
                            cursor="pointer",
                            on_click=lambda: cls.ir_a_imagen(2),
                            _hover={"bg": "blue.600"},
                            transition="all 0.2s"
                        ),
                        spacing="2",
                        margin_y="4"
                    ),
                    rx.cond(
                        cls.mensaje != "",
                        rx.text(
                            cls.mensaje,
                            font_size="lg",
                            color="blue.600",
                            font_weight="medium",
                            transition="all 0.2s",
                            animation="fadeIn 0.3s ease-in"
                        )
                    ),
                    rx.text(
                        f"Imagen {cls.indice_actual + 1} de {cls.total_imagenes}",
                        font_size="sm",
                        color="black",
                        font_weight="medium"
                    ),
                    spacing="4",
                    width="100%",
                    align="center"
                ),
                padding="2em",
                bg="white",
                border_radius="3xl",
                box_shadow="2xl",
                max_width="1200px",
                margin="auto"
            ),
            width="100%",
            min_height="100vh",
            bg="gray.50",
            padding="4em",
            spacing="6",
            **props
        )

# Crear el componente
swipeable_component = SwipeableComponent.create