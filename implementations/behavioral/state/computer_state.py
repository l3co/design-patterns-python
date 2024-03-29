class ComputerState:
    name = "state"
    allowed = []

    def handle(self, state):
        if state.name in self.allowed:
            print('Current: ', self, '=> switched to new state', state.name)
            self.__class__ = state
        else:
            print('Current: ', self, '=> switching to ', state.name, ' not possible')

    def __str__(self):
        return self.name


class Off(ComputerState):
    name = 'off'
    allowed = ['on']


class On(ComputerState):
    name = 'on'
    allowed = ['off', 'suspend', 'hibernate']


class Suspend(ComputerState):
    name = 'suspend'
    allowed = ['on']


class Hibernate(ComputerState):
    name = 'hibernate'
    allowed = ['on']


class Computer:
    def __init__(self, model):
        self.model = model
        self.state = Off()

    def change(self, state):
        self.state.handle(state)


if __name__ == '__main__':
    comp = Computer('Dell')

    # On
    comp.change(On)

    # Off
    comp.change(Off)

    # On
    comp.change(On)

    # Suspend
    comp.change(Suspend)

    # Hibernate
    comp.change(Hibernate)

    # On
    comp.change(On)

    # Off
    comp.change(Off)
