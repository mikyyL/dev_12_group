# 1. Перемножить все нечётные значения в диапазоне от 1 до 100.
start = int(input('Введите начало последовательности: '))
end = int(input('Введите конец последовательности: '))
mltiplicOfOddNum = 1

for i in range(start, end):
    if i % 2 == 1:
        mltiplicOfOddNum *= i
print(f"Произведение всех нечетных значений: \n{mltiplicOfOddNum}")
