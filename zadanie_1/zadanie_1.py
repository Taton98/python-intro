# zadanie_1.py
# Filip Sobczak
# Nr albumu: 152793

import random

# Tworzenie dwóch list
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']

#  Łączenie list za pomocą funkcji zip() 
# Dokumentacja: https://docs.python.org/3/library/functions.html#zip
polaczone = list(zip(lista1, lista2))
print("Połączone listy (zip):", polaczone)

#  Wykorzystanie funkcji z modułu random 
# Dokumentacja: https://docs.python.org/3/library/random.html
losowa_liczba = random.randint(1, 10)
print("Wylosowana liczba:", losowa_liczba)

#  Obsługa wyjątku ZeroDivisionError 
# Dokumentacja: https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
try:
    wynik = int(input("Podaj liczbę którą podzielisz: ")) / int(input("Podaj liczbę (różną od 0): "))
    print("Wynik dzielenia:", wynik)
except ZeroDivisionError:
    print("Nie można dzielić przez zero!")
except ValueError:
    print("Podano nieprawidłową wartość – wpisz liczbę.")