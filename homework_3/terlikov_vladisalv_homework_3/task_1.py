"""Определить, является ли год високосным."""
year = int(input('Введите год: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'{year} :высокосный год')
else:
    print(f'{year} :не высокосный год')
