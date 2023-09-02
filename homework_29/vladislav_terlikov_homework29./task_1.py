"""
1) С сайта https://www.21vek.by/mobile/iphone_12_mini/ спарсить все названия смартфонов с их ценами.
Записать в csv файл: 1 колонка - названия телефонов, 2 колонка - на сколько GB, 3 колонка - стоимость
Обработать файл и выяснить какой телефон с наименьшей стоимостью(вывести имя-GB-стоимость)
"""
import csv
import requests
from bs4 import BeautifulSoup

URL = 'https://www.21vek.by/mobile/iphone_12_mini/'
response = requests.get(URL, timeout=5)
response_text = response.text

soup = BeautifulSoup(response_text, 'lxml')

names = soup.find_all('span', class_="result__name")

phones = []
memory = []

for name in names:
    phone = name.text
    phones.append(phone)
txt = ' '.join(phones).split(' ')

for gb in txt:
    if gb[-1] == 'B':
        memory.append(gb)

for gb in memory:
    if gb == 'B':
        memory.remove('B')

prices = soup.find_all('form', class_='j-to_basket')

costs = []

for price in prices:
    costs.append(price['data-price'])

print("Смартфон с наименьшей ценой:")
print(
    f'Название телефона: {phones[7]}\nКоличество GB: {memory[7]}\nСтоимость: {min(costs)}')

with open("iphone.csv", 'w', newline="", encoding="Utf-8") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Название', 'Объём памяти GB', 'Стоимость'])

    for name, memory, costs in zip(phones, memory, costs):
        writer.writerow([name, memory, costs])
