# Даны два целых числа m и n (m≤n). Напишите программу, которая выводит все числа от m до n включительно.


m = int(input('Введите первое число: '))
n = int(input('Введите второе число: '))
if m < n:
    for i in range(m, n + 1):
        print(i)
elif m > n:
    print('Ошиба')
else:
    if m == n:
        print('Stop')

