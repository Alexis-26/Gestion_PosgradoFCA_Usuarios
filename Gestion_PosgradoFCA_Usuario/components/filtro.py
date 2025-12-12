"""
Definición de Componentes de UI para los Filtros de Consulta.

Este archivo crea funciones de componentes reutilizables (widgets)
que se usan en la barra de filtros de la página de consulta de horarios.
Cada componente se conecta a la variable o manejador de eventos
correspondiente del estado 'ConsultaHorarios'.
"""
import reflex as rx
from ..styles.colors import Colors
from ..state import ConsultaHorarios


def calendar() -> rx.Component:
    """
    Crea el componente de filtro de calendario (selector de fecha).

    Se conecta a `ConsultaHorarios.filter_fecha` para actualizar el estado
    cuando el usuario cambia la fecha.
    Utiliza `rx.tablet_and_desktop` y `rx.mobile_only` para
    ajustar el tamaño ('size') del input en diferentes dispositivos.

    Returns:
        rx.Component: Un componente 'box' con un input de tipo 'date'.
    """
    return rx.box(
        # --- Vista para Tablet y Escritorio ---
        rx.tablet_and_desktop(
            rx.vstack(
                rx.text("Filtro de fecha", size="4"),
                rx.input(
                    min=ConsultaHorarios.min_date, # No se pueden seleccionar fechas pasadas
                    default_value=ConsultaHorarios.fecha_hoy, # Valor inicial
                    name="filtro_fecha",
                    type="date",
                    size="3",
                    on_change=ConsultaHorarios.filter_fecha # Llama al handler del state
                ),
                spacing="0"
            )
        ),
        # --- Vista para Móvil ---
        rx.mobile_only(
            rx.vstack(
                rx.text("Filtro de fecha", size="2"),
                rx.input(
                    min=ConsultaHorarios.min_date,
                    default_value=ConsultaHorarios.fecha_hoy,
                    name="filtro_fecha",
                    type="date",
                    size="1",
                    on_change=ConsultaHorarios.filter_fecha
                ),
                spacing="0"
            )
        ),
        #background="green"
    )

def search_docente() -> rx.Component:
    """
    Crea el componente de búsqueda de docente (placeholder).

    Actualmente es un componente visual sin lógica de estado.
    La funcionalidad de búsqueda no está implementada.

    Returns:
        rx.Component: Un 'box' con un 'hstack' que contiene
                      un 'input' y un 'button'.
    """
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
    """
    Crea el componente de búsqueda de materia (placeholder).

    Actualmente es un componente visual sin lógica de estado.
    La funcionalidad de búsqueda no está implementada.

    Returns:
        rx.Component: Un 'box' con un 'hstack' que contiene
                      un 'input' y un 'button'.
    """
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
    """
    Crea el componente de filtro de grupo (placeholder para futuro).

    Este componente está visualmente presente pero su funcionalidad
    (lista de grupos y el handler 'on_change') está comentada
    para una implementación futura.

    Returns:
        rx.Component: Un componente 'select' (menú desplegable) deshabilitado.
    """
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
    """
    Crea el componente de filtro de hora (selector de hora).

    Se conecta a `ConsultaHorarios.filter_hora` para actualizar el estado.
    Puebla sus opciones desde `ConsultaHorarios.horas` y establece
    el valor por defecto a `ConsultaHorarios.hora_actual`.

    Returns:
        rx.Component: Un 'box' con un componente 'select' para las horas.
    """
    # Se asigna la variable de estado computada para usarla en 'default_value'
    hora = ConsultaHorarios.hora_actual
    return rx.box(
        rx.tablet_and_desktop(
            rx.vstack(
                rx.text("Filtro de hora", size="4"),
                rx.select(
                    ConsultaHorarios.horas, # Opciones del 'select'
                    default_value=hora, # Valor inicial
                    placeholder="Hora",
                    name="filtro_hora",
                    size="3",
                    width="150px",
                    position="popper",
                    on_change=ConsultaHorarios.filter_hora, # Handler del state
                ),
                spacing="0"
            )
        ),
        rx.mobile_only(
            rx.vstack(
                rx.text("Filtro de hora", size="2"),
                rx.select(
                    ConsultaHorarios.horas,
                    default_value=hora,
                    placeholder="Hora",
                    name="filtro_hora",
                    size="1",
                    width="80px",
                    position="popper",
                    on_change=ConsultaHorarios.filter_hora,
                    #on_mount=Tabla_ConsultaHorarios.informacion_horarios
                ),
                spacing="0"
            )
        )
    )