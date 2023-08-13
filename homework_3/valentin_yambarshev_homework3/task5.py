# Пользователь вводит три числа. Если все числа больше 10,
# то вывести на экран yes, иначе no

randomNum1 = int(input("Введите случайное первое число: "))
randomNum2 = int(input("Введите случайное второе число: "))
randomNum3 = int(input("Введите случайное третье число: "))
if randomNum1 > 10 and randomNum2 > 10 and randomNum3 > 10:
    print("Yes")
else:
    print("No")