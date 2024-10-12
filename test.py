# Глобальная переменная для подсчета вызовов
calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(s):
    count_calls()  # Увеличиваем счетчик вызовов
    length = len(s)  # Вычисляем длину строки
    upper_case = s.upper()  # Преобразуем строку в верхний регистр
    lower_case = s.lower()  # Преобразуем строку в нижний регистр
    return (length, upper_case, lower_case)  # Возвращаем кортеж

def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счетчик вызовов
    # Приводим искомую строку к нижнему регистру и проверяем в списке
    return string.lower() in [item.lower() for item in list_to_search]  # Сравниваем регистры

# Примеры вызовов функций
print(string_info('Capybara'))  # Пример строки
print(string_info('Armageddon'))  # Пример строки

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches

# Вывод общего количества вызовов
print(calls)