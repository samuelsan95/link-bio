import reflex as rx
from link_bio.styles.styles import Size


def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Samuelsan",
        ),
        position="sticky",
        bg="lightgray",
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index=999,
        top=0
    )