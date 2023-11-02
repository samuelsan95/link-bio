import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size
from link_bio.constants import LINKEDIN_URL, GITHUB_URL, MEDIUM_URL, CODEWARS_URL, EMAIL_URL

def links() -> rx.Component:
    return rx.vstack(
        title("Enlaces de interés"),
        link_button(
            "Linkedin",
            "Curriculum online",
            "icons/linkedin.svg",
            LINKEDIN_URL
        ),
        link_button(
            "Github",
            "Proyectos personales",
            "icons/github.svg",
            GITHUB_URL
        ),
        link_button(
            "Medium",
            "Todos mis articulos relacionados con programación",
            "icons/medium.svg",
            MEDIUM_URL
        ),
        link_button(
            "Codewars",
            "Desafíos resueltos",
            "icons/codewars.svg",
            CODEWARS_URL
        ),

        title("Contacto"),
        link_button(
            "Email",
            EMAIL_URL,
            "icons/email.svg",
            f"mailto::{EMAIL_URL}"
        ),

        width="100%",
        spacing=Size.MEDIUM.value
    )