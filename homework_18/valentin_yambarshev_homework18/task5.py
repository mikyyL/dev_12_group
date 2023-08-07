# 5. Функция для определения того, является ли строка палиндромом.


def palindrome(str1):
    list1 = list(str1)
    list2 = []
    for i in list1:
        if i != ' ':
            list2.append(i)
    if list2[::] == list2[::-1]:
        return True
    else:
        return False


plndrme = 'А роза упала на лапу Азора'.lower()  # input('Введите Палиндром: ')
print(palindrome(plndrme))
