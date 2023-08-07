import math
import random

# 1. Написать функцию is_year_leap, принимающую один аргумент - год, и возвращающую True, если год високосный
# и False иначе.


# def is_year_leap(year):
#     if year % 4 == 0:
#         return True
#     else:
#         return False
#
#
# print(is_year_leap(1246))


# 2. Написать функцию square? Принимающую 1 аргумент - сторону квадрата и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.
# Сторону квадрата вводить с клавиатуры.
# def square(a):
#     p = 4 * a
#     s = a * a
#     d = a * math.sqrt(2)
#     result = (p, s, d)
#     return result
#
#
# side_of_square = float(input("Введите сторону квадрата: "))
# print(square(side_of_square))

# 3. Написать функцию season, принимающую 1 аргумент - номер месяца (от 1 до 12) и возвращающую время года,
# которому этот месяц принадлежит (зима, весна, лето, осень).
# Номер месяца вводить с клавиатуры.

# def season(a):
#     list1 = [1, 2, 12]
#     list2 = [3, 4, 5]
#     list3 = [6, 7, 8]
#     list4 = [9, 10, 11]
#     if a in list1:
#         return 'зима'
#     elif a in list2:
#         return 'весна'
#     elif a in list3:
#         return 'лето'
#     elif a in list4:
#         return 'осень'
#     else:
#         return 'Такого месяца не существует'
#
#
# month = int(input('Введите номер месяца: '))
# print(season(month))

# 4. Функция, вычисляющая среднее арифметическое элементов списка. Список должен состоять из случайных чисел,
# длиной 10 элементов.

# def func():
#     list1 = [random.randint(1, 100) for i in range(10)]
#     print(f'Произвольный список элементов:\n{list1}')
#     average = sum(list1) / len(list1)
#     return average
#
#
# print(f'Среднее арифметическое данного списка:\n{func()}')
