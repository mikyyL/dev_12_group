"""
Создайте словарь из строки
' An apple a day keeps the doctor away'
следующим образом:
в качестве ключей возьмите символы строки,
а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку.
"""
string = 'An apple a day keeps the doctor away'
dictionary = {}
for i in string:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1

print(dictionary)
