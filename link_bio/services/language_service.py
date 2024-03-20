import json
import os

class Translator:
    def __init__(self, lang='es'):
        self.lang = lang
    
    def translate(self, property):
        language_file_path = os.path.join(os.path.dirname(__file__), f"../../assets/language/{self.lang}.json")
        
        with open(language_file_path) as texts_file:
            texts = json.loads(texts_file.read())
    
        return texts[property]
    
    def change_lang(self, new_lang):
        self.lang = new_lang