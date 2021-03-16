from baseMachine import BaseMachine


class Plane(BaseMachine):
    type_model = 'Самолёт'
    maximum_height = 5000

    def moving(self, name):
        return print(f"{name} is a plane and it flies.")

class Tu154(Plane):
    type_model = "Tyполев Ту-154"
    maximum_height = 12000

    def moving(self):
        print(f"{self.__class__.__name__} is flying!")
