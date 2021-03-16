from baseMachine import BaseMachine


class Ship(BaseMachine):
    type_model = 'Корабль'
    displacement = 20000

    def moving(self, name):
        return print(f"{name} is a ship and it floated.")


class Titanik(Ship):
    type_model = "Титаник"
    displacement = 45000

    def moving(self):
        print(f"{self.__class__.__name__} is floating!")
