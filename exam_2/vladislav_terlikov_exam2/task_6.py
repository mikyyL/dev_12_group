"""
6.Сжать массив, удалив из него все элементы, величина которых находится в интервале [а, b].
 Освободившиеся в конце массива элементы заполнить нулями.
"""
import random

a = int(input('Введите первое число (a): '))
b = int(input('Введите второе число (b): '))
list1 = [random.randint(a, b) for i in range(10)]
print(f'исходный список {list1}')
list2 = []
for i in list1:
    if a <= i <= b:
        del i
    else:
        list2.append(i)
n = len(list2)
for i in range(10 - n):
    list2.append(0)
print(f'список с нулями в конце на освободившее места после удаления элементов в пределах'
      f' a и b {list2}')
