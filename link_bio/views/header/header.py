import reflex as rx


def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(
            name="Samuel Sanchez",
            size="xl"
        ),
        rx.text(
            "@samuelsan"
        ),
        rx.text(
            "HOLA!, TE PREGUNTARÁS QUIEN SOY..."
        ),
        rx.text(
            """Mi nombre es Samuel y soy un desarrollador web apasionado del mundo tecnológico,
            con una experiencia de más de 5 años en el sector utilizando tecnologías y lenguajes
            como JavaScript y sus frameworks Angular 2+, Vue y NodeJs, HTML5, CSS3, Bootstrap y SQL"""
        )
    )