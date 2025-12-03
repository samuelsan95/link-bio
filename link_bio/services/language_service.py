import json
import os
import reflex as rx
from deep_translator import GoogleTranslator
from link_bio.language_state import LanguageState


class Translator:
    def __init__(self):
        pass
    
    def translate(self, property, lang=None):
        """
        Translate a property using the language file corresponding to the property.
        If lang is not provided, uses the global language state.
        """
        if lang is None:
            lang = LanguageState.language if hasattr(LanguageState, 'language') else 'es'
        
        language_file_path = os.path.join(os.path.dirname(__file__), f"../../assets/language/{lang}.json")
        
        try:
            with open(language_file_path) as texts_file:
                texts = json.loads(texts_file.read())
            return texts[property] if property in texts else property
        except:
            return property
    
    def external_translate(self, text, lang=None):
        """
        Translate external text using deep_translator (Google Translate).
        If lang is not provided, uses the global language state.
        """
        if lang is None:
            lang = LanguageState.language if hasattr(LanguageState, 'language') else 'es'
        
        if lang != "es":
            try:
                translator = GoogleTranslator(source='es', target=lang)
                return translator.translate(text)
            except Exception as e:
                return text
        else:
            return text


_translator = Translator()


def t(key: str):
    return rx.cond(
        LanguageState.language == "es",
        _translator.translate(key, "es"),
        _translator.translate(key, "en")
    )
