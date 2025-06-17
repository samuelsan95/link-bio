import reflex as rx
from link_bio.styles.styles import Size, navbar_title_style, logo_navbar_style
from link_bio.styles.colors import Color


def navbar() -> rx.Component:
    return rx.hstack(
        rx.flex(
            rx.image(
                src="logo.png",
                height=Size.EXTRA_LARGE.value,
                alt="Logo SamuelSan",
                style=logo_navbar_style
            ),
            rx.text(
                "amuel",
                color=Color.PRIMARY.value,
                style=navbar_title_style,
                as_="span"
            ),
            rx.image(
                src="logo.png",
                height=Size.EXTRA_LARGE.value,
                alt="Logo SamuelSan",
                style=logo_navbar_style
            ),
            rx.text(
                "an",
                color=Color.PRIMARY.value,
                style=navbar_title_style,
                as_="span"
            ),
            direction="row",
            spacing="0"
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index=999,
        top=0,
        spacing="1"
    )