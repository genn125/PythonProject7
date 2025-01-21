def add(self, *products):
    # цикл перебора наименований product в products
    for product in products:
        # условие проверки когда строки product нет в списке products.txt
        if str(product) not in self.get_products():
            # добавление отсутствующего product в файл products.txt
            file = open('products.txt', 'a')
            file.write(f'{str(product)}\n')
            file.close()
        # когда запись product есть в файле products.txt
        else:
            print(f'Продукт {product} уже есть в магазине')