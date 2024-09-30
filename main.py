from pprint import pprint
import io

class Product:

    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        str_products = f'{self.name}, {self.weight}, {self.category}'
        return str_products

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products_str = file.read()
        file.close()
        return products_str


    def add(self, *products):
        file = open(self.__file_name, 'a')
        for product in products:
            if str(product) not in Shop.get_products(self):
                file.write(str(product) + '\n')
            else:
                print(f'Продукт {str(product)} уже есть в магазине')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())