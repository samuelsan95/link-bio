from enum import Enum


class Font(Enum):
    DEFAULT = "Nunito, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    TITLE = "Nunito, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    LOGO = "Ubuntu, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"


class FontWeight(Enum):
    LIGHT = 300
    MEDIUM = 500