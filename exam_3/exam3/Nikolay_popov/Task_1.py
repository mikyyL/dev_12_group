# Требуется проверить, возможно ли из представленных отрезков условной длины сформировать
# треугольник. Для этого создайте класс TriangleChecker, принимающий только положительные
# числа. С помощью метода is_triangle() возвращаются следующие значения
# (в зависимости от ситуации):
# Ура, можно построить треугольник!
# С отрицательными числами ничего не выйдет!
# Жаль, но из этого треугольник не сделать.


class TriangleChecker:

    def __init__(self, a: int, b: int, c: int) -> str:
        try:
            if a < 0 or b < 0 or c < 0:
                raise ValueError
            else:
                self.a = a
                self.b = b
                self.c = c
            self.get_check_triangle()
        except ValueError:
            print('С отрицательными числами ничего не выйдет!')

    def get_check_triangle(self):
        if self.a < self.b + self.c:
            if self.c < self.b + self.a:
                if self.b < self.c + self.a:
                    print('Ура, можно построить треугольник!')
            else:
                print('Жаль, но из этого треугольник не сделать.')


d = TriangleChecker(-3, 3, 6)
