"""
3)	Создайте класс Soda (для определения типа газированной воды),
 принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду).
  В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки,
   а иначе отобразится следующая фраза: «Обычная газировка».
"""


class Soda:
    def __init__(self, additive=None):
        self.additive = additive

    def show_my_drink(self):
        if self.additive:
            print(f"Газировка и {self.additive}")
        else:
            print("Обычная газировка")


soda1 = Soda("лимон")
soda1.show_my_drink()  # Газировка и лимон

soda2 = Soda()
soda2.show_my_drink()  # Обычная газировка
