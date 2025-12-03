import reflex as rx
from link_bio.styles.colors import Color
from link_bio.styles.styles import Size
from link_bio.language_state import LanguageState


def selector_language() -> rx.Component:
    return rx.menu.root(
        rx.menu.trigger(
            rx.button(
                rx.text(
                    rx.cond(
                        LanguageState.language == "es",
                        "ES",
                        "EN"
                    ),
                    font_weight="600",
                    color=Color.PRIMARY.value
                ),
                background_color=Color.SECONDARY.value,
                padding=Size.SMALL.value,
                border_radius="8px",
                border=f"2px solid {Color.PRIMARY.value}",
                cursor="pointer",
                _hover={
                    "background_color": Color.CONTENT.value,
                    "transition": "all 0.2s ease"
                },
                display="flex",
                align_items="center",
                justify_content="center",
                gap="4px",
                width="68px"
            )
        ),
        rx.menu.content(
            rx.menu.item(
                rx.hstack(
                    rx.text("ES", font_weight="500"),
                    spacing="2"
                ),
                on_click=lambda: LanguageState.set_language("es"),
                cursor="pointer",
                background_color=rx.cond(
                    LanguageState.language == "es",
                    Color.PRIMARY.value,
                    "transparent"
                ),
                color=rx.cond(
                    LanguageState.language == "es",
                    Color.BACKGROUND.value,
                    Color.PRIMARY.value
                ),
                _hover={
                    "background_color": Color.PRIMARY.value,
                    "color": Color.BACKGROUND.value
                },
                padding="8px 12px",
                border_radius="4px",
                margin_bottom="4px"
            ),
            rx.menu.item(
                rx.hstack(
                    rx.text("EN", font_weight="500"),
                    spacing="2"
                ),
                on_click=lambda: LanguageState.set_language("en"),
                cursor="pointer",
                background_color=rx.cond(
                    LanguageState.language == "en",
                    Color.PRIMARY.value,
                    "transparent"
                ),
                color=rx.cond(
                    LanguageState.language == "en",
                    Color.BACKGROUND.value,
                    Color.PRIMARY.value
                ),
                _hover={
                    "background_color": Color.PRIMARY.value,
                    "color": Color.BACKGROUND.value
                },
                padding="8px 12px",
                border_radius="4px"
            ),
            background_color=Color.CONTENT.value,
            border=f"1px solid {Color.PRIMARY.value}",
            border_radius="8px",
            padding="4px"
        )
    )
