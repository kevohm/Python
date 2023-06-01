from Animal import Animal

class Dog(Animal):
    def __init__(self, name) -> None:
        self.__value = 40
        Animal.__init__(self, name)

    @property
    def get_value(self):
        return self.__value
