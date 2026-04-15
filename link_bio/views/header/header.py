import reflex as rx
from link_bio.styles.styles import Size, SizeReflex
from link_bio.components.info_text import info_text
from link_bio.styles.colors import TextColor, Color
from link_bio.services.language_service import t


def header(lang: str = "es") -> rx.Component:
    card_href = "/card" if lang == "es" else "/en/card"
    return rx.vstack(
        rx.flex(
            rx.box(
                rx.image(
                    src="avatar.webp",
                    alt=t("avatar_alt", lang),
                    width="100%",
                    height="100%",
                    border_radius="9999px",
                    object_fit="cover",
                    loading="eager",
                    html_width="192",
                    html_height="192"
                ),
                width="96px",
                height="96px",
                background_color=rx.color_mode_cond(
                    Color.LIGHT_CONTENT.value,
                    Color.CONTENT.value
                ),
                padding="2px",
                border_width="2px",
                border_style="solid",
                border_color=rx.color_mode_cond(
                    Color.LIGHT_ACCENT.value,
                    Color.PRIMARY.value
                ),
                border_radius="9999px",
                flex_shrink="0"
            ),
            rx.vstack(
                rx.heading(
                    "Samuel Sánchez",
                    size=SizeReflex.VERY_BIG.value
                ),
                rx.link(
                    rx.hstack(
                        rx.icon("credit-card", size=14),
                        rx.text(t("card_footer_link", lang), font_size=SizeReflex.SMALL.value),
                        spacing="1",
                        align="center"
                    ),
                    href=card_href,
                    color=rx.color_mode_cond(
                        Color.LIGHT_ACCENT.value,
                        Color.PRIMARY.value
                    ),
                    _hover={"opacity": "1"},
                    spacing=SizeReflex.SMALL.value,
                ),
                align_items="start"
            ),
            direction="row",
            spacing=SizeReflex.SMALL.value,
            align="center"
        ),
        rx.flex(
            info_text("10+", t("info_text_1", lang)),
            rx.spacer(),
            info_text("20+", t("info_text_2", lang)),
            rx.spacer(),
            width="100%",
            direction="row"
        ),
        rx.text(
            t("bio_text", lang),
            color=rx.color_mode_cond(
                TextColor.LIGHT_BODY.value,
                TextColor.BODY.value
            )
        ),
        spacing=SizeReflex.BIG.value,
        align_items="start"
    )
