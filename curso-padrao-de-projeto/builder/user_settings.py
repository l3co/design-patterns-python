from abc import ABC, abstractmethod


class User:

    def __init__(self, key='morango'):
        if key != 'banana':
            raise ValueError('You cannot instantiate this object ')

        self.first_name = None
        self.last_name = None
        self.age = 0


class IUser(ABC):

    @abstractmethod
    def builder(self): pass

    @abstractmethod
    def build(self): pass

    @abstractmethod
    def add_first_name(self, first_name): pass

    @abstractmethod
    def add_last_name(self, last_name): pass

    @abstractmethod
    def add_age(self, age): pass


class UserBuilder(IUser):

    def __init__(self):
        self.__user: User = None

    def builder(self) -> IUser:
        self.__user: User = User('banana')
        return self

    def build(self) -> User:
        return self.__user

    def add_first_name(self, first_name) -> IUser:
        self.__user.first_name = first_name
        return self

    def add_last_name(self, last_name) -> IUser:
        self.__user.last_name = last_name
        return self

    def add_age(self, age) -> IUser:
        self.__user.age = age
        return self


if __name__ == '__main__':
    builder = UserBuilder().builder()
    user: User = builder.add_first_name('Leandro').add_last_name('costa').add_age(18).build()
    print(user.__dict__)
