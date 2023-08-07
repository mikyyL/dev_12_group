# 1. Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа.
# Операции являются функциями. Обработать ошибку: “Деление на ноль”.
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).

try:
    def func_plus():
        return num1 + num2


    def func_minus():
        return num1 - num2


    def func_mltpl():
        return num1 * num2


    def func_dvsn():
        return num1 / num2


    while True:
        operation = input('Введите операцию "+", "-", "*", "/": ')
        num1 = float(input('Введите первое любое число: '))
        num2 = float(input('Введите второе любое число: '))


        def calc(x, y, z):
            if operation == '+':
                print(func_plus())
            elif operation == '-':
                print(func_minus())
            elif operation == '*':
                print(func_mltpl())
            elif operation == '/':
                print(func_dvsn())


        calc(operation, num1, num2)

except ZeroDivisionError:
    print('На ноль делить нельзя')
except Exception:
    print('Введены некорректные данные')
finally:
    print('Программа завершена')
