"""
Ввести 10 чисел с клавиатуры, данные числа добавить во множество.
"""
numbers = set()
for i in range(10):
    number = int(input("Введите число: "))
    numbers.add(number)

print(numbers)

