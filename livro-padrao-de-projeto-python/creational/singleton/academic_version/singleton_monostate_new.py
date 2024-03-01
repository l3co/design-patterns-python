class Borg:
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj


if __name__ == '__main__':
    b1 = Borg()

    b2 = Borg()
    b2.x = 4

    print("Borg Object", b1)
    print("Borg Object", b1.__dict__)

    print("Borg Object", b2)
    print("Borg Object", b2.__dict__)
