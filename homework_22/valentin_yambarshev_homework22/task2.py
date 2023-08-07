# 2. Создайте класс Робот
# создайте 2 типа оружия: меч, автомат
# Создайте 2 типа амуниции: броня, шлем
# Добавьте оружию и амуниции свои характеристики(например урон, прочность)
# Создайте своего робота с каким либо оружием
# (может быть несколько и брони может быть несколько. Так же может быть ничего)
# Выведите весь арсенал робота на экран


from armor import Armor
from weapon import Weapon


class Robot:

    def __init__(self, name, weapon, armor):
        self.name = name
        self.weapon = weapon
        self.armor = armor

    def __str__(self):
        return f'A robot name {self.name}, with {self.weapon} and {self.armor}'


gun = Weapon('Gun', 34, 50)
armor = Armor('Exoskelet', 103, 37)
robot1 = Robot('T1000', gun, armor)
print(robot1)
