import reflex as rx
from link_bio.styles.styles import Size
from link_bio.components.info_text import info_text
from link_bio.styles.colors import TextColor, Color



def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="avatar.jpeg",
                name="Samuel Sanchez",
                size="xl",
                background_color=Color.CONTENT.value,
                color=TextColor.HEADER.value,
                padding="2px",
                border="2px",
                border_color=Color.PRIMARY.value
            ),
            rx.vstack(
                rx.heading(
                    "Samuel Sánchez",
                    size="lg"
                ),
                rx.text(
                    "@samuelsan",
                    margin_top="0px !important",
                    color=TextColor.BODY.value
                ),
                align_items="start"
            ),
            spacing=Size.DEFAULT.value
        ),
        rx.flex(
            info_text("7+", "Años de experiencia"),
            rx.spacer(),
            info_text("20+", "Participación en proyectos"),
            rx.spacer(),
            width="100%"
        ),
        rx.text(
            """Soy Samuel, un entusiasta desarrollador web con más de cinco años de experiencia en el ámbito tecnológico.
            Durante mi trayectoria, he trabajado con diversas tecnologías y lenguajes. A continuación os dejo enlaces que pueden ser
            de interés y utilidad.""",
            color=TextColor.BODY.value
        ),
        spacing=Size.BIG.value,
        align_items="start"
    )