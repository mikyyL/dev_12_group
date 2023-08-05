import random

# 1. Введите два числа с клавиатуры. Поделите одно на другое. Обработайте ошибку деления на ноль,
# если ошибок нет, то результат деления возвести в квадрат. Также используйте оператор finally.
# try:
#     num1 = int(input('Введите первое число: '))
#     num2 = int(input('Введите первое число: '))
#     result = num1 / num2
# except Exception:  # через as erorr можем вывести само название
#     print('На ноль делить нельзя')
# else:
#     print(f'Результат в квадрате {result**2}')
# finally:
#     print('Конец программы')


# 2. Напишите программу для расчета среднего значения списка чисел.
# Ваша программа должна принимать список чисел от пользователя и выводить их среднее значение.
# Однако, необходимо учесть возможность возникновения исключений при вводе неккоректных данных.

# try:
#     input_str = input('Введите список чисел через пробел: ')
#     input_list = input_str.split(' ')
#     new_list = []
#     for i in input_list:
#         i = int(i)
#         new_list.append(i)
#         print(new_list)
#         result_arf = sum(new_list) / len(new_list)
# except Exception:
#     print('Введены некорректные данные')
# else:
#     print(f'Среднее арифметическое: {result_arf}')
# finally:
#     print('Программа завершена')

# 3. Вывести первые N чисел кратные M и больше K

# try:
#     num1 = int(input('Введите число, обозначающее кратность: '))
#     num2 = int(input('Введите число, обозначающее минимальное значение: '))
#     num_generate = [random.randint(1, 100) for i in range(10)]
#     list1 = []
#     print(num_generate)
#     for i in num_generate:
#         if i % num1 == 0 and i > num2:
#             list1.append(i)
# except Exception:
#     print('Введены неверные значения')
# else:
#     print(f'{list1}')
# finally:
#     print('Программа завершена')

# 4. Найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальные и максимальные элементы в сумму не включать.

# try:
#     max_num = int(input('Введите число, являющееся максимальным: '))
#     min_num = int(input('Введите число, являющееся минимальным: '))
#     list_generate = [random.randint(1, 100) for i in range(10)]
#     print(list_generate)
#     list1 = []
#     for i in list_generate:
#         if min_num < i < max_num:
#             list1.append(i)
#     print(list1)
# except Exception:
#     print('Введены некорректные значения')
# else:
#     print(f'Сумма чисел между {min_num} и {max_num}: {sum(list1)}')
# finally:
#     print('Программа завершена')

# 5. Заполнить словарь, где ключами выступают числа от 0 до n,
# а значениями вложенный словарь с ключами "name" и "email",
# а значения для этих ключей будут браться с клавиатуры.

# try:
#     num = int(input('Введите число, которое является ключом словаря: '))
#     dict_key = [i for i in range(num)]
#     dict1 = {i: {'name': input('Введите имя пользователя: '),
#                  'email': input('Введите электронную почту пользователя: ')} for i in dict_key}
# except Exception:
#     print('Введены некорректные значения')
# else:
#     print(f'{dict1}')
# finally:
#     print('Программа завершена')