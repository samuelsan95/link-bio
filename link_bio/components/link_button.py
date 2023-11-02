import reflex as rx
import link_bio.styles.styles as styles

def link_button(text: str, body: str, image: str, url: str) -> rx.Component:
    return rx.link(
            rx.button(
                rx.hstack(
                    rx.image(
                        src=image,
                        width=styles.Size.BIG.value,
                        height=styles.Size.BIG.value,
                        margin=styles.Size.MEDIUM.value
                    ),
                    rx.vstack(
                        rx.text(text, style=styles.button_title_style),
                        rx.text(body, style=styles.button_body_style),
                        spacing=styles.Size.SMALL.value,
                        align_items="start",
                        margin=styles.Size.ZERO.value,
                    )
                )
            ),
            href=url,
            is_external=True,
            width="100%"
        )