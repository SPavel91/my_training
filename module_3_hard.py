data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]


def calculate_structure_sum(summa):
    total_sum = 0
    if isinstance(summa, list):
        for i in summa:
            total_sum += calculate_structure_sum(i)
    elif isinstance(summa, dict):
        for key, value in summa.items():
            if isinstance(key, str):
                total_sum += len(key)
            total_sum += calculate_structure_sum(value)
    elif isinstance(summa, tuple):
        for i in summa:
            total_sum += calculate_structure_sum(i)
    elif isinstance(summa, set):
        for i in summa:
            total_sum += calculate_structure_sum(i)
    else:
        if isinstance(summa, str):
            total_sum += len(summa)
        elif isinstance(summa, int):
            total_sum += summa
    return total_sum


result = calculate_structure_sum(data_structure)
print(result)