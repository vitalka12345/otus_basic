from baseMachine import BaseMachine


class Titanik(BaseMachine):
    type_model = "Титаник"
    displacement = 45000

    def moving(self):
        print(f"{self.__class__.__name__} is floating!")
