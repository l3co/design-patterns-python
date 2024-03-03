def singleton(the_class):
    _instance = {}

    def get_class(*args, **kwargs):
        # This verification is inside the key name
        if the_class not in _instance:
            _instance[the_class] = the_class(*args, **kwargs)
        return _instance[the_class]

    return get_class


@singleton
class MyClass:
    def __init__(self):
        self.theme = 'dark'
        self.font = 'red'
        print('Hi')


if __name__ == '__main__':
    class1 = MyClass()
    class2 = MyClass()
