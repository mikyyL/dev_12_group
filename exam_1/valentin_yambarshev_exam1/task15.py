#  15. Необходимо удалить пустые строки из списка строк.

list1 = ["cat", "", "dog", "", "bird", "", "panda"]
for space in list1:
    if space == "":
        list1.remove(space)
print(list1)