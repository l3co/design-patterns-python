class Singleton(object):
    __instance = None

    def __init__(self):
        print(f"__instance is {Singleton.__instance}")
        if Singleton.__instance is None:
            print('__init__ method called..')
        else:
            print("Instance already created:", self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


if __name__ == '__main__':
    s1 = Singleton()
    print("Object created", s1.get_instance())

    s2 = Singleton()
