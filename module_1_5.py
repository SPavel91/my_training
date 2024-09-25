immutable_var = 1, '2', True, 0.123
print(immutable_var)
immutable_var[0] = 2 #  кортеж не поддерживает обращение по элементам, он используется в качестве хранилища, например, для какого-то списка, который мы ни коим образом не хотим трогать, то есть нам нужно чтобы он оставался неизменным. Кортеж занимает меньше места чем список
mutable_list = [1, '2', True, 0.123]
mutable_list[0] = 0.123
mutable_list[1] = False
mutable_list[2] = '3'
mutable_list[3] = 2
print(mutable_list)