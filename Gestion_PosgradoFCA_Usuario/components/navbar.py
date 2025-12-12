"""
Define la barra de navegación (Navbar) principal de la aplicación.

Este archivo contiene los componentes visuales para la cabecera
del sitio, mostrando el logo de la UABC y el título de la aplicación.
"""
import reflex as rx
from ..styles.colors import Colors
from ..styles.utils import Imagenes, Texto_Desktop, Texto_Mobile


def navbar() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.hstack(
                rx.image(src=Imagenes.LOGO_UABC_FCA.value, width=["60px", "120px"]) ,
                rx.text("CONSULTA DE HORARIOS", 
                        font_size=Texto_Desktop.TITULO_PRINCIPAL.value,
                        weight="bold", 
                        color=Colors.WHITE.value) ,
                justify="center",
            ),
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

def navbar_mobile() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.hstack(
                rx.image(src=Imagenes.LOGO_UABC_FCA.value, width="60px") ,
                rx.text("CONSULTA DE HORARIOS", 
                        font_size=Texto_Mobile.SUBTITULOS.value,
                        weight="bold", 
                        color=Colors.WHITE.value) ,
                justify="center",
            ),
            justify="center",
            align="center",
            width="100%",
            height="100%",
        ) ,
        width="100%",
        height="50px",
        background=Colors.PRIMARY_GREEN.value,
        padding_left="10px",
        padding_right="10px"
    )