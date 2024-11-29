def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        results[function.__name__] = function(int_list)
    return results


result1 = apply_all_func([6, 20, 15, 9], max, min)
result2 = apply_all_func([6, 20, 15, 9], len, sum, sorted)
print(result1, result2)