"""
Define el componente visual para la leyenda de colores (simbología).

Este componente es crucial para que el usuario entienda el significado
de los colores usados en la rejilla de horarios y el mapa interactivo.
"""
from ..styles.colors import Colors
import reflex as rx

def simbologia_colores():
    """
    Crea la leyenda de colores (simbología) de la aplicación.

    Muestra una guía visual para que el usuario comprenda el significado
    de los estados de los salones.

    -   Verde (SECONDARY_GREEN): Salón Libre.
    -   Rojo (RED): Salón Reservado (probablemente por una clase regular).
    -   Negro (BLACK): Salón con Reserva Fija (ej. laboratorio, auditorio).

    Utiliza `rx.desktop_only` y `rx.mobile_and_tablet` para ajustar
    el tamaño del indicador de color en diferentes dispositivos.

    Returns:
        rx.Component: Un 'box' que contiene los elementos de la leyenda.
    """
    return rx.box(
        # --- Vista para Escritorio ---
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.avatar(background=Colors.SECONDARY_GREEN.value),
                    rx.text("Libre"),
                    align="center"
                ),
                rx.hstack(
                    rx.avatar(background=Colors.RED.value),
                    rx.text("Reservado"),
                    align="center"
                ),
                rx.hstack(
                    rx.avatar(background=Colors.BLACK.value),
                    rx.text("Reserva Fija"),
                    align="center"
                ),
            )
        ),
        # --- Vista para Móvil y Tablet ---
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.avatar(background=Colors.SECONDARY_GREEN.value, size="1"),
                    rx.text("Libre"),
                    align="center"
                ),
                rx.hstack(
                    rx.avatar(background=Colors.RED.value, size="1"),
                    rx.text("Reservado"),
                    align="center"
                ),
                rx.hstack(
                    rx.avatar(background=Colors.BLACK.value, size="1"),
                    rx.text("Reserva Fija"),
                    align="center"
                ),
            )
        ),
    )