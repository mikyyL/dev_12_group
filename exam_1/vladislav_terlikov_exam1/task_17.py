"""
17*.
Дезоксирибонуклеиновая кислота (ДНК) представляет собой
химическое вещество, находящееся в ядре клеток и несущее
«инструкции» по развитию и функционированию живых организмов.
В цепочках ДНК символы «А» и «Т» дополняют друг друга, как «С» и
«G».Вам нужно вернуть другую дополнительную сторону. Нить
ДНК никогда не бывает пустой или ДНК вообще не существует.
Пример: (ввод --> вывод)

“АТТGС" --> "ТААСG"
“GТАТ" --> "САТА"
"""
dna = input('Введите сторону ДНК:')
new_dna = ''
for i in dna:
    if i == 'A':
        new_dna += 'T'
    elif i == 'T':
        new_dna += 'A'
    elif i == 'C':
        new_dna += 'G'
    elif i == 'G':
        new_dna += 'C'
print(new_dna)