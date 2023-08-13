# 4. Ввести 10 чисел с клавиатуры, данные числа добавить во множество.
num_range_ten = input('Введите 10 чисел через пробел (" "): ').split()
list_num = list(map(int, num_range_ten))
set_num = set(list_num)
print(f'Множество чисел:\n{set_num}')

