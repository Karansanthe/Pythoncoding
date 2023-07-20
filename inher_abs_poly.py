import abc

class Animal(abc.ABC):
  @abc.abstractmethod
  def make_sound(self):
    pass

class Dog(Animal):
  def make_sound(self):
    print("Woof!")

class Cat(Animal):
  def make_sound(self):
    print("Meow!")

def make_animal_sound(animal):
  animal.make_sound()

dog = Dog()
cat = Cat()

make_animal_sound(dog)
# Woof!

make_animal_sound(cat)
# Meow!
