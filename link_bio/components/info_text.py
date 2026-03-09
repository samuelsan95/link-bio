import reflex as rx
from link_bio.styles.styles import Size
from link_bio.styles.colors import TextColor, Color


def info_text(title: str, body: str) -> rx.Component:
    return rx.flex(
        rx.text(
            title,
            font_weight="bold",
            color=rx.color_mode_cond(
                Color.LIGHT_ACCENT.value,
                Color.PRIMARY.value
            )
        ),

        rx.text(
            body,
            font_size=Size.MEDIUM.value,
            color=rx.color_mode_cond(
                TextColor.LIGHT_BODY.value,
                TextColor.BODY.value
            )
        ),
        direction="row",
        spacing="2"
    )