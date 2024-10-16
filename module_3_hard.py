data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]


def calculate_structure_sum(*summa):
    total_sum = 0
    for i in summa:
        if isinstance(i, list):
            total_sum += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            for key, value in i.items():
                if isinstance(key, str):
                    total_sum += len(key)
                total_sum += value
        elif isinstance(i, tuple):
            total_sum += calculate_structure_sum(*i)
        elif isinstance(i, set):
            total_sum += calculate_structure_sum(*i)
        else:
            if isinstance(i, str):
                total_sum += len(i)
            elif isinstance(i, int):
                total_sum += i
    return total_sum


result = calculate_structure_sum(data_structure)
print(result)