# 4. Дан список чисел. Если число встречается более двух раз, то добавить его в новый список

listNum = [1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6, 9]
newListNum = []
for i in listNum:
    if listNum.count(i) > 2:
        newListNum.append(i)
    if newListNum.count(i) > 1:
        newListNum.remove(i)
print(f" Новый список:\n {newListNum}")
