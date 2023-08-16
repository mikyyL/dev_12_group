"""Определить существование треугольника."""
abc = 'Треугольник'
ab = float(input('Сторона ab: '))
bc = float(input('Сторона bc: '))
ac = float(input('Сторона ac: '))
if ab + bc > ac and ac + bc > ab and ab + ac > bc:
    print(f'{abc} существует')
else:
    print(f'{abc} не существует')
