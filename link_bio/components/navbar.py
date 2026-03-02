import reflex as rx
from link_bio.styles.styles import Size, navbar_title_style, logo_navbar_style
from link_bio.styles.colors import Color
from link_bio.components.selector_language import selector_language
from link_bio.components.hamburger_menu import hamburger_button, hamburger_menu


def navbar(lang: str = "es") -> rx.Component:
    return rx.box(
        # Hidden checkbox — controls menu open/close via CSS
        rx.el.input(
            type="checkbox",
            id="nav-toggle",
            class_name="nav-toggle-input"
        ),
        # Top bar: logo + hamburger button
        rx.hstack(
            rx.flex(
                rx.image(
                    src="logo.png",
                    height=Size.EXTRA_LARGE.value,
                    width="auto",
                    alt="Logo SamuelSan",
                    loading="eager",
                    html_width="180",
                    html_height="127",
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
                    width="auto",
                    alt="Logo SamuelSan",
                    loading="eager",
                    html_width="180",
                    html_height="127",
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
            rx.spacer(),
            # Language selector visible only on desktop
            rx.box(selector_language(lang), class_name="desktop-lang"),
            # Hamburger button — visible only on mobile
            hamburger_button(),
            align="center",
            padding_x=Size.BIG.value,
            padding_y=Size.DEFAULT.value,
            width="100%"
        ),
        # Dropdown menu — toggled by CSS using the checkbox state
        hamburger_menu(lang),
        bg=Color.CONTENT.value,
        position="fixed",
        z_index=999,
        top=0,
        width="100%"
    )
