import reflex as rx
from link_bio.styles.styles import card_style


def card(title: str, description: str, url: str) -> rx.Component:

    return rx.card(
        body=rx.vstack(
            rx.text(description),
        ),
        header=rx.heading(title, size="md", height="75px"),
        footer=rx.link(
            rx.heading("Ver más", size="sm"),
            href=str(url),
            is_external=True
        ),
        style=card_style
    )