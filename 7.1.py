# 7.1  "Режимы открытия файлов"
# Задача "Учёт товаров":
from pprint import pprint



class Product:


    def  __init__ (self, name, weight, category):
        self.name=name                       # название продукта (строка)
        self.weight=weight          # общий вес товара (дробное число)
        self.category=category           # категория товара (строка).


    def __str__ (self):
        return (f'{self.name}, {self.weight}, {self.category}')








p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
