import reflex as rx
import datetime
from ..styles.colors import Colors
from ..styles.styles import FontSize
from ..state import ConsultaHorarios

def calendar() -> rx.Component:
    return rx.box(
        rx.tablet_and_desktop(
            rx.input(
                #min=datetime.datetime.now(), Falta configurar
                default_value=ConsultaHorarios.fecha_seleccionada,
                name="filtro_fecha",
                type="date",
                size="3",
                on_change=ConsultaHorarios.filter_fecha
            ),
        ),
        rx.mobile_only(
            rx.input(
                #min=datetime.datetime.now(), Falta configurar
                default_value=ConsultaHorarios.fecha_seleccionada,
                name="filtro_fecha",
                type="date",
                size="1",
                on_change=ConsultaHorarios.filter_fecha
            ),
        ),
        #background="green"
    )

def search_docente() -> rx.Component:
    return rx.box(
        rx.tablet_and_desktop(
            rx.hstack(
                rx.input(
                    placeholder="Buscar Docente",
                    size="3",
                    width="100%"
                ),
                rx.button(
                    rx.icon("search"),
                    size="3",
                    background=Colors.PRIMARY_ORANGE.value
                ),
                spacing="1",
                #background="blue",
            ),
        ),
        rx.mobile_only(
            rx.hstack(
                rx.input(
                    placeholder="Buscar Docente",
                    size="1",
                    width="100%"
                ),
                rx.button(
                    rx.icon("search", size=20),
                    size="1",
                    background=Colors.PRIMARY_ORANGE.value
                ),
                spacing="1",
                #background="blue",
            ),
        ),
        width=["80%", "30%"]
    )

def search_materia() -> rx.Component:
    return rx.box(
        rx.tablet_and_desktop(
            rx.hstack(
                rx.input(
                    placeholder="Buscar Materia",
                    size="3",
                    width="100%",
                ),
                rx.button(
                    rx.icon("search"),
                    size="3",
                    background=Colors.PRIMARY_ORANGE.value
                ),
                spacing="1",
                #background="blue",
            ),
        ),
        rx.mobile_only(
            rx.hstack(
                rx.input(
                    placeholder="Buscar Materia",
                    size="1",
                    width="100%"
                ),
                rx.button(
                    rx.icon("search", size=20),
                    size="1",
                    background=Colors.PRIMARY_ORANGE.value
                ),
                spacing="1",
                #background="blue",
            ),
        ),
        width=["80%", "30%"]
    )

def grupo() -> rx.Component:
    return rx.box(
        rx.tablet_and_desktop(
            rx.select(
                #Tabla_ConsultaHorarios.grupos,
                placeholder="Grupo",
                size="3",
                width="150px",
                #on_change=Tabla_ConsultaHorarios.filter_grupo,
            )
        ),
        rx.mobile_only(
            rx.select(
               # Tabla_ConsultaHorarios.grupos,
                placeholder="Grupo",
                size="1",
                width="80px",
                #on_change=Tabla_ConsultaHorarios.filter_grupo,
            )
        )
    )

def hora() -> rx.Component:
    return rx.box(
        rx.tablet_and_desktop(
            rx.select(
                ConsultaHorarios.horas,
                default_value=ConsultaHorarios.select_horas,
                placeholder="Hora",
                name="filtro_hora",
                size="3",
                width="150px",
                on_change=ConsultaHorarios.filter_hora,
                #on_mount=Tabla_ConsultaHorarios.informacion_horarios
            )
        ),
        rx.mobile_only(
            rx.select(
                ConsultaHorarios.horas,
                default_value=ConsultaHorarios.select_horas,
                placeholder="Hora",
                name="filtro_hora",
                size="1",
                width="80px",
                on_change=ConsultaHorarios.filter_hora,
                #on_mount=Tabla_ConsultaHorarios.informacion_horarios
            )
        )
    )