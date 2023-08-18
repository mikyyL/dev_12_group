class Tomato:
    states = {
        0: 'Отсутствует',
        1: 'Цветение',
        2: 'Зеленый',
        3: 'Красный'
    }

    def __init__(self, index):
        self._index = index
        self._state = self.states[0]

    def grow(self):
        if self._state != self.states[3]:
            current_state = list(self.states.keys())[list(self.states.values()).index(self._state)]
            next_state = self.states[current_state + 1]
            self._state = next_state

    def is_ripe(self):
        return self._state == self.states[3]


class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(index) for index in range(1, num_tomatoes + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        ripeness = [tomato.is_ripe() for tomato in self.tomatoes]
        return all(ripeness)

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай собран!")
        else:
            print("Не все помидоры созрели. Продолжаем ухаживать.")

    @staticmethod
    def knowledge_base():
        print("""
        Садоводство - наука и искусство выращивания растений в саду или огороде. 
        Для успешного выращивания растений необходимо обеспечить их правильный уход: полив, подкормка, удаление сорняков и т.д.
        Помните, что каждое растение имеет свои особенности и требует индивидуального подхода.
        Не забывайте следить за погодными условиями, так как они могут значительно влиять на рост и развитие растений.
        """)


def main():
    Gardener.knowledge_base()  # Вызываем справку


    bush = TomatoBush(5)
    gardener = Gardener("Иван", bush)


    gardener.work()


    gardener.harvest()


    gardener.work()
    gardener.harvest()
    gardener.harvest()


if __name__ == "__main__":
    main()