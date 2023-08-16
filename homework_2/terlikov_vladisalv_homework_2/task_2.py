# Разделить строку “Apples, Oranges, Pears, Bananas, Berries”
# по запятым и вывести на экран.
# Затем объединить элементы с использованием пробела,
# чтобы программа вывела “Apples Oranges Pears Bananas Berries”.
string = "Apples, Oranges, Pear, Bananas, Berries"
string_split = string.split(',')  # разделяем строку по символу ','
print(string_split)
string_join = ' '.join(string_split)  # объеденяем строку с использованием проблема
print(string_join)
