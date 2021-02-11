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
            return True
        else:
            print("Not enough fuel!")
            return False

    def get_type_model(self, item):
        return item

    def riding(self, name, fuel):
        if self.start(fuel=fuel) == True:
            print(f"{name} is a car and it goes.")
        else:
            print(f"{name} Can't riding! Not enough fuel!")
