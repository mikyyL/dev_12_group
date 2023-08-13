# Требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник. Для этого создайте
# класс TriangleChecker, принимающий только положительные числа. С помощью метода is_triangle() возвращаются следующие значения
# (в зависимости от ситуации):
# Ура, можно построить треугольник!
# С отрицательными числами ничего не выйдет!
# Жаль, но из этого треугольник не сделать.


class TriangleChecker:
    def __init__(self, ot_a, ot_b, ot_c):
        self.ot_a = ot_a
        self.ot_b = ot_b
        self.ot_c = ot_c

    def is_triangle(self):
        if(self.ot_a and self.ot_b and self.ot_c) > 0:
            return 'Ура, можно построить треугольник!'
        if(self.ot_a and self.ot_b and self.ot_c) < 0:
            return 'С отрицательными числами ничего не выйдет!'
        if(self.ot_a and self.ot_b and self.ot_c) == 0:
            return 'Жаль, но из этого треугольник не сделать.'
        else:
            return 'Ошибка'

test_triugol = TriangleChecker(-2, -3, -12)
print(test_triugol.is_triangle())





