# 2. Если в функцию передается кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нем. Число - количество нечетных цифр.
# Строка - количество букв.


def func(x):
    if type(x) == tuple:
        list_tuple = len(x)
        print(f'Длина слов: {list_tuple}')
    elif type(x) == list:
        num_of_number = 0
        num_of_letters = 0
        for i in x:
            if type(i) == int:
                num_of_number += 1
        else:
            num_of_letters += len(i)
        print(f'Количество чисел в списке: {num_of_number}')
        print(f'Количество букв в списке: {num_of_letters}')
    elif type(x) == int:
        even = 0
        for i in str(x):
            if int(i) % 2 != 0:
                even += 1
        print(f'Количество нечетных цифр в числе: {even}')
    elif type(x) == str:
        num2 = 0
        for i in x:
            if i.isalpha():
               num2 += 1
        print(f'Количество букв в строке: {num2}')


func(('hello', 'world'))
func([1, 2, 3, 'hello'])
func(3456)
func('hello world')




