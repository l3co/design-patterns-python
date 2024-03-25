from abc import ABC, abstractmethod
from typing import List


class Colleague(ABC):

    @abstractmethod
    def direct(self, message: str) -> None: pass

    @abstractmethod
    def broadcast(self, message: str) -> None: pass


class Person(Colleague):

    def __init__(self, name: str, mediator: Colleague) -> None:
        self.name = name
        self.mediator = mediator

    def direct(self, message: str) -> None:
        pass

    def broadcast(self, message: str) -> None:
        pass


class Mediator(ABC):
    @abstractmethod
    def broadcast(self, colleague: Colleague, message: str) -> None: pass

    @abstractmethod
    def direct(self, sender: Colleague, receiver: str, message: str) -> None: pass


class ChatRoom(Mediator):

    def __init__(self):
        self.colleagues: List[Colleague] = []

    def is_colleague(self, colleague: Colleague) -> bool:
        return colleague in self.colleagues

    def add_colleague(self, colleague: Colleague) -> None:
        if not self.is_colleague(colleague):
            self.colleagues.append(colleague)

    def remove_colleague(self, colleague: Colleague) -> None:
        if self.is_colleague(colleague):
            self.colleagues.remove(colleague)

    def broadcast(self, colleague: Colleague, message: str) -> None:
        pass

    def direct(self, sender: Colleague, receiver: str, message: str) -> None:
        pass
