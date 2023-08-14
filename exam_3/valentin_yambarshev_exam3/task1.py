# Требуется проверить, возможно ли из представленных отрезков условной длины
# сформировать треугольник. Для этого создайте класс TriangleChecker,
# принимающий только положительные числа.
# С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
# Ура, можно построить треугольник!
# С отрицательными числами ничего не выйдет!
# Жаль, но из этого треугольник не сделать.

class TriangleChecker:

    def __init__(self, sides):
        self.sides = sides

    def is_triangle(self):
        if self.sides[0] + self.sides[1] >= self.sides[2] and self.sides[1] + self.sides[2] >= self.sides[0] and \
                self.sides[2] + self.sides[0] >= self.sides[1]:
            return f'{"Ура, можно построить треугольник!"}'
        elif self.sides[0] < 0 or self.sides[1] < 0 or self.sides[2] < 0:
            return f'{"С отрицательными числами ничего не выйдет!"}'
        else:
            return f'{"Жаль, но из этого треугольник не сделать."}'


triangleChecker = TriangleChecker([2, 3, 4])
print(triangleChecker.is_triangle())
triangleChecker1 = TriangleChecker([10, 2, 3])
print(triangleChecker1.is_triangle())
triangleChecker2 = TriangleChecker([1, -2, -3])
print(triangleChecker2.is_triangle())
