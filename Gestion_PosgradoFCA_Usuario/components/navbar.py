import reflex as rx
from ..styles.colors import Colors
from ..styles.styles import FontSize
from ..styles.utils import Imagenes

def navbar() -> rx.Component:
    return rx.box(
        rx.flex(
            # Elemento vacío para balancear el lado izquierdo
            #rx.box(width=["60px", "160px"]) ,
            
            # Título centrado con logo
            rx.hstack(
                rx.image(src=Imagenes.LOGO.value, width=["20px", "60px"]) ,
                rx.text("REGISTROS DE HORARIOS", 
                        font_size=["16px", FontSize.EXTRA_LARGE.value],
                        weight="bold", 
                        color=Colors.WHITE.value) ,
                justify="center",
            ) ,
            
            # Botón en el lado derecho
            # rx.hstack(
            #     cambio_password(),
            #     cerrar_sesion(),
            # ),

            justify="center",
            align="center",
            width="100%",
            height="100%",
        ) ,
        width="100%",
        height=["50px", "100px"],
        background=Colors.PRIMARY_GREEN.value,
        padding_left=["10px", "60px"],
        padding_right=["10px", "60px"]
    )