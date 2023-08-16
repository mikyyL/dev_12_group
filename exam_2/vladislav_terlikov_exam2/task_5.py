"""
Есть словарь песен группы
 Depeche Mode violator songsdict
= { 'World in My Eyes': 4.76,
'Sweetest Perfection': 5.43,
'Personal Jesus': 4.56,
'Halo': 4.30,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.6,
'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68, }
Выведите общее время звучания всех песен.
Создайте список песен, время звучаниях которых больше 5 минут
Создайте новый словарь тех песен, в название которых состоит из одного слова
"""
songsdict = {'World in My Eyes': 4.76,
             'Sweetest Perfection': 5.43,
             'Personal Jesus': 4.56,
             'Halo': 4.30,
             'Waiting for the Night': 6.07,
             'Enjoy the Silence': 4.6,
             'Policy of Truth': 4.88,
             'Blue Dress': 4.18, 'Clean': 5.68}

values = songsdict.values()
longsongs = [song for song, duration in songsdict.items() if duration > 5]
one_word_songs = {song: duration for song, duration in songsdict.items() if len(song.split()) == 1}
print(f'Словарь тех песен, в название которых состоит из одного слова: {one_word_songs}')
print(f' Список песен с длительностью > 5 мин -  {longsongs}')
print(f' Общее время зувучания альбома - {sum(values)} мин.')









