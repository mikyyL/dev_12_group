"""
Создать 4 фрукта.

Апельсин, яблоко, мандарин, банан
У всех фруктов есть сорт, список витаминов, цена, имя
У апельсина, мандарина, банана есть метод очистить
У яблока метод порезать
У банана есть характеристика: кол-во калия.
cоздать 4 объекта фрукта и использовать все доступные методы и характеристики
При вызове метода очистить, должно писаться имя фрукта
Например:
apple = Apple("sort", [a, b, c], 120, "apple")
apple.clear()
>>"apple очищен"
"""


class Fruits:

    def __init__(self, name, sort, vitamins, price):
        self.sort = sort
        self.vitamins = list(vitamins)
        self.price = price
        self.name = name

    def info(self):
        print(f'Фрукт: {self.name}\n'
              f'Cорт: {self.sort}\n'
              f'Витамины: {self.vitamins}\n'
              f'Цена: {self.price}\n')


class Orange(Fruits):

    def clear(self):
        print(f'{self.name} очищен')


class Apple(Fruits):

    def cut(self):
        print(f'{self.name} порезано')


class Mandarin(Fruits):

    def clear(self):
        print(f'{self.name} очищен')


class Banana(Fruits):

    def __init__(self, name, sort, vitamins, price, potassium):
        super().__init__(name, sort, vitamins, price)
        self.potassium = potassium

    def info(self):
        super().info()
        print(f'Кол-во калия {self.potassium} мг')


    def clear(self):
        print(f'{self.name} очищен')


orange = Orange('Апельсин', 'Навель', 'ACD', 10)
orange.info(), orange.clear()

apple = Apple('Яблоко', 'Голден', 'CDE', 9)
apple.info(), apple.cut()

mandarin = Mandarin('Мандарин', 'Клементин', 'ABD', 8)
mandarin.info(), mandarin.clear()

banana = Banana('Банан', 'Кавендишь', 'BCD', 10, 23)
banana.info(), banana.clear()
