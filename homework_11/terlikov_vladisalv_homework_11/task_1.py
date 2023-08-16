"""
1) Есть список состоящий из слов и чисел,
 нужно записать в файл сначала слова в порядке их длины,
  а после слов цифры в порядке возрастания.
"""
lst = ['hi', 1, 5, 'pythonist', 'world', 9, 3]
lst_words = [i for i in lst if type(i) == str]
lst_words.sort(key=len)
lst_nums = [i for i in lst if type(i) == int]
lst_nums.sort()
lst2 = lst_words + lst_nums
str_file = ''.join(str(lst2))
file_str = str_file.replace('[', '').replace(']', '')
print(str_file)

with open('text.txt', 'w') as file:
    file.write(file_str)
