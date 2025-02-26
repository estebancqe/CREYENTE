import reflex as rx
from Creyente.state.PageState import MuebleState
from Creyente.style.style import Spacing, Size
from Creyente.Presupuesto.acordion_modelos import acordion_modelos


def tabs_muebles() -> rx.Component:
    return rx.container(
        # Componente de Tabs
        rx.tabs.root(
            rx.scroll_area(
                rx.tabs.list(
                    rx.foreach(
                        MuebleState.muebles,
                        lambda mueble, index: rx.tabs.trigger(
                            mueble.mueble,  # Usamos el nombre del mueble como título de la pestaña
                            value=f"tab{index}",
                            color="black"
                        )
                    ),
                    size="2",
                    width="100%",
                
                ),
                type="always",
                scrollbars="horizontal",
                style=rx.Style({
                    "background_color": rx.color("black", 7),
                    "border_color": rx.color("blue", 1),
                    
                }),
                padding_y=Size.SMALL.value,
                width="100%",
                
            ),
        
            
            rx.foreach(
                MuebleState.muebles,
                lambda mueble, index: 
                    rx.tabs.content(
                        rx.box(
                            rx.hstack(
                                rx.box(
                                    rx.vstack(
                                        rx.heading(mueble.mueble, color="black",),
                                        rx.image(
                                            src=mueble.url_image,
                                            height="auto",
                                            width="250px",
                                        ),
                                        rx.text(mueble.descripcion, color="black"),
                                        width="200px",
                                        padding_top=Size.BIG.value,
                                        aling="center"    
                                    ),
                                ),
                                rx.box(
                                    acordion_modelos(mueble.id),
                                    width="300px",
                                ),
                                
                                padding_left=Size.SMALL.value,
                                flex_direction=["column", "row"],
                                width="100%",
                            ),
                            
                        ),
                        
                        width="100%", 
                        value=f"tab{index}",
                        
                    )
            ),
            value=MuebleState.tab_selected,
            on_change=MuebleState.change_tab,
            on_mount=MuebleState.load_muebles,
            orientation="horizontal",
            spacing=Spacing.BIG.value,
            width="100%",
            
        ),
        width="100%",
    )