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

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            return f"Килограммы задаются только числами"


kg_to_pounds = KgToPounds(10)
print(kg_to_pounds.to_pounds())
print(kg_to_pounds.kg())
