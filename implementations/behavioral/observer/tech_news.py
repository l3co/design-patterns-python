from abc import ABC, abstractmethod


class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latest_news = None

    def attach(self, subscribe):
        self.__subscribers.append(subscribe)

    def detach(self):
        return self.__subscribers.pop()

    def subscribes(self):
        return [type(x).__name__ for x in self.__subscribers]

    def notify_subscribers(self):
        for subscriber in self.__subscribers:
            subscriber.update()

    def add_news(self, news):
        self.__latest_news = news

    def get_news(self):
        return 'Got News: ', self.__latest_news


class Subscriber(ABC):

    @abstractmethod
    def update(self): pass


class SMSSubscriber(Subscriber):

    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


class EmailSubscriber(Subscriber):

    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


class AnyOtherSubscriber(Subscriber):

    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


if __name__ == '__main__':
    news_publisher = NewsPublisher()

    for subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        subscribers(news_publisher)

    print("\nSubscribers:", news_publisher.subscribes())

    news_publisher.add_news("Hello World!")
    news_publisher.notify_subscribers()

    print("\nDetach:", type(news_publisher.detach()).__name__)
    print("\nSubscribers:", news_publisher.subscribes())

    news_publisher.add_news("My second news!")
    news_publisher.notify_subscribers()
