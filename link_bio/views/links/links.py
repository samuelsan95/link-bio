import reflex as rx
from typing import List, Dict
from link_bio.components.link_button import link_button
from link_bio.components.card import card
from link_bio.components.title import title
from link_bio.styles.styles import Size
from link_bio.constants import LINKEDIN_URL, GITHUB_URL, MEDIUM_URL, CODEWARS_URL, EMAIL_URL
from link_bio.services.publication_service import get_last_publications_medium, get_publication_image, get_publication_description


publications: List[Dict[str, str]] = get_last_publications_medium()


def links() -> rx.Component:
    return rx.vstack(
        title("Últimas publicaciones"),
        rx.hstack(
            card(
                publications[0]['title'],
                get_publication_description(publications[0]),
                get_publication_image(publications[0]),
                publications[0]['link']
            ),
            card(
                publications[1]['title'],
                get_publication_description(publications[1]),
                get_publication_image(publications[1]),
                publications[1]['link']
            )
        ),
        title("Enlaces de interés"),
        link_button(
            "Linkedin",
            "Curriculum online",
            "icons/medium.svg",
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