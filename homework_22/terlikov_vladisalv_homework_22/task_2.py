"""
Создайте класс Робот.
Создайте 2 типа оружия: меч, автомат
Создайте 2 типа амуниции: броня, шлем
Добавьте оружию и амуниции свои характеристики(например урон, прочность)
Создайте своего робота с каким либо оружием
(может быть несколько и брони может быть несколько. Так же может быть ничего)
Выведите весь арсенал робота на экран

"""


class Robot:
    def __init__(self, name, weapons, armors):
        self.name = name
        self.weapons = dict(weapons)
        self.armors = dict(armors)

    def info(self):
        info = f'Робот: {self.name}\n'
        info += f'Оружие: {", ".join(self.weapons.keys())}\n'
        info += f'Наносимый урон:\n'
        for weapon in self.weapons:
            info += f'- {weapon} - наносит {self.weapons[weapon]} единиц урона\n'
        info += f'Амуниция: {", ".join(self.armors.keys())}\n'
        info += f'Прочность:\n'
        for armor in self.armors:
            info += f'- {armor} - запас прочности {self.armors[armor]} единиц\n'
        return info


robot = Robot("Терминатор-1", [("Меч", 50), ("Автомат", 30)], [("Шлем", 100), ("Броня", 90)])
print(robot.info())


class MyRobot(Robot):
    def __init__(self, name, weapons, armors):
        super().__init__(name, weapons, armors)

    def info(self):
        info = super().info()
        return info


my_robot = MyRobot("Терминатор-2", [("Меч", 50), ("Автомат", 30), ("Граната", 100)], [("Шлем", 100), ("Броня", 90),
                                                                                      ("Очки", 30)])
print(my_robot.info())


class Rodot_01:

    def __init__(self, name, weapon, armor):
        self.name = name
        self.weapon = weapon
        self.armor = armor

    def __str__(self):
        return f'A robot name {self.name}, with {self.weapon} and {self.armor}' \
               f''


class Weapon:

    def __init__(self, name, damage, durability):
        self.name = name
        self.damage = damage
        self.durability = durability

    def __str__(self):
        return f'{self.name} deals {self.damage} to the head, but its durability is {self.durability}'


class Armor:

    def __init__(self, name, strength, weight):
        self.name = name
        self.strength = strength
        self.weight = weight

    def __str__(self):
        return f'{self.name} has strength {self.strength} and its mass {self.weight} kg'


gun = Weapon('blaster', 100, 50)
armor = Armor('exoskelet', 100, 300)
robot = Robot('Bumblebee', gun, armor)
print(Robot)
