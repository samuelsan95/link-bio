import reflex as rx

config = rx.Config(
    app_name="link_bio",
    tailwind=None,
    show_built_with_reflex=False,
    disable_plugins=['reflex.plugins.sitemap.SitemapPlugin'],
    _no_sio=True,
    api_url='localhost:3000'
)