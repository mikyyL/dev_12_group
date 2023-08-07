# 7. Напишите функцию, которая определяет количество гласных в строке.
# «A», «E», «I», «O», «U», «Y»

def number_of_vowels(str1):
    sum_of_vowels = 0
    list_of_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    for i in str1.lower():
        if i in list_of_vowels:
            sum_of_vowels += 1
    print(f'Количество гласных букв в строке: {sum_of_vowels}')


random_str = 'hEllowOrldcAtdogbird'  # input('Введите случайную строку на латинице: ')
number_of_vowels(random_str)
