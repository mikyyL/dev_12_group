class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (1 - discount)


class SmallHouse(House):
    def __init__(self):
        super().__init__(40, 100000)


class Human:
    default_name = "John"
    default_age = 30

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nMoney: {self.__money}\nHouse: {self.__house}")

    @staticmethod
    def default_info():
        print(f"Default name: {Human.default_name}\nDefault age: {Human.default_age}")

    def make_deal(self, house, price):
        if self.__money >= price:
            self.__money -= price
            self.__house = house
            print("Deal is done!")
        else:
            print("Not enough money!")

    def earn_money(self):
        self.__money += 1000

    def buy_house(self, house, discount=0):
        price = house.final_price(discount)
        if self.__money >= price:
            self.make_deal(house, price)
        else:
            print("Not enough money!")


small_house = SmallHouse()
human = Human()
human.info()
human.earn_money()
human.buy_house(small_house)
human.info()
