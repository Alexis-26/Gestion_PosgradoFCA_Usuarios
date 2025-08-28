import reflex as rx
from .components.navbar import navbar, navbar_mobile
from .components.filtro import calendar, search_docente, search_materia, grupo, hora
#from .components.consulta_horarios import tabla_horarios, lista_horarios, matriz_horarios, mapa_primer_nivel, mapa_segundo_nivel
from .components.mapa import mapa_primer_nivel, mapa_segundo_nivel
from .components.matriz import horario_table_1, horario_table_2
from .styles.utils import Texto_Desktop, Texto_Mobile
from .state import ConsultaHorarios

def reservacion_page() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            navbar(),
            # rx.button(
            #     f"ESTADO DISABLED: {AsignacionHorarios.select_horario}",
            #     disabled=AsignacionHorarios.select_horario
            # ),
            # FILTROS
            rx.box(
                # rx.hstack(
                #     #search_docente(),
                #     #search_materia(),
                #     justify="center",
                #     spacing="3"
                # ),
                rx.vstack(
                    rx.hstack(
                        rx.text("Fecha del dia de hoy:", font_size=Texto_Desktop.SUBTITULOS.value, weight="bold"),
                        rx.text(ConsultaHorarios.fecha_actual, font_size=Texto_Desktop.SUBTITULOS.value),
                    ),
                    rx.vstack(
                        rx.text("Filtros de Fecha y Hora", font_size=Texto_Desktop.SECCIONES.value),
                        rx.hstack(
                            calendar(),
                            hora(),
                            # grupo(),
                            justify="center",
                            spacing="3",
                            margin_top="10px",
                        ),
                        align="center",
                        spacing="0"
                    ),
                    #mis_reservaciones(),
                    align="center"
                ),
                #margin_top="10px",
                padding="10px",
                position="sticky",
                top="0",
                z_index="999",
                background="#ffffff",
                box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
            ),

            # INFORMACION DE LAS RESERVACIONES DEL PISO 1
            rx.box(
                #tabla_horarios(),
                mapa_primer_nivel(),
                #background="pink",
                margin_top="20px",
                # margin_left="20px",
                # margin_right="20px",
                # padding="20px",
                # border_radius="10px",
                # box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
            ),
            rx.flex(
                #tabla_horarios(),
                horario_table_1(),
                #background="pink",
                margin_top="20px",
                justify="center",
                width="100%",
                padding="40px"
                # margin_left="20px",
                # margin_right="20px",
                # padding="20px",
                # border_radius="10px",
                # box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
            ),

            # INFORMACION DE LAS RESERVACIONES DEL PISO 2
            rx.box(
                #tabla_horarios(),
                mapa_segundo_nivel(),
                #background="pink",
                margin_top="20px",
                # margin_left="20px",
                # margin_right="20px",
                # padding="20px",
                # border_radius="10px",
                # box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
            ),
            rx.flex(
                #tabla_horarios(),
                horario_table_2(),
                #background="pink",
                margin_top="20px",
                justify="center",
                width="100%",
                padding="40px"
                # margin_left="20px",
                # margin_right="20px",
                # padding="20px",
                # border_radius="10px",
                # box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
            ),
        ),
        rx.mobile_and_tablet(
            navbar_mobile(),
            rx.box(
                rx.vstack(
                    #search_docente(),
                    #search_materia(),
                    rx.hstack(
                        rx.text("Fecha del dia de hoy:", font_size=Texto_Mobile.SUBTITULOS.value, weight="bold"),
                        rx.text(ConsultaHorarios.fecha_actual, font_size=Texto_Mobile.SUBTITULOS.value),
                    ),
                    rx.vstack(
                        rx.text("Filtros de Fecha y Hora", font_size=Texto_Mobile.SECCIONES.value),
                        rx.hstack(
                            calendar(),
                            hora(),
                            # grupo(),
                            spacing="3"
                        ),
                        spacing="0",
                        align="center",
                    ),
                    #mis_reservaciones(),
                    spacing="3",
                    align="center",
                ),
                # background="#f2f3f7",
                #margin_top="10px",
                # margin_left="20px",
                # margin_right="20px",
                # padding="5px",
                # border_radius="10px",
                # box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
                #width="80%",
                padding="10px",
                position="sticky",
                top="0",
                z_index="999",
                background="#ffffff",
                box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
            ),
            rx.box(
                mapa_primer_nivel(),
                # background="#f2f3f7",
                margin_top="10px",
                # margin_left="10px",
                # margin_right="10px",
                # padding="10px",
                # border_radius="10px",
                # box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
            ),
            rx.flex(
                horario_table_1(),
                # background="#f2f3f7",
                margin_top="10px",
                padding="5px",
                justify="center",
                width="100%",
                # margin_left="10px",
                # margin_right="10px",
                # padding="10px",
                # border_radius="10px",
                # box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
            ),
            rx.box(
                mapa_segundo_nivel(),
                # background="#f2f3f7",
                margin_top="10px",
                # margin_left="10px",
                # margin_right="10px",
                # padding="10px",
                # border_radius="10px",
                # box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
            ),
            rx.flex(
                horario_table_2(),
                # background="#f2f3f7",
                margin_top="10px",
                padding="5px",
                justify="center",
                width="100%",
                # margin_left="10px",
                # margin_right="10px",
                # padding="10px",
                # border_radius="10px",
                # box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
            ),
        ),
        # rx.dialog.root(
        #     rx.dialog.content(
        #         rx.dialog.title(
        #             "Formulario de Reservación",
        #             display="none"
        #         ),
        #         rx.dialog.description(
        #             "Formulario para reservar un salón",
        #             display="none"
        #         ),
        #         rx.box(
        #             form_reservar(),
        #             width="100%",
        #         ),
        #         style={
        #             "background": "transparent",
        #             "box_shadow": "none",
        #             "max_width": "900px",
        #             "width": "100%",
        #         },
        #     ),
        #     open=AsignacionHorarios.mostrar_formulario,
        # ),
        # rx.dialog.root(
        #     rx.dialog.content(
        #         rx.dialog.title(
        #             "Formulario de Cambio de Contraseña",
        #             display="none"
        #         ),
        #         rx.dialog.description(
        #             "Formulario para Cambiar la Contraseña",
        #             display="none"
        #         ),
        #         rx.box(
        #             form_cambio(),
        #             width="100%",
        #         ),
        #         style={
        #             "background": "transparent",
        #             "box_shadow": "none",
        #             "max_width": "900px",
        #             "width": "100%",
        #         },
        #     ),
        #     open=FormCambio.mostrar_formulario,
        # ),
        background_color="#FFFFFF",
        width="100%",
        min_height="100vh",
        margin="0px",
        padding="0px",
    )


