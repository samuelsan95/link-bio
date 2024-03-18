import reflex as rx
from link_bio.styles.styles import card_style
from link_bio.utils.utils import shorten_string

MAX_CHARACTERES = 200

def card(title: str, description: str, url: str) -> rx.Component:

    return rx.card(
        body=rx.vstack(
            rx.text(
                shorten_string(description, MAX_CHARACTERES)
            ),
        ),
        header=rx.heading(title, size="md", height="75px"),
        footer=rx.link(
            rx.heading("Ver más", size="sm"),
            href=str(url),
            is_external=True
        ),
        style=card_style
    )