from enum import Enum

class Color(Enum):
    PRIMARY = "#D3E29F"
    SECONDARY = "#7B82B8"  # Oscurecido para mejor contraste con texto claro
    BACKGROUND = "#181B34"
    CONTENT = "#6B73A8"  # Oscurecido para mejor contraste con texto claro

class TextColor(Enum):
    HEADER = "#FFFFFF"  # Blanco puro para máximo contraste
    BODY = "#E8EAED"  # Más claro para mejor contraste sobre fondos oscuros
    FOOTER = "#C5C9CE"  # Aclarado para cumplir ratio 4.5:1