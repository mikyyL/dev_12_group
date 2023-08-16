"""
2)	Функция sum(a,b) принимает 2 числа и возвращает их сумму. Написать декоратор,
который возвращает ошибку если переданы не числовые параметры(например строка)
примерно такое:
@validate_int_parameters
def sum(a,b)
sum(3, "1") => ошибка sum(4, 2) = > 6
"""


def validate_int_parameters(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError(f"{arg} не числовое значение")
        return func(*args)
    return wrapper


@validate_int_parameters
def sum(a, b):
    return a + b


a = 2
b = '2'
print(sum(a, b))
