"""3. Дана длина ребра куба. Найти объем куба и площадь его боковой поверхности."""
import math
cubeLth = 6
cubeVlm = math.pow(cubeLth, 3)
sqSrfcArea = 4 * math.pow(cubeLth, 2)
print('Объем куба: ', cubeVlm)
print('Площадь боковой поверхности куба: ', sqSrfcArea)