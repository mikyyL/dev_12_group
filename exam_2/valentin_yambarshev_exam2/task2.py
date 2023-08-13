# 2. Найти в списке те элементы, значение которых меньше среднего арифметического,
# взятого от всех элементов списка.
import random

list1 = [random.randint(1, 20) for i in range(10)]
print(f'Список чисел: {list1}')
list2 = []
average = sum(list1) / len(list1)
print(f'Среднее арифметическое списка: {average}')
for i in list1:
    if i < average:
        list2.append(i)
print(f'Список чисел, которые меньше {average}: {list2}')
