#  1. Даны два словаря: dictionary_1 = {'a': 300, 'b': 400} и dictionary_2 = {'c': 500, 'd': 600}.
#  Объедините их в один, при помощи встроенных функций языка Python.
print(f"\nСпособ № 1 через метод UPDATE")
dictionary_1 = {"a": 300, "b": 400}
dictionary_2 = {"c": 500, "d": 400}
dictionary_1.update(dictionary_2)
print(dictionary_1)

print(f"\nСпособ № 2 через оператор '**' ")
merged_dict1 = {**dictionary_1, **dictionary_1}
print(merged_dict1)

print(f"\nСпособ № 3 через оператор '|' ")
merged_dict2 = dictionary_1 | dictionary_1
print(merged_dict2)
