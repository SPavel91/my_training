result = ''
n = int(input("Введите число от 3 до 20: ",))
z = 0
x = 1

while not 2 < n < 21:
    print('Вы ввели не верное число, по пробуйте еще раз!')
    n = int(input())
    continue

while 2 < n:
    z += 1
    while 2 < n:
        x += 1
        if n % (z + x) == 0:
            result += str(z) + str(x)
            if x >= n // 2 + 1:
                x = z + 1
                break
    if x + z == n or x + z + 1 == n:
        break

print(result)