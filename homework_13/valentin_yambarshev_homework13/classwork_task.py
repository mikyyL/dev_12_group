# 1. Напишите программу, которая запрашивает у пользователя данные о студентах
# и сохраняет их в файл формата CSV.
# Требования: программа должна запрашивать у пользователя информацию о каждом студенте,
# включая имя, фамилию и возраст.
# Информация о каждом студенте должна быть сохранена в отдельной строке файла CSV.
# Файл CSV должен иметь следующие заголовки столбцов: "Имя", "Фамилия", "Возраст".
# Программа должна продолжать запрашивать информацию о студентах до тех пор, пока пользователь
# не введет команду "stop" для завершения.
# В конце программы должно быть выведено сообщение об успешном сохранении данных.
import csv
import random

# print('Task #1')
#
# with open('classwork_task1.csv', 'w', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow(["Имя", "Фамилия", "Возраст"])
#     while True:
#         fist_name = input('Для окончания введите "stop" или для продолжения введите свое имя: ')
#         if fist_name == 'stop':
#             break
#         last_name = input('Введите свою фамилию: ')
#         age = int(input('Введите свой возраст: '))
#         writer.writerow([fist_name, last_name, age])
#     print('Данные сохранены')

# 2. Дан список некоторых целых чисел, найдите значение 30 в нем и, если оно присутствует, заменить его на 250.
# Обновите список только при первом вхождении числа 30.

# print('Task #2')
#
# list1 = [random.randint(1, 40) for i in range(20)]
# if 30 in list1:
#     index = list1.index(30)
#     list1[index] = 250
#     print(f'Произошла замена\n{list1}')
# else:
#     print('В списке нет числа 30')


# 3. Задан список слов, в которых встречается символ "_" (подчеркивания).
# Создать новый список, в котором символ подчеркивания в словах "_" заменить символом " " (пробел).
# L = [ 'ab_cd_e', 'abc', 'a_b_c', 'a__bc_d_', '__' ].

# print('Task #3')
#
# list1 = ['ab_cd_e', 'abc', 'a_b_c', 'a__bc_d_', '__']
# str1 = ','.join(list1).replace('_', ' ')
# list2 = str1.split(',')
# print(list2)


# 4. На вход программы подается словарь a = {1:10, 2:20, 3:30}, необходимо получить список произведения ключа
# на значение.

# print('Task #4')

# dict1 = {1: 10, 2: 20, 3: 30}
# list1 = []
# for key, value in dict1.items():
#     list1.append(key * value)
# print(list1)

# 5. Создай список, замени первый его элемент на [1, 2, 3], затем в конце списка добавь сумму элементов
# вложенного списка.

# print('Task #5')
#
# list1 = [random.randint(1, 100) for i in range(10)]
# list1[0] = [1, 2, 3]
# list1.append(sum(list1[0]))
# print(list1)
