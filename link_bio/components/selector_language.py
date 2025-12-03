import reflex as rx
from link_bio.styles.colors import Color
from link_bio.styles.styles import Size


def selector_language(current_lang: str) -> rx.Component:
    target_lang = "en" if current_lang == "es" else "es"
    target_url = "/en" if current_lang == "es" else "/"
    button_text = "EN" if current_lang == "es" else "ES"
    
    return rx.link(
        rx.button(
            rx.text(
                button_text,
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
            width="48px"
        ),
        href=target_url,
        underline="none"
    )
