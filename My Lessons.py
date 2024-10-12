def find_unique_pairs(target):
    password = ''

    for a in range(1, target // 2 + 1):
        for b in range(a + 1, target + 1 - a):
            if target % (a + b) == 0:
                password += str(a) + str(b)
    return password

print(find_unique_pairs(20))