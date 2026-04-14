import reflex as rx
from link_bio.styles.styles import Size
from link_bio.styles.colors import TextColor, Color
from link_bio.services.language_service import t

def footer(lang: str = "es") -> rx.Component:
    card_href = "/card" if lang == "es" else "/en/card"
    return rx.flex(
        rx.image(
            src="logo.png",
            height=Size.VERY_BIG.value,
            alt=t("alt_img_logo", lang)
        ),
        rx.text(
            t("footer_text", lang),
            font_size=Size.MEDIUM.value
        ),
        rx.link(
            rx.hstack(
                rx.icon("credit-card", size=14),
                rx.text(t("card_footer_link", lang), size="2"),
                spacing="1",
                align="center"
            ),
            href=card_href,
            color=rx.color_mode_cond(
                Color.LIGHT_ACCENT.value,
                Color.PRIMARY.value
            ),
            margin_top=Size.SMALL.value,
            opacity="0.7",
            _hover={"opacity": "1"}
        ),
        padding_bottom=Size.BIG.value,
        color=rx.color_mode_cond(
            TextColor.LIGHT_FOOTER.value,
            TextColor.FOOTER.value
        ),
        direction="column",
        align="center",
        width="100%"
    )