# from pprint import pprint



class Product:

    def  __init__ (self, name, weight, category):
        self.name=name                       # название продукта (строка)
        self.weight=weight          # общий вес товара (дробное число)
        self.category=category           # категория товара (строка).


    def __str__ (self):
        return f'{self.name}, {self.weight}, {self.category}'

class  Shop():
    def __init__(self):
       self.__file_name = 'products.txt'


    def get_products(self):
        self.__file_name=open('products.txt','r')
        print (f'{self.__file_name.read()}')
        self.__file_name.close()

    def add(self, *products):
        for i in products:
            s = (str(i))
            file = open(self.__file_name, 'r')
            f = file.read()
            file.close()
            if s in f:
                print(f'Продукт {s} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{s}\n')
                file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(f'просто вывод в консоль:, {p2}\n')  # __str__

s1.add( p1, p2, p3)
print(s1.get_products())




