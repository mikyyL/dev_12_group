# Напишите программу, которая выполняет сравнение двух переменных.

randomNum1 = int(input(" Введите первое случайное число: "))
randomNum2 = int(input(" Введите первое случайное число: "))
if randomNum1 > randomNum2:
    print(f"{randomNum1} больше {randomNum2}")
else:
    print(f"{randomNum2} больше {randomNum1}")