"""1. Перемножить все нечётные значения
 в диапазоне от 1 до 100."""

d = range(1, 100)
result = 1
for i in d:
    if i % 2 != 0:
        result *= i
        print(result)
