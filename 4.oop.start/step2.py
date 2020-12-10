# 1. ООП нужен чтобы хронить состояние объекта во время выполнения кода
# 2. Какая ответственность лежит на нашем классе SRP(должна быть одна едиственная причина изменения класса)
# 3. Методы внутри класса должны быть сильнее сцеплены. Классы должны быть как можно больше разделены между собой
# 4.
class Product:
    type_name = None  # class var

    def __init__(self, name, price):
        self.name = name  # instance var
        self.price = price
        # self.type_name = 'Foo'


product_1 = Product('iPhone 12', 44000)
product_2 = Product('MateBook', 38000)
print(type(product_1.type_name))
print(product_1.type_name)

product_1.type_name = 'Bar'
print(product_1.type_name)
print(Product.type_name)