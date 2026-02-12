import reflex as rx
from reflex.plugins.sitemap import SitemapPlugin

config = rx.Config(
    app_name="link_bio",
    tailwind=None,
    show_built_with_reflex=False,
    _no_sio=True,
    plugins=[SitemapPlugin()],
)