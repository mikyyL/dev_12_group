# 1) С сайта https://www.21vek.by/mobile/iphone_12_mini/ спарсить все названия смартфонов с их ценами.
# записать в csv файл: 1 колонка - названия телефонов, 2 колонка - на сколько GB, 3 колонка - стоимость
# Обработать файл и выяснить какой телефон с наименьшей стоимостью(вывести имя-GB-стоимость)
import time

import requests
from bs4 import BeautifulSoup
import lxml
import csv
import datetime

start_time = time.time()
current_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
with open(f'file_iphone_info_{current_time}.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(
        (
            'id',
            'Название телефона',
            'Объём постоянной памяти',
            'Цена'
        )
    )


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
count = 0
url = 'https://www.21vek.by/mobile/iphone_12_mini/'
response = requests.get(url=url, headers=header)

soup = BeautifulSoup(response.text, 'lxml')
catalog_all_phone = soup.find_all('li', class_='result__item')
for item in catalog_all_phone:
    iphone_name = item.find('div', class_='catalog-result__item_data').find('a').find_all('span')[1].text
    iphone_ram = item.find('dd', class_='result__desc').find_all('tr')[3].find_all('td')[1].text
    try:
        iphone_price = int(item.find('div', class_='catalog-result__item_tools').find_all('span')[0].find('span')['content'].replace('.', ''))
        count += 1
    except:
        iphone_price = 'Нет цены'
        count += 1
    # print(iphone_name)
    # print(iphone_ram)
    # print(iphone_price)
    # print(count)

    iphone_data = (
        {
            'id': count,
            'iphone_name': iphone_name,
            'iphone_ram': iphone_ram,
            'iphone_price': iphone_price
        }
    )

    with open(f'file_iphone_info_{current_time}.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([(count), (iphone_name), (iphone_ram), (iphone_price)])

with open(f'file_iphone_info_{current_time}.csv', encoding='utf-8') as file:
    file_rider = csv.DictReader(file, delimiter=',')
    min_price_iphone = []
    for row in file_rider:
        if row['Цена'] != 'Нет цены':
            min_price_iphone.append(row['Цена'])
    print(min(min_price_iphone))







finish_time = time.time() - start_time
print(finish_time)

