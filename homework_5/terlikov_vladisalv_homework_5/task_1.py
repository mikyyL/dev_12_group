import random

x = 0  # число попыток

while True:  # создаём цикл
    numbers = random.randint(1, 10)  # генерируем числа
    colors = random.randint(1, 2)  # генерируем цвет
    if colors < 2:
        colors = 'красный'
    else:
        colors = 'чёрный'

    n1 = int(input('Введите число: '))
    n2 = input('Введите цвет: ')

    if n1 != numbers or n2 != colors:
        print(f'Правильная комбинация {numbers} - {colors}')
    else:
        print(f'Вы выйграли!')
        break  # выходим из цикла
    x += 1
    if x >= 5:
        print('Вы израсходовали число попыток')
        break
