# 5. Сгенерировать список используя генератор списков. В списке должно быть
# 10 элементов в произвольном случайном диапазоне.
# Перевести все числа в строку и получить из списка - строку.
import random

list1 = [random.randint(1, 100) for i in range(10)]
list2 = []
for i in list1:
    i = str(i)
    list2.append(i)
str1 = " ".join(list2)
print(str1)

