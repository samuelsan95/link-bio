import reflex as rx
from typing import List, Dict, Any

from link_bio.components.card import card
from link_bio.styles.styles import SizeReflex
from link_bio.styles.colors import Color
from link_bio.services.language_service import _translator
from link_bio.services.publication_service import get_publication_description
from link_bio.utils.utils import shorten_string

MAX_CHARACTERS = 200


def _build_carousel_js(n: int) -> str:
    return f"""
(function() {{
    var pubPage = 0;
    var pubTotal = {n};

    function getPerPage() {{
        return window.innerWidth >= 768 ? 2 : 1;
    }}

    function getMaxPage() {{
        return Math.ceil(pubTotal / getPerPage()) - 1;
    }}

    function showPage(page) {{
        var perPage = getPerPage();
        var maxPage = getMaxPage();
        if (page < 0) page = 0;
        if (page > maxPage) page = maxPage;
        pubPage = page;

        for (var i = 0; i < pubTotal; i++) {{
            var el = document.getElementById('pub-card-' + i);
            if (el) {{
                el.style.display = (i >= page * perPage && i < (page + 1) * perPage) ? '' : 'none';
            }}
        }}

        var prev = document.getElementById('pub-prev');
        var next = document.getElementById('pub-next');
        if (prev) prev.style.visibility = page === 0 ? 'hidden' : 'visible';
        if (next) next.style.visibility = page >= maxPage ? 'hidden' : 'visible';
    }}

    window.pubPrev = function() {{ showPage(pubPage - 1); }};
    window.pubNext = function() {{ showPage(pubPage + 1); }};

    function init() {{ showPage(0); }}

    if (document.readyState === 'loading') {{
        document.addEventListener('DOMContentLoaded', init);
    }} else {{
        init();
    }}

    window.addEventListener('resize', function() {{ showPage(pubPage); }});
}})();
"""


def publication_carousel(publications: List[Dict[str, Any]], lang: str = "es") -> rx.Component:
    n = len(publications)

    def get_title(pub: Dict[str, Any]) -> str:
        title = pub.get('title', '')
        if lang == "es":
            return title
        return _translator.external_translate(title, "en")

    def get_description(pub: Dict[str, Any]) -> str:
        desc = shorten_string(get_publication_description(pub), MAX_CHARACTERS)
        if lang == "es":
            return desc
        return _translator.external_translate(desc, "en")

    cards = [
        rx.box(
            card(get_title(pub), get_description(pub), pub.get('link', '#'), lang),
            id=f"pub-card-{i}",
            style={"display": "none"},
            height="100%",
        )
        for i, pub in enumerate(publications)
    ]

    arrow_style = {
        "background": "transparent",
        "border": "none",
        "padding": "4px",
        "cursor": "pointer",
        "flex_shrink": "0",
        "min_width": "32px",
    }

    return rx.vstack(
        rx.script(_build_carousel_js(n)),
        rx.hstack(
            rx.button(
                rx.icon("chevron-left", size=20),
                id="pub-prev",
                on_click=rx.call_script("pubPrev()"),
                variant="ghost",
                color=rx.color_mode_cond(Color.LIGHT_ACCENT.value, Color.PRIMARY.value),
                style={**arrow_style, "visibility": "hidden"},
            ),
            rx.grid(
                *cards,
                columns=rx.breakpoints(sm="1", md="2"),
                width="100%",
                spacing=SizeReflex.MEDIUM.value,
            ),
            rx.button(
                rx.icon("chevron-right", size=20),
                id="pub-next",
                on_click=rx.call_script("pubNext()"),
                variant="ghost",
                color=rx.color_mode_cond(Color.LIGHT_ACCENT.value, Color.PRIMARY.value),
                style=arrow_style,
            ),
            width="100%",
            align="center",
            spacing="2",
        ),
        width="100%",
    )
