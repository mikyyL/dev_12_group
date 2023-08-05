#  Файл содержит числа и буквы, каждый элемент записан в отдельной строке.
#  Необходимо вывести так, чтобы сначала шли цифры по возрастанию, а потом слова по возрастанию их длины.

with open("task2.txt", "r") as file:
    text = file.readlines()
    print(text)
str1 = ""
list_word = []
list_num = []
list1 = []
for i in text:
    str1 = i[:-1]
    list1.append(str1)
print(list1)
for i in list1:
    if i.isdigit():
        list_num.append(i)
    else:
        list_word.append(i)
print(list_num)
print(list_word)
list_num.sort()
list_word.sort()
list3 = list_num + list_word
print(list3)


