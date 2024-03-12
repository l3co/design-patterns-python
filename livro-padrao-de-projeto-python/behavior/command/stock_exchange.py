from abc import ABC, abstractmethod


class Order(ABC):
    @abstractmethod
    def execute(self): pass


class BuyStockOrder(Order):

    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


class SellStockOrder(Order):

    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()


class StockTrade:
    def buy(self):
        print("You will buy a stock!")

    def sell(self):
        print("You will sell a stock!")


class Agent:
    def __init__(self):
        self.__orders = []

    def place_order(self, order: Order):
        self.__orders.append(order)
        order.execute()


if __name__ == '__main__':
    stock = StockTrade()
    buy_stock = BuyStockOrder(stock)
    sell_stock = SellStockOrder(stock)

    agent = Agent()
    agent.place_order(buy_stock)
    agent.place_order(sell_stock)
