#  9. Дан список [student1, student2, student3] с помощью цикла for
#  добавить к каждому элементу списка слово “ good”. Вывести на экран.

list1 = ["student1", "student2", "student3"]
list2 = []
for word in list1:
    list2.append(word + " good")
print(list2)
