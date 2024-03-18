from __future__ import annotations

from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float: pass


class TwentyPercentDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.2)


class FiftyPercentDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.5)


class CustomPercentDiscount(DiscountStrategy):

    def __init__(self, discount: float) -> None:
        self.discount = discount / 100

    def calculate(self, value: float) -> float:
        return value - (value * self.discount)


class Order:
    def __init__(self, total: float, discount: DiscountStrategy):
        self.__total = total
        self.__discount = discount

    @property
    def total(self) -> float:
        return self.__total

    @property
    def total_with_discount(self) -> float:
        return self.__discount.calculate(self.__total)


if __name__ == '__main__':
    twenty_percent = TwentyPercentDiscount()
    order = Order(total=1000, discount=twenty_percent)

    print(f"Total={order.total}, Total with Discount={order.total_with_discount}")

    fifty_percent = FiftyPercentDiscount()
    order1 = Order(total=1000, discount=fifty_percent)

    print(f"Total={order1.total}, Total with Discount={order1.total_with_discount}")

    custom_discount = CustomPercentDiscount(15)
    order2 = Order(total=1000, discount=custom_discount)

    print(f"Total={order2.total}, Total with Discount={order2.total_with_discount}")
