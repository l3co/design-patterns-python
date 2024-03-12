from abc import ABC, abstractmethod
from typing import List, Dict


class IObserver(ABC):

    def update(self): pass


class IObservable(ABC):
    @abstractmethod
    def state(self) -> Dict: pass

    @abstractmethod
    def add_observer(self, observer: IObserver): pass

    @abstractmethod
    def remove_observer(self, observer: IObserver): pass

    @abstractmethod
    def notify_observers(self): pass


class SmartPhone(IObserver):
    def __init__(self, name, observable: IObservable):
        self.name = name
        self.observable = observable
        self.observable.add_observer(self)

    def update(self):
        observable_name = self.observable.__class__.__name__
        print(f"{self.name}: {observable_name}"
              f"acabou de ser atualizado => {self.observable.state}")


class WeatherStation(IObservable):

    def __init__(self):
        self.__observers: List[IObserver] = []
        self.__state: Dict = {}

    @property
    def state(self) -> Dict:
        return self.__state

    @state.setter
    def state(self, state: Dict) -> None:
        new_state: Dict = {**self.__state, **state}
        if new_state != self.__state:
            self.__state = state
            self.notify_observers()

    def reset_state(self) -> None:
        self.__state = {}

    def add_observer(self, observer: IObserver) -> None:
        self.__observers.append(observer)

    def remove_observer(self, observer: IObserver):
        if observer not in self.__observers:
            return

        self.__observers.remove(observer)

    def notify_observers(self):
        for observer in self.__observers:
            observer.update()


if __name__ == '__main__':
    weather_station = WeatherStation()
    iphone = SmartPhone('Iphone 14', weather_station)
    samsung = SmartPhone('Galaxy', weather_station)

    weather_station.state = {'temperature': 32, 'humidity': 100}
    weather_station.state = {'temperature': 14, 'humidity': 100}
