class Tomato:
    states = {'stages': ['absent', 'flowering', 'green', 'red']}

    def __init__(self, index):
        self.__index = index
        self.__state = self.states['stages'][self.__index]

    def grow(self):
        if self.__state != self.states['stages'][-1]:
            self.__index += 1
            self.__state = self.states['stages'][self.__index]
        print(f'На {self.__state} стадии созревания')
        return self.__state

    def is_ripe(self):
        if self.__state == self.states['stages'][-1]:
            return True
        else:
            return False


class TomatoBush:

    def __init__(self, tomato_count):
        # super().__init__(index)
        self.tomato_count = tomato_count
        self.tomatoes = []
        for tomat in range(tomato_count):
            self.tomatoes.append(Tomato(tomat))

    def grow_all(self):
        for tomat in self.tomatoes:
            if tomat.__dict__['_Tomato__state'] != tomat.__dict__['_Tomato__state'][-1]:
                tomat.grow()
                self.tomatoes.append(tomat)
            return self.tomatoes

    def all_arr_ripe(self):
        for tomat in self.tomatoes:
            if not tomat.is_ripe():
                return False
            else:
                return True
        # self.all_arr_ripe()

    def give_away_all(self):
        if self.all_arr_ripe() is True:
           self.tomatoes.clear()


class Gardener:

    def __init__(self, name):
        self.name = name
        self.__plant = Tomato(0)

    def work(self):
        return self.__plant.grow()

    def harvest(self):
        if self.__plant.is_ripe() is True:
            print('Садовник собирает урожай!!')
        else:
            print('Урожай ещё не созрел')

    @staticmethod
    def knowledge_base():
        print('Помидоры необходимо регулярно поливать 3-5 литра на куст\n'
              'Поливать помидоры 1-2 раза в неделю\n'
              'Опрыскивать от вредителей\n'
              'Рыхлить почву каждые 10-12 дней')


Gardener.knowledge_base()
bush = TomatoBush(3)
gardener = Gardener('Sancheller')
gardener.work()
gardener.harvest()
gardener.work()
gardener.work()
gardener.harvest()
