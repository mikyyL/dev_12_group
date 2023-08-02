# 1. Напишите программу, которая запрашивает у пользователя информацию о различных книгах
# и сохраняет их данные в файл формата CSV.
# Требования: Программа должна запрашивать у пользователя информацию о каждой книге,
# включая название, автора и год издания. Информация о каждой книге должна быть сохранена
# в отдельной строке файла CSV. Файл CSV должен иметь следующие заголовки столбцов:
# "Название", "Автор", "Год издания". Программа должна продолжать запрашивать информацию
# о книгах до тех пор, пока пользователь не введет команду "stop" для завершения.
# В конце выполнения программы должно быть выведено сообщение об успешном сохранении данных.
import csv

with open('task1.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["Название", "Автор", "Год издания"])
    while True:
        name = input('Введите "stop" для завершения или введите название книги: ')
        if name == "stop":
            break
        autor = input('Введите автора книги: ')
        year = input('Введите год издания книги: ')
        writer.writerow([name, autor, year])
    print('Данные введены успешно')
