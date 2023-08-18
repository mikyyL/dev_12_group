class Human:
    default_name = "John"
    default_age = 18

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}, Money: {self.__money}, House: {self.__house}")

    @staticmethod
    def default_info():
        print(f"Default Name: {Human.default_name}, Default Age: {Human.default_age}")

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, amount):
        self.__money += amount

    def buy_house(self, house, discount):
        final_price = house.final_price(discount)
        if self.__money >= final_price:
            self.__make_deal(house, final_price)
            print("House purchased successfully!")
        else:
            print("Not enough money to buy the house!")


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price - discount


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(40, price)


Human.default_info()
person = Human("Alice", 25)
person.info()


house = SmallHouse(50000)


person.buy_house(house, 10000)
person.earn_money(60000)
person.buy_house(house, 10000)
person.info()