import sqlite3


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    connection = None

    def __init__(self):
        self.cursor = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db.sqlite3')
            self.cursor = self.connection.cursor()
        return self.cursor


if __name__ == '__main__':
    db1 = Database().connect()
    db2 = Database().connect()

    print("Database object DB1", db1)
    print("Database object DB2", db1)
