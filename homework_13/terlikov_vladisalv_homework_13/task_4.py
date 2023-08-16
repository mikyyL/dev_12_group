"""
4) Имеется файл file.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту:

• количество букв латинского алфавита;

• число слов; • число строк.

Пример ввода и вывода Предположим, что file.txt содержит приведенный ниже текст:
"""

data = "Beautiful is better than ugly. \nExplicit is better than implicit." \
       "\nSimple is better than complex. " \
       "\nComplex is better than complicated."

with open('file.txt', 'w') as f:
    write = f.write(data)
with open('file.txt', 'r') as f:
    lines = f.readlines()
    print(f'Количество строк: {len(lines)}')
    el_lines = 0
    str_lines = ''.join(lines)
    for i in str_lines:
        if i.isalpha():
            el_lines += 1
    print(f'Количество букв в файле: {el_lines}')
    word_lines = str_lines.split(' ')
    print(f'Количество слов в файле: {len(word_lines)}')

