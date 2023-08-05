# 4. Имеется файл file.txt с текстом на латинице.
# Напишите программу, которая выводит следующую статистику по тексту:
# •	количество букв латинского алфавита;
# •	число слов;
# •	число строк.
# Пример ввода и вывода
# Предположим, что file.txt содержит приведенный ниже текст:
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

num_letter = 0
num_word = 0
num_string = 0
with open('task4.txt', 'r') as file:
    text = file.readlines()
    print(text)
for i in text:
    num_string += 1
print(f' Количество строк в тексте: {num_string}')
for i in text:
    num_word = (i.count(" ") + 1) * num_string
print(f'Количество слов в тексте: {num_word}')
for i in text:
    for letter in i:
        if letter.isalpha():
            num_letter += 1
print(f'Количество букв в тексте: {num_letter}')


