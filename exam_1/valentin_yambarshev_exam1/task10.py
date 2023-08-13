#  10. Вывести на экран числа от 0 до 50, кроме 35.

for digit in range(0, 52):
    if digit == 35:
        continue
    print(digit)