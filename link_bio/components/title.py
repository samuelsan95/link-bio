import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import SizeReflex


def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        style=styles.title_style,
        size=SizeReflex.BIG.value
    )