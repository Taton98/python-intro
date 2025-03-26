
# Moduł math_tools - funkcje matematyczne

import math

def factorial(n):
    # Oblicza silnię liczby n
    if n < 0:
        raise ValueError("Liczba musi być nieujemna")
    return math.factorial(n)

def is_prime(n):
    # Sprawdza, czy liczba jest pierwsza
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
