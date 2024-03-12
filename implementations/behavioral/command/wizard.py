class Wizard:

    def __init__(self, root_dir, src):
        self.__choices = []
        self.__root_dir = root_dir
        self.__src = src

    def preferences(self, command):
        self.__choices.append(command)

    def execute(self):
        for command in self.__choices:
            if list(command.values())[0]:
                print("Copying binaries -- ", self.__src, " to ", self.__root_dir)
            else:
                print("No Operation")


if __name__ == '__main__':
    wizard = Wizard('python3.5.gzip', '/usr/bin/')
    wizard.preferences({'python': True})
    wizard.preferences({'Java': False})

    wizard.execute()
