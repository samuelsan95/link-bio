import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links
import link_bio.styles.styles as styles


def _page(lang: str) -> rx.Component:
    return rx.box(
        navbar(lang),
        rx.center(
            rx.vstack(
                header(lang),
                links(lang),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value,
                padding=styles.Size.BIG.value
            )
        ),
        footer(lang)
    )


@rx.page(
    title="SamuelSan | Developer",
    description="Mi nombre es Samuel y soy un desarrollador web apasionado del mundo tecnológico, con una experiencia de más de 10 años",
    image="avatar.jpeg",
)
def index() -> rx.Component:
    return _page("es")

@rx.page(
    route="/en",
    title="SamuelSan | Developer",
    description="My name is Samuel and I am a web developer passionate about the technological world, with more than 10 years of experience",
    image="avatar.jpeg",
)
def index_en() -> rx.Component:
    return _page("en")


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
