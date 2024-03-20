from __future__ import annotations

from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, next_handle: Handler):
        self.__next_handler = next_handle

    @property
    def next_handler(self):
        return self.__next_handler

    @abstractmethod
    def handle(self, letter: str) -> str: pass


class HandlerABC(Handler):
    def __init__(self, next_handle: Handler):
        super().__init__(next_handle)
        self.letters = ['A', 'B', 'C']

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f"HandlerABC : can work with {letter}"
        return self.next_handler.handle(letter)


class HandlerDEF(Handler):
    def __init__(self, next_handle: Handler):
        super().__init__(next_handle)
        self.letters = ['D', 'E', 'F']

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f"HandlerDEF : can work with {letter}"
        return self.next_handler.handle(letter)


class HandlerUnsolved(Handler):
    def __init__(self):
        super().__init__(None)

    def handle(self, letter: str) -> str:
        return f"Handler Unsolved : {letter}"


if __name__ == '__main__':
    handler = HandlerABC(HandlerDEF(HandlerUnsolved()))
    print(handler.handle('A'))
    print(handler.handle('B'))
    print(handler.handle('E'))
    print(handler.handle('X'))
