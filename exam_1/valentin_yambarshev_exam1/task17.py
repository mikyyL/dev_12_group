#  17. Дезоксирибонуклеиновая кислота (ДНК) представляет собой
# химическое вещество, находящееся в ядре клеток и несущее
# «инструкции» по развитию и функционированию живых организмов.
# В цепочках ДНК символы «А» и «Т» дополняют друг друга, как «С» и «G».
# Вам нужно вернуть другую дополнительную сторону.
# Нить ДНК никогда не бывает пустой или ДНК вообще не существует.
# Пример: (ввод --> вывод)
# “АТТGС" --> "ТААСG"
# “GТАТ" --> "САТА"

strAny = input("Введите строку из букв 'А' 'C' 'G' 'T': ").upper()
newStr = ""
for letter in strAny:
    if letter == "A":
        newStr += "T"
    elif letter == "T":
        newStr += "A"
    elif letter == "C":
        newStr += "G"
    elif letter == "G":
        newStr += "C"
print(newStr)

