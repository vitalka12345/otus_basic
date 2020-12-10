# 1. ООП нужен чтобы хронить состояние объекта во время выполнения кода
# 2. Какая ответственность лежит на нашем классе SRP(должна быть одна едиственная причина изменения класса)
# 3. Методы внутри класса должны быть сильнее сцеплены. Классы должны быть как можно больше разделены между собой
# 4.
class BaseProduct:
    type_name = None  # class var

    def __init__(self, name, price):
        self.name = name  # instance var
        self.price = price
        # self.type_name = 'Foo'


class Phone(BaseProduct):
    type_name = 'телефон'


class NoteBook(BaseProduct):
    type_name = 'ноутбук'


product_1 = Phone('iPhone 12', 44000)
product_2 = NoteBook('MateBook', 38000)

print(product_1.type_name, product_1.name)
print(product_2.type_name, product_2.name)
