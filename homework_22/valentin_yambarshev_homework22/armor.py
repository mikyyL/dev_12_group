class Armor:

    def __init__(self, name, strength, weight):
        self.name = name
        self.strength = strength
        self.weight = weight

    def __str__(self):
        return f"{self.name} has strength {self.strength} and it's mass {self.weight} kg"