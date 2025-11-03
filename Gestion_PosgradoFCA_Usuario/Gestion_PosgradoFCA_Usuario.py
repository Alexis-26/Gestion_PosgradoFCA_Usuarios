from .components.navbar import navbar, navbar_mobile
from .components.filtro import calendar, hora
from .components.mapa import mapa_primer_nivel, mapa_segundo_nivel
from .components.matriz import horario_table_1, horario_table_2
from .styles.utils import Texto_Desktop, Texto_Mobile
from .state import ConsultaHorarios
import reflex as rx

def reservacion_page() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            navbar(),
            # FILTROS
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.text("Fecha del dia de hoy:", font_size=Texto_Desktop.SECCIONES.value, weight="bold"),
                        rx.text(rx.moment(ConsultaHorarios.fecha_hoy, format="DD-MM-YYYY"), font_size=Texto_Desktop.SECCIONES.value),
                    ),
                    rx.vstack(
                        rx.hstack(
                            calendar(),
                            hora(),
                            justify="center",
                            spacing="3",
                            margin_top="10px",
                        ),
                        align="center",
                        spacing="0"
                    ),
                    align="center",
                    spacing="0"
                ),
                padding="10px",
                position="sticky",
                top="0",
                z_index="999",
                background="#ffffff",
                box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
            ),

            # INFORMACION DE LAS RESERVACIONES DEL PISO 1
            rx.box(
                mapa_primer_nivel(),
                margin_top="20px",
            ),
            rx.flex(
                horario_table_1(),
                margin_top="20px",
                justify="center",
                width="100%",
                padding="40px"
            ),

            # INFORMACION DE LAS RESERVACIONES DEL PISO 2
            rx.box(
                mapa_segundo_nivel(),
                margin_top="20px",
            ),
            rx.flex(
                horario_table_2(),
                margin_top="20px",
                justify="center",
                width="100%",
                padding="40px"
            ),
        ),
        rx.mobile_and_tablet(
            navbar_mobile(),
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.text("Fecha del dia de hoy:", font_size=Texto_Mobile.SUBTITULOS.value, weight="bold"),
                        rx.text(rx.moment(ConsultaHorarios.fecha_hoy, format="DD-MM-YYYY"), font_size=Texto_Mobile.SUBTITULOS.value),
                    ),
                    rx.vstack(
                        rx.text("Filtros de Fecha y Hora", font_size=Texto_Mobile.SECCIONES.value),
                        rx.hstack(
                            calendar(),
                            hora(),
                            spacing="3"
                        ),
                        spacing="0",
                        align="center",
                    ),
                    spacing="3",
                    align="center",
                ),
                padding="10px",
                position="sticky",
                top="0",
                z_index="999",
                background="#ffffff",
                box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
            ),
            rx.box(
                mapa_primer_nivel(),
                margin_top="10px",
            ),
            rx.flex(
                horario_table_1(),
                margin_top="10px",
                padding="5px",
                justify="center",
                width="100%",
            ),
            rx.box(
                mapa_segundo_nivel(),
                margin_top="10px",
            ),
            rx.flex(
                horario_table_2(),
                margin_top="10px",
                padding="5px",
                justify="center",
                width="100%",
            ),
        ),
        background_color="#FFFFFF",
        width="100%",
        min_height="100vh",
        margin="0px",
        padding="0px",
    )


global_style = {
    "font_family": "Nunito Sans, sans-serif",
    "button": {
        "cursor": "pointer",
    },
}

app = rx.App(
    theme=rx.theme(color_mode="light"),
    stylesheets=[
        'https://fonts.googleapis.com/css2?family=Nunito+Sans:ital,opsz,wght@0,6..12,200..1000;1,6..12,200..1000&display=swap'
    ],
    style=global_style)

app.add_page(reservacion_page, route="/", title="Reservaciones")
