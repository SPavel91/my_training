class Product:

    def __init__(self, name, weight, category):
        if isinstance(name, str):
            self.name = name
        if isinstance(weight, float):
            self.weight = weight
        if isinstance(category, str):
            self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self. category}'


class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        existing_products = self.get_products().splitlines()

        for product in products:
            if product.name not in [p.split(", ")[0] for p in existing_products]:
                file = open(self.__file_name, 'a')
                file.write(f"{product}\n")
                file.close()
            else:
                print(f"Продукт {product.name} {product.weight} {product.category} уже есть в магазине.")


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
