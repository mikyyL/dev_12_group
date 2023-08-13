# Определить, является ли год високосным.

leapYear = int(input('Введите случайный год: '))
if leapYear % 4 == 0:
    print(f"{leapYear} является високосным годом")
else:
    print(f"{leapYear} не является високосным годом")