# def index():
#     return rx.box(
#         rx.tablet_and_desktop(
#             navbar(),
#             rx.box(
#                 rx.hstack(
#                     search_docente(),
#                     search_materia(),
#                     justify="center",
#                     spacing="3"
#                 ),
#                 rx.hstack(
#                     calendar(),
#                     hora(),
#                     grupo(),
#                     justify="center",
#                     spacing="3",
#                     margin_top="10px",
#                 ),
#                 background="#f2f3f7",
#                 margin_top="10px",
#                 margin_left="20px",
#                 margin_right="20px",
#                 padding="5px",
#                 border_radius="10px",
#                 box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
#                 #width="80%", Modificacion pendiente
#             ),
#             rx.box(
#                 #tabla_horarios(),
#                 mapa_primer_nivel(),
#                 background="#f2f3f7",
#                 margin_top="10px",
#                 margin_left="20px",
#                 margin_right="20px",
#                 padding="20px",
#                 border_radius="10px",
#                 box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
#             ),
#             rx.box(
#                 #tabla_horarios(),
#                 mapa_segundo_nivel(),
#                 background="#f2f3f7",
#                 margin_top="10px",
#                 margin_left="20px",
#                 margin_right="20px",
#                 padding="20px",
#                 border_radius="10px",
#                 box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
#             ),
#         ),
#         rx.mobile_only(
#             navbar(),
#             rx.box(
#                 rx.vstack(
#                     search_docente(),
#                     search_materia(),
#                     rx.hstack(
#                         calendar(),
#                         hora(),
#                         grupo(),
#                         spacing="3"
#                     ),
#                     spacing="3",
#                     align="center",
#                 ),
#                 background="#f2f3f7",
#                 margin_top="10px",
#                 margin_left="20px",
#                 margin_right="20px",
#                 padding="5px",
#                 border_radius="10px",
#                 box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
#                 #width="80%",
#             ),
#             rx.box(
#                 mapa_primer_nivel(),
#                 background="#f2f3f7",
#                 margin_top="10px",
#                 margin_left="10px",
#                 margin_right="10px",
#                 padding="10px",
#                 border_radius="10px",
#                 box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
#             ),
#             rx.box(
#                 mapa_segundo_nivel(),
#                 background="#f2f3f7",
#                 margin_top="10px",
#                 margin_left="10px",
#                 margin_right="10px",
#                 padding="10px",
#                 border_radius="10px",
#                 box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
#             ),
#         ),
#         background_color="#FFFFFF",
#         width="100%",
#         min_height="100vh",
#         margin="0px",
#         padding="0px",
#         )



global_style = {
    "font_family": "Nunito Sans, sans-serif",
}

app = rx.App(
    theme=rx.theme(color_mode="light"),
    stylesheets=[
        'https://fonts.googleapis.com/css2?family=Nunito+Sans:ital,opsz,wght@0,6..12,200..1000;1,6..12,200..1000&display=swap'
    ],
    style=global_style)

app.add_page(reservacion_page, route="/")
