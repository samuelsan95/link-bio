import reflex as rx
from link_bio.styles.styles import Size
from link_bio.styles.colors import TextColor
from link_bio.services.language_service import t

def footer() -> rx.Component:
    return rx.flex(
        rx.image(
            src="logo.png",
            height=Size.VERY_BIG.value,
            alt=t("alt_img_logo")
        ),
        rx.text(
            t("footer_text"),
            font_size=Size.MEDIUM.value
        ),
        padding_bottom=Size.BIG.value,
        color=TextColor.FOOTER.value,
        direction="column",
        align="center",
        width="100%"
    )