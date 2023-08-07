#  5. Есть список чисел с дубликатами. Создать новый список в котором будут только уникальные элементы.

listNum = [1, 2, 2, 3, 3, 4, 5, 6, 6, 9]
newListNum = []
for i in listNum:
    if i in newListNum:
        continue
    else:
        newListNum.append(i)
print(newListNum)