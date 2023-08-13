# Требуется проверить, возможно ли из представленных отрезков условной длины
# сформировать треугольник. Для этого создайте класс TriangleChecker,
# принимающий только положительные числа.
# С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
# Ура, можно построить треугольник!
# С отрицательными числами ничего не выйдет!
# Жаль, но из этого треугольник не сделать.

class TriangleChecker:

    def __init__(self, positive_num):
        self.positive_num = positive_num

    def is_triangle(self):
        if self.positive_num > 0:
            return f'{"Ура, можно построить треугольник!"}'
        elif self.positive_num < 0:
            return f'{"С отрицательными числами ничего не выйдет!"}'
        else:
            return f'{"Жаль, но из этого треугольник не сделать."}'


triangleChecker = TriangleChecker(0)
print(triangleChecker.is_triangle())
