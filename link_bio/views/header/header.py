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
            info_text("7+", "Años de experiencia"),
            rx.spacer(),
            info_text("7+", "Años de experiencia"),
            width="100%"
        ),
        rx.text(
            """Mi nombre es Samuel y soy un desarrollador web apasionado del mundo tecnológico,
            con una experiencia de más de 5 años en el sector utilizando tecnologías y lenguajes
            como JavaScript y sus frameworks Angular 2+, Vue y NodeJs, HTML5, CSS3, Bootstrap y SQL""",
            color=TextColor.BODY.value
        ),
        spacing=Size.BIG.value,
        align_items="start"
    )