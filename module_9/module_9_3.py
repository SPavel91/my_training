first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(i[0]) - len(i[1])) for i in zip(first, second) if len(i[0]) != len(i[1]))
second_result = (len(first[z]) == len(second[x]) for z in range(len(first)) for x in range(len(second)) if z == x)

print(list(first_result))
print(list(second_result))
