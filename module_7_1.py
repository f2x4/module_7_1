import os

class Product:
    def __init__(self, name, weight, category):
        self.name =  self.check_value(name, str)
        self.weight = self.check_value(weight, float)
        self.category = self.check_value(category, str)

    @staticmethod
    def check_value(x, type_):
        """ Проверить является ли x переменной типа type_.
        Иначе вывести сообщение. """
        if isinstance(x, type_):
            return x
        else:
            print(f'Значение {x} должно быть {type_}')

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def __init__(self):
        # Если файл products.txt не существует, то создать его
        if not os.path.isfile(self.__file_name):
            my_file = open(self.__file_name, 'w')
            my_file.write('')
            my_file.close()

    def get_products(self):
        file = open(self.__file_name, 'r', encoding='utf-8')
        content = file.read()
        file.close()
        return content

    def add(self, *products):
        file_content = self.get_products()
        file = open(self.__file_name, 'a+')
        for product in products:
            if product.name in file_content:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file.write(
                    f'{product.name}, {product.weight}, {product.category}\n'
                )
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())