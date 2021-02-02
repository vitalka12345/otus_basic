from baseMachine import BaseMachine


class Car(BaseMachine):
    type_model = 'Легковой автомобиль'
    wheel_count = 4

    def riding(self, name):
        return print(f"{name} is a car and it goes.")


class Nine(Car):
    type_model = 'Девятка'
    wheel_count = 4

    def start(self, fuel):
        if fuel > 10:
            print("Engine started!")
        else:
            print("Not enough fuel!")

    def get_type_model(self, item):
        return item

    def riding(self, name):
        return print(f"{name} is a car and it goes.")


