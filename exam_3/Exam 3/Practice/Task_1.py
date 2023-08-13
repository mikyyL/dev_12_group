print('Требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник. '
      'Для этого создайте класс TriangleChecker, принимающий только положительные числа. '
      'С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):'
      'Ура, можно построить треугольник!'
      'С отрицательными числами ничего не выйдет!'
      'Жаль, но из этого треугольник не сделать.')


class TriangleChecker:

    def is_triangle(self, side_1, side_2, side_3):
        if (side_1 + side_2 >= side_3) and (side_2 + side_3 >= side_1) and (side_1 + side_3 >= side_2):
            return 'Ура, можно построить треугольник!'
        elif side_1 < 0 or side_2 < 0 or side_3 < 0:
            return 'С отрицательными числами ничего не выйдет!'
        else:
            return 'Жаль, но из этого треугольник не сделать.'


tr_check = TriangleChecker()
side1 = float(input('Enter length of the first side. Answer: '))
side2 = float(input('Enter length of the second side. Answer: '))
side3 = float(input('Enter length of the third side. Answer: '))
print(tr_check.is_triangle(side1, side2, side3))
