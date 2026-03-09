import reflex as rx
from link_bio.styles.styles import Size, SizeReflex
from link_bio.styles.colors import Color, TextColor
from link_bio.components.selector_language import selector_language
from link_bio.services.language_service import t
from link_bio.components.theme_button import theme_button


def _nav_link(text: str, href: str) -> rx.Component:
    return rx.link(
        text,
        href=href,
        color=TextColor.HEADER.value,
        font_size=Size.DEFAULT.value,
        display="block",
        padding=Size.SMALL.value,
        border_radius="8px",
        width="100%",
        underline="none",
        _hover={
            "background_color": Color.SECONDARY.value,
            "color": Color.PRIMARY.value,
        },
        transition="all 0.2s ease"
    )


def hamburger_button() -> rx.Component:
    return rx.el.label(
        rx.box(
            width="22px",
            height="2px",
            background_color=Color.PRIMARY.value,
            border_radius="2px",
            class_name="hamburger-line"
        ),
        rx.box(
            width="22px",
            height="2px",
            background_color=Color.PRIMARY.value,
            border_radius="2px",
            class_name="hamburger-line"
        ),
        rx.box(
            width="22px",
            height="2px",
            background_color=Color.PRIMARY.value,
            border_radius="2px",
            class_name="hamburger-line"
        ),
        html_for="nav-toggle",
        display="flex",
        flex_direction="column",
        justify_content="center",
        gap="5px",
        cursor="pointer",
        padding=Size.SMALL.value,
        border_radius="8px",
        aria_label="Menú de navegación",
        _hover={
            "background_color": Color.SECONDARY.value
        },
        transition="background-color 0.2s ease",
        class_name="hamburger-btn"
    )


def hamburger_menu(lang: str) -> rx.Component:
    return rx.box(
        rx.script(
            "document.addEventListener('click', function(e) {"
            "  if (e.target.closest('.nav-menu a')) {"
            "    document.getElementById('nav-toggle').checked = false;"
            "  }"
            "});"
        ),
        rx.vstack(
            _nav_link(t("title_last_publications", lang), "#publications"),
            _nav_link(t("title_projects", lang), "#projects"),
            _nav_link(t("title_links", lang), "#links"),
            _nav_link(t("title_contact", lang), "#contact"),
            rx.box(
                height="1px",
                width="100%",
                background_color="rgba(211, 226, 159, 0.3)"
            ),
            rx.hstack(
                theme_button(),
                selector_language(lang),
                spacing="4",
                align="center",
                padding_left=Size.SMALL.value
            ),
            align_items="start",
            spacing=SizeReflex.SMALL.value,
            padding_x=Size.BIG.value,
            padding_top=Size.SMALL.value,
            padding_bottom=Size.DEFAULT.value
        ),
        background_color=Color.CONTENT.value,
        class_name="nav-menu"
    )
