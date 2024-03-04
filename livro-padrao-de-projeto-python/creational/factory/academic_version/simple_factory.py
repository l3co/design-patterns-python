from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self): pass


class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow Bhow Bhow!!")


class Cat(Animal):
    def do_say(self):
        print("Meow Meow Meow Meow!!")


class ForestFactory:
    """
    This method receive a name of Animal Types (Dog, Cat) and return beyond reflection a new instance of the Anima!
    """

    @staticmethod
    def make_sound(object_type):
        return eval(object_type)().do_say()


if __name__ == '__main__':
    animal = input("Which animal should make_sound Dog or Cat ? ")
    ForestFactory.make_sound(animal)
