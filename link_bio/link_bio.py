import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.language_state import LanguageState
import link_bio.styles.styles as styles


@rx.page(
    title="SamuelSan | Developer",
    description="Mi nombre es Samuel y soy un desarrollador web apasionado del mundo tecnológico, con una experiencia de más de 5 años",
    image="avatar.jpeg",
    on_load=LanguageState.detect_browser_language
)
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value,
                padding=styles.Size.BIG.value
            )
        ),
        footer()
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
