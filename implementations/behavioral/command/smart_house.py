from abc import abstractmethod, ABC
from typing import Dict, List


class Light:
    """ Receiver """

    def __init__(self, name: str, color: str = 'Default color') -> None:
        self.name = name
        self.color = color

    def on(self):
        print(f"Light {self.name}  is now ON")

    def off(self):
        print(f"Light {self.name} is now OFF")

    def change_color(self, color: str) -> None:
        print(f"Light {self.name} with color {self.color} changed to {color}")
        self.color = color


class ICommand(ABC):
    """ Command Interface """

    @abstractmethod
    def execute(self) -> None: pass

    @abstractmethod
    def undo(self) -> None: pass


class LightOnCommand(ICommand):
    """ Concrete command """

    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()


class RemoteController:
    """ Invoker """

    def __init__(self) -> None:
        self.__buttons: Dict[str, List[ICommand]] = {}

    def add_button(self, name: str, command: ICommand) -> None:
        if name not in self.__buttons:
            self.__buttons[name] = [command]
        else:
            self.__buttons[name].append(command)

    def button_execute(self, name: str) -> None:
        if name in self.__buttons:
            for command in self.__buttons[name]:
                command.execute()

    def button_undo(self, name: str) -> None:
        if name in self.__buttons:
            for command in self.__buttons[name]:
                command.undo()


if __name__ == '__main__':
    bedroom_leandro = Light('Bedroom Leandro')
    bedroom_gabriel = Light('Bedroom Gabriel')

    bedroom_command_l = LightOnCommand(bedroom_leandro)
    bedroom_command_g = LightOnCommand(bedroom_gabriel)

    remote = RemoteController()
    remote.add_button('good morning', bedroom_command_l)
    remote.add_button('good morning', bedroom_command_g)

    remote.button_execute('good morning')
    remote.button_undo('good morning')
