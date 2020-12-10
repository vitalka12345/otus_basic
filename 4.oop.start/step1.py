# print(len([1, 2, True]))
# print(len('hi'))


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


product_1 = Product('iPhone 12', 44000)
product_2 = Product('MateBook', 38000)
print(type(product_1))
print(product_1)
print(product_1.name)
print(product_1.price)

print(type(product_2))
print(product_2)
print(product_2.name)
print(product_2.name)
print(product_2.price)
