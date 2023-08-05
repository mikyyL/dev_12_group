# 1. Написать программу, со следующим интерфейсом: пользователю предоставляется
# на выбор 12 вариантов
# перевода(описанных в первой задаче).
# Пользователь вводит цифру от одного до двенадцати.
# После программа запрашивает ввести численное значение.
# Затем программа выдает конвертированный результат.
# Использовать функции из первого задания.
# Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.


inch_in_centimeter = lambda x: x * 2.54  # 1. Дюймы в сантиметры
centimeter_in_inch = lambda x: x * 1 / 2.54  # 2. Сантиметры в дюймы
mile_in_kilometer = lambda x: x * 1.60934  # 3. Мили в километры
kilometer_in_mile = lambda x: x * 1 / 1.60934  # 4. Километры в мили
pounds_in_kilogram = lambda x: x * 0.453592  # 5. Фунты в килограммы
kilogram_in_pounds = lambda x: x * 1 / 0.453592  # 6. Килограммы в фунты
ounce_in_gram = lambda x: x * 28.3495  # 7. Унции в граммы
gram_in_ounce = lambda x: x * 1 / 28.3495  # 8. Граммы в унции
gallon_in_liter = lambda x: x * 4.54609  # 9. Галлон в литры
liter_in_gallon = lambda x: x * 1 / 4.54609  # 10. Литры в галлоны
pint_in_liter = lambda x: x * 0.568261  # 11. Пинты в литры
liter_in_pint = lambda x: x * 1 / 0.568261  # 12. Литры в пинты

dict1 = {1: 'Дюймы в сантиметры',
         2: 'Сантиметры в дюймы',
         3: 'Мили в километры',
         4: 'Мили в километры',
         5: 'Фунты в килограммы',
         6: 'Килограммы в фунты',
         7: 'Унции в граммы',
         8: 'Граммы в унции',
         9: 'Галлон в литры',
         10: 'Литры в галлоны',
         11: 'Пинты в литры',
         12: 'Литры в пинты'
         }
for key, value in dict1.items():
    print(f'{key}: {value}')

while True:
    choice = int(input('Введите число, которое соответствует переводу из одних единиц в другие, либо 0 для выхода: '))
    if choice == 0:
        break
    x = int(input('Введите число для перевода: '))
    if choice == 1:
        print(inch_in_centimeter(x))
    elif choice == 2:
        print(centimeter_in_inch(x))
    elif choice == 3:
        print(mile_in_kilometer(x))
    elif choice == 4:
        print(kilometer_in_mile(x))
    elif choice == 5:
        print(pounds_in_kilogram(x))
    elif choice == 6:
        print(kilogram_in_pounds(x))
    elif choice == 7:
        print(ounce_in_gram(x))
    elif choice == 8:
        print(gram_in_ounce(x))
    elif choice == 9:
        print(gallon_in_liter(x))
    elif choice == 10:
        print(liter_in_gallon(x))
    elif choice == 11:
        print(pint_in_liter(x))
    elif choice == 12:
        print(liter_in_pint(x))
