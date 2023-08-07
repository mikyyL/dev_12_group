# Пользователь вводит два числа с клавиатуры. Вывести на экран yes,
# если они отличаются друг от друга на 135,
# иначе вывести на экран No;

randomNum1 = int(input("Введите случайное первое число: "))
randomNum2 = int(input("Введите случайное второе число: "))
differenceOfNum = abs(randomNum1 - randomNum2)
if differenceOfNum == 135:
    print("Yes")
else:
    print("No")