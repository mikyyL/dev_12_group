"""
5.Есть список чисел с дубликатами.
 Создать новый список в котором будут только уникальные элементы.
"""
lst = [1, 1, 1, 2, 3, 4, 4, 4]
new_lst = []
for i in lst:
    if lst.count(i) > 1:
        new_lst.append(i)
    if new_lst.count(i) > 1:
        new_lst.remove(i)
print(f"{new_lst} - новый список")
