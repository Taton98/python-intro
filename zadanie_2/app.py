import re
from datetime import datetime

def is_valid_email(email: str) -> bool:
    #Sprawdza poprawność adresu e-mail.
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

def calculate_area(shape: str, *dimensions) -> float:
    #Oblicza pole figury: koła, kwadratu lub prostokąta.
    if shape == "circle" and len(dimensions) == 1:
        radius = dimensions[0]
        return 3.14159 * radius ** 2
    elif shape == "square" and len(dimensions) == 1:
        side = dimensions[0]
        return side ** 2
    elif shape == "rectangle" and len(dimensions) == 2:
        length, width = dimensions
        return length * width
    else:
        raise ValueError("Niepoprawne parametry dla figury.")

def process_list(data: list, filter_even: bool = True) -> list:
    #Sortuje listę i opcjonalnie filtruje tylko parzyste liczby.
    sorted_data = sorted(data)
    return [x for x in sorted_data if x % 2 == 0] if filter_even else sorted_data

def convert_date_format(date_str: str, current_format: str, new_format: str) -> str:
    #Konwertuje format daty.
    try:
        date_obj = datetime.strptime(date_str, current_format)
        return date_obj.strftime(new_format)
    except ValueError:
        raise ValueError("Niepoprawny format daty.")

def is_palindrome(text: str) -> bool:
    #Sprawdza, czy dany tekst jest palindromem.
    cleaned_text = re.sub(r"[^a-zA-Z0-9]", "", text.lower())
    return cleaned_text == cleaned_text[::-1]


print("Testowanie funkcji ręcznie:\n")

# Sprawdzenie poprawności adresu e-mail
print("Czy 'test@example.com' jest poprawnym e-mailem?", is_valid_email("test@example.com"))
print("Czy 'invalid-email' jest poprawnym e-mailem?", is_valid_email("invalid-email"))

# Obliczanie pól figur
print("Pole koła o promieniu 3:", calculate_area("circle", 3))
print("Pole kwadratu o boku 4:", calculate_area("square", 4))
print("Pole prostokąta 4x5:", calculate_area("rectangle", 4, 5))

# Przetwarzanie listy
numbers = [5, 2, 8, 1, 3, 10]
print("Posortowana lista z parzystymi:", process_list(numbers))
print("Posortowana lista bez filtracji:", process_list(numbers, filter_even=False))

# Konwersja daty
print("Konwersja daty:", convert_date_format("25-03-2025", "%d-%m-%Y", "%Y/%m/%d"))

# Sprawdzenie palindromu
print("Czy 'Kajak' to palindrom?", is_palindrome("Kajak"))
print("Czy 'Python' to palindrom?", is_palindrome("Python"))
print("Czy 'Kamil Ślimak?", is_palindrome("Kamil Ślimak"))
