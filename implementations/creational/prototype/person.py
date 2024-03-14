from __future__ import annotations

from copy import deepcopy
from typing import List


class Person:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

        self.address: List[Address] = []

    def add_address(self, addr: Address) -> None:
        self.address.append(addr)

    def clone(self) -> Person:
        return deepcopy(self)

    def __str__(self):
        name = self.__class__.__name__ + ': '
        attrs = ['{}={}'.format(k, v) for (k, v) in self.__dict__.items()]
        return name + ', '.join(attrs)


class Address:
    def __init__(self, street: str, city: str, state: str):
        self.street = street
        self.city = city
        self.state = state


if __name__ == '__main__':
    leandro = Person('leandro', 'Costa', 31)

    address = Address(street='Av. Larina', city='São Paulo', state='São Paulo')
    leandro.add_address(address)

    juliana = leandro.clone()
    juliana.name = 'Juliana'

    print(leandro)
    print(juliana)
