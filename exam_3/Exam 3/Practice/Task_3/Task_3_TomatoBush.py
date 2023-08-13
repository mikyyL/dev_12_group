from Task_3_Tomato import Tomato


class TomatoBush:

    def __init__(self, tomatoes):
        self.tomatoes = [Tomato(index=0, state='Отсутствует') for i in range(1, tomatoes + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        all_ripe = [tomato.is_ripe() for tomato in self.tomatoes]
        # all_states = []
        # for tomato in self.tomatoes:
        #     all_states = [True for i in self.tomatoes if list(tomato.states.values()).index(tomato._state) == 3]
        # print(all_ripe)
        print(all(all_ripe))
        return all(all_ripe)

    def give_away_all(self):
        self.tomatoes = []


# tb = TomatoBush(3)
# tb.grow_all()
# tb.grow_all()
# tb.grow_all()
# tb.all_are_ripe()
