my_dict = {'Pasha' : 1991, 'Dasha' : 1992, 'Masha' : 1993, 'Vera' : 1980}
print(my_dict)
print(my_dict['Pasha'])
print(my_dict.get('Denis'))
my_dict.update({'Dima' : 2000, 'Lena' : 2003})
del my_dict['Pasha']
print(my_dict.get('Pasha'))
print(my_dict)
# Работа с множествами
my_set = {'Привет', 'Привет', True, True, 10, 10, 0.123, 0.123, (12, 13, 14, 15), (12, 13, 14, 15)}
print(my_set)
my_set.update({False, 'Пока'})
my_set.discard('Привет')
print(my_set)