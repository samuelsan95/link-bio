def shorten_string(text: str, characteres: int):

    if len(text) > characteres:
        return f"{text[:characteres]} ..."
    return text