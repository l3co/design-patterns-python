class Singleton(object):
    love = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


if __name__ == '__main__':
    s1 = Singleton()
    print("Object created", s1)

    s2 = Singleton()
    print("Object created", s2)
