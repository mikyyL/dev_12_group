"""
1)	Написать 12 функций по переводу:
1. Дюймы в сантиметры
2. Сантиметры в дюймы
3. Мили в километры
4. Километры в мили
5. Фунты в килограммы
6. Килограммы в фунты
7. Унции в граммы
8. Граммы в унции
9. Галлон в литры
10. Литры в галлоны
11. Пинты в литры
12. Литры в пинты.
 Написать программу, со следующим интерфейсом:
пользователю предоставляется на выбор 12 вариантов перевода(описанных в первой задаче).
Пользователь вводит цифру от одного до двенадцати. После программа запрашивает ввести численное значение.
Затем программа выдает конвертированный результат. Использовать функции из первого задания.
Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.
"""


def inch_to_sm(inch):
    return inch * 2.54


def sm_to_inch(sm):
    return sm * 0.393701


def miles_to_km(miles):
    return miles * 1.60934


def km_to_miles(km):
    return km * 0.621371


def pound_to_kg(pound):
    return pound * 0.453592


def kg_to_pound(kg):
    return kg * 2.20462


def ounce_to_gr(ounce):
    return ounce * 28.3495


def gr_to_ounce(gr):
    return gr * 0.035274


def gallon_to_liter(gallon):
    return gallon * 3.78541


def liter_to_gallon(liter):
    return liter * 0.264172


def pint_to_liter(pint):
    return pint * 0.568261


def liter_to_pint(liter):
    return liter * 1.75975


print('Введите номер функции для перевода, от 1 до 12 или 0 для выхода из программы')
print('1. Дюймы в сантиметры\n'
      '2. Сантиметры в дюймы\n'
      '3. Мили в километры\n'
      '4. Километры в мили\n'
      '5. Фунты в килограммы\n'
      '6. Килограммы в фунты\n'
      '7. Унции в граммы\n'
      '8. Граммы в унции\n'
      '9. Галлон в литры\n'
      '10. Литры в галлоны\n'
      '11. Пинты в литры\n'
      '12. Литры в пинты')

value = float(input('Введите значение: '))
while True:
    choice = input('Введите ваш выбор: ')
    if choice == '0':
        break
    elif choice == '1':
        print(f'{value} дюймов = {inch_to_sm(value)} сантиметров')
    elif choice == '2':
        print(f'{value} сантиметров = {sm_to_inch(value)} дюймов')
    elif choice == '3':
        print(f'{value} миль = {miles_to_km(value)} километров')
    elif choice == '4':
        print(f'{value} километров = {km_to_miles(value)} миль')
    elif choice == '5':
        print(f'{value} фунтов = {pound_to_kg(value)} килограмм')
    elif choice == '6':
        print(f'{value} килограмм = {kg_to_pound(value)} фунтов')
    elif choice == '7':
        print(f'{value} унций = {ounce_to_gr(value)} грамм')
    elif choice == '8':
        print(f'{value} грамм = {gr_to_ounce(value)} унций')
    elif choice == '9':
        print(f'{value} галлон = {gallon_to_liter(value)} литров')
    elif choice == '10':
        print(f'{value} литров = {liter_to_gallon(value)} галлон')
    elif choice == '11':
        print(f'{value} пинт = {pint_to_liter(value)} литров')
    elif choice == '12':
        print(f'{value} литров = {liter_to_pint(value)} пинт')
    else:
        print('Неправильный выбор, пожалуйста выберете функцию из списка')
