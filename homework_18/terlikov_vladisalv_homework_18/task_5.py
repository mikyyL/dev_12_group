"""
5)	Функция для определения того, является ли строка палиндромом
"""


def is_palindrome(string):
    string = string.lower().replace(" ", "")
    return string == string[::-1]


string = input("Введите строку: ")
print(is_palindrome(string))
