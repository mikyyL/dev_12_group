#  2. Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
#  Окончанием ввода пусть служит пустая строка.
lines = input("Введите что-нибудь: ")
lines1 = input("Введите еще что-нибудь: ")
lines2 = input("Окончание ввода, просто нажмите ENTER")
list_input = [lines, lines1, lines2]
with open("task4.txt", "w") as file:
    for i in list_input:
        file.write(i + "\n")
with open("task4.txt", "r") as file:
    elements = file.read()
    print(elements)
