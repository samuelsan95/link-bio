import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.colors import Color, TextColor

def link_button(title: str, body: str, image: str, url: str) -> rx.Component:
    return rx.link(
            rx.button(
                rx.hstack(
                    rx.image(
                        src=image,
                        width=styles.Size.BIG.value,
                        height=styles.Size.BIG.value,
                        margin=styles.Size.MEDIUM.value,
                        alt=title,
                        loading="lazy",
                        style={
                            "filter": rx.color_mode_cond(
                                "invert(1)",
                                "none"
                            )
                        }
                    ),
                    rx.vstack(
                        rx.text(title, style=styles.get_button_title_style(), size=styles.SizeReflex.MEDIUM.value),
                        rx.text(body, style=styles.get_button_body_style(), size=styles.SizeReflex.SMALL.value),
                        spacing=styles.SizeReflex.SMALL.value,
                        align_items="start",
                        margin=styles.Size.ZERO.value,
                        padding_right=styles.Size.SMALL.value
                    ),
                    width="100%"
                ),
                style=styles.link_style,
                background_color=rx.color_mode_cond(
                    Color.LIGHT_CONTENT.value,
                    Color.CONTENT.value
                ),
                color=rx.color_mode_cond(
                    TextColor.LIGHT_HEADER.value,
                    TextColor.HEADER.value
                ),
                _hover={
                    "background_color": rx.color_mode_cond(
                        Color.LIGHT_SECONDARY.value,
                        Color.SECONDARY.value
                    ),
                }
            ),
            href=url,
            is_external=True,
            width="100%"
        )