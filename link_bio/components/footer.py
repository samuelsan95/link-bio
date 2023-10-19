import reflex as rx
from link_bio.styles.styles import Size


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico"
        ),
        rx.text(
            "...Lorem impsum....",
            font_size=Size.MEDIUM.value
        ),
        margin_bottom=Size.BIG.value
    )