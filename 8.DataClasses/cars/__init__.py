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
            raise ValueError("Not enough fuel!", f"Fuel level is {fuel} liters!")


    def get_type_model(self, item):
        return item

    def riding(self, name, fuel=0):
        try:
            self.start(fuel=fuel)
        except ValueError as error:
            for i in error.args:
                print(i)
        else:
            print(f"{name} is a car and it goes! Fuel level {fuel} is good!")
