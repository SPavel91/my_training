calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(z):
    count_calls()
    number = len(z)
    upper_c = z.upper()
    lower_c = z.lower()
    return (number, upper_c, lower_c)

def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for item in list_to_search:
        if string == item.lower():
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(string_info('Python'))
print(string_info('Program'))
print(is_contains('Milk', ['Tia', 'Rat', 'CaT']))
print(is_contains('Bus', ['Game', 'bus']))
print(calls)