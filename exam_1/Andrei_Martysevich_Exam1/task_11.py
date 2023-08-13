# Дана строка [“hello my friend”, “my name is”, “house”, “cat”, “dog”]. В новый список добавить элементы, которые содержат пробел.

string = ['hello my friend', 'my name is', 'house', 'cat', 'dog']
new_string = []
for i in string:
    if not i.isalpha():
        new_string.append(i)
        print(new_string)
