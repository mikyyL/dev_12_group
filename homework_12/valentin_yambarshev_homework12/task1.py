# 1. При заданном целом числе n посчитайте n + nn + nnn.
try:
    input_num = int(input("Введите любое целое число: "))
    n1 = str(input_num)
    n2 = n1 + n1
    n3 = n2 + n1
    result = int(n1) + int(n2) + int(n3)
except Exception:
    print("Введены некорректные данные")
else:
    print(f"Получившаяся сумма: {result}")
finally:
    print("Программа завершена")
