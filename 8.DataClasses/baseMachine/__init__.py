from abc import ABC
# TODO необходимо дописать использование ABC класса.


class BaseMachine(ABC):
    type_model = None

    def calling(self, name):
        return print(f"Beep-Beep! {name}")

    def riding(self, name):
        return print(f"{name} is riding!")

    def __init__(self, price, power, weight, load_capacity):
        self.price = price
        self.power = power
        self.weight = weight
        self.load_capacity = load_capacity

    def __str__(self):
        return f'Цена: {self.price} Мощность: {self.power} Вес: {self.weight} Грузоподъемность: {self.load_capacity}'
