class Human:
    default_name = 'Nikolay'
    default_age = 36

    def __init__(self,name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None


    def get_info(self):
        return f'Name: {self.name}, Age: {self.age}, Money: {self._Human__money}, House: {self._Human__house}'

    @classmethod
    def static_method_info(cls):
        return f'Name: {cls.default_name}, Age: {cls.default_age}'

    def __make_deal(self, house, price):
        if self.__money >= price:
            self.__money = self.__money - price
            self.__house = house
        else:
            return f"Вам нехватает {price - self.__money}"


    def earn_money(self):
        self.__money += 10000


    def buy_house(self, house, discount):
        res_price = house.final_price(discount)
        return self.__make_deal(house, res_price)



class House:

    def __init__(self, area, price):
        self.__area = area
        self.__price = price

    def final_price(self, discount):
        self.discount = discount / 100
        res_discount = self.__price * self.discount
        return self.__price - res_discount


class SmallHouse(House):

    def __init__(self, area, price):
        super().__init__(40, 40000)



print(Human.static_method_info())
human = Human()
print(human.get_info())

house1 = SmallHouse(40, 80000)
print(human.buy_house(house1, 20))
human.earn_money()
print(human.buy_house(house1, 20))
human.earn_money()
print(human.buy_house(house1, 20))
human.earn_money()
print(human.buy_house(house1, 20))
human.earn_money()
print(human.buy_house(house1, 20))
print(human.get_info())