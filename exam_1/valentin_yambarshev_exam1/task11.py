#  11. Дана строка [“hello my friend”, “my name is”, “house”, “cat”, “dog”].
#  В новый список добавить элементы, которые содержат пробел.

listWord = ["hello my friend", "my name is", "house", "cat", "dog"]
listWordSpace = []
for word in listWord:
    if not word.isalpha():
        listWordSpace.append(word)
print(listWordSpace)

# if " " in i:
    # listWordSpace.append(word)