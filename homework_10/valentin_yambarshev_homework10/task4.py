# 4. Дана строка. Сохранить в ней только первые вхождения символов,
# удалив все остальные. Результат вывести в виде кортежа.
str1 = "helloworld"
print(str1)
print(tuple(set(str1).pop()))


