"""
2.	Найти в списке те элементы,
 значение которых меньше среднего арифметического,
  взятого от всех элементов списка.
"""
lst = [i for i in range(11)]
arifm = sum(lst)/len(lst)

lst2 = []
for i in lst:
    if i < arifm:
        lst2.append(i)

print(f'числа меньше среднего арифметического {arifm}:\n'
      f'{lst2}\n'
      f'в списке: {lst}')