# from src.base_web import BaseWeb

def equal_text(text):
    return f"/self::*[normalize-space(text()) = '\{text}'\]"
