"""
1)	Реализовать калькулятор с 4 методами:
Сумма, вычитание , умножение, деление.
Метод принимает 2 аргумента и возвращает результат.
Невалидные данные должны быть обработаны.
Валидатором является в программе метод, который будет проверять ваши аргументы на то, является ли это число
"""


# class Calculate:
#     def validator(self, num1, num2):
#         try:
#             if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
#                 return True
#         except ValueError:
#             return False
#
#     def addition(self, num1, num2):
#         return num1 + num2
#
#     def subtraction(self, num1, num2):
#         return num1 - num2
#
#     def multiplication(self, num1, num2):
#         return num1 * num2
#
#     def division(self, num1, num2):
#         try:
#             return num1 / num2
#         except ZeroDivisionError:
#             return '"Ошибка: на ноль делить нельзя"'
#
#
# calculate = Calculate()
# while True:
#     select_operation = ("0: Выход из программы \n"
#                         "1: Сложение\n"
#                         "2: Вычитание\n"
#                         "3: Умножение\n"
#                         "4: Деление")
#     print(select_operation)
#     enter_operation = int(input('Введите номер операции: '))
#     if enter_operation == 0:
#         print('Вы вышли из программы')
#         break
#
#     num1 = 5
#     # num2 = 23
#     num2 = '23'
#     if calculate.validator(num1, num2):
#         if enter_operation == 1:
#             print(f'{num1} + {num2} = {calculate.addition(num1, num2)}')
#         elif enter_operation == 2:
#             print(f'{num1} - {num2} = {calculate.subtraction(num1, num2)}')
#         elif enter_operation == 3:
#             print(f'{num1} * {num2} = {calculate.multiplication(num1, num2)}')
#         elif enter_operation == 4:
#             print(f'{num1} / {num2} = {calculate.division(num1, num2)}')
#     else:
#         print('"Ошибка: значение не является числом!"')
#
#
#
# """Валидатор Артмёма"""
#
# def validate_numbers(self, first_number, second_number):
#     is_valid_first_number = isinstance(first_number, int) or isinstance(first_number, float)
#     is_valid_second_number = isinstance(second_number, int) or isinstance(second_number, float)
#     if is_valid_first_number and is_valid_second_number:
#         print('Valid')
#     else:
#         raise Exception('Not valid')

def validate_numbers(function):
    def wrapper_arguments(arg1, arg2):
        print(f'аргументы для проверки: {arg1}, {arg2}')
        if arg1.isalpha() or arg2.isalpha():
            raise Exception('arg is str')
        else:
            function(int(arg1), int(arg2))
        return wrapper_arguments()

def sum(a, b):
    return a + b

a = input('enter num: ')
b = input('enter num2: ')