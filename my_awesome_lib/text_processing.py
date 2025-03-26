# Moduł text_processing - operacje na tekście


def reverse_text(text):
    # Odwraca podany tekst
    return text[::-1]

def count_words(text):
    # Zlicza słowa w tekście
    return len(text.split())
