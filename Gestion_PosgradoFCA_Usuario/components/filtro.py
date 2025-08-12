import reflex as rx
import datetime
from ..styles.colors import Colors
from ..styles.styles import FontSize
from ..state import Tabla_ConsultaHorarios

def calendar() -> rx.Component:
    return rx.box(
        rx.tablet_and_desktop(
            rx.input(
                #min=datetime.datetime.now(), Falta configurar
                default_value=Tabla_ConsultaHorarios.fecha_seleccionada,
                type="date",
                size="3",
                on_change=Tabla_ConsultaHorarios.filter_fecha
            ),
        ),
        rx.mobile_only(
            rx.input(
                #min=datetime.datetime.now(), Falta configurar
                default_value=Tabla_ConsultaHorarios.fecha_seleccionada,
                type="date",
                size="1",
                on_change=Tabla_ConsultaHorarios.filter_fecha
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
                Tabla_ConsultaHorarios.grupos,
                placeholder="Grupo",
                size="3",
                width="150px",
                on_change=Tabla_ConsultaHorarios.filter_grupo,
            )
        ),
        rx.mobile_only(
            rx.select(
                Tabla_ConsultaHorarios.grupos,
                placeholder="Grupo",
                size="1",
                width="80px",
                on_change=Tabla_ConsultaHorarios.filter_grupo,
            )
        )
    )

def hora() -> rx.Component:
    return rx.box(
        rx.tablet_and_desktop(
            rx.select(
                Tabla_ConsultaHorarios.horas,
                default_value=Tabla_ConsultaHorarios.select_horas,
                placeholder="Hora",
                size="3",
                width="150px",
                on_change=Tabla_ConsultaHorarios.filter_hora,
                #on_mount=Tabla_ConsultaHorarios.informacion_horarios
            )
        ),
        rx.mobile_only(
            rx.select(
                Tabla_ConsultaHorarios.horas,
                default_value=Tabla_ConsultaHorarios.select_horas,
                placeholder="Hora",
                size="1",
                width="80px",
                on_change=Tabla_ConsultaHorarios.filter_hora,
                #on_mount=Tabla_ConsultaHorarios.informacion_horarios
            )
        )
    )