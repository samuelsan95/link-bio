import reflex as rx
from link_bio.styles.styles import Size
from link_bio.styles.colors import TextColor
from link_bio.services.language_service import Translator

translator = Translator()

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="logo.png",
            height=Size.VERY_BIG.value,
            alt=translator.translate("title_contact")
        ),
        rx.text(
            translator.translate("footer_text"),
            font_size=Size.MEDIUM.value
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        color=TextColor.FOOTER.value
    )