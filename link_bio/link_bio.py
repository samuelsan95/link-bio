import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links
import link_bio.styles.styles as styles


def _page(lang: str) -> rx.Component:
    return rx.fragment(
        rx.script(src="/manifest.json", type="application/manifest+json"),
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin="anonymous"),
        rx.box(
            rx.el.nav(
                navbar(lang)
            ),
            rx.el.main(
                rx.center(
                    rx.vstack(
                        header(lang),
                        links(lang),
                        max_width=styles.MAX_WIDTH,
                        width="100%",
                        margin_y=styles.Size.BIG.value,
                        padding=styles.Size.BIG.value
                    )
                )
            ),
            rx.el.footer(
                footer(lang)
            )
        )
    )


@rx.page(
    title="SamuelSan | Developer",
    description="Mi nombre es Samuel y soy un desarrollador web apasionado del mundo tecnológico, con una experiencia de más de 10 años",
    image="avatar.jpeg",
    meta=[
        {"name": "keywords", "content": "desarrollador web, programador, python, javascript, reflex, desarrollo software"},
        {"name": "author", "content": "Samuel Sánchez López"},
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"},
        {"name": "robots", "content": "index, follow"},
        {"property": "og:type", "content": "website"},
        {"property": "og:url", "content": "https://samuelsan.es"},
        {"property": "og:title", "content": "SamuelSan | Developer"},
        {"property": "og:description", "content": "Mi nombre es Samuel y soy un desarrollador web apasionado del mundo tecnológico, con una experiencia de más de 10 años"},
        {"property": "og:image", "content": "https://samuelsan.es/avatar.jpeg"},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:title", "content": "SamuelSan | Developer"},
        {"name": "twitter:description", "content": "Mi nombre es Samuel y soy un desarrollador web apasionado del mundo tecnológico, con una experiencia de más de 10 años"},
        {"name": "twitter:image", "content": "https://samuelsan.es/avatar.jpeg"},
        {"name": "theme-color", "content": "#1a1a2e"},
        {"http-equiv": "Content-Language", "content": "es"},
    ],
)
def index() -> rx.Component:
    return _page("es")

@rx.page(
    route="/en",
    title="SamuelSan | Developer",
    description="My name is Samuel and I am a web developer passionate about the technological world, with more than 10 years of experience",
    image="avatar.jpeg",
    meta=[
        {"name": "keywords", "content": "web developer, programmer, python, javascript, reflex, software development"},
        {"name": "author", "content": "Samuel Sánchez López"},
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"},
        {"name": "robots", "content": "index, follow"},
        {"property": "og:type", "content": "website"},
        {"property": "og:url", "content": "https://samuelsan.es/en"},
        {"property": "og:title", "content": "SamuelSan | Developer"},
        {"property": "og:description", "content": "My name is Samuel and I am a web developer passionate about the technological world, with more than 10 years of experience"},
        {"property": "og:image", "content": "https://samuelsan.es/avatar.jpeg"},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:title", "content": "SamuelSan | Developer"},
        {"name": "twitter:description", "content": "My name is Samuel and I am a web developer passionate about the technological world, with more than 10 years of experience"},
        {"name": "twitter:image", "content": "https://samuelsan.es/avatar.jpeg"},
        {"name": "theme-color", "content": "#1a1a2e"},
        {"http-equiv": "Content-Language", "content": "en"},
    ],
)
def index_en() -> rx.Component:
    return _page("en")


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    enable_state=False
)
