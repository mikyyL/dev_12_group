"""
2)	Создайте программу, которая, принимая массив имён, возвращает строку описывающая количество лайков (как в Facebook).
Примеры:
likes() -> "no one likes this"
likes("Ann") -> "Ann likes this"
likes("Ann", "Alex") -> "Ann and Alex like this"
likes("Ann", "Alex", "Mark") -> "Ann, Alex and Mark like this"
likes("Ann", "Alex", "Mark", "Max") -> "Ann, Alex and 2 others like this"
"""


def likes(names):
    if len(names) == 0:
        return f"{names}  no one likes this"
    elif len(names) == 1:
        return f"{names}, likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]}  likes this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]}  likes this"
    elif len(names) == 4:
        return f"{names[0]}, {names[1]} and 2 others like this"


names = []

while True:
    name = input("Введите имя пользователя или stop для завершения ввода: ")
    if name == 'stop':
        break
    else:
        names.append(name)


print(likes(names))
