import reflex as rx
from link_bio.styles.styles import Size
from link_bio.components.info_text import info_text


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Samuel Sanchez",
                size="xl"
            ),
            rx.vstack(
                rx.heading(
                    "Samuel Sánchez",
                    size="lg"
                ),
                rx.text(
                    "@samuelsan",
                    margin_top="0px !important"
                ),
                align_items="start"
            ),
            spacing=Size.DEFAULT.value
        ),
        rx.flex(
            info_text("+7", "Años de experiencia"),
            rx.spacer(),
            info_text("+7", "Años de experiencia"),
            rx.spacer(),
            info_text("+7", "Años de experiencia"),
            width="100%"
        ),
        rx.text(
            """Mi nombre es Samuel y soy un desarrollador web apasionado del mundo tecnológico,
            con una experiencia de más de 5 años en el sector utilizando tecnologías y lenguajes
            como JavaScript y sus frameworks Angular 2+, Vue y NodeJs, HTML5, CSS3, Bootstrap y SQL"""
        ),
        spacing=Size.BIG.value,
        align_items="start"
    )