def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [3, 'Daria', False]
values_dict = {'a': True, 'b': [5, 7], 'c': 91}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['oki', 12]
print_params(*values_list_2, 42)