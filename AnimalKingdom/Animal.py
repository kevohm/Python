class Animal():
    __count = 0
    def __init__(self, name = None) -> None:
        self.name = name
        self.hunger = 0
        self.life = 100
        Animal.count()
    
    @classmethod
    def total_animals(cls) -> int:
        return cls.__count
        
    @classmethod
    def count(cls):
        cls.__count += 1
    
    def eat(self, animal) -> None:
        value = animal.get_value
        if(self.life < 100 and self.hunger > 0):
            self.hunger -= value
            self.life += value
        elif(self.hunger > 0):
            self.hunger -= value
        elif(self.life < 100):
            self.life += value

        animal.die()
    
    def die(self) -> None:
        if(self.life <= 0):
            del self
    
    def statistics(self) -> str:
        c_n = self.__class__.__name__
        name = "{}: {}\n".format(c_n, self.name)
        hunger = "Hunger: {}\n".format(self.hunger)
        life = "Life: {}\n".format(self.life)
        return '{}{}{}'.format(name,hunger,life)
        
    def __str__(self) -> str:
        return "My name is {}. I am an {}".format(self.name,self.__class__.__name__)
