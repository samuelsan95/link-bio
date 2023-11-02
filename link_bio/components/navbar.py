import reflex as rx
from link_bio.styles.styles import Size, navbar_title_style
from link_bio.styles.colors import Color


def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.span(
                "Samuel",
                color=Color.PRIMARY.value
            ),
            rx.span(
                "San",
                color=Color.SECONDARY.value
            ),
            style=navbar_title_style
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index=999,
        top=0
    )