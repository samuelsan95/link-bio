import reflex as rx
from typing import List, Dict
from link_bio.components.link_button import link_button
from link_bio.components.card import card
from link_bio.components.title import title
from link_bio.styles.styles import SizeReflex
from link_bio.constants import LINKEDIN_URL, GITHUB_URL, MEDIUM_URL, CODEWARS_URL, EMAIL_URL
from link_bio.services.publication_service import get_last_publications_medium, get_publication_description
from link_bio.services.language_service import t, _translator
from link_bio.utils.utils import shorten_string

MAX_CHARACTERES = 200

translator = _translator
publications: List[Dict[str, str]] = get_last_publications_medium()


def links(lang: str = "es") -> rx.Component:
    has_publications = len(publications) >= 2
    
    return rx.vstack(
        rx.cond(
            has_publications,
            rx.vstack(
                title(t("title_last_publications", lang)),
                rx.grid(
                    card(
                        rx.cond(
                            lang == "es",
                            publications[0]['title'],
                            translator.external_translate(publications[0]['title'], "en")
                        ),
                        rx.cond(
                            lang == "es",
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
                        publications[0]['link'],
                        lang
                    ),
                    card(
                        rx.cond(
                            lang == "es",
                            publications[1]['title'],
                            translator.external_translate(publications[1]['title'], "en")
                        ),
                        rx.cond(
                            lang == "es",
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
                        publications[1]['link'],
                        lang
                    ),
                    columns=rx.breakpoints(sm="1", md="2"),
                    width="100%",
                    spacing=SizeReflex.MEDIUM.value
                ),
                width="100%",
                spacing=SizeReflex.MEDIUM.value
            ),
            rx.fragment()
        ),
        title(t("title_links", lang)),
        link_button(
            t("linkedin_title", lang),
            t("linkedin_description", lang),
            "icons/linkedin.svg",
            LINKEDIN_URL
        ),
        link_button(
            t("github_title", lang),
            t("github_description", lang),
            "icons/github.svg",
            GITHUB_URL
        ),
        link_button(
            t("medium_title", lang),
            t("medium_description", lang),
            "icons/medium.svg",
            MEDIUM_URL
        ),
        link_button(
            t("codewars_title", lang),
            t("codewars_description", lang),
            "icons/codewars.svg",
            CODEWARS_URL
        ),

        title(t("title_contact", lang)),
        link_button(
            t("email_title", lang),
            EMAIL_URL,
            "icons/email.svg",
            f"mailto:{EMAIL_URL}"
        ),

        width="100%",
        spacing=SizeReflex.MEDIUM.value
    )
