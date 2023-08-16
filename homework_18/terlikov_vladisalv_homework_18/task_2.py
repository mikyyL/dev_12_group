"""
2)	Написать функцию date, принимающую 3 аргумента — день, месяц и год.
 Вернуть True, если такая дата есть в нашем календаре, и False иначе.
"""


def date(day, month, year):
    if month < 1 or month > 12:
        return False
    if year < 1:
        return False

    if month in [1, 3, 5, 7, 8, 10, 12]:
        days_in_month = 31
    elif month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days_in_month = 29
        else:
            days_in_month = 28
    else:
        days_in_month = 30

    if day < 1 or day > days_in_month:
        return False
    return True


day = int(input("Введите месяц: "))
month = int(input("Введите месяц: "))
year = int(input("Введите год: "))
print(date(day, month, year))
