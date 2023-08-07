# Определить существование треугольника.

# triangleAngle1 = int(input("Введите первый угол треугольника: "))
# triangleAngle2 = int(input("Введите второй угол треугольника: "))
# triangleAngle3 = int(input("Введите третий угол треугольника: "))
# triangle = 'треугольником'
# sumTriangleAngle = triangleAngle1 + triangleAngle2 + triangleAngle3
# if sumTriangleAngle == 180:
#     print(f"Испрашиваемая фигура является {triangle}")
# else:
#     print(f"Испрашиваемая фигура не является {triangle}")

triangleSide1 = int(input("Введите первую сторону треугольника: "))
triangleSide2 = int(input("Введите вторую сторону треугольника: "))
triangleSide3 = int(input("Введите третью сторону треугольника: "))
triangle = 'треугольником'
if triangleSide1 + triangleSide2 > triangleSide3:
    print(f"Испрашиваемая фигура является {triangle}")
elif triangleSide1 + triangleSide3 > triangleSide2:
    print(f"Испрашиваемая фигура является {triangle}")
elif triangleSide2 + triangleSide3 > triangleSide1:
    print(f"Испрашиваемая фигура является {triangle}")
else:
    print(f"Испрашиваемая фигура не является {triangle}")
