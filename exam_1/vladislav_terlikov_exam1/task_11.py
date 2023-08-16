"""
11.	Дана строка [“hello my friend”, “my name is”, “house”, “cat”, “dog”].
 В новый список добавить элементы, которые содержат пробел.
"""
string = "hello my friend, my name is, house, cat, dog"
lst = string.split(", ")  # разделяем строку на элементы по запятым
new_lst = [i for i in lst if ' ' in i]  # список который будет содержать только те подстроки,
                                        # которые содержат пробелы
print(new_lst)
