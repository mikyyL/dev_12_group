# 16*. Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин) в введенной строке
# (программа не должна зависеть от регистра вводимых символов). Например, в строке "acggtgttat" процентное содержание символов
# G и C равно 4/10 ⋅ 100 = 40.0 где 4 - это количество символов G и C, а 10 -- это длина строки.

chem_formula = input('Введите хим формулу: ').upper()
count_simb = 0
proc_simb = 0
for i in chem_formula:
    if i == 'c' or i == 'C':
        count_simb += 1
    if i == 'g' or i == 'G':
        count_simb += 1
    proc_simb = count_simb * 100/len(chem_formula)
    print(proc_simb)