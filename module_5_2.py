class House:
    def __init__(self, name, number_of_floors):
        self.new_floor = None
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors: # внес изменения по Вашему замечанию :)
            self.new_floor = new_floor
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print('"Такого этажа не существует"')


    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
# h1.go_to(5)
# h2.go_to(10)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
