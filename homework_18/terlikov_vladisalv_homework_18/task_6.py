"""
6)	Напишите функцию для сортировки слов в алфавитном порядке
"""


def sort_words(words):
    words.sort()
    return words


words = []
while True:
    word = input('Введите слово: ')
    words.append(word)
    if word == "":
        words.remove("")
        break

print(sort_words(words))
