from abc import ABC, abstractmethod


class Order:
    """ Context """

    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self) -> None:
        self.state.pending()

    def approve(self) -> None:
        self.state.approve()

    def reject(self) -> None:
        self.state.reject()


class OrderState(ABC):

    def __init__(self, order: Order):
        self.order = order

    @abstractmethod
    def pending(self) -> None: pass

    @abstractmethod
    def approve(self) -> None: pass

    @abstractmethod
    def reject(self) -> None: pass


# class Payment(Enum):
#     pass


class PaymentPending(OrderState):
    def __init__(self, order: Order):
        self.order = order

    def pending(self) -> None:
        print("Payment is Pending, we can't do this again")

    def approve(self) -> None:
        self.order.state = PaymentApproved(self.order)
        print("Payment approved!")

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print("Payment Reject!")


class PaymentApproved(OrderState):
    def __init__(self, order: Order):
        self.order = order

    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print("Payment is pending now!")

    def approve(self) -> None:
        print("Payment is approved, we can't do this again")

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print("Payment rejected!")


class PaymentRejected(OrderState):
    def __init__(self, order: Order):
        self.order = order

    def pending(self) -> None:
        print("Payment reject we can't do this")

    def approve(self) -> None:
        print("Payment reject we can't do this")

    def reject(self) -> None:
        print("Payment reject we can't do this again")


if __name__ == '__main__':
    order_1 = Order()
    order_1.pending()
    order_1.approve()
    order_1.reject()

    order_2 = Order()
    order_2.pending()
    order_2.reject()
    order_2.approve()
