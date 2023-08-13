# Класс Human
# Создайте класс Human.
# Определите для него два статических атрибута: default_name и default_age.
# Создайте метод __init__(), который помимо self принимает еще два параметра: name и age. Для этих параметров задайте
# значения по умолчанию, используя атрибута default_name и default_age. В методе __init__() определите четыре атрибута:
# Публичные - name и age. Приватные - money и house.
# Реализуйте справочный метод info(), который будет выводить поля name, age, house и money.
# Реализуйте справочный статический метод default_info(), который будет выводить статические атрибуты default_name и default_age.
# Реализуйте приватный метод make_deal(), который будет отвечать за техническую реализацию покупки дома: уменьшать количество
# денег на счету и присваивать ссылку на только что купленный дом. В качестве аргументов данный метод принимает объект дома и его цену.
# Реализуйте метод earn_money(), увеличивающий значение свойства money.
# Реализуйте метод buy_house(), который будет проверять, что у человека достаточно денег для покупки, и совершать сделку.
# Если денег слишком мало - нужно вывести предупреждение в консоль. Параметры метода: ссылка на дом и размер скидки

class Human:
    default_name = 'Олег'
    default_age = '39'

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'{self.name}, {self.age}, {self.__money}, {self.__house}')

    @staticmethod
    def default_info():
        print(f'{Human.default_name}, {Human.default_age}')

    def __make_deal(self, house, price):
        self.__house = house
        self.__money = price

    def earn_money(self, increase):
        self.__money += increase

    def buy_house(self, house, warning):
        final_price = house.final_price(warning)
        if self.__money >= final_price :
            self.__make_deal(house, final_price)
            return 'У вас хватило денег на покупку дома.'
        else:
            return 'У вас не достаточно денег на покупку дома.'

# Класс House
# Создайте класс House
# Создайте метод __init__() и определите внутри него два атрибута: _area и _price. Свои начальные значения они получают
# из параметров метода __init__()
# Создайте метод final_price(), который принимает в качестве параметра размер скидки и возвращает цену с учетом данной скидки.

class House:
    def __init__(self, _area, _price):
        self._area = _area
        self._price = _price

    def final_price(self, warning):
        return self._price - warning
# Класс SmallHouse
# Создайте класс SmallHouse, унаследовав его функционал от класса House
# Внутри класса SmallHouse переопределите метод __init__() так, чтобы он создавал объект с площадью 40м2

class SmallHouse(House):
    def __init__(self, price):
        super().__init__(40, price)

# Тесты
# Вызовите справочный метод default_info() для класса Human()
# Создайте объект класса Human
# Выведите справочную информацию о созданном объекте (вызовите метод info()).
# Создайте объект класса SmallHouse
# Попробуйте купить созданный дом, убедитесь в получении предупреждения.
# Поправьте финансовое положение объекта - вызовите метод earn_money()
# Снова попробуйте купить дом
# Посмотрите, как изменилось состояние объекта класса Human

Human.default_info()
buyer = Human('Олег', 39)
buyer.info()
house = SmallHouse(179000)
buyer.buy_house(house, 29000)
buyer.earn_money(240000)
buyer.buy_house(house,179000)
buyer.info()
# У меня тут что-то не так, как посмотрите скажите пожалуйста что.
