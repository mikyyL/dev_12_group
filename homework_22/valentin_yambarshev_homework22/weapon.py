class Weapon:

    def __init__(self, name, damage, durability):
        self.name = name
        self.damage = damage
        self.durability = durability

    def __str__(self):
        return f"{self.name} deals {self.damage} to the head, but it's durability is {self.durability}"
    