from Animal import Animal

class Cat(Animal):
    def __init__(self, name) -> None:
        self.__value = 30
        Animal.__init__(self, name)
    
    @property
    def get_value(self):
        return self.__value