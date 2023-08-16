"""
4) Дано три числа. Найти количество положительных чисел среди них
"""
a = 1
b = -2
c = 3
lst = []
plusnum = 0
lst.extend((a, b, c))
for i in lst:
    if i > 0:
        plusnum += 1
print(plusnum)
        