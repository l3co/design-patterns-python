from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def handle(self): pass


class StartState(State):
    def handle(self):
        print("TV Switching ON...")


class StopState(State):
    def handle(self):
        print("TV Switching OFF...")


class TVContext(State):

    def __init__(self):
        self.__state = None

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state

    def handle(self):
        self.__state.handle()


if __name__ == '__main__':
    context = TVContext()
    start = StartState()

    context.state = start
    context.state.handle()

    stop = StopState()
    context.state = stop

    context.state.handle()
