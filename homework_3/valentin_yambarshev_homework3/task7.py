# Творческое задание. Придумать свою задачу на тему занятия.
# Обязательно использовать несколько вложений if-else(elif).

string = input("Введите что-нибудь: ")
num = int(input("Введите любое число: "))
lenStr1 = len(string) > num
lenStr2 = len(string) == num
if lenStr1:
    correctString = "Вы ввели что-то непонятное \nподумайте лучше"
    print(f"{correctString}")
elif lenStr2:
    print(f"{string}")
else:
    print(f"Длина данной строки меньше {num}")