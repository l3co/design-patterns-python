from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def do_pay(self): pass


class Bank(Payment):

    def __init__(self):
        self.card = None
        self.account = None

    def __get_account(self):
        self.account = self.card
        return self.account

    def __has_found(self):
        print("Bank :: Checking if account", self.__get_account(), "has enough money")
        return True

    def set_card(self, card):
        self.card = card

    def do_pay(self):
        if self.__has_found():
            print("Bank :: Paying the merchant")
            return True
        else:
            print("Bank :: Sorry, not enough funds!")
            return False


class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input("Proxy :: Punch in Card Number : ")
        self.bank.set_card(card)
        return self.bank.do_pay()


class You:
    def __init__(self):
        print("You :: Lets buy the Denim shirt")
        self.debit_card = DebitCard()
        self.is_purchased = None

    def make_payment(self):
        self.is_purchased = self.debit_card.do_pay()

    def __del__(self):
        if self.is_purchased:
            print("You :: Wow! Denim shirt is Mine :-)")
        else:
            print("You :: I should earn more :(")


if __name__ == '__main__':
    you = You()
    you.make_payment()
