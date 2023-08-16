"""
4. Дан список чисел. Если число встречается более двух раз,
 то добавить его в новый список
"""
lst = [2, 2, 2, 3, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6]
new_lst = []
for i in lst:
    if lst.count(i) > 2:
        new_lst.append(i)
    if new_lst.count(i) > 1:
        new_lst.remove(i)
print(f"новый список - {new_lst}")
