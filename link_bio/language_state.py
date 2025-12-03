import reflex as rx

class LanguageState(rx.State):
    """State to handle the application language."""
    
    language: str = "es"
    is_hydrated: bool = False

    def set_language(self, new_lang: str):
        if new_lang in ["es", "en"]:
            self.language = new_lang
    
    def on_language_detected(self, detected_lang: str):
        if detected_lang in ["es", "en"]:
            self.language = detected_lang
        self.is_hydrated = True 

    def detect_browser_language(self):
        """Detect browser language and call callback."""
        return rx.call_script(
            """
            (function() {
                const lang = navigator.language || navigator.userLanguage;
                const shortLang = lang.split('-')[0];
                return ['es', 'en'].includes(shortLang) ? shortLang : 'es';
            })()
            """,
            callback=LanguageState.on_language_detected
        )