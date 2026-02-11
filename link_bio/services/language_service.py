import json
import os
from deep_translator import GoogleTranslator


class Translator:
    _cache = {}

    def __init__(self):
        pass

    def _load_language(self, lang):
        if lang not in self._cache:
            language_file_path = os.path.join(os.path.dirname(__file__), f"../../assets/language/{lang}.json")
            try:
                with open(language_file_path) as texts_file:
                    self._cache[lang] = json.loads(texts_file.read())
            except (FileNotFoundError, json.JSONDecodeError):
                self._cache[lang] = {}
        return self._cache[lang]

    def translate(self, property, lang="es"):
        """
        Translate a property using the language file corresponding to the property.
        """
        texts = self._load_language(lang)
        return texts.get(property, property)

    def external_translate(self, text, lang="es"):
        """
        Translate external text using deep_translator (Google Translate).
        """
        if lang != "es":
            try:
                translator = GoogleTranslator(source='es', target=lang)
                return translator.translate(text)
            except Exception:
                return text
        else:
            return text


_translator = Translator()


def t(property, lang="es"):
    return _translator.translate(property, lang)
