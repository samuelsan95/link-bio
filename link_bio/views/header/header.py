import reflex as rx
from link_bio.styles.styles import Size, SizeReflex
from link_bio.components.info_text import info_text
from link_bio.styles.colors import TextColor, Color
from link_bio.services.language_service import Translator

translator = Translator()


def header() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.avatar(
                src="avatar.jpeg",
                name="Samuel Sanchez",
                size=SizeReflex.BIG.value,
                background_color=Color.CONTENT.value,
                color=TextColor.HEADER.value,
                padding="2px",
                border="2px",
                border_color=Color.PRIMARY.value,
                radius="full"
            ),
            rx.vstack(
                rx.heading(
                    "Samuel Sánchez",
                    size=SizeReflex.VERY_BIG.value
                ),
                rx.text(
                    "@samuelsan",
                    margin_top="0px !important",
                    color=TextColor.BODY.value
                ),
                align_items="start"
            ),
            direction="row",
            spacing=SizeReflex.MEDIUM.value,
            align="center"
        ),
        rx.flex(
            info_text("7+", translator.translate("info_text_1")),
            rx.spacer(),
            info_text("20+", translator.translate("info_text_2")),
            rx.spacer(),
            width="100%",
            direction="row"
        ),
        rx.text(
            translator.translate("bio_text"),
            color=TextColor.BODY.value
        ),
        spacing=SizeReflex.BIG.value,
        align_items="start"
    )