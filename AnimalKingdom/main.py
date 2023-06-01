from Animal import Animal
from Dog import Dog
from Cat import Cat

dog = Dog("Bosco")
print(dog)
print(dog.statistics())
cat = Cat("Basil")
print(cat)
cat.eat(dog)
print(cat.statistics())
print(dog)
print(Animal.total_animals())