"""
4)	Функция для определения всех чисел, на которые без остатка делится указанное
"""


def find_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

number = int(input("Введите число: "))
print(find_divisors(number))