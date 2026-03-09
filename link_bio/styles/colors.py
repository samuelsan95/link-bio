from enum import Enum

class Color(Enum):
    # Dark Theme (Original)
    PRIMARY = "#D3E29F"
    SECONDARY = "#7B82B8"
    BACKGROUND = "#181B34"
    CONTENT = "#6B73A8"
    
    # Light Theme
    LIGHT_PRIMARY = "#D3E29F"
    LIGHT_ACCENT = "#5C7021" #  Green variant for text on light background
    LIGHT_SECONDARY = "#E2E8F0"
    LIGHT_BACKGROUND = "#F1F2F6"
    LIGHT_CONTENT = "#FFFFFF"

class TextColor(Enum):
    # Dark Theme (Original)
    HEADER = "#FFFFFF"
    BODY = "#E8EAED"
    FOOTER = "#C5C9CE"
    
    # Light Theme
    LIGHT_HEADER = "#1A202C"
    LIGHT_BODY = "#2D3748"
    LIGHT_FOOTER = "#4A5568"