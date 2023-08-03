# 2. Функция sum(a,b) принимает 2 числа и возвращает их сумму.
# Написать декоратор, который возвращает ошибку если переданы не числовые параметры(например строка)
# примерно такое:
# @validate_int_parameters
# def sum(a,b)
# sum(3, "1") => ошибка sum(4, 2) = > 6

def validate_int_parameters(func):
    def wrapper(a, b):
        if type(a) is int and type(b) is int:
            return func(a, b)
        else:
            return 'Ошибка'

    return wrapper


@validate_int_parameters
def sum1(a, b):
    return a + b


num1 = 3
num2 = "1"
print(sum1(num1, num2))

"""Я не могу понять! Почему если через int(input()), то не срабатывает обработчик исключений и raise,
а если через просто присваивание элементов, то все работает? Объясни Артем!!! Кстати, тоже самое
происходит с этим кодом, если присвоены просто значения, то все работает."""
