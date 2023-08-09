class Tomato:
    states = {0: "Отсутствует", 1: "Цветение", 2: "Зеленый", 3: "Красный"}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1
            print(f"Томат {self._index} перешел в стадию {Tomato.states[self._state]}")
        else:
            print(f"Томат {self._index} уже созрел")

    def is_ripe(self):
        return self._state == 3


class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(i) for i in range(num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print(f"{self.name} работает в саду")
        self._plant.grow_all()
        print(f"{self.name} закончил работу")

    def harvest(self):
        print(f"{self.name} собирает урожай")
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print(f"{self.name} собрал весь урожай")
        else:
            print(f"Слишком рано! Еще есть зеленые томаты")

    @staticmethod
    def knowledge_base():
        print("""
Справка по садоводству:
- Чтобы вырастить помидоры, нужно создать куст с помидорами и садовника, который будет за ним ухаживать.
- Садовник может работать в саду, чтобы ускорить рост помидоров.
- Садовник может собирать урожай, когда все помидоры созреют.
- Помидоры проходят четыре стадии созревания: отсутствие, цветение, зеленый и красный.
""")


if __name__ == "__main__":

    Gardener.knowledge_base()

    bush = TomatoBush(3)
    gardener = Gardener("Дмитрий", bush)

    while not bush.all_are_ripe():
        gardener.work()
        gardener.harvest()
        print()

    gardener.harvest()
