import reflex as rx
from typing import List, Dict
from link_bio.components.link_button import link_button
from link_bio.components.card import card
from link_bio.components.title import title
from link_bio.styles.styles import SizeReflex
from link_bio.constants import LINKEDIN_URL, GITHUB_URL, MEDIUM_URL, CODEWARS_URL, EMAIL_URL
from link_bio.services.publication_service import get_last_publications_medium, get_publication_description
from link_bio.services.language_service import Translator, t
from link_bio.utils.utils import shorten_string
from link_bio.language_state import LanguageState

MAX_CHARACTERES = 200

translator = Translator()
publications: List[Dict[str, str]] = get_last_publications_medium()


def links() -> rx.Component:
    return rx.vstack(
        title(t("title_last_publications")),
        rx.grid(
            card(
                rx.cond(
                    LanguageState.language == "es",
                    publications[0]['title'],
                    translator.external_translate(publications[0]['title'], "en")
                ),
                rx.cond(
                    LanguageState.language == "es",
                    shorten_string(
                        get_publication_description(publications[0]), 
                        MAX_CHARACTERES
                    ),
                    translator.external_translate(
                        shorten_string(
                            get_publication_description(publications[0]), 
                            MAX_CHARACTERES
                        ),
                        "en"
                    )
                ),
                publications[0]['link']
            ),
            card(
                rx.cond(
                    LanguageState.language == "es",
                    publications[1]['title'],
                    translator.external_translate(publications[1]['title'], "en")
                ),
                rx.cond(
                    LanguageState.language == "es",
                    shorten_string(
                        get_publication_description(publications[1]), 
                        MAX_CHARACTERES
                    ),
                    translator.external_translate(
                        shorten_string(
                            get_publication_description(publications[1]), 
                            MAX_CHARACTERES
                        ),
                        "en"
                    )
                ),
                publications[1]['link']
            ),
            columns=rx.breakpoints(sm="1", md="2"),
            width="100%",
            spacing=SizeReflex.MEDIUM.value
        ),
        title(t("title_links")),
        link_button(
            t("linkedin_title"),
            t("linkedin_description"),
            "icons/linkedin.svg",
            LINKEDIN_URL
        ),
        link_button(
            t("github_title"),
            t("github_description"),
            "icons/github.svg",
            GITHUB_URL
        ),
        link_button(
            t("medium_title"),
            t("medium_description"),
            "icons/medium.svg",
            MEDIUM_URL
        ),
        link_button(
            t("codewars_title"),
            t("codewars_description"),
            "icons/codewars.svg",
            CODEWARS_URL
        ),

        title(t("title_contact")),
        link_button(
            t("email_title"),
            EMAIL_URL,
            "icons/email.svg",
            f"mailto::{EMAIL_URL}"
        ),

        width="100%",
        spacing=SizeReflex.MEDIUM.value
    )
