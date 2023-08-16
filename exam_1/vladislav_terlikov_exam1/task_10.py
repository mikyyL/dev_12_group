"""
10.	Вывести на экран числа от 0 до 50, кроме 35.
"""
lst = [i for i in range(51)]
for i in lst:
    if i != 35:
        print(i)
