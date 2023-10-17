import reflex as rx


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico"
        ),
        rx.text("...Lorem impsum....")
    )