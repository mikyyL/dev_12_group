# Создан класс KgToPounds с параметром kg, куда передается определенное количество
# килограмм, а с помощью метода to_pounds() они переводятся в фунты. Чтобы закрыть доступ
# к переменной kg реализованы методы set_kg() – для задания нового значения килограммов,
# get_kg() – для вывода текущего значения кг. Из-за этого возникло неудобство: нам нужно
# теперь использовать эти 2 метода для задания и вывода значений.
# Помогите переделать класс с использованием свойств-декораторов @property.
# Код приведен ниже.

class KgToPounts:

    def __init__(self, kg):
        self.__kg = kg

    def to_pounts(self):
        return self.__kg * 2.205

    @property
    def set_print_kg(self):
        return self.__kg

    @set_print_kg.setter
    def set_print_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            print('Килограммы задаются только числами')


d = KgToPounts(10)
print(d.to_pounts())
print(d.set_print_kg)