import reflex as rx
from link_bio.styles.styles import link_style
from link_bio.styles.styles import SizeReflex
from link_bio.styles.colors import TextColor, Color
from link_bio.services.language_service import t


def card(title: str, description: str, url: str, lang: str = "es") -> rx.Component:
    return rx.card(
        rx.flex(
            rx.heading(
                title, 
                size=SizeReflex.MEDIUM.value, 
                min_height="75px",
                color=rx.color_mode_cond(
                    TextColor.LIGHT_HEADER.value,
                    TextColor.HEADER.value
                )
            ),
            rx.text(
                description, 
                size=SizeReflex.SMALL.value, 
                flex="1",
                color=rx.color_mode_cond(
                    TextColor.LIGHT_BODY.value,
                    TextColor.BODY.value
                )
            ),
            rx.link(
                rx.heading(
                    t("card_see_more", lang), 
                    size=SizeReflex.SMALL.value,
                    color=rx.color_mode_cond(
                        TextColor.LIGHT_HEADER.value,
                        TextColor.HEADER.value
                    )
                ),
                href=url,
                is_external=True,
                style=link_style
            ),
            direction="column",
            spacing=SizeReflex.BIG.value,
            height="100%"
        ),
        style={
            "&::after": {
                "borderRadius": '1.2em'
            }
        },
        background_color=rx.color_mode_cond(
            Color.LIGHT_CONTENT.value,
            Color.CONTENT.value
        ),
        _hover={
            "background_color": rx.color_mode_cond(
                Color.LIGHT_SECONDARY.value,
                Color.SECONDARY.value
            ),
        },
        size="3",
        height="100%"
    )