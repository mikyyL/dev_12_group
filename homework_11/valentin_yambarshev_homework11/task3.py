#  1. Есть список состоящий из слов и чисел, нужно записать в файл сначала слова в порядке их длины,
#  а после слов цифры в порядке возрастания.

with open("task3.txt", "r") as file:
    elements = file.readlines()
    print(elements)

str1 = ""
numbers = []
words = []

for i in elements:
    i = i[:-1]
    print(i)
    if i.isalpha():
        i = str(i)
        words.append(i)
    else:
        i = int(i)
        numbers.append(i)
numbers.sort()
words.sort()
list1 = numbers + words
print(list1)

#  Артем не могу понять по какой причине слова не становятся в порядке возрастания
