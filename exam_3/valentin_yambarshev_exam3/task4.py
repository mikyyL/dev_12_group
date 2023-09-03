class Human:
    default_name = 'Oleg'
    default_age = 32

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        return f'Имя: {self.name}\nВозраст: {self.age}\nНаличие денег: {self.__money}\n' \
               f'Наличие жилья: {self.__house}'

    @staticmethod
    def default_info():
        return f'Изначальное имя: {Human.default_name}\nИзначальный возраст: {Human.default_age}'

    def earn_money(self, amount):
        self.__money += amount
        return f'Мы заработали: {amount} денег! Текущий счет: {self.__money}'

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print('Недостаточно денег')

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f'Окончательная стоимость: {final_price}')
        return final_price

class SmallHouse(House):

    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


alex = Human('Alex', 34)
house = House(100, 9000)
alex.buy_house(house, 3)
small_house = SmallHouse(9000)
alex.buy_house(small_house, 3)
print(alex.earn_money(100000))
print(alex.info())
alex.buy_house(3, small_house)



