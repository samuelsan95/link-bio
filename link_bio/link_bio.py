import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links
import link_bio.styles.styles as styles


@rx.page(
    title="SamuelSan | Developer",
    description="Mi nombre es Samuel y soy un desarrollador web apasionado del mundo tecnológico, con una experiencia de más de 5 años",
    image="avatar.jpeg",
)
def index() -> rx.Component:
    return rx.box(
        navbar("es"),
        rx.center(
            rx.vstack(
                header("es"),
                links("es"),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value,
                padding=styles.Size.BIG.value
            )
        ),
        footer("es")
    )

@rx.page(
    route="/en",
    title="SamuelSan | Developer",
    description="My name is Samuel and I am a web developer passionate about the technological world, with more than 5 years of experience",
    image="avatar.jpeg",
)
def index_en() -> rx.Component:
    return rx.box(
        navbar("en"),
        rx.center(
            rx.vstack(
                header("en"),
                links("en"),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value,
                padding=styles.Size.BIG.value
            )
        ),
        footer("en")
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
