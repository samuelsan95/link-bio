import json
import os
import translate as translate_lib


class Translator:
    def __init__(self, lang='es'):
        self.lang = lang
    
    def translate(self, property):
        language_file_path = os.path.join(os.path.dirname(__file__), f"../../assets/language/{self.lang}.json")
        
        with open(language_file_path) as texts_file:
            texts = json.loads(texts_file.read())
    
        return texts[property] if property in texts else property
    
    def external_translate(self, text):
        if (self.lang != "es"):
            translator = translate_lib.Translator(from_lang="es", to_lang=self.lang)
            return translator.translate(text)
        else:
            return text
    
    def change_lang(self, new_lang):
        self.lang = new_lang
