#  1. Дан список list = [15,48,'hello',6,19,'world’].
#  Все числа этого списка проверить на чётность.
#  Если число чётное, то посчитать сумму его цифр.
#  Если нечётное, то заменить его на 1 в списке.
#  Все слова: посчитать количество гласных и согласных. Вывести всё на экран.

list1 = [15, 48, 'hello', 6, 19, 'world']
listEven = []
listOfNumbers = []
listOfString = []
listOfBoolean = []
listVowels = ["a", "e", "i", "o", "u", "y"]
sumEven = 0
vowels = 0
consonants = 0
print(f"Изначальный список: {list1}")

#  Разделяем список на числа, строки и булевые значения
for elem in list1:
    if type(elem) == int:
        listOfNumbers.append(elem)
    elif type(elem) == str:
        listOfString.append(elem)
    else:
        listOfBoolean.append(elem)
print(f"Список слов: {listOfString}")
print(f"Список целых чисел: {listOfNumbers}")

#  Считаем количество гласных и согласных букв
strListWord = "".join(listOfString)
for letter in strListWord:  # перебираем в цикле все символы
    if letter in listVowels:  # проверяем наличие символа в списке гласных символов
        vowels += 1  #  гласные
    else:
        consonants += 1  #  согласные
print(f"Количество гласных букв в списке слов {listOfString}: {vowels}")
print(f"Количество согласных букв в списке слов {listOfString}: {consonants}")

#  Проверяем, если четное число, добавляем в новый список, если нечетное, то заменяем нечетное на единицу
for index, num in enumerate(listOfNumbers):
    if num % 2 == 0:
        listEven.append(num)
    else:
        listOfNumbers[index] = 1
print(f"Список целых чисел, в котором нечетное число заменили '1': {listOfNumbers}")
print(f"Список четных целых чисел: {listEven}")

#  Считаем сумму цифр в списке четных чисел
strListEven = [str(i) for i in listEven]  # каждый элемент переводим в строку в списке (до этого были числа)
strOfNum = ''.join(strListEven)  # объединяем список в одну строку без разделителя
num1 = int(strOfNum)  # переводим получившуюся строку в число
while num1 != 0:  # пока число не станет равно 0 цикл работает
    n = num1 % 10  # находим остаток от деления и далее добавляем в сумму
    sumEven += n
    num1 = num1 // 10  # избавляемся от ранее добавленного остатка в сумму
print(f"Сумма четных целых цифр каждого числа списка {listEven}: {sumEven}")