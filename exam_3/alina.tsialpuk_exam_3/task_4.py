"""
Задача: покупка дома
	Описание классовой структуры
Есть Человек, характеристиками которого являются:
Имя
Возраст
Наличие денег
Наличие собственного жилья
Человек может:
Предоставить информацию о себе
Заработать деньги
Купить дом
Также же есть Дом, к свойствам которого относятся:
Площадь
Стоимость
Для Дома можно:
Применить скидку на покупку
Также есть Небольшой Типовой Дом, обязательной площадью 40м2.
Задание
Класс Human
Создайте класс Human.
Определите для него два статических атрибута: default_name и default_age.
Создайте метод __init__(), который помимо self принимает еще два параметра: name и age.
Для этих параметров задайте значения по умолчанию, используя атрибута default_name и default_age.
В методе __init__() определите четыре атрибута: Публичные - name и age. Приватные - money и house.
Реализуйте справочный метод info(), который будет выводить поля name, age, house и money.
Реализуйте справочный статический метод default_info(), который будет выводить статические атрибуты default_name и default_age.
Реализуйте приватный метод make_deal(), который будет отвечать за техническую реализацию покупки дома: уменьшать количество денег на счету и присваивать ссылку на только что купленный дом. В качестве аргументов данный метод принимает объект дома и его цену.
Реализуйте метод earn_money(), увеличивающий значение свойства money.
Реализуйте метод buy_house(), который будет проверять, что у человека достаточно денег для покупки, и совершать сделку. Если денег слишком мало - нужно вывести предупреждение в консоль. Параметры метода: ссылка на дом и размер скидки
Класс House
Создайте класс House
Создайте метод __init__() и определите внутри него два атрибута: _area и _price. Свои начальные значения они получают из параметров метода __init__()
Создайте метод final_price(), который принимает в качестве параметра размер скидки и возвращает цену с учетом данной скидки.
Класс SmallHouse
Создайте класс SmallHouse, унаследовав его функционал от класса House
Внутри класса SmallHouse переопределите метод __init__() так, чтобы он создавал объект с площадью 40м2
Тесты
Вызовите справочный метод default_info() для класса Human()
Создайте объект класса Human
Выведите справочную информацию о созданном объекте (вызовите метод info()).
Создайте объект класса SmallHouse
Попробуйте купить созданный дом, убедитесь в получении предупреждения.
Поправьте финансовое положение объекта - вызовите метод earn_money()
Снова попробуйте купить дом
Посмотрите, как изменилось состояние объекта класса Human


"""
class Human:
    default_name = 'Alex'
    default_age = 32
    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 30000
        self.__house = None
    def info(self):
        return f'Меня зовут {self.name}, мне {self.age} года. У меня есть {self.__money} денег и' \
               f' дом {self.__house}'

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
            print("Дом ваш!")
        else:
            print("У вас нехватает денег на этот дом!")


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price - discount


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(40, price)


Human.default_info() #вызываем справочный метод
human1 = Human("Alina", 32) #объект класса
print(human1.info()) #справочная информация об объекте

house = SmallHouse(100000) #объект класса

human1.buy_house(house, 10000) #пробуем купить дом
human1.earn_money(60000) #попровляем финансовое положение
human1.buy_house(house, 10000) #пробуем купить дом
print(human1.info()) #смотрим, как изменилась информация об объекте