import reflex as rx
from link_bio.styles.styles import link_style
from link_bio.styles.styles import SizeReflex


def card(title: str, description: str, url: str) -> rx.Component:
    return rx.card(
        rx.flex(
            rx.heading(title, size=SizeReflex.MEDIUM.value, height="75px"),
            rx.text(description, size=SizeReflex.SMALL.value),
            rx.link(
                rx.heading("Ver más", size=SizeReflex.SMALL.value),
                href=url,
                is_external=True,
                style=link_style
            ),
            direction="column",
            spacing=SizeReflex.BIG.value
        ),
        style={
            "&::after": {
                "borderRadius": '1.2em'
            }
        },
        size="3"
    )