#  14. С клавиатуры вводится десятизначное число.
#  Вывести на экран четные числа входящие в данное число.
#  Например 1234567892  2 4 6 7 8 2

num1 = int(input("Введите целое 10-ти значное число: "))
strNum1 = str(num1)
list2 = []
print(type(strNum1))
for i in strNum1:
    if int(i) % 2 == 0:
        list2.append(i)
print(list2)
