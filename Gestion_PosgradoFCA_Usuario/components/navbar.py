import reflex as rx
from ..styles.colors import Colors
from ..styles.styles import FontSize

def navbar() -> rx.Component:
    return rx.box(
        rx.center(
            rx.hstack(
                #rx.image(src="favicon.ico"),
                rx.text("Bienvenido", font_size=[FontSize.MEDIUM.value, FontSize.EXTRA_LARGE.value], color=Colors.WHITE.value),
            )
        ),
        width="100%",
        background = Colors.PRIMARY_GREEN.value
    )