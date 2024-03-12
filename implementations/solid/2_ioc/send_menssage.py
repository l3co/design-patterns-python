from abc import ABC, abstractmethod


class NotificationService(ABC):

    @abstractmethod
    def notify(self, addressee: str, message: str):
        raise NotImplementedError


class EmailNotification(NotificationService):
    def notify(self, addressee: str, message: str):
        print(f"Send email to {addressee}: {message}")


class Client:
    def __init__(self, service: NotificationService):
        self.service = service

    def notify_client(self, message):
        self.service.notify(message=message, addressee="<EMAIL>")


if __name__ == '__main__':
    email_service = EmailNotification()
    client = Client(email_service)
    client.notify_client("teste")
