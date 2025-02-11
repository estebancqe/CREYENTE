import reflex as rx
from Creyente.state.PageState import PageState
from Creyente.routes import Route
from Creyente.estilo.estilo import Color, Spacing  ,Size 
from Creyente.components.link_button import link_button
from Creyente.components.title import title 
# from Creyente.Presupuesto.hereda.modelos_melamina import modelos_melamina
from Creyente.Presupuesto.doc_prueba import doc_prueba
from Creyente.Presupuesto.tabs_muebles import tabs_muebles

from Creyente.Presupuesto.informacion_muebles import informacion_muebles
from Creyente.Presupuesto.infrmacion_modelos import infrmacion_modelos




def cotizar_links(HERRAJES=[], MUEBLES=[]) -> rx.Component:
    return rx.vstack(
        # title("Muestra del contenido del archivo prueba"),
        # doc_prueba(),
        
        
        title("Nuestros Modelos de Muebles"),
        tabs_muebles(),  


        # title("Valores de la tabla Mubeles"), 
        # rx.cond(
        #     PageState.mueble_info,
        #     rx.vstack(
        #         rx.flex(
        #             rx.foreach(
        #                 PageState.mueble_info,
        #                   informacion_muebles,
        
        #             ),
        #             flex_direction=["column", "row"],
        #             spacing=Spacing.DEFAULT.value
        #         ),
        #         spacing=Spacing.DEFAULT.value
        #     )
        # ),
        
        
        # title("VAlores de la tabla Modelos"),
        # rx.cond(
        #     PageState.modelo_info,
        #     rx.vstack(
                
        #         rx.flex(
                    
        #             rx.foreach(
        #                 PageState.modelo_info,
        #                   infrmacion_modelos
        #             ),
        #             flex_direction=["column", "row"],
        #             spacing=Spacing.DEFAULT.value
        #         ),
        #         spacing=Spacing.DEFAULT.value
        #     )
        # ),
        
    
    
    width="100%",
    )