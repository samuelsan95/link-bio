import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size


def links() -> rx.Component:
    return rx.vstack(
        title("Enlaces de interés"),
        link_button(
            "Linkedin",
            "Curriculum online",
            "https://www.linkedin.com/in/samuel-sanchez-lopez/"
        ),
        link_button(
            "Github",
            "Proyectos personales",
            "https://github.com/samuelsan95"
        ),
        link_button(
            "Medium",
            "Todos mis articulos relacionados con programación",
            "https://medium.com/@sanchezlopezsamuel"
        ),
        link_button(
            "Codewars",
            "Desafíos resueltos",
            "https://medium.com/@sanchezlopezsamuel"
        ),
        width="100%",
        spacing=Size.MEDIUM.value
    )