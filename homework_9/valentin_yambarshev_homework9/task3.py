#  3. Задан список слов, в которых встречается символ ‘_’ (подчеркивание).
#  Создать новый список, в котором символ подчеркивания в словах ‘_’ заменить символом ‘ ‘ (пробел).
#  l = [ "ab_cd_e", "abc", "a_b_c", "a__bc_d_", "__" ].

list1 = ["ab_cd_e", "abc", "a_b_c", "a__bc_d_", "__"]
list2 = []
for i in list1:
    list2.append(i.replace("_", " "))
print(list2)
