# 6. Сжать массив, удалив из него все элементы, величина которых находится в интервале [а, b].
# Освободившиеся в конце массива элементы заполнить нулями.

import random

num1 = int(input('Введите первое число интервала: '))
num2 = int(input('Введите второе число интервала: '))
list1 = [random.randint(1, 20) for i in range(10)]
print(list1)
list2 = []
for i in list1:
    if num1 <= i <= num2:
        del i
    else:
        list2.append(i)
n = len(list2)
for i in range(10 - n):
    list2.append(0)
print(list2)
