"""
5) Сгенерировать список используя генератор списков.
В списке должно быть 10 элементов в произвольном случайном диапазоне.
Перевести все числа в строку и получить из списка - строку.
"""
import random
lst = [random.randint(1, 100) for i in range(10)]
lst2 = [str(i) for i in lst]
stroka = ','.join(lst2)
print(stroka)
print(type(stroka))