from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import List, Any


class CustomIterator(Iterator):

    def __init__(self, collections: List[Any]):
        self.__collections = collections
        self.__index = 0

    def __next__(self):
        try:
            item = self.__collections[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration


class GroceryList(Iterable):

    def __init__(self) -> None:
        self.__items: List[Any] = []

    def add(self, value: Any) -> None:
        self.__items.append(value)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self.__items})'

    def __iter__(self):
        return CustomIterator(self.__items)


if __name__ == '__main__':
    custom = GroceryList()
    custom.add('Orange')
    custom.add('Pineapple')
    custom.add('Bread')
    custom.add('Meal')
    custom.add('Pork')

    for item in custom:
        print(item)
