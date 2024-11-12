from math import pi, sqrt

class Figure:
    sides_count = 0

    def __init__(self, color, sides):
        self.__sides = sides
        self.__color = color
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        self.__color = list(self.__color)                 # меняет цвет
        if self.__is_valid_color(r, g, b):
            self.__color[0] = r
            self.__color[1] = g
            self.__color[2] = b
        else:
            pass

    def __is_valid_sides(self, *sides_valid):
        count_sides = 0
        if isinstance(self.__sides, int):
            if isinstance(self.__sides, int) and self.__sides > 0:
                return True
            else:
                return False
        if isinstance(self.__sides, list):
            for i in sides_valid:
                if isinstance(i, int) and i > 0:
                    count_sides += 1
            if count_sides == len(self.__sides):
                return True
            else:
                return False

    def get_sides(self):
        if len(self.__sides) == 1:
            return list(self.__sides)
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = new_sides
        else:
            pass


class Circle(Figure):
    sides_count = 1

    def get_square(self):
        self.radius = self.__sides[0] / (2 * pi)
        return pi * self.radius * 2


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        self.semi_perimeter = super().__len__() / 2
        return sqrt(self.semi_perimeter
                    * (self.semi_perimeter - self.__sides[0])
                    * (self.semi_perimeter - self.__sides[1])
                    * (self.semi_perimeter - self.__sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        self.color = color
        self.sides = [sides] * self.sides_count
        super().__init__(self.color,self.sides)

    def get_volume(self):
        self.v_cube = self.sides[0] ** 3
        return self.v_cube


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

























