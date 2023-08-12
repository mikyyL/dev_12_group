# Необходимо удалить пустые строки из списка строк.

list1 = ['Cat', "" 'Dog', "" 'Bird']
# for i in list1:
#     if i == "":
#         list1.remove(i)
# print(list1)
list1_new = [i for i in list1 if i != ""]
print(list1_new)