from Task_4_SmallHouse import SmallHouse

print('Класс Human'
      'Создайте класс Human.'
      'Определите для него два статических атрибута: default_name и default_age.'
      'Создайте метод __init__(), который помимо self принимает еще два параметра: name и age. Для этих параметров задайте значения по умолчанию, используя атрибута default_name и default_age. В методе __init__() определите четыре атрибута: Публичные - name и age. Приватные - money и house.'
      'Реализуйте справочный метод info(), который будет выводить поля name, age, house и money.'
      'Реализуйте справочный статический метод default_info(), который будет выводить статические атрибуты default_name и default_age.'
      'Реализуйте приватный метод make_deal(), который будет отвечать за техническую реализацию покупки дома: уменьшать количество денег на счету и присваивать ссылку на только что купленный дом. В качестве аргументов данный метод принимает объект дома и его цену.'
      'Реализуйте метод earn_money(), увеличивающий значение свойства money.'
      'Реализуйте метод buy_house(), который будет проверять, что у человека достаточно денег для покупки, и совершать сделку. Если денег слишком мало - нужно вывести предупреждение в консоль. Параметры метода: ссылка на дом и размер скидки'
      'Класс House'
      'Создайте класс House'
      'Создайте метод __init__() и определите внутри него два атрибута: _area и _price. Свои начальные значения они получают из параметров метода __init__()'
      'Создайте метод final_price(), который принимает в качестве параметра размер скидки и возвращает цену с учетом данной скидки.'
      'Класс SmallHouse'
      'Создайте класс SmallHouse, унаследовав его функционал от класса House'
      'Внутри класса SmallHouse переопределите метод __init__() так, чтобы он создавал объект с площадью 40м2'
      'Тесты'
      'Вызовите справочный метод default_info() для класса Human()'
      'Создайте объект класса Human'
      'Выведите справочную информацию о созданном объекте (вызовите метод info()).'
      'Создайте объект класса SmallHouse'
      'Попробуйте купить созданный дом, убедитесь в получении предупреждения.'
      'Поправьте финансовое положение объекта - вызовите метод earn_money()'
      'Снова попробуйте купить дом'
      'Посмотрите, как изменилось состояние объекта класса Human')


class Human:

    default_name = 'Mike'
    default_age = 27

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        return f'Name: {self.name}\n' \
               f'Age: {self.age}\n' \
               f'House: {self.__house}\n' \
               f'Money: {self.__money}'

    @staticmethod
    def default_info():
        return f'Name: {Human.default_name}\n' \
               f'Age: {Human.default_age}\n'

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self):
        salary = float(input('How much money have you earn? '))
        self.__money += salary

    def buy_house(self, house, discount):
        final_price = house.final_price(discount)
        # print(final_price)
        if final_price <= self.__money:
            self.__make_deal(house, final_price)
            print(f'The house was successfully bought.')
        else:
            print('Not enough money:(')


print(Human.default_info())
man = Human('Den', 20)
print(man.info())
sm_h = SmallHouse(35000)
man.buy_house(sm_h, 15)
man.earn_money()
print(man.info())
man.buy_house(sm_h, 15)
print(man.info())
