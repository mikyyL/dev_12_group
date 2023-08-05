#  1. В файле в одну строку записаны слова и числа через пробел и нижнее подчеркивание.
#  Найти сумму всех чисел.

with open("task1.txt", "r") as file:
    elements = file.readlines()
    print(elements)

str1 = ""
sum1 = 0
#  Данным циклом проходимся по элементам и переводим в строку, чтобы избавиться от "_"
for i in elements:
    str1 = i.replace("_", " ")
    print(str1)
#  Переводим в список чтобы правильно посчитать цифры
list1 = str1.split(" ")
print(list1)
#  Данным циклом проверяем если элемент число, то его прибавляем
for i in list1:
    if i.isdigit():
        i = int(i)
        sum1 += i
print(sum1)
