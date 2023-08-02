# 1. Реализовать калькулятор с 4 методами:
# Сумма, вычитание , умножение, деление.
# Метод принимает 2 аргумента и возвращает результат.
# Невалидные данные должны быть обработаны.
# Валидатором является в программе метод,
# который будет проверять ваши аргументы на то, является ли это число


class Calculator:

    def validator(self, num1, num2):
        try:
            if type(num1) == int and type(num2) == int:
                return num1, num2
        except (TypeError, ValueError):
            return 'Переменная не соответствуют числовому типу'

    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError:
            return 'На ноль делить нельзя'


calculator = Calculator()
while True:
    dict_of_operation = {0: 'Выход', 1: 'Сложение', 2: 'Вычитание', 3: 'Умножение', 4: 'Деление'}
    for key, value in dict_of_operation.items():
        print(f'{key} - {value}')
    select_of_operation = int(input('Выберите номер операции: '))
    if select_of_operation == 0:
        break

    num1 = 2
    num2 = '2'
    if calculator.validator(num1, num2):
        if select_of_operation == 1:
            print(f'Результат: {calculator.addition(num1, num2)}\n')
        elif select_of_operation == 2:
            print(f'Результат: {calculator.subtraction(num1, num2)}\n')
        elif select_of_operation == 3:
            print(f'Результат: {calculator.multiplication(num1, num2)}\n')
        elif select_of_operation == 4:
            print(f'Результат: {calculator.division(num1, num2)}\n')

