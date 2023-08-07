# 6. Напишите функцию для сортировки слов в алфавитном порядке.
def sort_func(str1):
    list_of_str = str1.split(' ')
    return sorted(list_of_str)


random_str = 'hello world cat dog bird'  # input('Введите произвольную строку из слов, через пробел " ": ')
print(sort_func(random_str))
