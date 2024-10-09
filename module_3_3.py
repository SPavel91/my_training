def print_params(a = 1, b = "string", c = True):
    print(a, b, c)

values_list = [5, "строка", (1, 2, 3)]
values_dict = {'a' : 1, 'b' : [8, 7, 6], 'c' : 'hello'}
values_list_2 = [345, "строчка"]

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)