# 1) С сайта https://www.21vek.by/mobile/iphone_12_mini/ спарсить все названия смартфонов с их ценами.
# Записать в csv файл: 1 колонка - названия телефонов, 2 колонка - на сколько GB, 3 колонка - стоимость.
# Обработать файл и выяснить какой телефон с наименьшей стоимостью(вывести имя-GB-стоимость).
import csv
import requests
from bs4 import BeautifulSoup

URL = 'https://www.21vek.by/mobile/iphone_12_mini/'
response = requests.get(URL, timeout=5)
response_text = response.text

soup = BeautifulSoup(response_text, 'lxml')
block_name = soup.find_all('span', class_='result__name')
list_name = []
list_memory = []

for name in block_name:
    list_name.append(name.text)
text = ' '.join(list_name).split(' ')

for elem in text:
    if elem[-1] == 'B':
        list_memory.append(elem)

for elem in list_memory:
    if elem == 'B':
        list_memory.remove('B')

block_price = soup.find_all('form', class_='j-to_basket')
list_price = []
for price in block_price:
    list_price.append(price['data-price'])
print(list_price.index(min(list_price)))
print(f'Название телефона: {list_name[7]}\nКоличество встроенной памяти: {list_memory[7]}\nСтоимость: {min(list_price)}')
data = [
    ['Название телефона', 'Количество встроенной памяти', 'Стоимость']
]
with open('task1.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    for name, memory, price in zip(list_name, list_memory, list_price):
        row = [name, memory, price]
        data.append(row)
    writer.writerows(data)
