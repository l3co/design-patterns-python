class Borg:
    __shared_state = {"1": "2"}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass


if __name__ == '__main__':
    b1 = Borg()

    b2 = Borg()
    b2.x = 4

    print("Borg Object", b1)
    print("Borg Object", b1.__dict__)
    
    print("Borg Object", b2)
    print("Borg Object", b2.__dict__)
