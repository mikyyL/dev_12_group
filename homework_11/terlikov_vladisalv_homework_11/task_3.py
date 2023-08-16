"""
3) В текстовом файле посчитать количество строк,
 а также для каждой отдельной строки определить
  количество в ней символов.
"""
filename = 'text3.txt'
line_count = 0
with open(filename, 'r') as file:
    lines = file.readlines()
    print(f'количество строк - {len(lines)}')
    for i, line in enumerate(lines):
        print(f"Строка {i + 1}: {len(line.strip())} символов")
