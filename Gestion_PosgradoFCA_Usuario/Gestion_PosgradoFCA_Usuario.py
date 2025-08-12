import reflex as rx
from .components.navbar import navbar
from .components.filtro import calendar, search_docente, search_materia, grupo, hora
from .components.consulta_horarios import tabla_horarios, lista_horarios, matriz_horarios, mapa_primer_nivel, mapa_segundo_nivel

style = {
    "body": {
        "background_color": "#20343C",
        #"background_color": "#FFFFFF",
        "margin": "0",
        "padding": "0",
    }
}

def index():
    return rx.box(
        rx.tablet_and_desktop(
            navbar(),
            rx.box(
                rx.hstack(
                    search_docente(),
                    search_materia(),
                    justify="center",
                    spacing="3"
                ),
                rx.hstack(
                    calendar(),
                    hora(),
                    grupo(),
                    justify="center",
                    spacing="3",
                    margin_top="10px",
                ),
                background="#f2f3f7",
                margin_top="10px",
                margin_left="20px",
                margin_right="20px",
                padding="5px",
                border_radius="10px",
                box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
                #width="80%", Modificacion pendiente
            ),
            rx.box(
                #tabla_horarios(),
                mapa_primer_nivel(),
                background="#f2f3f7",
                margin_top="10px",
                margin_left="20px",
                margin_right="20px",
                padding="20px",
                border_radius="10px",
                box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
            ),
            rx.box(
                #tabla_horarios(),
                mapa_segundo_nivel(),
                background="#f2f3f7",
                margin_top="10px",
                margin_left="20px",
                margin_right="20px",
                padding="20px",
                border_radius="10px",
                box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
            ),
        ),
        rx.mobile_only(
            navbar(),
            rx.box(
                rx.vstack(
                    search_docente(),
                    search_materia(),
                    rx.hstack(
                        calendar(),
                        hora(),
                        grupo(),
                        spacing="3"
                    ),
                    spacing="3",
                    align="center",
                ),
                background="#f2f3f7",
                margin_top="10px",
                margin_left="20px",
                margin_right="20px",
                padding="5px",
                border_radius="10px",
                box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
                #width="80%",
            ),
            rx.box(
                mapa_primer_nivel(),
                background="#f2f3f7",
                margin_top="10px",
                margin_left="10px",
                margin_right="10px",
                padding="10px",
                border_radius="10px",
                box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
            ),
            rx.box(
                mapa_segundo_nivel(),
                background="#f2f3f7",
                margin_top="10px",
                margin_left="10px",
                margin_right="10px",
                padding="10px",
                border_radius="10px",
                box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
            ),
        ),
        background_color="#FFFFFF",
        width="100%",
        min_height="100vh",
        margin="0px",
        padding="0px",
        )

app = rx.App(
    theme=rx.theme(appearance="light"),
    style=style
    )

app.add_page(index)
