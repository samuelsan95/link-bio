import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.colors import Color

def theme_button() -> rx.Component:
    return rx.button(
        rx.color_mode_cond(
            rx.icon(tag="moon"),
            rx.icon(tag="sun"),
        ),
        width="48px",
        on_click=rx.toggle_color_mode,
        padding=styles.Size.SMALL.value,
        border_radius=styles.Size.DEFAULT.value,
        background_color=Color.CONTENT.value,
        color=Color.PRIMARY.value,
        _hover={
            "background_color": Color.SECONDARY.value,
        }
    )
