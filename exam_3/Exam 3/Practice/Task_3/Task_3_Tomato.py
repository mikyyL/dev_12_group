class Tomato:

    states = {0: 'Отсутствует', 1: 'Цветение', 2: 'Зелёный', 3: 'Зрелый'}

    def __init__(self, index, state=states[0]):
        self._index = index
        self._state = state

    def grow(self):
        if self._state != self.states[3]:
            current_state = list(self.states.values()).index(self._state)
            next_state = current_state + 1
            self._state = self.states[next_state]
            return f'Плод {self._index} спеет.\n' \
                   f'Новое состояние: {self._state}'

    def is_ripe(self):
        return self._state == self.states[3]
        #     return f'Плод с индексом {self._index} созрел.'
        # else:
        #     return f'Плод с индексом {self._index} ещё в процессе созревания.'


t = Tomato(1, 'Зелёный')
# t2 = Tomato(2, 'Цветение')
t3 = Tomato(3, 'Зелёный')
# print(t.grow())
# print(t2.grow())
# print(t2.grow())
# print(t3.grow())
# # print(t.is_ripe())
