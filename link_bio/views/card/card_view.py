import reflex as rx
from link_bio.styles.styles import Size, SizeReflex
from link_bio.styles.colors import Color, TextColor
from link_bio.services.language_service import t
from link_bio.components.theme_button import theme_button
from link_bio.components.selector_language import selector_language
from link_bio import constants


def _card_link(icon: str, display: str, url: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.image(
                src=f"icons/{icon}",
                width="16px",
                height="16px",
                alt=display,
                style={
                    "filter": rx.color_mode_cond("invert(0.6)", "none")
                }
            ),
            rx.text(
                display,
                size=SizeReflex.SMALL.value,
                color=rx.color_mode_cond(
                    TextColor.LIGHT_BODY.value,
                    TextColor.BODY.value
                )
            ),
            spacing="2",
            align="center"
        ),
        href=url,
        is_external=True,
    )


def card_view(lang: str = "es") -> rx.Component:
    back_href = "/" if lang == "es" else "/en"
    share_url = "https://samuelsan.es/card" if lang == "es" else "https://samuelsan.es/en/card"
    share_script = (
        f"if(navigator.share){{"
        f"navigator.share({{title:'Samuel Sánchez — Developer',url:'{share_url}'}})"
        f"}}else{{"
        f"navigator.clipboard.writeText('{share_url}')"
        f"}}"
    )

    return rx.vstack(
        # Controls bar (hidden on print)
        rx.hstack(
            rx.link(
                rx.hstack(
                    rx.icon("arrow-left", size=14),
                    rx.text(
                        t("card_back_button", lang),
                        size=SizeReflex.SMALL.value,
                    ),
                    spacing="1",
                    align="center"
                ),
                href=back_href,
                color=rx.color_mode_cond(
                    Color.LIGHT_ACCENT.value,
                    Color.PRIMARY.value
                ),
            ),
            rx.spacer(),
            theme_button(),
            selector_language(lang),
            width="100%",
            max_width="400px",
            class_name="no-print",
            align="center"
        ),

        # The business card
        rx.box(
            rx.vstack(
                # Header: avatar + identity
                rx.hstack(
                    rx.image(
                        src="avatar.webp",
                        width="72px",
                        height="72px",
                        border_radius="9999px",
                        object_fit="cover",
                        border_width="2px",
                        border_style="solid",
                        border_color=rx.color_mode_cond(
                            Color.LIGHT_ACCENT.value,
                            Color.PRIMARY.value
                        ),
                        flex_shrink="0"
                    ),
                    rx.vstack(
                        rx.heading(
                            "Samuel Sánchez",
                            size=SizeReflex.BIG.value,
                            color=rx.color_mode_cond(
                                TextColor.LIGHT_HEADER.value,
                                TextColor.HEADER.value
                            )
                        ),
                        rx.text(
                            "@samuelsan",
                            size=SizeReflex.SMALL.value,
                            color=rx.color_mode_cond(
                                TextColor.LIGHT_BODY.value,
                                TextColor.BODY.value
                            )
                        ),
                        rx.text(
                            t("card_role", lang),
                            size=SizeReflex.SMALL.value,
                            color=rx.color_mode_cond(
                                Color.LIGHT_ACCENT.value,
                                Color.PRIMARY.value
                            ),
                            font_weight="500"
                        ),
                        spacing="1",
                        align_items="start"
                    ),
                    spacing=SizeReflex.MEDIUM.value,
                    align="center",
                    width="100%"
                ),

                # Divider
                rx.divider(
                    border_color=rx.color_mode_cond(
                        "rgba(92,112,33,0.2)",
                        "rgba(211,226,159,0.15)"
                    )
                ),

                # Social links
                rx.vstack(
                    _card_link("linkedin.svg", "linkedin.com/in/samuel-sanchez-lopez", constants.LINKEDIN_URL),
                    _card_link("github.svg", "github.com/samuelsan95", constants.GITHUB_URL),
                    _card_link("medium.svg", "medium.com/@samuelsan95", constants.MEDIUM_URL),
                    _card_link("email.svg", constants.EMAIL_URL, f"mailto:{constants.EMAIL_URL}"),
                    spacing="2",
                    align_items="start",
                    width="100%"
                ),

                # Divider
                rx.divider(
                    border_color=rx.color_mode_cond(
                        "rgba(92,112,33,0.2)",
                        "rgba(211,226,159,0.15)"
                    )
                ),

                # Footer: site URL + QR code
                rx.hstack(
                    rx.vstack(
                        rx.text(
                            "samuelsan.es",
                            color=rx.color_mode_cond(
                                Color.LIGHT_ACCENT.value,
                                Color.PRIMARY.value
                            ),
                            font_weight="500",
                            size=SizeReflex.SMALL.value
                        ),
                        rx.text(
                            t("card_role", lang),
                            color=rx.color_mode_cond(
                                TextColor.LIGHT_FOOTER.value,
                                TextColor.FOOTER.value
                            ),
                            size="1"
                        ),
                        spacing="1",
                        align_items="start"
                    ),
                    rx.spacer(),
                    rx.image(
                        src="qr_code.png",
                        width="72px",
                        height="72px",
                        alt="QR samuelsan.es",
                        border_radius="4px",
                        style={
                            "filter": rx.color_mode_cond("none", "invert(1)")
                        }
                    ),
                    width="100%",
                    align="end"
                ),

                spacing=SizeReflex.MEDIUM.value,
                width="100%"
            ),
            background_color=rx.color_mode_cond(
                Color.LIGHT_CONTENT.value,
                "#212547"
            ),
            border_radius="16px",
            padding=Size.BIG.value,
            box_shadow=rx.color_mode_cond(
                "0 4px 24px rgba(0,0,0,0.10)",
                "0 4px 32px rgba(0,0,0,0.50)"
            ),
            width="100%",
            max_width="400px",
            class_name="card-container"
        ),

        # Action buttons (hidden on print)
        rx.hstack(
            rx.button(
                t("card_print_button", lang),
                on_click=rx.call_script("window.print()"),
                background_color=rx.color_mode_cond(
                    Color.LIGHT_ACCENT.value,
                    Color.PRIMARY.value
                ),
                color=rx.color_mode_cond(
                    Color.LIGHT_CONTENT.value,
                    Color.BACKGROUND.value
                ),
                border_radius=Size.DEFAULT.value,
                width="auto",
                height="auto",
                padding_x=Size.DEFAULT.value,
                padding_y=Size.SMALL.value,
                cursor="pointer",
                display="inline-flex",
                align_items="center"
            ),
            rx.button(
                t("card_share_button", lang),
                on_click=rx.call_script(share_script),
                background_color=rx.color_mode_cond(
                    Color.LIGHT_SECONDARY.value,
                    Color.SECONDARY.value
                ),
                color=rx.color_mode_cond(
                    TextColor.LIGHT_HEADER.value,
                    TextColor.HEADER.value
                ),
                border_radius=Size.DEFAULT.value,
                width="auto",
                height="auto",
                padding_x=Size.DEFAULT.value,
                padding_y=Size.SMALL.value,
                cursor="pointer",
                display="inline-flex",
                align_items="center"
            ),
            spacing=SizeReflex.SMALL.value,
            class_name="no-print"
        ),

        align="center",
        justify="center",
        spacing=SizeReflex.MEDIUM.value,
        padding=Size.BIG.value,
        min_height="100vh",
        width="100%"
    )
