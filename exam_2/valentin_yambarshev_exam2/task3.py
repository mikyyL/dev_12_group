# 3. Создайте словарь из строки 'An apple a day keeps the doctor away' следующим образом:
# в качестве ключей возьмите символы строки, а значениями пусть будут числа,
# соответствующие количеству вхождений данной буквы в строку.

str1 = 'An apple a day keeps the doctor away'
dict1 = {key: }
set1 = set(str1)
for i in set1:
    dict1 = {i: str1.count(i)}
    print(dict1)

