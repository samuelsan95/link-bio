import reflex as rx
from link_bio.components.link_button import link_button


def links() -> rx.Component:
    return rx.vstack(
        link_button("Linkedin", "https://www.linkedin.com/in/samuel-sanchez-lopez/"),
        link_button("Github", "https://github.com/samuelsan95"),
        link_button("Medium", "https://medium.com/@sanchezlopezsamuel")
    )