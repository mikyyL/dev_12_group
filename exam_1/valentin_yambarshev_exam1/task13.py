#  13. Дан список чисел, необходимо удалить все вхождения числа 20 из него.
listNumbers = [20, 20, 32, 20, 45, 56, 20, 2, 47]
num1 = 20
listNumbers = [digit for digit in listNumbers if digit != 20]
print(listNumbers)

# for digit in list1:
#     if digit == 20:
#         list1.remove(20)
# print(list1)
"""Не могу понять почему если в начале написать 20, то он тогда не все 20 убирает. Напиши потом Артем"""
"""Смещается индекс, поэтому не удаляет"""
#
# while 20 in listNumbers:
#     numbers.remove(20)