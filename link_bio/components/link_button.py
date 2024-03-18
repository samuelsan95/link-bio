import reflex as rx
import link_bio.styles.styles as styles

def link_button(title: str, body: str, image: str, url: str) -> rx.Component:
    return rx.link(
            rx.button(
                rx.hstack(
                    rx.image(
                        src=image,
                        width=styles.Size.BIG.value,
                        height=styles.Size.BIG.value,
                        margin=styles.Size.MEDIUM.value,
                        alt=title
                    ),
                    rx.vstack(
                        rx.text(title, style=styles.button_title_style),
                        rx.text(body, style=styles.button_body_style),
                        spacing=styles.Size.SMALL.value,
                        align_items="start",
                        margin=styles.Size.ZERO.value,
                        padding_right=styles.Size.SMALL.value
                    ),
                    width="100%"
                )
            ),
            href=url,
            is_external=True,
            width="100%"
        )