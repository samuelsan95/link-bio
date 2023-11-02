import reflex as rx
from link_bio.styles.styles import Size
from link_bio.styles.colors import TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico"
        ),
        rx.text(
            "...Lorem impsum....",
            font_size=Size.MEDIUM.value
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        color=TextColor.FOOTER.value
    )