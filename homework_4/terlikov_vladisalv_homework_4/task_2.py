"""
2.Есть список с четными и нечетными элементами.
 Посчитать количество четных и нечетных элементов.
"""
# 1 способ

lst = range(0, 100001)
chet = []
nechet = []
for i in lst:
    if i % 2 == 0:
        chet.append('i')
    else:
        nechet.append('i')

print(f"Количество чётных чисел: {chet.count('i')}")
print(f"Количество нечётных чисел: {nechet.count('i')}")

# 2 способ

chet_1 = 0
nechet_1 = 0
for i in lst:
    if i % 2 == 0:
        chet_1 += 1
    else:
        nechet_1 += 1
print(f'{chet_1} :Количество чётных чисел')
print(f'{nechet_1} :Количество не чётных чисел')
