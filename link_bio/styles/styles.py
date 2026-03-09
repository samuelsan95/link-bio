import reflex as rx
from enum import Enum
from .colors import Color, TextColor
from .fonts import Font, FontWeight


# Sizes
class Size(Enum):
    VERY_SMALL = "0.2em"
    SMALL = "0.8em"
    MEDIUM = "1em"
    DEFAULT = "1.2em"
    LARGE = "1.5em"
    EXTRA_LARGE = "1.8em"
    BIG = "2em"
    VERY_BIG = "4em"
    ZERO = "0px !important"

class SizeReflex(Enum):
    SMALL = "3"
    MEDIUM = "5"
    BIG = "7"
    VERY_BIG = "8"


STYLESHEETS = [
    "/fonts.css",
    "/styles.css"
]

# Styles general
# We keep BASE_STYLE focused on layout and common typography
# Colors are applied directly in components for dynamic mode compatibility
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    rx.heading: {
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value,
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "white_space": "normal",
        "text_align": "start",
        "transition": "background-color 0.2s ease, color 0.2s ease",
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    },
    rx.card: {
        "border_radius": Size.DEFAULT.value,
        "transition": "background-color 0.2s ease",
    }
}

# Style components
navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.LARGE.value,
    margin_inline_start="-0.5em !important"
)

logo_navbar_style = dict(
    margin_bottom=f"{Size.VERY_SMALL.value} !important",
    margin_inline_start="-0.5em !important"
)

# Helper functions for dynamic styles to avoid resolvedColorMode error
def get_button_title_style():
    return dict(
        font_family=Font.TITLE.value,
        font_weight=FontWeight.MEDIUM.value,
        color=rx.color_mode_cond(
            TextColor.LIGHT_HEADER.value,
            TextColor.HEADER.value
        )
    )

def get_button_body_style():
    return dict(
        font_family=Font.DEFAULT.value,
        font_weight=FontWeight.LIGHT.value,
        color=rx.color_mode_cond(
            TextColor.LIGHT_BODY.value,
            TextColor.BODY.value
        )
    )

title_style = dict(
    width = "100%",
    padding_top = Size.DEFAULT.value
)

link_style = dict(
    cursor="pointer"
)

# Constants
MAX_WIDTH = "650px"
