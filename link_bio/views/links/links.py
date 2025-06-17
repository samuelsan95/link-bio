import reflex as rx
from typing import List, Dict
from link_bio.components.link_button import link_button
from link_bio.components.card import card
from link_bio.components.title import title
from link_bio.styles.styles import SizeReflex
from link_bio.constants import LINKEDIN_URL, GITHUB_URL, MEDIUM_URL, CODEWARS_URL, EMAIL_URL
from link_bio.services.publication_service import get_last_publications_medium, get_publication_description
from link_bio.services.language_service import Translator
from link_bio.utils.utils import shorten_string

MAX_CHARACTERES = 200

translator = Translator()
publications: List[Dict[str, str]] = get_last_publications_medium()


def links() -> rx.Component:
    return rx.vstack(
        title(translator.translate("title_last_publications")),
        rx.grid(
            card(
                publications[0]['title'],
                shorten_string(
                    get_publication_description(publications[0]), 
                    MAX_CHARACTERES
                ),
                publications[0]['link']
            ),
            card(
                translator.external_translate(publications[1]['title']),
                translator.external_translate(
                    shorten_string(
                        get_publication_description(publications[1]), 
                        MAX_CHARACTERES
                    )
                ),
                publications[1]['link']
            ),
            columns=rx.breakpoints(sm="1", md="2"),
            width="100%",
            spacing=SizeReflex.MEDIUM.value
        ),
        title(translator.translate("title_links")),
        link_button(
            translator.translate("linkedin_title"),
            translator.translate("linkedin_description"),
            "icons/linkedin.svg",
            LINKEDIN_URL
        ),
        link_button(
            translator.translate("github_title"),
            translator.translate("github_description"),
            "icons/github.svg",
            GITHUB_URL
        ),
        link_button(
            translator.translate("medium_title"),
            translator.translate("medium_description"),
            "icons/medium.svg",
            MEDIUM_URL
        ),
        link_button(
            translator.translate("codewars_title"),
            translator.translate("codewars_description"),
            "icons/codewars.svg",
            CODEWARS_URL
        ),

        title(translator.translate("title_contact")),
        link_button(
            translator.translate("email_title"),
            EMAIL_URL,
            "icons/email.svg",
            f"mailto::{EMAIL_URL}"
        ),

        width="100%",
        spacing=SizeReflex.MEDIUM.value
    )