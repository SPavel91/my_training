class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        if isinstance(owner, str):
            self.owner = owner
        if isinstance(model, str):
            self.__model = model
        if isinstance(engine_power, int):
            self.__engine_power = engine_power
        if isinstance(color, str):
            self.__color = color

    def get_model(self):
        return f'Модель {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(Vehicle.get_model(self))
        print(Vehicle.get_horsepower(self))
        print(Vehicle.get_color(self))
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if isinstance(new_color, str):
            for color in range(len(self.__COLOR_VARIANTS)):
                if self.__COLOR_VARIANTS[color].lower() == new_color.lower():
                    self.__color = new_color
                    break
            else:
                print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
# Изначальные свойства
vehicle1.print_info()
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
# Проверяем что поменялось
vehicle1.print_info()