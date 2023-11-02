import reflex as rx
from enum import Enum
from .colors import Color, TextColor
from .fonts import Font


# Sizes
class Size(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    ZERO = "0px !important"


# Styles general
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "background_color": Color.BACKGROUND.value,
    rx.Heading: {
        "color": TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
    },
    rx.Button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "background_color": Color.CONTENT.value,
        "color": TextColor.HEADER.value,
        "_hover": {
            "background_color": Color.SECONDARY.value,
        }
    },
    rx.Link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

# Style components
navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_size=Size.LARGE.value
)

button_title_style = dict(
    font_family = Font.TITLE.value,
    font_size = Size.DEFAULT.value,
    color = TextColor.HEADER.value
)

button_body_style = dict(
    font_family = Font.DEFAULT.value,
    font_size = Size.MEDIUM.value,
    color = TextColor.BODY.value
)

title_style = dict(
    width = "100%",
    padding_top = Size.DEFAULT.value
)

# Constants
MAX_WIDTH = "600px"
