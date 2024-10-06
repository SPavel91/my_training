result_bug = []
result = []
n = int(input("Введите число от 3 до 20: ",))

while n < 3:
    print('Вы ввели не верное число, по пробуйте еще раз!')
    n = int(input())
    continue

while n > 20:
    print('Вы ввели не верное число, по пробуйте еще раз!')
    n = int(input())
    continue

for i in range(1, 10):
    for j in range(10):
        for z in range(9):
            num_n_2 = (i + j) * z
            if num_n_2 == n:
                if i < j:
                    result_bug.append(f'{i}{j}')
    for j in range(2, n):
        num_n = i + j
        if num_n == n:
            if i < j:
                result_bug.append(f'{i}{j}')

result = list(dict.fromkeys(result_bug))
print('Код к числу:', n, "-", ''.join(result))







