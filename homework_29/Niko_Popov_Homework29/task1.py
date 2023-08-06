# 1) С сайта https://www.21vek.by/mobile/iphone_12_mini/ спарсить все названия смартфонов с их ценами.
# записать в csv файл: 1 колонка - названия телефонов, 2 колонка - на сколько GB, 3 колонка - стоимость
# Обработать файл и выяснить какой телефон с наименьшей стоимостью(вывести имя-GB-стоимость)


import requests
from bs4 import BeautifulSoup
import lxml

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
count = 0
url = 'https://www.21vek.by/mobile/iphone_12_mini/'
response = requests.get(url=url, headers=header)

soup = BeautifulSoup(response.text, 'lxml')
catalog_all_phone = soup.find_all('li', class_='result__item')
for item in catalog_all_phone:
    iphon_name = item.find('div', class_='catalog-result__item_data').find('a').find_all('span')[1].text
    iphon_ram = item.find('dd', class_='result__desc').find_all('tr')[3].find_all('td')[1].text
    try:
        iphone_price = item.find('div', class_='catalog-result__item_tools').find_all('span')[0].find('span')['content']
    except:
        iphone_price = 'На данный товар нет цены'


