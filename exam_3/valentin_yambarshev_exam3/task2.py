# Создан класс KgToPounds с параметром kg, куда передается определенное количество килограмм,
# а с помощью метода to_pounds() они переводятся в фунты. Чтобы закрыть доступ к переменной kg
# реализованы методы set_kg() – для задания нового значения килограммов,
# get_kg() – для вывода текущего значения кг.
# Из-за этого возникло неудобство: нам нужно теперь использовать эти 2 метода
# для задания и вывода значений. Помогите переделать класс с использованием свойств-декораторов @property.
# Код приведен ниже.


class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    def set_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            return f"Килограммы задаются только числами"

    @property
    def get_kg(self):
        return self.__kg

    def property(self, set_kg):
        def wrapper():
            set_kg()

        return wrapper()


kg_to_pounds = KgToPounds(10)
print(kg_to_pounds.to_pounds())
# kg_to_pounds.set_kg(20)
# print(kg_to_pounds.get_kg())
print(kg_to_pounds.get_kg())

