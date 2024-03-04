from abc import ABC, abstractmethod


class PizzaFactory(ABC):
    @abstractmethod
    def create_veg_pizza(self): pass

    @abstractmethod
    def create_non_veg_pizza(self): pass


class VegPizza(ABC):
    @abstractmethod
    def prepare(self, VegPizza): pass


class NonVegPizza(ABC):
    @abstractmethod
    def serve(self, VegPizza): pass


class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print("Prepare ", type(self).__name__)


class ChickenPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Chicken on ", type(VegPizza).__name__)


class MexicanVeggiePizza(VegPizza):
    def prepare(self):
        print("Prepare ", type(self).__name__)


class HamPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Ham on ", type(VegPizza).__name__)


class IndiaPizzaFactory(PizzaFactory):
    def create_veg_pizza(self):
        return DeluxVeggiePizza()

    def create_non_veg_pizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    def create_veg_pizza(self):
        return MexicanVeggiePizza()

    def create_non_veg_pizza(self):
        return HamPizza()


class PizzaStore:

    def __init__(self):
        self.non_veg_pizza: NonVegPizza = None
        self.veg_pizza: VegPizza = None
        self.factory = None

    def make_pizza(self):
        for factory in [IndiaPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.non_veg_pizza = self.factory.create_non_veg_pizza()
            self.veg_pizza = self.factory.create_veg_pizza()
            self.veg_pizza.prepare()
            self.non_veg_pizza.serve(self.veg_pizza)


if __name__ == '__main__':
    pizza = PizzaStore()
    pizza.make_pizza()
