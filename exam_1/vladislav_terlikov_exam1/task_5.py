"""
5.	 Даны два целых числа m и n. Напишите программу,
 которая выводит все числа от m до n включительно в порядке возрастания,
 если m<n, или в порядке убывания в противном случае.
"""
m = int(input('Введите число m: '))
n = int(input('Введите число n: '))
new_lst = []
if m < n:
    for i in range(m - 1, n):
        i += 1
        new_lst.append(i)
    print(f'{m} < {n}: выводим список в порядке возрастания  \n {new_lst} ')
elif m > n:
    for i in range(n - 1, m):
        i += 1
        new_lst.append(i)
        new_lst.sort(reverse=True)
    print(f'{m} > {n}: выводим список в порядке убывания  \n {new_lst} ')
