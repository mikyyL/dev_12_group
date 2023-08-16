"""
7)	Напишите функцию, которая определяет количество гласных в строке
"""
'A, E, I, O, U, Y'


def vowel_letters(string):
    count_letter = 0
    while True:
        for letter in string:
            if letter in 'a, e, i, o, u, y':
                count_letter += 1
        return count_letter


string = input("Введите строку: ")
print(vowel_letters(string))
