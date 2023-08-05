# 4. Дано три числа. Найти количество положительных чисел среди них.
x = 1
y = -3
z = -1
pol_num = 0
list1 = [x, y, z]
for i in list1:
    if i < 0:
        pol_num += 1
print(pol_num)
