from baseMachine import BaseMachine


class Tu154(BaseMachine):
    type_model = "Tyполев Ту-154"
    maximum_height = 12000

    def moving(self):
        print(f"{self.__class__.__name__} is flying!")
