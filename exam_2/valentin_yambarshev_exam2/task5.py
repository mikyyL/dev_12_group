# 5. Есть словарь песен группы
# Depeche Mode violator songsdict =
# {'World in My Eyes': 4.76,
# 'Sweetest Perfection': 5.43,
# 'Personal Jesus': 4.56,
# 'Halo': 4.30,
# 'Waiting for the Night': 6.07,
# 'Enjoy the Silence': 4.6,
# 'Policy of Truth': 4.88,
# 'Blue Dress': 4.18,
# 'Clean': 5.68, }
# Выведите общее время звучания всех песен.
# Создайте список песен, время звучаниях которых больше 5 минут.
# Создайте новый словарь тех песен, в название которых состоит из одного слова.

songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 5.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68
}
time_songs = 0
list1 = []
list2 = []
list3 = 0
dict1 = {}
dict2 = {}
for key, value in songs_dict.items():
    list1.append(value)
    time_songs = sum(list1)
    if value > 5:
        list2.append(key)
    if " " not in key:
        dict1 = {key: value}
        # print(dict1)
        dict2.update(dict1)

print(f'Общее время звучания всех песен: {time_songs}\n')
print(f'Список песен, время звучаниях которых больше 5 минут:\n{list2}\n')
print(f'Песни, название которых состоит из одного слова: {dict2}')


