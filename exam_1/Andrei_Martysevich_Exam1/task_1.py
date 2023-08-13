# Используя стандартные арифметические операции представьте самое большое целое число из цифр 4, 4, 4 и приведите его значение.
num1 = 4
num2 = 4
num3 = 4
a = num1 + num2 + num3
b = num1 * num2 * num3
c = num1 ** num2 ** num3
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)
else:
    print(f'Ошибка')
