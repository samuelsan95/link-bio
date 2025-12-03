import json
import os
import reflex as rx
from deep_translator import GoogleTranslator


class Translator:
    def __init__(self):
        pass
    
    def translate(self, property, lang="es"):
        """
        Translate a property using the language file corresponding to the property.
        """
        language_file_path = os.path.join(os.path.dirname(__file__), f"../../assets/language/{lang}.json")
        
        try:
            with open(language_file_path) as texts_file:
                texts = json.loads(texts_file.read())
            return texts[property] if property in texts else property
        except:
            return property
    
    def external_translate(self, text, lang="es"):
        """
        Translate external text using deep_translator (Google Translate).
        """
        if lang != "es":
            try:
                translator = GoogleTranslator(source='es', target=lang)
                return translator.translate(text)
            except Exception as e:
                return text
        else:
            return text


def t(property, lang="es"):
    translator = Translator()
    return translator.translate(property, lang)
