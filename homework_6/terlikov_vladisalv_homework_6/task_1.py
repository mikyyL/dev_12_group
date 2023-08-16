"""
1) Дан список list=[15,48,'hello',6,19,'world’].
Все числа этого списка проверить на чётность.
Если число чётное, то посчитать сумму его цифр.
Если нечётное, то заменить его на 1 в списке.
Все слова: посчитать количество гласных и согласных.
Вывести всё на экран.
"""

lst = [15, 48, 'hello', 6, 19, 'world']
print(f'{lst}: исходный список')

lst3 = []

for i in lst:
    if type(i) == int:
        if i % 2 == 0:
            num1 = i % 10
            num2 = i // 10
            num3 = num1 + num2
            lst3.append(num3)
        else:
            ind = lst.index(i)
            lst[ind] = 1
print(f'{lst3}: сумма цифр чётных чисел')
print(f'{lst}: замена нечётный чисел на 1')

lst2 = [i for i in lst if type(i) == str]
string = ''.join(lst2)
glas = 0
soglas = 0
for i in string:
    if i == 'a':
        glas += 1
    elif i == 'e':
        glas += 1
    elif i == 'i':
        glas += 1
    elif i == 'o':
        glas += 1
    elif i == 'u':
        glas += 1
    elif i == 'y':
        glas += 1
    else:
        soglas += 1

print(f'{glas}: количество гласных букв в {lst2}')
print(f'{soglas}: количество согласных букв в {lst2}')
