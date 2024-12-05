def is_prime(func):
    def wrapper(*args):
        num = sum(args)
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count == 2:
            print("Простое")
        else:
            print("Составное")
        return func(*args)
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)