import reflex as rx
from link_bio.styles.styles import Size, navbar_title_style, logo_navbar_style
from link_bio.styles.colors import Color


def navbar() -> rx.Component:
    return rx.hstack(
        # rx.box(
                rx.image(
                    src="logo.png",
                    height=Size.EXTRA_LARGE.value,
                    alt="Logo SamuelSan",
                    style=logo_navbar_style
                ),
                rx.span(
                    "amuel",
                    color=Color.PRIMARY.value,
                    style=navbar_title_style
                ),
                rx.image(
                    src="logo.png",
                    height=Size.EXTRA_LARGE.value,
                    alt="Logo SamuelSan",
                    style=logo_navbar_style
                ),
                rx.span(
                    "an",
                    color=Color.PRIMARY.value,
                    style=navbar_title_style
                ),
        # ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index=999,
        top=0
    )