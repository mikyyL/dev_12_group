#  16. Напишите программу, которая вычисляет процентное содержание
#  символов G (гуанин) и C (цитозин) в введенной строке
#  (программа не должна зависеть от регистра вводимых символов).
#  Например, в строке "acggtgttat" процентное содержание
#  символов G и C равно 4/10 ⋅ 100 = 40.0 где 4 - это количество символов G и C,
#  а 10 -- это длина строки.

strAny = input("Введите строку из букв английского алфавита: ")
strLowerCase = strAny.lower()
lenStrAny = len(strLowerCase)
countLetterC = 0
countLetterG = 0
for letter in strLowerCase:
    if letter == "c":
        countLetterC += 1
    elif letter == "g":
        countLetterG += 1
percent = (countLetterC + countLetterG) / lenStrAny * 100
print(f"Процентное содержание символов G и C равно: {percent}")
