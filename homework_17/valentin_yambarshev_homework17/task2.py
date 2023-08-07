# 2. Создайте программу, которая, принимая массив имён,
# возвращает строку описывающая количество лайков (как в Facebook).
# Примеры:
# likes() -> "no one likes this"
# likes("Ann") -> "Ann likes this"
# likes("Ann", "Alex") -> "Ann and Alex like this"
# likes("Ann", "Alex", "Mark") -> "Ann, Alex and Mark like this"
# likes("Ann", "Alex", "Mark", "Max") -> "Ann, Alex and 2 others like this"

def likes(list_of_name):
    like = len(list_of_name)
    rpt_frs = ' likes this'
    if like == 0:
        return 'no one' + rpt_frs
    elif like == 1:
        return list_of_name[0] + rpt_frs
    elif like == 2:
        return ' and '.join(list_of_name) + rpt_frs
    elif like == 3:
        return ', '.join(list_of_name[0:2]) + f' and {list_of_name[2]}{rpt_frs}'
    elif like > 3:
        return ', '.join(list_of_name[0:2]) + f' and {like - 2} others{rpt_frs}'


print(likes([]))
print(likes(["Ann"]))
print(likes(["Ann", "Alex"]))
print(likes(["Ann", "Alex", "Mark"]))
print(likes(["Ann", "Alex", "Mark", "Max"]))
print(likes(["Ann", "Alex", "Mark", "Max", "Pit", "Ivan"]))
