"""
Strategy Pattern

🔧 Practice: Implement a payment processor

Strategies: CreditCardPayment, PayPalPayment, CryptoPayment.

A PaymentProcessor should accept any strategy and call .pay(amount).

🧠 Bonus: Add the ability to change the strategy at runtime.
"""

from abc import ABC, abstractmethod

class AbstractPayment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(AbstractPayment):
    def __init__(self, card_number: str, cvv: str):
        # Example of state you might need later
        self.card_number = card_number
        self.cvv = cvv

    def pay(self, amount):
        # (In real life, you’d call some CC‐gateway API here.)
        print(f"Paid {amount} using CreditCardPayment (card ending in {self.card_number[-4:]})")


class PayPalPayment(AbstractPayment):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount):
        # (In real life, call PayPal SDK / REST API.)
        print(f"Paid {amount} using PayPal (account: {self.email})")


class CryptoPayment(AbstractPayment):
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    def pay(self, amount):
        # (In reality you’d do blockchain calls or use a library.)
        print(f"Paid {amount} using CryptoPayment (wallet: {self.wallet_address[:6]}...)")


class PaymentProcessor:
    def __init__(self, strategy: AbstractPayment):
        # Enforce at runtime that strategy is an AbstractPayment
        if not isinstance(strategy, AbstractPayment):
            raise TypeError("strategy must be an instance of AbstractPayment")
        self.strategy = strategy

    def pay(self, amount):
        # Delegate to whichever strategy instance we hold
        self.strategy.pay(amount)

    def set_strategy(self, strategy: AbstractPayment):
        """
        Change strategy at runtime. Enforce it still implements AbstractPayment.
        """
        if not isinstance(strategy, AbstractPayment):
            raise TypeError("strategy must be an instance of AbstractPayment")
        self.strategy = strategy


# Usage:

# 1. Create a real credit‐card‐strategy instance:
cc_strategy = CreditCardPayment(card_number="4111111111111111", cvv="123")
pp_strategy = PayPalPayment(email="alice@example.com")
crypto_strategy = CryptoPayment(wallet_address="0xABCDEF1234567890")

processor = PaymentProcessor(strategy=pp_strategy)
processor.pay(800)  # → "Paid 800 using PayPal (account: alice@example.com)"

# 2. Switch to crypto at runtime:
processor.set_strategy(crypto_strategy)
processor.pay(600)  # → "Paid 600 using CryptoPayment (wallet: 0xABCD...)"
