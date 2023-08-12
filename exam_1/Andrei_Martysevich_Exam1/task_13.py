# Дан список чисел, необходимо удалить все вхождения числа 20 из него.



# list1 = [i for i in range(0,30)]
# list1.remove(20)
# print(list1)

numbers = [1, 2, 3, 20, 200, 20, 20, 30]
while 20 in numbers:
    numbers.remove(20)
    print(numbers)