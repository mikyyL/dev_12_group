"""
1)	Простейший калькулятор c введёнными двумя числами вещественного типа.
Ввод с клавиатуры: операции + - * / и два числа.
Операции являются функциями. Обработать ошибку:
“Деление на ноль” Ноль использовать в качестве завершения программы (сделать как отдельную операцию).
"""

def add(x, y):
    return x + y

def subt(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

print("Выберете операцию")
print("1: '+' ")
print("2: '-' ")
print("3: '*' ")
print("4: '/' ")
print("0: '0' - Выход")

while True:
    choice = input("Введите номер операции (1/2/3/4/0): ")
    if choice in ('1', '2', '3', '4', '0'):
        if choice == '0':
          print("Программа завершена.")
          break
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите число.")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subt(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", mult(num1, num2))
        elif choice == '4':
            try:
                print(num1, "/", num2, "=", div(num1, num2))
            except ZeroDivisionError:
                print("Деление на ноль невозможно.")
        else:
            print("Неверный ввод. Пожалуйста, выберите один из вариантов.")


