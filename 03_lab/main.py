import math
from math import sqrt
from collections import Counter


def pietro(chr):
    print(f"{chr}        {chr}")
    print(f"{chr}    O   {chr}")
    print(f"{chr}________{chr}")


def dach(chr):
    print(f"    {chr}{chr}   ")
    print(f"   {chr}  {chr}  ")
    print(f"  {chr}    {chr} ")
    print(f" {chr}      {chr}")
    print(f"{chr}________{chr}")


def rysuj_dom(floors, roof_chr, wall_chr):
    dach(roof_chr)
    for _ in range(floors):
        pietro(wall_chr)


def szukaj_w_liscie(arr, a):
    try:
        return arr.count(int(a))
    except ValueError:
        if isinstance(a, bool):
            return arr.count(0 if a else 1)
        elif isinstance(a, str):
            return sum(ord(char) for char in a)
        else:
            raise TypeError("Nieprawidłowy typ argumentu")


def dist(p1, p2):
    return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def obwod_trojkata(p1, p2, p3):
    if collinear(p1, p2, p3):
        print("not a triangle")
        return 0

    return dist(p1, p2) + dist(p1, p3) + dist(p2, p3)


def collinear(p1, p2, p3):
    return (p1[1] - p2[1]) * (p1[0] - p3[0]) == (p1[1] - p3[1]) * (p1[0] - p2[0])


def podstawowe_statystyki(liczby):
    if not liczby:
        return None, None, None, None, None

    srednia = sum(liczby) / len(liczby)
    posortowane = sorted(liczby)
    n = len(posortowane)
    if n % 2 == 0:
        mediana = (posortowane[n//2-1] + posortowane[n//2]) / 2
    else:
        mediana = posortowane[n//2]

    minimum = min(liczby)
    maksimum = max(liczby)
    roznice = [(x - srednia)**2 for x in liczby]
    wariancja = sum(roznice) / (len(liczby) - 1)
    odchylenie_standardowe = sqrt(wariancja)

    return mediana, srednia, minimum, maksimum, odchylenie_standardowe


def czy_anagram(a, b):
    aa = Counter(a)
    bb = Counter(b)
    return aa == bb


def sortuj_liste(liczby, rosnaco=True):
    if rosnaco:
        return sorted(liczby)
    else:
        return sorted(liczby, reverse=True)


def czy_pierwsza(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def najdluzszy_wspolny_podciag(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)


def konwertuj_temperature(temp, skala_zrodlowa, skala_docelowa):
    if skala_zrodlowa == 'C' and skala_docelowa == 'F':
        return (temp * 9/5) + 32
    elif skala_zrodlowa == 'F' and skala_docelowa == 'C':
        return (temp - 32) * 5/9
    else:
        return temp


def rysuj_figure(figura, parametry):
    if figura == 'kolo':
        promien = parametry
        print(f'Rysowanie koła o promieniu {promien}')
        pole = math.pi * promien ** 2
        print(f'Pole koła: {pole:.2f}')
    elif figura == 'kwadrat':
        bok = parametry
        print(f'Rysowanie kwadratu o boku {bok}')
        pole = bok ** 2
        print(f'Pole kwadratu: {pole:.2f}')
    else:
        print('Nieobsługiwana figura')


def szyfruj_tekst(tekst, klucz):
    zaszyfrowany = ''
    for char in tekst:
        if char.isalpha():
            if char.isupper():
                zaszyfrowany += chr((ord(char) + klucz - 65) % 26 + 65)
            else:
                zaszyfrowany += chr((ord(char) + klucz - 97) % 26 + 97)
        else:
            zaszyfrowany += char
    return zaszyfrowany


def reverse_string(s):
    return s[::-1]


class Person:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def przedstaw_sie(self):
        print(f"Mam na imię {self.imie} i mam {self.wiek} lat.")


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Niewystarczające środki na koncie.")


class Student:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append({"name": name, "grade": None})

    def add_grade(self, name, grade):
        for student in self.students:
            if student["name"] == name:
                student["grade"] = grade
                break


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percent):
        self.price *= (1 - percent / 100)


class User:
    def __init__(self):
        self.username = None
        self.password = None

    def register(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if self.username == username and self.password == password:
            print("Zalogowano pomyślnie.")
        else:
            print("Nieprawidłowa nazwa użytkownika lub hasło.")


if __name__ == "__main__":
    rysuj_dom(5, "#", "*")
    print(szukaj_w_liscie([1, 1, 1, 2, 3], 1))
    print(szukaj_w_liscie([1, 1, 1, 2, 3], "1"))
    print(szukaj_w_liscie([1, 1, 1, 2, 3], True))
    print(dist([0, 0], [2, 3]))
    print(obwod_trojkata([0, 0], [1, 0], [1, 2]))
    print(obwod_trojkata([0, 0], [1, 0], [2, 0]))
    print(czy_anagram("listen", "silent"))

    osoba = Person("Jan", 30)
    osoba.przedstaw_sie()

    prostokat = Rectangle(5, 10)
    print(prostokat.area())

    konto = BankAccount(1000)
    konto.deposit(500)
    konto.withdraw(200)
    print(konto.balance)

    student = Student()
    student.add_student("Jan")
    student.add_grade("Jan", 4.5)

    produkt = Product("Telewizor", 2000)
    produkt.apply_discount(10)
    print(produkt.price)

    uzytkownik = User()
    uzytkownik.register("jankowalski", "haslo123")
    uzytkownik.login("jankowalski", "haslo124")
    uzytkownik.login("jankowalski", "zlehaslo")
