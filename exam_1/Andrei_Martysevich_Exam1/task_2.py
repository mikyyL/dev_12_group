#Написать программу для вычисления значения выражений. Проверить правильность выполнения задания с помощью тестовых значений.
import math

a = int(input('Введите alpha: '))
b = int(input('Введите beta: '))
g = int(input('Введите gama: '))
y = 1/4 * (math.sin(a + b - g) + math.sin(b + g - a) + math.sin(g + a - b) - math.sin(a + b + g))
print(y)
