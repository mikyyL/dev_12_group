'''5. Найти результат выражения. Переменная a вводится с клавиатуры.'''

import math
a = int(input('Введите число: '))
y = math.pow((((1 + a + math.pow(a, 2)) / (2 * a + math.pow(a, 2)) + 2) - (1 - a + math.pow(a, 2)) / (2 * a - math.pow(a, 2))), (-1)) * (5 - 2 * math.pow(a, 2))
print(y)